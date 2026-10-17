using System.Diagnostics;
using System.Globalization;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace BookWriter.Engine;

/// <summary>
/// Generates a real, KDP-sized portrait book cover image for a <see cref="BookOutline"/>: a
/// base illustration from one of three generative-image tiers, then two real ffmpeg finishing
/// passes (combined into a single -vf call) that (a) resize+crop it to EXACTLY Amazon KDP's
/// own ideal cover dimensions, 1600x2560 pixels (a 1:1.6 ratio - see
/// <see cref="KdpCoverWidthPixels"/>/<see cref="KdpCoverHeightPixels"/>), and (b) drawtext the
/// real book title over a semi-translucent box near the lower third.
///
/// The 3-tier generative-image fallback chain below mirrors
/// MediaMaker.ScriptToVideo.ThumbnailAI.ThumbnailVariantGenerator's own chain byte-for-byte in
/// shape and coding style (deliberately duplicated rather than cross-referenced, matching this
/// codebase's own established precedent of small per-domain HTTP/ffmpeg wrappers over a
/// cross-project reference for ~30-100 lines of plumbing - see that class's own doc comment for
/// this precedent), adapted only for PORTRAIT framing and book-cover subject matter instead of a
/// landscape YouTube thumbnail:
///
/// Tier 1, OpenAI: gpt-image-1 at size "1024x1536" (its one true portrait option - gpt-image-1
/// only accepts "1024x1024", "1536x1024", "1024x1536", or "auto"), retried once with dall-e-3 at
/// "1024x1792" (its closest portrait option) only when the gpt-image-1 attempt looks like a
/// model-unavailable/no-access problem for this key/account - same b64_json/url response
/// handling and same &gt;=1000-byte sanity floor against a truncated/garbage response as
/// ThumbnailVariantGenerator.TryOpenAiImageModelAsync.
///
/// Tier 2, Gemini "Nano Banana Pro" (model id gemini-3-pro-image), tried only when OpenAI isn't
/// configured or fails: POST https://generativelanguage.googleapis.com/v1beta/interactions,
/// header x-goog-api-key, body {"model":"gemini-3-pro-image","input":"...","response_format":
/// {"type":"image","mime_type":"image/jpeg","aspect_ratio":"2:3"}}. "2:3" is Gemini's closest
/// supported portrait ratio to KDP's own 1:1.6 ideal - an approximation, NOT an exact match; the
/// mismatch is corrected afterward by this class's own ffmpeg scale+crop pass to the real
/// 1600x2560 target, so the final file is always precisely on-spec regardless of which tier's
/// approximate aspect ratio actually produced the base image. Image bytes are read from the
/// response's own "output_image.data" convenience accessor, falling back to the same real
/// steps[]/content[] walk LyriaMusicGenerator.TryExtractAudio already uses for this endpoint
/// family (adapted to an "image" block type instead of "audio"). This exact endpoint/model/
/// shape is carried forward unchanged from ThumbnailVariantGenerator's own doc comment
/// (confirmed there against ai.google.dev's live docs); it was not independently re-fetched for
/// this class, per this class's own instruction to mirror that file's chain rather than
/// re-research it.
///
/// Tier 3, YandexART (Yandex Cloud Foundation Models), tried only when neither OpenAI nor Gemini
/// above is configured or succeeds: submit POST llm.api.cloud.yandex.net/foundationModels/v1/
/// imageGenerationAsync, header "Authorization: Api-Key {yandexApiKey}", modelUri
/// "art://{yandexFolderId}/yandex-art/latest", body's generationOptions.aspectRatio set to
/// widthRatio "2"/heightRatio "3" (same 2:3 portrait approximation and same "corrected
/// afterward by ffmpeg" reasoning as Gemini's tier above); then poll GET
/// operation.api.cloud.yandex.net/operations/{id}, same Authorization header, until the
/// envelope's own "done":true, exactly like NovaReelVideoGenerator.PollUntilDoneAsync's own
/// "poll until done" loop shape for a different async job on a different provider.
///
/// LOWER-CONFIDENCE DISCLOSURE, carried forward unchanged from ThumbnailVariantGenerator's own
/// doc comment rather than re-researched (this class reuses that exact tier, so the same
/// caveat applies unchanged): Yandex Cloud's own imageGenerationAsync reference page returned a
/// CAPTCHA wall on every fetch attempt during that class's own research, so the shape above is
/// reconstructed from secondhand corroborating sources describing this same API family rather
/// than a direct, confirmed read of Yandex's own docs. If this reconstructed shape turns out
/// wrong in some real, specific way (a renamed field, a different model URI scheme), this
/// class's own honest-degrade convention means the real, current failure (a parse error, an
/// unexpected 4xx) is what gets logged and surfaced, never a fabricated success.
///
/// FONT-FILE QUIRK: same one ThumbnailVariantGenerator's own doc comment documents in detail -
/// passing an ABSOLUTE Windows font path straight into drawtext's fontfile= option silently
/// mis-parses at the drive letter's colon on this solution's bundled ffmpeg build, so the
/// finishing pass below passes fontfile as a bare filename with the ffmpeg child process's
/// WorkingDirectory set to that font's own folder instead. The title overlay itself is a basic,
/// legible treatment (bold font, outline, semi-translucent background box, centered near the
/// lower third) - not full professional cover typography/layout; an honest scope note, not a
/// claim of design quality.
///
/// The generation prompt (see <see cref="BuildCoverImagePrompt"/>) is built from
/// outline.Title/outline.Premise (plus outline.Setting for Fiction, when non-empty) and, for the
/// same reason ThumbnailVariantGenerator's own BuildImagePrompt gives an image model no text/
/// captions to draw (no image model reliably renders legible text), explicitly instructs the
/// image model to produce no text/captions/watermark/logo of its own - the real title is always
/// added afterward by this class's own drawtext pass.
///
/// Every public method here returns "" (or null, per its own return shape) on success and a
/// clear, honest, human-readable error/note string on failure - never throws for an ordinary
/// failure (no tier configured, every configured tier failing, or ffmpeg itself being missing/
/// failing). Real failures are logged via <see cref="AppLog.Warning"/>/<see cref="AppLog.Info"/>.
/// The finished cover is built to a same-directory temp file first and only
/// File.Move(...)'d into place once that temp file is confirmed to exist and be non-empty - a
/// mid-write ffmpeg failure never leaves a truncated/corrupt file at the real output path.
/// </summary>
public sealed class BookCoverArtGenerator(string ffmpegExe, string openAiApiKey = "", string geminiApiKey = "", string yandexApiKey = "", string yandexFolderId = "")
{
    private const string GeminiInteractionsEndpoint = "https://generativelanguage.googleapis.com/v1beta/interactions";
    private const string GeminiImageModel = "gemini-3-pro-image";

    private const string YandexArtSubmitEndpoint = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync";
    private const string YandexArtOperationEndpointFormat = "https://operation.api.cloud.yandex.net/operations/{0}";
    private const string YandexArtModelName = "yandex-art";

    /// <summary>Real per-poll interval/overall budget for YandexART's async imageGenerationAsync
    /// job - same values and same disclosed lower-confidence caveat as
    /// ThumbnailVariantGenerator's own YandexArtPollInterval/YandexArtPollTimeout, since a
    /// single still cover image is a comparably light generation task to a thumbnail image.</summary>
    private static readonly TimeSpan YandexArtPollInterval = TimeSpan.FromSeconds(3);
    private static readonly TimeSpan YandexArtPollTimeout = TimeSpan.FromSeconds(90);

    /// <summary>gpt-image-1's one true portrait size option (it only accepts "1024x1024",
    /// "1536x1024", "1024x1536", or "auto") - the closest it offers to a tall book-cover
    /// framing; see this class's own doc comment for why this is an approximation later
    /// corrected by ffmpeg, not an exact KDP-ratio match.</summary>
    private const string GenerativeImageSize = "1024x1536";

    private const string FontGeorgia = @"C:\Windows\Fonts\georgia.ttf";
    private const string FontFallback = @"C:\Windows\Fonts\arialbd.ttf";

    /// <summary>Amazon KDP's own documented ideal cover pixel dimensions (a 1:1.6 ratio) - the
    /// exact size every finished cover from this class is resized/cropped to, regardless of
    /// which generative tier's own approximate portrait ratio produced the base image.</summary>
    private const int KdpCoverWidthPixels = 1600;
    private const int KdpCoverHeightPixels = 2560;

    private static readonly HttpClient Http = new();

    /// <summary>True only when a real, non-placeholder OpenAI key was passed to the
    /// constructor - same exposed-for-diagnostics purpose as
    /// ThumbnailVariantGenerator.GenerativeFallbackConfigured.</summary>
    public bool GenerativeFallbackConfigured => !string.IsNullOrEmpty(openAiApiKey);

    /// <summary>True only when a real, non-placeholder Gemini key was passed to the
    /// constructor - only ever attempted when OpenAI's own fallback isn't configured or fails,
    /// per this class's own doc comment.</summary>
    public bool GeminiFallbackConfigured => !string.IsNullOrEmpty(geminiApiKey);

    /// <summary>True only when BOTH a real Yandex Cloud API key AND folder id were passed to the
    /// constructor - YandexART's request needs both together (the folder id names which Cloud
    /// folder's quota/billing the job draws from via the request's own modelUri). Only ever
    /// attempted when neither the OpenAI nor the Gemini fallback above is configured or
    /// succeeds, per this class's own doc comment.</summary>
    public bool YandexArtFallbackConfigured => !string.IsNullOrEmpty(yandexApiKey) && !string.IsNullOrEmpty(yandexFolderId);

    /// <summary>
    /// The single entry point: resolves one base cover illustration via the 3-tier generative
    /// fallback chain (see this class's own doc comment), then runs the real ffmpeg finishing
    /// pass (resize/crop to KDP's ideal dimensions plus a title overlay) and writes the finished
    /// JPEG under <paramref name="workFolder"/>. Never throws - on total failure (no tier
    /// configured, every configured tier failing, or ffmpeg itself missing/failing) returns
    /// (null, an honest reason).
    /// </summary>
    public async Task<(string? CoverImagePath, string Note)> GenerateAsync(BookOutline outline, string workFolder, CancellationToken ct = default)
    {
        if (outline is null)
            return (null, "No outline supplied to generate a cover for.");

        string title = string.IsNullOrWhiteSpace(outline.Title) ? "Untitled Book" : outline.Title.Trim();

        try
        {
            Directory.CreateDirectory(workFolder);
        }
        catch (Exception ex)
        {
            AppLog.Warning("BookCoverArtGenerator: could not create work folder {Path}: {Error}", workFolder, ex.Message);
            return (null, $"Could not create the work folder \"{workFolder}\": {ex.Message}");
        }

        if (!File.Exists(ffmpegExe))
            return (null, $"ffmpeg.exe was not found at \"{ffmpegExe}\" - a finished cover needs ffmpeg's own resize/crop/title pass even once a base image is generated.");

        (string? basePath, string tier, string resolveNote) = await ResolveBaseImageAsync(outline, workFolder, ct);
        if (basePath is null)
            return (null, resolveNote);

        string outputPath = Path.Combine(workFolder, $"book_cover_{Guid.NewGuid():N}.jpg");
        string renderError = RenderFinalCover(basePath, title, outputPath);
        if (renderError.Length > 0)
        {
            AppLog.Warning("BookCoverArtGenerator: finishing pass failed for \"{Title}\": {Error}", title, renderError);
            return (null, $"A base cover image was generated via {tier}, but the ffmpeg finishing pass (resize/crop/title) failed: {renderError}");
        }

        AppLog.Info("BookCoverArtGenerator: wrote cover {Path} for \"{Title}\" (base image via {Tier})", outputPath, title, tier);
        return (outputPath, $"Cover art generated via {tier}, then resized/cropped to KDP's ideal {KdpCoverWidthPixels}x{KdpCoverHeightPixels} and given a title overlay by ffmpeg.");
    }

    // ==================== Base-image tier resolution ====================

    /// <summary>
    /// Tries each generative image tier in order - OpenAI first (if configured), then Gemini
    /// "Nano Banana Pro" (if OpenAI isn't configured or fails), then YandexART (if neither of
    /// the above is configured or succeeds) - exactly like
    /// ThumbnailVariantGenerator.ResolveSourceFrameAsync's own tier order for its analogous
    /// generative fallbacks. Returns null with an honest, specific reason when no tier produced
    /// a usable image - never a fabricated success.
    /// </summary>
    private async Task<(string? Path, string Tier, string Note)> ResolveBaseImageAsync(BookOutline outline, string workFolder, CancellationToken ct)
    {
        if (!string.IsNullOrEmpty(openAiApiKey))
        {
            string? openAiPath = await TryGenerateBaseImageAsync(outline, workFolder, ct);
            if (openAiPath is not null) return (openAiPath, "OpenAI", "");
            LogFailure("OpenAI-images", outline.Title, "every OpenAI model attempt failed - trying the Gemini fallback next, if configured");
        }

        if (!string.IsNullOrEmpty(geminiApiKey))
        {
            string? geminiPath = await TryGenerateBaseImageViaGeminiAsync(outline, workFolder, ct);
            if (geminiPath is not null) return (geminiPath, "Gemini (Nano Banana Pro)", "");
            LogFailure("Gemini-images", outline.Title, "the Gemini fallback also failed - trying the YandexART fallback next, if configured");
        }

        if (YandexArtFallbackConfigured)
        {
            string? yandexPath = await TryGenerateBaseImageViaYandexArtAsync(outline, workFolder, ct);
            if (yandexPath is not null) return (yandexPath, "YandexART", "");
        }

        bool nothingConfigured = string.IsNullOrEmpty(openAiApiKey) && string.IsNullOrEmpty(geminiApiKey) && !YandexArtFallbackConfigured;
        string reason = nothingConfigured
            ? "No OpenAI, Gemini, or YandexART key is configured (openai_key / gemini_key / yandex_api_key+yandex_folder_id) - nothing to generate a cover image from."
            : "Every configured image-generation tier (OpenAI/Gemini/YandexART) failed to produce a usable base image - see the console/log for the real reason.";
        return (null, "", reason);
    }

    /// <summary>Deliberately asks for NO text/captions/watermark/logo in the generated
    /// illustration - the real title is this class's own drawtext overlay, added identically on
    /// top of whichever tier produced the base image, so the title is always rendered with a
    /// real, legible, spelling-correct font rather than trusting an image model to draw it. Only
    /// includes outline.Setting for story-bible genres (<see cref="BookGenreRules.UsesStoryBible"/>)
    /// when it is non-empty (per <see cref="BookOutline"/>'s own doc comment, Setting is always
    /// empty for NonFiction).</summary>
    private static string BuildCoverImagePrompt(BookOutline outline)
    {
        string title = string.IsNullOrWhiteSpace(outline.Title) ? "Untitled Book" : outline.Title.Trim();
        string premise = string.IsNullOrWhiteSpace(outline.Premise) ? "" : outline.Premise.Trim();
        string settingClause = BookGenreRules.UsesStoryBible(outline.Genre) && !string.IsNullOrWhiteSpace(outline.Setting)
            ? $" Setting: {outline.Setting.Trim()}."
            : "";

        return "A striking, professional, portrait-orientation illustration for a full book cover, for a book titled " +
            $"\"{title}\". Premise: {(premise.Length > 0 ? premise : "see the title")}." + settingClause +
            " Genre-appropriate mood and color palette, one strong focal composition, dramatic lighting, " +
            "art suitable for filling an entire tall book-cover background. No text, no captions, no title " +
            "lettering, no watermark, no logos, no borders - the real title is added afterward as a separate overlay, not by the image itself.";
    }

    // ==================== OpenAI generative fallback (ThumbnailVariantGenerator's exact call shape) ====================

    /// <summary>Tries gpt-image-1 first, retrying once with dall-e-3 only if that specific
    /// attempt looks like an account/key access problem - byte-for-byte the same two-model
    /// retry policy as ThumbnailVariantGenerator.TryGenerateBaseImageAsync.</summary>
    private async Task<string?> TryGenerateBaseImageAsync(BookOutline outline, string workFolder, CancellationToken ct)
    {
        string prompt = BuildCoverImagePrompt(outline);

        (string? path, bool modelUnavailable) = await TryOpenAiImageModelAsync("gpt-image-1", GenerativeImageSize, prompt, workFolder, ct);
        if (path is not null) return path;
        if (!modelUnavailable) return null;

        LogFailure("OpenAI-images", outline.Title, "gpt-image-1 looks unavailable for this key/account - retrying once with dall-e-3");
        (path, _) = await TryOpenAiImageModelAsync("dall-e-3", MapSizeForDalle3(GenerativeImageSize), prompt, workFolder, ct);
        return path;
    }

    private static string MapSizeForDalle3(string gptImageSize) => gptImageSize switch
    {
        "1024x1536" => "1024x1792",
        "1536x1024" => "1792x1024",
        _ => "1024x1024",
    };

    /// <summary>One real call to OpenAI's images/generations endpoint - same request shape/
    /// response parsing/model-unavailable detection/suspiciously-small-response guard as
    /// ThumbnailVariantGenerator.TryOpenAiImageModelAsync, adapted only in what it logs the
    /// query/file names as.</summary>
    private async Task<(string? Path, bool ModelUnavailable)> TryOpenAiImageModelAsync(
        string model, string size, string prompt, string workFolder, CancellationToken ct)
    {
        try
        {
            var payload = new Dictionary<string, object?>
            {
                ["model"] = model,
                ["prompt"] = prompt,
                ["size"] = size,
                ["n"] = 1,
            };
            if (model == "dall-e-3") payload["response_format"] = "b64_json";

            using var request = new HttpRequestMessage(HttpMethod.Post, "https://api.openai.com/v1/images/generations")
            {
                Content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json"),
            };
            request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", openAiApiKey);

            using var response = await Http.SendAsync(request, ct);
            string body = await response.Content.ReadAsStringAsync(ct);

            if (!response.IsSuccessStatusCode)
            {
                bool modelUnavailable = response.StatusCode == HttpStatusCode.Forbidden ||
                    (response.StatusCode == HttpStatusCode.BadRequest &&
                     (body.Contains("model_not_found", StringComparison.OrdinalIgnoreCase) ||
                      body.Contains("does not have access", StringComparison.OrdinalIgnoreCase)));
                LogFailure($"OpenAI-images({model})", "book-cover-base-image", $"HTTP {(int)response.StatusCode}: {Truncate(body, 200)}");
                return (null, modelUnavailable);
            }

            using var doc = JsonDocument.Parse(body);
            if (!doc.RootElement.TryGetProperty("data", out var data) || data.ValueKind != JsonValueKind.Array || data.GetArrayLength() == 0)
            {
                LogFailure($"OpenAI-images({model})", "book-cover-base-image", "response had no image data");
                return (null, false);
            }

            var first = data[0];
            byte[] bytes;
            string? b64 = TryGetString(first, "b64_json");
            if (!string.IsNullOrEmpty(b64))
            {
                bytes = Convert.FromBase64String(b64);
            }
            else
            {
                string? imageUrl = TryGetString(first, "url");
                if (string.IsNullOrEmpty(imageUrl))
                {
                    LogFailure($"OpenAI-images({model})", "book-cover-base-image", "response had neither b64_json nor url");
                    return (null, false);
                }

                using var imgResponse = await Http.GetAsync(imageUrl, ct);
                if (!imgResponse.IsSuccessStatusCode)
                {
                    LogFailure($"OpenAI-images({model})", "book-cover-base-image", $"downloading generated image failed: HTTP {(int)imgResponse.StatusCode}");
                    return (null, false);
                }
                bytes = await imgResponse.Content.ReadAsByteArrayAsync(ct);
            }

            // A real PNG at any of these sizes is always well over this many bytes - guards
            // against a truncated/garbage response being silently treated as a real image.
            if (bytes.Length < 1000)
            {
                LogFailure($"OpenAI-images({model})", "book-cover-base-image", $"returned a suspiciously small image ({bytes.Length} bytes) - treating as a failure, not a fabricated success");
                return (null, false);
            }

            Directory.CreateDirectory(workFolder);
            string fileName = $"book_cover_base_{model.Replace('-', '_')}_{Guid.NewGuid():N}.png";
            string destPath = Path.Combine(workFolder, fileName);
            await File.WriteAllBytesAsync(destPath, bytes, ct);
            return (destPath, false);
        }
        catch (Exception ex) when (ex is not OperationCanceledException)
        {
            LogFailure($"OpenAI-images({model})", "book-cover-base-image", ex.Message);
            return (null, false);
        }
    }

    // ==================== Gemini (Nano Banana Pro) generative fallback ====================

    /// <summary>Real call to Google's Gemini Interactions API for image generation - see this
    /// class's own doc comment for the endpoint/model/shape (carried forward unchanged from
    /// ThumbnailVariantGenerator's own confirmed research) and for the 2:3-portrait-approximation
    /// disclosure. Same "no text/captions/watermark/logo" prompt instruction as
    /// BuildCoverImagePrompt gives every tier, for the identical reason (this class's own
    /// drawtext-based title overlay is the real title-rendering mechanism, not the image
    /// model).</summary>
    private async Task<string?> TryGenerateBaseImageViaGeminiAsync(BookOutline outline, string workFolder, CancellationToken ct)
    {
        string prompt = BuildCoverImagePrompt(outline);

        try
        {
            var bodyDict = new Dictionary<string, object>
            {
                ["model"] = GeminiImageModel,
                ["input"] = prompt,
                ["response_format"] = new Dictionary<string, object>
                {
                    ["type"] = "image",
                    ["mime_type"] = "image/jpeg",
                    ["aspect_ratio"] = "2:3",
                },
            };

            using var request = new HttpRequestMessage(HttpMethod.Post, GeminiInteractionsEndpoint)
            {
                Content = new StringContent(JsonSerializer.Serialize(bodyDict), Encoding.UTF8, "application/json"),
            };
            request.Headers.Add("x-goog-api-key", geminiApiKey);

            using HttpResponseMessage response = await Http.SendAsync(request, ct);
            byte[] body = await response.Content.ReadAsByteArrayAsync(ct);

            if (!response.IsSuccessStatusCode)
            {
                LogFailure("Gemini-images", outline.Title, BuildGeminiErrorMessage(response, body));
                return null;
            }

            byte[]? imageBytes = TryExtractGeminiImage(body);
            if (imageBytes is null || imageBytes.Length < 1000)
            {
                LogFailure("Gemini-images", outline.Title, imageBytes is null
                    ? "response parsing failed: no image content block found in a successful response"
                    : $"returned a suspiciously small image ({imageBytes.Length} bytes) - treating as a failure, not a fabricated success");
                return null;
            }

            Directory.CreateDirectory(workFolder);
            string destPath = Path.Combine(workFolder, $"book_cover_base_gemini_{Guid.NewGuid():N}.jpg");
            await File.WriteAllBytesAsync(destPath, imageBytes, ct);
            return destPath;
        }
        catch (Exception ex) when (ex is not OperationCanceledException)
        {
            LogFailure("Gemini-images", outline.Title, ex.Message);
            return null;
        }
    }

    /// <summary>Tries the documented "output_image.data" convenience accessor first, then falls
    /// back to the same real steps[]/content[] walk LyriaMusicGenerator.TryExtractAudio already
    /// uses for this exact endpoint family, just matching an "image" block type instead of
    /// "audio" - identical logic to ThumbnailVariantGenerator.TryExtractGeminiImage.</summary>
    private static byte[]? TryExtractGeminiImage(byte[] body)
    {
        try
        {
            using var doc = JsonDocument.Parse(body);
            JsonElement root = doc.RootElement;
            JsonElement obj = root.ValueKind == JsonValueKind.Array && root.GetArrayLength() > 0 ? root[0] : root;

            if (obj.TryGetProperty("output_image", out var outputImage) &&
                outputImage.TryGetProperty("data", out var directDataEl) && directDataEl.ValueKind == JsonValueKind.String)
            {
                string? directBase64 = directDataEl.GetString();
                if (!string.IsNullOrEmpty(directBase64))
                    return Convert.FromBase64String(directBase64);
            }

            if (!obj.TryGetProperty("steps", out var steps) || steps.ValueKind != JsonValueKind.Array)
                return null;

            foreach (var step in steps.EnumerateArray())
            {
                if (!step.TryGetProperty("content", out var content) || content.ValueKind != JsonValueKind.Array)
                    continue;

                foreach (var block in content.EnumerateArray())
                {
                    if (block.TryGetProperty("type", out var typeEl) && typeEl.ValueKind == JsonValueKind.String &&
                        typeEl.GetString() == "image" &&
                        block.TryGetProperty("data", out var dataEl) && dataEl.ValueKind == JsonValueKind.String)
                    {
                        string? base64 = dataEl.GetString();
                        if (!string.IsNullOrEmpty(base64))
                            return Convert.FromBase64String(base64);
                    }
                }
            }

            return null;
        }
        catch
        {
            return null;
        }
    }

    /// <summary>Same real single-element-array-or-bare-object {"error":{"code","status",
    /// "message"}} envelope ThumbnailVariantGenerator.BuildGeminiErrorMessage already uses
    /// against this exact endpoint.</summary>
    private static string BuildGeminiErrorMessage(HttpResponseMessage response, byte[] body)
    {
        string raw = "";
        try { raw = Encoding.UTF8.GetString(body); } catch { /* non-UTF8 body - fall through */ }

        string reason = "";
        try
        {
            using var doc = JsonDocument.Parse(raw);
            JsonElement root = doc.RootElement;
            JsonElement obj = root.ValueKind == JsonValueKind.Array && root.GetArrayLength() > 0 ? root[0] : root;

            if (obj.TryGetProperty("error", out var errorEl))
            {
                string code = errorEl.TryGetProperty("code", out var codeEl) ? codeEl.ToString() : "";
                string status = errorEl.TryGetProperty("status", out var statusEl) ? statusEl.GetString() ?? "" : "";
                string message = errorEl.TryGetProperty("message", out var msgEl) ? msgEl.GetString() ?? "" : "";
                reason = string.Join(" ", new[] { code, status, message }.Where(s => s.Length > 0));
            }
        }
        catch { /* not JSON - reason stays "", raw is used below instead */ }

        return $"HTTP {(int)response.StatusCode}: {(reason.Length > 0 ? reason : (raw.Length > 0 ? Truncate(raw, 200) : (response.ReasonPhrase ?? "")))}";
    }

    // ==================== YandexART (Yandex Cloud Foundation Models) generative fallback - ASYNC JOB ====================

    /// <summary>Submits one YandexART imageGenerationAsync job and polls it to completion - see
    /// this class's own top doc comment for the disclosed lower-confidence caveat on this exact
    /// request/response shape (carried forward unchanged from ThumbnailVariantGenerator's own
    /// research). Same "no text/captions/watermark/logo" prompt instruction as
    /// BuildCoverImagePrompt gives every tier, for the identical reason.</summary>
    private async Task<string?> TryGenerateBaseImageViaYandexArtAsync(BookOutline outline, string workFolder, CancellationToken ct)
    {
        string prompt = BuildCoverImagePrompt(outline);
        string modelUri = $"art://{yandexFolderId}/{YandexArtModelName}/latest";

        try
        {
            var payload = new Dictionary<string, object?>
            {
                ["modelUri"] = modelUri,
                ["messages"] = new object[]
                {
                    new Dictionary<string, object?> { ["weight"] = 1, ["text"] = prompt },
                },
                ["generationOptions"] = new Dictionary<string, object?>
                {
                    // Every documented example includes mimeType explicitly (currently the only
                    // supported value) rather than relying on an implicit default.
                    ["mimeType"] = "image/jpeg",
                    // Same 2:3 portrait approximation and same "corrected afterward by this
                    // class's own ffmpeg pass" reasoning as Gemini's own aspect_ratio above.
                    ["aspectRatio"] = new Dictionary<string, object?> { ["widthRatio"] = "2", ["heightRatio"] = "3" },
                },
            };

            using var submitRequest = new HttpRequestMessage(HttpMethod.Post, YandexArtSubmitEndpoint)
            {
                Content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json"),
            };
            submitRequest.Headers.Authorization = new AuthenticationHeaderValue("Api-Key", yandexApiKey);

            using HttpResponseMessage submitResponse = await Http.SendAsync(submitRequest, ct);
            string submitBody = await submitResponse.Content.ReadAsStringAsync(ct);

            if (!submitResponse.IsSuccessStatusCode)
            {
                LogFailure("YandexArt-images", outline.Title, $"submitting the generation job failed: HTTP {(int)submitResponse.StatusCode}: {Truncate(submitBody, 200)}");
                return null;
            }

            string? operationId = TryGetYandexOperationId(submitBody);
            if (string.IsNullOrEmpty(operationId))
            {
                LogFailure("YandexArt-images", outline.Title, "submit response had no recognizable operation id - cannot poll for a result");
                return null;
            }

            (byte[]? imageBytes, string pollError) = await PollYandexArtOperationAsync(operationId, ct);
            if (imageBytes is null)
            {
                LogFailure("YandexArt-images", outline.Title, pollError);
                return null;
            }

            // A real JPEG cover base image is always well over this many bytes - guards
            // against a truncated/garbage response being silently treated as a real image,
            // same guard TryOpenAiImageModelAsync/TryGenerateBaseImageViaGeminiAsync both apply.
            if (imageBytes.Length < 1000)
            {
                LogFailure("YandexArt-images", outline.Title, $"returned a suspiciously small image ({imageBytes.Length} bytes) - treating as a failure, not a fabricated success");
                return null;
            }

            Directory.CreateDirectory(workFolder);
            string destPath = Path.Combine(workFolder, $"book_cover_base_yandexart_{Guid.NewGuid():N}.jpg");
            await File.WriteAllBytesAsync(destPath, imageBytes, ct);
            return destPath;
        }
        catch (Exception ex) when (ex is not OperationCanceledException)
        {
            LogFailure("YandexArt-images", outline.Title, ex.Message);
            return null;
        }
    }

    /// <summary>Polls GET operation.api.cloud.yandex.net/operations/{id} until the envelope's
    /// own "done":true, modeled on NovaReelVideoGenerator.PollUntilDoneAsync's own real
    /// submit-then-poll loop shape for a different (video) async job on a different provider -
    /// identical logic to ThumbnailVariantGenerator.PollYandexArtOperationAsync.</summary>
    private async Task<(byte[]? ImageBytes, string Error)> PollYandexArtOperationAsync(string operationId, CancellationToken ct)
    {
        DateTime deadline = DateTime.UtcNow + YandexArtPollTimeout;
        string operationUrl = string.Format(YandexArtOperationEndpointFormat, operationId);

        while (true)
        {
            ct.ThrowIfCancellationRequested();

            string pollBody;
            try
            {
                using var pollRequest = new HttpRequestMessage(HttpMethod.Get, operationUrl);
                pollRequest.Headers.Authorization = new AuthenticationHeaderValue("Api-Key", yandexApiKey);

                using HttpResponseMessage pollResponse = await Http.SendAsync(pollRequest, ct);
                pollBody = await pollResponse.Content.ReadAsStringAsync(ct);

                if (!pollResponse.IsSuccessStatusCode)
                    return (null, $"polling the generation job failed: HTTP {(int)pollResponse.StatusCode}: {Truncate(pollBody, 200)}");
            }
            catch (OperationCanceledException) { throw; }
            catch (Exception ex)
            {
                return (null, "polling the generation job failed: " + ex.Message);
            }

            try
            {
                using var doc = JsonDocument.Parse(pollBody);
                JsonElement root = doc.RootElement;

                bool done = root.TryGetProperty("done", out var doneEl) && doneEl.ValueKind == JsonValueKind.True;
                if (!done)
                {
                    if (DateTime.UtcNow > deadline)
                        return (null, $"generation job timed out after {YandexArtPollTimeout.TotalSeconds:F0}s waiting for operation \"{operationId}\".");

                    await Task.Delay(YandexArtPollInterval, ct);
                    continue;
                }

                if (root.TryGetProperty("error", out var errorEl) && errorEl.ValueKind == JsonValueKind.Object)
                {
                    string message = errorEl.TryGetProperty("message", out var msgEl) && msgEl.ValueKind == JsonValueKind.String
                        ? msgEl.GetString() ?? ""
                        : "";
                    return (null, "generation job reported an error: " + (message.Length > 0 ? message : Truncate(pollBody, 200)));
                }

                if (root.TryGetProperty("response", out var responseEl) &&
                    responseEl.TryGetProperty("image", out var imageEl) && imageEl.ValueKind == JsonValueKind.String)
                {
                    string? b64 = imageEl.GetString();
                    if (!string.IsNullOrEmpty(b64))
                        return (Convert.FromBase64String(b64), "");
                }

                return (null, "generation job finished but the response had no recognizable image data.");
            }
            catch (Exception ex)
            {
                return (null, "parsing the generation job's status response failed: " + ex.Message);
            }
        }
    }

    /// <summary>Pulls the submit response's top-level "id" field (the long-running operation id
    /// to poll next) - identical logic to ThumbnailVariantGenerator.TryGetYandexOperationId.</summary>
    private static string? TryGetYandexOperationId(string body)
    {
        try
        {
            using var doc = JsonDocument.Parse(body);
            return doc.RootElement.TryGetProperty("id", out var idEl) && idEl.ValueKind == JsonValueKind.String
                ? idEl.GetString()
                : null;
        }
        catch
        {
            return null;
        }
    }

    // ==================== ffmpeg finishing pass: resize/crop to KDP spec + title overlay ====================

    /// <summary>
    /// The two real finishing steps every base image (whichever tier produced it) goes through,
    /// combined into a single ffmpeg -vf pass: (a) scale+crop to EXACTLY KDP's ideal
    /// <see cref="KdpCoverWidthPixels"/>x<see cref="KdpCoverHeightPixels"/> cover dimensions
    /// regardless of which tier's own approximate portrait aspect ratio actually produced the
    /// base image, using "scale=W:H:force_original_aspect_ratio=increase,crop=W:H"; then (b)
    /// drawtext the real title over a semi-translucent box near the lower third - a basic,
    /// legible title treatment, not full professional cover typography/layout (see this class's
    /// own doc comment). Builds to a same-directory temp file first and only File.Move(...)'s it
    /// into place once that temp file is confirmed to exist and be non-empty; the leftover temp
    /// file is deleted (best-effort) on any failure.
    /// </summary>
    private string RenderFinalCover(string baseImagePath, string title, string outputPath)
    {
        string tempPath = "";
        try
        {
            if (!File.Exists(baseImagePath)) return $"Base cover image was not found at \"{baseImagePath}\".";

            string? outDir = Path.GetDirectoryName(outputPath);
            if (!string.IsNullOrEmpty(outDir)) Directory.CreateDirectory(outDir);

            string dirForTemp = string.IsNullOrEmpty(outDir) ? "." : outDir;
            tempPath = Path.Combine(dirForTemp, $"~{Path.GetFileName(outputPath)}.{Guid.NewGuid():N}.tmp");

            string fontPath = ResolveFont(FontGeorgia);
            string fontWorkingDirectory = Path.GetDirectoryName(Path.GetFullPath(fontPath)) ?? "";
            string fontFileArg = Path.GetFileName(fontPath); // bare filename - see class doc comment (font-file colon quirk)

            string displayTitle = BuildDisplayTitle(title);

            int fontSize = Math.Clamp(KdpCoverWidthPixels / 13, 60, 150);
            int boxBorderWidth = Math.Max(24, KdpCoverWidthPixels / 40);
            // Anchored around 78% down the cover (the lower third), not flush to the very
            // bottom edge, so the title box doesn't collide with a printed spine/trim area.
            string yExpr = (KdpCoverHeightPixels * 78 / 100).ToString(CultureInfo.InvariantCulture) + "-text_h/2";

            string filters =
                $"scale={KdpCoverWidthPixels}:{KdpCoverHeightPixels}:force_original_aspect_ratio=increase," +
                $"crop={KdpCoverWidthPixels}:{KdpCoverHeightPixels}," +
                "drawtext=fontfile=" + fontFileArg +
                ":" + DrawtextEscaping.TextClause(displayTitle) +
                ":fontsize=" + fontSize.ToString(CultureInfo.InvariantCulture) +
                ":fontcolor=0xFFFFFF" +
                ":borderw=3:bordercolor=black@0.85" +
                ":box=1:boxcolor=black@0.55:boxborderw=" + boxBorderWidth.ToString(CultureInfo.InvariantCulture) +
                ":x=(w-text_w)/2:y=" + yExpr;

            string arguments = $"-y -i \"{baseImagePath}\" -vf \"{filters}\" -frames:v 1 -q:v 2 \"{tempPath}\"";
            RunFfmpeg(arguments, fontWorkingDirectory);

            if (!File.Exists(tempPath) || new FileInfo(tempPath).Length == 0)
            {
                TryDeleteTemp(tempPath);
                return "ffmpeg ran but produced no cover output file.";
            }

            File.Move(tempPath, outputPath, overwrite: true);
            return "";
        }
        catch (Exception ex)
        {
            TryDeleteTemp(tempPath);
            return "ffmpeg finishing pass failed: " + ex.Message;
        }
    }

    /// <summary>Book-cover title treatment: collapses any internal line breaks to a single
    /// line, then uppercases it - a basic legible treatment, not full cover typography (see
    /// this class's own doc comment).</summary>
    private static string BuildDisplayTitle(string title)
    {
        string oneLine = title.Replace("\r\n", " ").Replace('\r', ' ').Replace('\n', ' ').Trim();
        return oneLine.Length == 0 ? "UNTITLED" : oneLine.ToUpperInvariant();
    }

    /// <summary>Returns fontFilePath unchanged if it exists on disk; otherwise FontFallback
    /// (Arial Bold, ships on every Windows install this app targets) - same
    /// never-fail-the-whole-render-over-one-missing-font-file spirit as
    /// ThumbnailVariantGenerator.ResolveFont.</summary>
    private static string ResolveFont(string fontFilePath) => File.Exists(fontFilePath) ? fontFilePath : FontFallback;

    private void RunFfmpeg(string arguments, string? workingDirectory)
    {
        using var proc = new Process();
        proc.StartInfo = new ProcessStartInfo
        {
            FileName = ffmpegExe,
            Arguments = arguments,
            UseShellExecute = false,
            CreateNoWindow = true,
            WorkingDirectory = workingDirectory ?? "",
        };
        proc.Start();
        proc.WaitForExit();
        if (proc.ExitCode != 0)
            throw new InvalidOperationException($"ffmpeg failed (exit code {proc.ExitCode}): {arguments}");
    }

    /// <summary>Best-effort cleanup of a leftover temp file after a failed render - deliberately
    /// swallows any exception of its own (a locked/already-gone file here must never mask the
    /// real failure the caller is already reporting).</summary>
    private static void TryDeleteTemp(string path)
    {
        try
        {
            if (path.Length > 0 && File.Exists(path))
                File.Delete(path);
        }
        catch
        {
            // Best-effort only - a failure to delete a temp file is not worth surfacing.
        }
    }

    private static string? TryGetString(JsonElement element, string propertyName) =>
        element.TryGetProperty(propertyName, out var prop) && prop.ValueKind == JsonValueKind.String ? prop.GetString() : null;

    private static string Truncate(string s, int maxLength) => s.Length <= maxLength ? s : s[..maxLength] + "...";

    /// <summary>Internal, non-throwing log of a genuine failure - a failed generative call or
    /// ffmpeg pass is a diagnosable warning, not a reason to crash a caller.</summary>
    private static void LogFailure(string stage, string context, string reason) =>
        AppLog.Warning("BookCoverArtGenerator: {Stage} failed for {Context} - {Reason}", stage, context, reason);
}

