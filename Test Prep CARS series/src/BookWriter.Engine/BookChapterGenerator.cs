using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace BookWriter.Engine;

/// <summary>
/// Expands one chapter of a BookOutline into full prose. Mirrors ScriptGenerator's own 5-tier
/// provider chain and freeform-prose contract exactly (Claude, then Gemini, then Grok, then
/// YandexGPT, then OpenAI, same honest-degrade "any failure falls through" convention) -- this
/// is the same kind of task (long-form creative/expository writing) ScriptGenerator already
/// solves, just for a book chapter instead of a video script.
///
/// CONTINUITY DESIGN: rather than tracking a separate, evolving "story so far" summary updated
/// after every chapter (which would need its own extra AI call per chapter, doubling cost and
/// adding a second failure point), every chapter call instead receives the WHOLE BookOutline --
/// every chapter's own title+summary (not just prior ones, ALL of them), plus the Fiction book
/// bible (characters/setting/plotArc) when present -- and is told to write ONLY the one
/// requested chapter's full prose. Since the outline itself is compact (a few sentences per
/// chapter) this fits comfortably in context even for a 30+ chapter book, and guarantees every
/// chapter is grounded against the exact same fixed plan rather than a summary that could drift
/// from what earlier chapters actually ended up containing.
/// </summary>
public sealed class BookChapterGenerator(string openAiApiKey, string anthropicApiKey = "", string geminiApiKey = "", string xaiApiKey = "", string yandexApiKey = "", string yandexFolderId = "")
{
    private const string AnthropicModel = "claude-sonnet-5";
    private const string GeminiModel = "gemini-3.6-flash";
    private const string GrokModel = "grok-4.5";
    private const string YandexModel = "yandexgpt/latest";
    private const string OpenAiModel = "gpt-4o-mini";

    private static readonly HttpClient Http = new() { Timeout = TimeSpan.FromMinutes(3) };

    public bool AnthropicConfigured => !string.IsNullOrWhiteSpace(anthropicApiKey);
    public bool GeminiConfigured => !string.IsNullOrWhiteSpace(geminiApiKey);
    public bool XaiConfigured => !string.IsNullOrWhiteSpace(xaiApiKey);
    public bool YandexConfigured => !string.IsNullOrWhiteSpace(yandexApiKey) && !string.IsNullOrWhiteSpace(yandexFolderId);

    private static string BuildSystemPrompt(BookOutline outline)
    {
        var sb = new StringBuilder();
        sb.Append("You are a professional author writing one chapter of a full-length ").Append(outline.Genre).Append(" book. ");
        sb.Append("Book title: \"").Append(outline.Title).Append("\". Premise: ").Append(outline.Premise).Append(' ');

        if (BookGenreRules.UsesStoryBible(outline.Genre))
        {
            if (outline.Characters.Count > 0)
            {
                sb.Append("Characters (keep names/descriptions/roles exactly consistent with this list): ");
                foreach (BookCharacter c in outline.Characters)
                    sb.Append(c.Name).Append(" (").Append(c.Role).Append("): ").Append(c.Description).Append(". ");
            }
            if (outline.Setting.Length > 0) sb.Append("Setting: ").Append(outline.Setting).Append(' ');
            if (outline.PlotArc.Length > 0) sb.Append("Overall plot arc: ").Append(outline.PlotArc).Append(' ');
        }

        sb.Append("Full chapter plan for the whole book (for your own context/consistency only -- do NOT write any chapter but the one requested below):\n");
        foreach (ChapterOutline ch in outline.Chapters)
            sb.Append(ch.Number).Append(". ").Append(ch.Title).Append(" - ").Append(ch.Summary).Append('\n');

        if (BookGenreRules.IsExamPrep(outline.Genre))
            sb.Append('\n').Append(ExamPrepRules.ChapterSystemGuidance()).Append('\n');

        sb.Append("\nWrite ONLY the full prose text of the one requested chapter below. No chapter-number heading, no title line, no meta-commentary -- just the chapter's own narrative/expository prose, ready to drop directly into the manuscript.");
        return sb.ToString();
    }

    private static string BuildUserMessage(ChapterOutline chapter, BookOutline outline)
    {
        if (BookGenreRules.IsExamPrep(outline.Genre))
            return ExamPrepRules.BuildChapterRequest(chapter);

        if (BookGenreRules.HasScienceAppendix(outline.Genre) && BookGenreRules.LooksLikeAppendixChapter(chapter.Title))
        {
            return $"Write the science appendix section \"{chapter.Title}\" now (this is chapter {chapter.Number} of the book). " +
                   "This is NOT narrative fiction -- write clear, accurate, expository science prose that explains the real science " +
                   $"behind themes, technologies, or phenomena from the story. Cover: {chapter.Summary} " +
                   "Use accessible but rigorous language; explain real concepts, mechanisms, and evidence; do not invent fake science " +
                   "or continue the fictional plot as story beats. No chapter-number heading, no title line, no meta-commentary -- just the appendix prose.";
        }

        return $"Write chapter {chapter.Number}, \"{chapter.Title}\", now. This chapter should cover: {chapter.Summary}";
    }

    /// <summary>Never throws for an ordinary provider failure -- falls through every configured
    /// tier in order, same honest-degrade contract as ScriptGenerator.GenerateScriptTextAsync.
    /// Returns ("", reason) only if every configured tier failed or none was configured at
    /// all.</summary>
    public async Task<(string ChapterText, string Error)> GenerateChapterAsync(BookOutline outline, int chapterIndex, CancellationToken ct = default)
    {
        if (chapterIndex < 0 || chapterIndex >= outline.Chapters.Count)
            return ("", $"Chapter index {chapterIndex} is out of range for a {outline.Chapters.Count}-chapter outline.");

        ChapterOutline chapter = outline.Chapters[chapterIndex];
        string systemPrompt = BuildSystemPrompt(outline);
        string userMessage = BuildUserMessage(chapter, outline);

        if (AnthropicConfigured)
        {
            (string text, string error) = await GenerateViaAnthropicAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return (text, "");
            AppLog.Warning("BookChapterGenerator: Claude failed for chapter {Number} - {Error}", chapter.Number, error);
        }
        if (GeminiConfigured)
        {
            (string text, string error) = await GenerateViaGeminiAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return (text, "");
            AppLog.Warning("BookChapterGenerator: Gemini failed for chapter {Number} - {Error}", chapter.Number, error);
        }
        if (XaiConfigured)
        {
            (string text, string error) = await GenerateViaGrokAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return (text, "");
            AppLog.Warning("BookChapterGenerator: Grok failed for chapter {Number} - {Error}", chapter.Number, error);
        }
        if (YandexConfigured)
        {
            (string text, string error) = await GenerateViaYandexAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return (text, "");
            AppLog.Warning("BookChapterGenerator: YandexGPT failed for chapter {Number} - {Error}", chapter.Number, error);
        }
        if (!string.IsNullOrWhiteSpace(openAiApiKey))
        {
            (string text, string error) = await GenerateViaOpenAiAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return (text, "");
            return ("", error);
        }

        return ("", "No AI provider is configured -- cannot write this chapter.");
    }

    private async Task<(string Text, string Error)> GenerateViaAnthropicAsync(string systemPrompt, string userMessage, CancellationToken ct)
    {
        try
        {
            var requestBody = new
            {
                model = AnthropicModel,
                max_tokens = 8192,
                system = systemPrompt,
                messages = new object[] { new { role = "user", content = userMessage } },
            };

            using var request = new HttpRequestMessage(HttpMethod.Post, "https://api.anthropic.com/v1/messages");
            request.Headers.TryAddWithoutValidation("x-api-key", anthropicApiKey);
            request.Headers.TryAddWithoutValidation("anthropic-version", "2023-06-01");
            request.Content = new StringContent(JsonSerializer.Serialize(requestBody), Encoding.UTF8, "application/json");

            using HttpResponseMessage response = await Http.SendAsync(request, ct);
            string body = await response.Content.ReadAsStringAsync(ct);
            if (!response.IsSuccessStatusCode)
                return ("", $"Anthropic request failed ({(int)response.StatusCode}): {Truncate(body, 300)}");

            using var doc = JsonDocument.Parse(body);
            string? stopReason = doc.RootElement.TryGetProperty("stop_reason", out var srEl) ? srEl.GetString() : null;

            var textBuilder = new StringBuilder();
            if (doc.RootElement.TryGetProperty("content", out var contentEl) && contentEl.ValueKind == JsonValueKind.Array)
            {
                foreach (JsonElement block in contentEl.EnumerateArray())
                {
                    if (block.TryGetProperty("type", out var typeEl) && typeEl.GetString() == "text" &&
                        block.TryGetProperty("text", out var textEl) && textEl.ValueKind == JsonValueKind.String)
                        textBuilder.Append(textEl.GetString());
                }
            }

            if (string.Equals(stopReason, "max_tokens", StringComparison.OrdinalIgnoreCase))
                return ("", "Anthropic's response hit the token limit before finishing this chapter.");

            string text = StripMarkdownFences(textBuilder.ToString().Trim());
            return text.Length > 0 ? (text, "") : ("", "Anthropic returned an empty chapter.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "Anthropic chapter generation failed: " + ex.Message); }
    }

    private async Task<(string Text, string Error)> GenerateViaGeminiAsync(string systemPrompt, string userMessage, CancellationToken ct)
    {
        try
        {
            var bodyDict = new Dictionary<string, object>
            {
                ["model"] = GeminiModel,
                ["input"] = userMessage,
                ["system_instruction"] = systemPrompt,
                ["generation_config"] = new Dictionary<string, object> { ["max_output_tokens"] = 8192 },
            };

            using var request = new HttpRequestMessage(HttpMethod.Post, "https://generativelanguage.googleapis.com/v1beta/interactions")
            {
                Content = new StringContent(JsonSerializer.Serialize(bodyDict), Encoding.UTF8, "application/json"),
            };
            request.Headers.Add("x-goog-api-key", geminiApiKey);

            using HttpResponseMessage response = await Http.SendAsync(request, ct);
            string body = await response.Content.ReadAsStringAsync(ct);
            if (!response.IsSuccessStatusCode)
                return ("", $"Gemini request failed ({(int)response.StatusCode}): {Truncate(body, 300)}");

            using var doc = JsonDocument.Parse(body);
            JsonElement root = doc.RootElement;
            JsonElement obj = root.ValueKind == JsonValueKind.Array && root.GetArrayLength() > 0 ? root[0] : root;

            string? status = obj.TryGetProperty("status", out var statusEl) ? statusEl.GetString() : null;
            if (string.Equals(status, "incomplete", StringComparison.OrdinalIgnoreCase) ||
                string.Equals(status, "budget_exceeded", StringComparison.OrdinalIgnoreCase))
                return ("", "Gemini's response hit the token limit before finishing this chapter.");

            var textBuilder = new StringBuilder();
            if (obj.TryGetProperty("steps", out var steps) && steps.ValueKind == JsonValueKind.Array)
            {
                foreach (JsonElement step in steps.EnumerateArray())
                {
                    if (!step.TryGetProperty("type", out var stEl) || stEl.GetString() != "model_output") continue;
                    if (!step.TryGetProperty("content", out var cEl) || cEl.ValueKind != JsonValueKind.Array) continue;
                    foreach (JsonElement block in cEl.EnumerateArray())
                    {
                        if (block.TryGetProperty("type", out var bt) && bt.GetString() == "text" &&
                            block.TryGetProperty("text", out var te) && te.ValueKind == JsonValueKind.String)
                            textBuilder.Append(te.GetString());
                    }
                }
            }

            string text = StripMarkdownFences(textBuilder.ToString().Trim());
            return text.Length > 0 ? (text, "") : ("", "Gemini returned an empty chapter.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "Gemini chapter generation failed: " + ex.Message); }
    }

    private async Task<(string Text, string Error)> GenerateViaGrokAsync(string systemPrompt, string userMessage, CancellationToken ct)
    {
        try
        {
            var payload = new
            {
                model = GrokModel,
                input = new object[]
                {
                    new { role = "system", content = systemPrompt },
                    new { role = "user", content = userMessage },
                },
            };

            using var request = new HttpRequestMessage(HttpMethod.Post, "https://api.x.ai/v1/responses")
            {
                Content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json"),
            };
            request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", xaiApiKey);

            using HttpResponseMessage response = await Http.SendAsync(request, ct);
            string body = await response.Content.ReadAsStringAsync(ct);
            if (!response.IsSuccessStatusCode)
                return ("", $"Grok request failed ({(int)response.StatusCode}): {Truncate(body, 300)}");

            string text = StripMarkdownFences(ExtractGrokOutputText(body).Trim());
            return text.Length > 0 ? (text, "") : ("", "Grok returned an empty chapter.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "Grok chapter generation failed: " + ex.Message); }
    }

    private static string ExtractGrokOutputText(string responseJson)
    {
        using var doc = JsonDocument.Parse(responseJson);
        var sb = new StringBuilder();
        if (doc.RootElement.TryGetProperty("output", out JsonElement output) && output.ValueKind == JsonValueKind.Array)
        {
            foreach (JsonElement item in output.EnumerateArray())
            {
                if (!item.TryGetProperty("type", out JsonElement typeEl) || typeEl.GetString() != "message") continue;
                if (!item.TryGetProperty("content", out JsonElement content) || content.ValueKind != JsonValueKind.Array) continue;
                foreach (JsonElement block in content.EnumerateArray())
                {
                    if (block.TryGetProperty("type", out JsonElement bt) && bt.GetString() == "output_text" &&
                        block.TryGetProperty("text", out JsonElement te) && te.GetString() is string t)
                        sb.Append(t);
                }
            }
        }
        return sb.ToString();
    }

    private async Task<(string Text, string Error)> GenerateViaYandexAsync(string systemPrompt, string userMessage, CancellationToken ct)
    {
        try
        {
            var requestBody = new
            {
                modelUri = $"gpt://{yandexFolderId}/{YandexModel}",
                completionOptions = new { stream = false, temperature = 0.8, maxTokens = "8192" },
                messages = new object[]
                {
                    new { role = "system", text = systemPrompt },
                    new { role = "user", text = userMessage },
                },
            };

            using var request = new HttpRequestMessage(HttpMethod.Post, "https://llm.api.cloud.yandex.net/foundationModels/v1/completion")
            {
                Content = new StringContent(JsonSerializer.Serialize(requestBody), Encoding.UTF8, "application/json"),
            };
            request.Headers.TryAddWithoutValidation("Authorization", $"Api-Key {yandexApiKey}");

            using HttpResponseMessage response = await Http.SendAsync(request, ct);
            string body = await response.Content.ReadAsStringAsync(ct);
            if (!response.IsSuccessStatusCode)
                return ("", $"YandexGPT request failed ({(int)response.StatusCode}): {Truncate(body, 300)}");

            using var doc = JsonDocument.Parse(body);
            string text = StripMarkdownFences((doc.RootElement.GetProperty("alternatives")[0].GetProperty("message").GetProperty("text").GetString() ?? "").Trim());
            return text.Length > 0 ? (text, "") : ("", "YandexGPT returned an empty chapter.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "YandexGPT chapter generation failed: " + ex.Message); }
    }

    private async Task<(string Text, string Error)> GenerateViaOpenAiAsync(string systemPrompt, string userMessage, CancellationToken ct)
    {
        try
        {
            var payload = new
            {
                model = OpenAiModel,
                messages = new object[]
                {
                    new { role = "system", content = systemPrompt },
                    new { role = "user", content = userMessage },
                },
                temperature = 0.8,
                max_tokens = 4096,
            };

            using var request = new HttpRequestMessage(HttpMethod.Post, "https://api.openai.com/v1/chat/completions")
            {
                Content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json"),
            };
            request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", openAiApiKey);

            using HttpResponseMessage response = await Http.SendAsync(request, ct);
            string body = await response.Content.ReadAsStringAsync(ct);
            if (!response.IsSuccessStatusCode)
                return ("", $"OpenAI request failed ({(int)response.StatusCode}): {Truncate(body, 300)}");

            using var doc = JsonDocument.Parse(body);
            JsonElement firstChoice = doc.RootElement.GetProperty("choices")[0];
            string? finishReason = firstChoice.TryGetProperty("finish_reason", out var frEl) ? frEl.GetString() : null;
            if (string.Equals(finishReason, "length", StringComparison.OrdinalIgnoreCase))
                return ("", "OpenAI's response hit the max_tokens limit before finishing this chapter.");

            string text = StripMarkdownFences((firstChoice.GetProperty("message").GetProperty("content").GetString() ?? "").Trim());
            return text.Length > 0 ? (text, "") : ("", "OpenAI returned an empty chapter.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "OpenAI chapter generation failed: " + ex.Message); }
    }

    private static string StripMarkdownFences(string s)
    {
        s = s.Trim();
        if (!s.StartsWith("```")) return s;

        int firstNewline = s.IndexOf('\n');
        if (firstNewline >= 0) s = s[(firstNewline + 1)..];
        int lastFence = s.LastIndexOf("```", StringComparison.Ordinal);
        if (lastFence >= 0) s = s[..lastFence];
        return s.Trim();
    }

    private static string Truncate(string s, int maxLen) => s.Length <= maxLen ? s : s[..maxLen].TrimEnd();
}

