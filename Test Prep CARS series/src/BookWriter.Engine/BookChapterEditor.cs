using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace BookWriter.Engine;

/// <summary>Everything <see cref="BookChapterEditor"/> needs about the book a chapter belongs
/// to that is not the chapter's own text: the title and genre (for voice), and the number +
/// title of every chapter (so a continuity check and an <see cref="EditPass.Hyperlinks"/>
/// <c>[text](chapter:N)</c> link both have something real to point at). Deliberately does NOT
/// carry other chapters' prose -- titles are enough to ground an edit, and full text for every
/// chapter would blow up cost and context on a long book, the same trade-off
/// <see cref="BookChapterGenerator"/> makes.</summary>
public sealed class BookEditContext
{
    public string Title { get; init; } = "";
    public BookGenre Genre { get; init; }
    public IReadOnlyList<(int Number, string Title)> AllChapters { get; init; } = Array.Empty<(int, string)>();
}

/// <summary>The outcome of one chapter edit. <see cref="Error"/> is empty on success;
/// <see cref="Changed"/> is false when the editor deliberately returned the chapter untouched
/// ("no changes needed"). On failure <see cref="RevisedText"/> is empty and the caller keeps
/// the original chapter.</summary>
public sealed record ChapterEditResult(string RevisedText, string ChangeSummary, bool Changed, string Error)
{
    public static ChapterEditResult Failed(string error) => new("", "", false, error);
}

/// <summary>
/// Revises one already-written chapter in place, applying a chosen set of
/// <see cref="EditPass"/>es in a single provider call. Mirrors
/// <see cref="BookChapterGenerator"/>'s own 5-tier provider chain and honest-degrade contract
/// exactly (Claude, then Gemini, then Grok, then YandexGPT, then OpenAI; any tier failing falls
/// through to the next; every tier failing returns an honest <see cref="ChapterEditResult.Error"/>
/// rather than a fabricated edit) -- editing a chapter is the same class of long-form task as
/// writing one, just seeded with existing prose instead of an outline entry.
///
/// The model is told to return the ENTIRE revised chapter followed by a
/// <c>---CHANGES---</c> marker and a short bullet list of what it changed. This class splits
/// the response on that marker: everything before is the new chapter text, everything after is
/// the human-readable change log shown in the Edit UI. If the marker is missing, the whole
/// response is treated as the revised text and the change log is left empty (the UI still shows
/// a before/after view, so a missing log degrades gracefully).
/// </summary>
public sealed class BookChapterEditor(string openAiApiKey, string anthropicApiKey = "", string geminiApiKey = "", string xaiApiKey = "", string yandexApiKey = "", string yandexFolderId = "")
{
    private const string AnthropicModel = "claude-sonnet-5";
    private const string GeminiModel = "gemini-3.6-flash";
    private const string GrokModel = "grok-4.5";
    private const string YandexModel = "yandexgpt/latest";
    private const string OpenAiModel = "gpt-4o-mini";

    private const string ChangesMarker = "---CHANGES---";

    private static readonly HttpClient Http = new() { Timeout = TimeSpan.FromMinutes(4) };

    public bool AnthropicConfigured => !string.IsNullOrWhiteSpace(anthropicApiKey);
    public bool GeminiConfigured => !string.IsNullOrWhiteSpace(geminiApiKey);
    public bool XaiConfigured => !string.IsNullOrWhiteSpace(xaiApiKey);
    public bool YandexConfigured => !string.IsNullOrWhiteSpace(yandexApiKey) && !string.IsNullOrWhiteSpace(yandexFolderId);

    /// <summary>True when at least one provider tier is configured -- the Edit UI greys out its
    /// "run" buttons and says so when this is false, rather than letting every chapter edit fail
    /// one call at a time.</summary>
    public bool AnyProviderConfigured =>
        AnthropicConfigured || GeminiConfigured || XaiConfigured || YandexConfigured || !string.IsNullOrWhiteSpace(openAiApiKey);

    private static string BuildSystemPrompt(BookEditContext context, IReadOnlyList<EditPass> passes, string editorNotes, string chapterTitle)
    {
        bool isScienceAppendix = BookGenreRules.HasScienceAppendix(context.Genre)
            && BookGenreRules.LooksLikeAppendixChapter(chapterTitle);

        var sb = new StringBuilder();
        sb.Append("You are a meticulous professional book editor working on one ")
          .Append(isScienceAppendix ? "section" : "chapter")
          .Append(" of a full-length ")
          .Append(BookGenreRules.DisplayName(context.Genre)).Append(" book");
        if (!string.IsNullOrWhiteSpace(context.Title)) sb.Append(" titled \"").Append(context.Title.Trim()).Append('"');
        sb.Append(". You will be given that ").Append(isScienceAppendix ? "section" : "chapter")
          .Append("'s full current text and a set of editorial passes to apply.\n\n");

        if (isScienceAppendix)
        {
            sb.Append("NOTE: this is a SCIENCE APPENDIX section, not narrative fiction -- it is expository ")
              .Append("prose explaining the real science behind the story. Keep it factual and accurate; ")
              .Append("do not turn it into story beats, and hold any Storytelling pass to clarity and flow only.\n\n");
        }

        if (BookGenreRules.IsExamPrep(context.Genre))
            sb.Append(ExamPrepRules.EditorNote(chapterTitle)).Append(ExamPrepRules.SafetyRules).Append("\n\n");

        sb.Append("HARD RULES:\n");
        sb.Append("- Return the ENTIRE revised chapter text, start to finish -- never a diff, a summary, or only the changed parts.\n");
        sb.Append("- Preserve the author's voice and every intended plot event / argument, except exactly where a pass below tells you to change something.\n");
        sb.Append("- Do NOT add a chapter number, a chapter title line, or any meta-commentary at the top of the chapter.\n");
        sb.Append("- Keep paragraphs separated by a blank line, as in the input.\n");
        sb.Append("- After the full chapter text, output a line containing exactly ").Append(ChangesMarker)
          .Append(" and then a short bullet list (up to 8 bullets) of the substantive changes you made and why. ");
        sb.Append("If you changed nothing, write a single bullet \"- No changes needed.\"\n\n");

        if (context.AllChapters.Count > 0)
        {
            sb.Append("EVERY CHAPTER IN THIS BOOK (for continuity checks and for [text](chapter:N) links):\n");
            foreach ((int number, string title) in context.AllChapters)
                sb.Append(number).Append(". ").Append(string.IsNullOrWhiteSpace(title) ? "(untitled)" : title.Trim()).Append('\n');
            sb.Append('\n');
        }

        sb.Append("PASSES TO APPLY THIS TIME (apply only these):\n");
        foreach (EditPass pass in passes)
            sb.Append("- ").Append(EditPassInfo.PromptInstruction(pass)).Append('\n');

        if (!string.IsNullOrWhiteSpace(editorNotes))
        {
            sb.Append("\nADDITIONAL NOTES FROM THE AUTHOR (treat as high priority):\n");
            sb.Append(editorNotes.Trim()).Append('\n');
        }

        return sb.ToString();
    }

    private static string BuildUserMessage(int chapterNumber, string chapterTitle, string chapterText)
    {
        var sb = new StringBuilder();
        sb.Append("Chapter ").Append(chapterNumber);
        if (!string.IsNullOrWhiteSpace(chapterTitle)) sb.Append(": ").Append(chapterTitle.Trim());
        sb.Append("\n\n").Append(chapterText.Trim());
        return sb.ToString();
    }

    /// <summary>Revises one chapter. Never throws for an ordinary provider failure -- falls
    /// through every configured tier and returns <see cref="ChapterEditResult.Failed"/> only if
    /// every configured tier failed or none is configured. <paramref name="passes"/> must be
    /// non-empty; an empty pass list is itself returned as a failure (nothing to do).</summary>
    public async Task<ChapterEditResult> EditChapterAsync(
        BookEditContext context, string chapterText, int chapterNumber, string chapterTitle,
        IReadOnlyList<EditPass> passes, string editorNotes = "", CancellationToken ct = default)
    {
        if (passes is null || passes.Count == 0)
            return ChapterEditResult.Failed("No edit passes were selected.");
        if (string.IsNullOrWhiteSpace(chapterText))
            return ChapterEditResult.Failed("That chapter has no text to edit.");

        string systemPrompt = BuildSystemPrompt(context, passes, editorNotes, chapterTitle);
        string userMessage = BuildUserMessage(chapterNumber, chapterTitle, chapterText);
        string lastError = "No AI provider is configured -- cannot edit this chapter.";

        if (AnthropicConfigured)
        {
            (string text, string error) = await ViaAnthropicAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return Interpret(text, chapterText);
            lastError = error;
            AppLog.Warning("BookChapterEditor: Claude failed for chapter {Number} - {Error}", chapterNumber, error);
        }
        if (GeminiConfigured)
        {
            (string text, string error) = await ViaGeminiAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return Interpret(text, chapterText);
            lastError = error;
            AppLog.Warning("BookChapterEditor: Gemini failed for chapter {Number} - {Error}", chapterNumber, error);
        }
        if (XaiConfigured)
        {
            (string text, string error) = await ViaGrokAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return Interpret(text, chapterText);
            lastError = error;
            AppLog.Warning("BookChapterEditor: Grok failed for chapter {Number} - {Error}", chapterNumber, error);
        }
        if (YandexConfigured)
        {
            (string text, string error) = await ViaYandexAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return Interpret(text, chapterText);
            lastError = error;
            AppLog.Warning("BookChapterEditor: YandexGPT failed for chapter {Number} - {Error}", chapterNumber, error);
        }
        if (!string.IsNullOrWhiteSpace(openAiApiKey))
        {
            (string text, string error) = await ViaOpenAiAsync(systemPrompt, userMessage, ct);
            if (text.Length > 0) return Interpret(text, chapterText);
            lastError = error;
            AppLog.Warning("BookChapterEditor: OpenAI failed for chapter {Number} - {Error}", chapterNumber, error);
        }

        return ChapterEditResult.Failed(lastError);
    }

    /// <summary>Splits a raw provider response on the <see cref="ChangesMarker"/> into the new
    /// chapter text and the change log, and decides whether anything actually changed.</summary>
    private static ChapterEditResult Interpret(string rawResponse, string originalChapter)
    {
        string response = StripMarkdownFences(rawResponse.Trim());

        string revised = response;
        string summary = "";

        int markerIndex = IndexOfMarker(response);
        if (markerIndex >= 0)
        {
            revised = response[..markerIndex].TrimEnd();

            string fromMarker = response[markerIndex..];
            int newline = fromMarker.IndexOf('\n');
            summary = newline >= 0 ? fromMarker[(newline + 1)..].Trim() : "";
        }

        revised = revised.Trim();
        if (revised.Length == 0)
            return ChapterEditResult.Failed("The editor returned an empty chapter.");

        bool noChangeClaimed = summary.Length > 0 &&
            summary.Replace("-", "").Replace("*", "").Trim().StartsWith("No changes needed", StringComparison.OrdinalIgnoreCase);
        bool textIdentical = string.Equals(
            Normalize(revised), Normalize(originalChapter), StringComparison.Ordinal);

        bool changed = !textIdentical && !noChangeClaimed;
        return new ChapterEditResult(revised, summary, changed, "");
    }

    private static int IndexOfMarker(string text)
    {
        // Tolerate "---CHANGES---", "## CHANGES", "**CHANGES**", "CHANGES:" on their own line.
        string[] lines = text.Replace("\r\n", "\n").Split('\n');
        int offset = 0;
        foreach (string line in lines)
        {
            string bare = line.Trim().Trim('#', '*', '-', ' ', ':').Trim();
            if (bare.Equals("CHANGES", StringComparison.OrdinalIgnoreCase) ||
                line.Contains(ChangesMarker, StringComparison.OrdinalIgnoreCase))
                return offset;
            offset += line.Length + 1;
        }
        return -1;
    }

    private static string Normalize(string s) =>
        System.Text.RegularExpressions.Regex.Replace(s.Replace("\r\n", "\n"), @"\s+", " ").Trim();

    // ==================== Provider tiers (parallel to BookChapterGenerator's) ====================

    private async Task<(string Text, string Error)> ViaAnthropicAsync(string systemPrompt, string userMessage, CancellationToken ct)
    {
        try
        {
            var requestBody = new
            {
                model = AnthropicModel,
                max_tokens = 16000,
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

            var sb = new StringBuilder();
            if (doc.RootElement.TryGetProperty("content", out var contentEl) && contentEl.ValueKind == JsonValueKind.Array)
            {
                foreach (JsonElement block in contentEl.EnumerateArray())
                {
                    if (block.TryGetProperty("type", out var t) && t.GetString() == "text" &&
                        block.TryGetProperty("text", out var txt) && txt.ValueKind == JsonValueKind.String)
                        sb.Append(txt.GetString());
                }
            }

            if (string.Equals(stopReason, "max_tokens", StringComparison.OrdinalIgnoreCase))
                return ("", "Anthropic's response hit the token limit before the whole revised chapter was returned -- try fewer passes at once, or split this chapter.");

            string text = sb.ToString().Trim();
            return text.Length > 0 ? (text, "") : ("", "Anthropic returned an empty response.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "Anthropic edit failed: " + ex.Message); }
    }

    private async Task<(string Text, string Error)> ViaGeminiAsync(string systemPrompt, string userMessage, CancellationToken ct)
    {
        try
        {
            var bodyDict = new Dictionary<string, object>
            {
                ["model"] = GeminiModel,
                ["input"] = userMessage,
                ["system_instruction"] = systemPrompt,
                ["generation_config"] = new Dictionary<string, object> { ["max_output_tokens"] = 16000 },
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
                return ("", "Gemini's response hit the token limit before the whole revised chapter was returned.");

            var sb = new StringBuilder();
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
                            sb.Append(te.GetString());
                    }
                }
            }

            string text = sb.ToString().Trim();
            return text.Length > 0 ? (text, "") : ("", "Gemini returned an empty response.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "Gemini edit failed: " + ex.Message); }
    }

    private async Task<(string Text, string Error)> ViaGrokAsync(string systemPrompt, string userMessage, CancellationToken ct)
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

            string text = ExtractGrokOutputText(body).Trim();
            return text.Length > 0 ? (text, "") : ("", "Grok returned an empty response.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "Grok edit failed: " + ex.Message); }
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

    private async Task<(string Text, string Error)> ViaYandexAsync(string systemPrompt, string userMessage, CancellationToken ct)
    {
        try
        {
            var requestBody = new
            {
                modelUri = $"gpt://{yandexFolderId}/{YandexModel}",
                completionOptions = new { stream = false, temperature = 0.3, maxTokens = "8192" },
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
            string text = (doc.RootElement.GetProperty("alternatives")[0].GetProperty("message").GetProperty("text").GetString() ?? "").Trim();
            return text.Length > 0 ? (text, "") : ("", "YandexGPT returned an empty response.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "YandexGPT edit failed: " + ex.Message); }
    }

    private async Task<(string Text, string Error)> ViaOpenAiAsync(string systemPrompt, string userMessage, CancellationToken ct)
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
                temperature = 0.4,
                max_tokens = 16000,
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
                return ("", "OpenAI's response hit the max_tokens limit before the whole revised chapter was returned.");

            string text = (firstChoice.GetProperty("message").GetProperty("content").GetString() ?? "").Trim();
            return text.Length > 0 ? (text, "") : ("", "OpenAI returned an empty response.");
        }
        catch (OperationCanceledException) { throw; }
        catch (Exception ex) { return ("", "OpenAI edit failed: " + ex.Message); }
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
