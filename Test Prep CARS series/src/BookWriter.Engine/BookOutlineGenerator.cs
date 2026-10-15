using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace BookWriter.Engine;

/// <summary>
/// Generates a BookOutline (chapter list, plus a Fiction "book bible": characters/setting/plot
/// arc) from a title/genre/premise -- the one-time planning call every later BookChapterGenerator
/// call is grounded against. Mirrors MediaStar.GPT's own MetadataGenerator provider chain/shape
/// (Claude Structured Outputs first, then OpenAI response_format:"json_object", then YandexGPT
/// prompted JSON, then a minimal local fallback), since this is the same kind of task
/// (schema-shaped JSON from a prompt) that class already solves.
///
/// One schema is requested regardless of genre (characters/setting/plotArc are simply left
/// empty for NonFiction, per the prompt's own instruction) rather than two different JSON
/// schemas per genre -- keeps one call shape for both, and an empty Fiction-only field costs
/// nothing for a NonFiction book that never reads it.
/// </summary>
public sealed class BookOutlineGenerator(string openAiApiKey, string anthropicApiKey = "", string yandexApiKey = "", string yandexFolderId = "")
{
    private const string OpenAiEndpoint = "https://api.openai.com/v1/chat/completions";
    private const string Model = "gpt-4o-mini";
    private const string AnthropicModel = "claude-sonnet-5";
    private const string YandexModel = "yandexgpt/latest";

    private static readonly HttpClient Http = new() { Timeout = TimeSpan.FromSeconds(90) };
    private static readonly JsonSerializerOptions JsonOptions = new() { PropertyNameCaseInsensitive = true };

    public bool AnthropicConfigured => !string.IsNullOrWhiteSpace(anthropicApiKey);
    public bool YandexConfigured => !string.IsNullOrWhiteSpace(yandexApiKey) && !string.IsNullOrWhiteSpace(yandexFolderId);

    private static string BuildSystemPrompt(BookGenre genre, int chapterCount)
    {
        string genreGuidance;
        if (genre == BookGenre.ExamPrep)
        {
            genreGuidance = ExamPrepRules.OutlineGuidance(chapterCount);
        }
        else if (genre == BookGenre.FictionWithScienceAppendix)
        {
            genreGuidance =
                "This is a FICTION book WITH a SCIENCE APPENDIX. Invent a cast of characters " +
                "(name/description/role for each), a concrete setting, and an overall plot arc " +
                "(a brief 3-act-style summary of how the story rises and resolves) -- these must " +
                "stay consistent across every narrative chapter, since each chapter will later be " +
                "written by a SEPARATE call that only sees this outline, not the other chapters' " +
                "own prose. Structure the chapter list so the LAST 20-30% of chapters are science " +
                "appendices: their titles MUST begin with exactly \"Appendix:\" (e.g. \"Appendix: " +
                "The Physics of Wormholes\") and their summaries must describe real, accurate " +
                "science explainers tied to themes, technologies, or phenomena from the story -- " +
                "NOT more plot. The earlier chapters are narrative fiction; the appendix chapters " +
                "are non-fiction science exposition that a curious reader can learn from.";
        }
        else if (genre == BookGenre.Fiction)
        {
            genreGuidance =
                "This is a FICTION book. Invent a cast of characters (name/description/role for each), " +
                "a concrete setting, and an overall plot arc (a brief 3-act-style summary of how the " +
                "story rises and resolves) -- these must stay consistent across every chapter, since " +
                "each chapter will later be written by a SEPARATE call that only sees this outline, " +
                "not the other chapters' own prose.";
        }
        else
        {
            genreGuidance =
                "This is a NON-FICTION book. Leave \"characters\" as an empty array, and \"setting\"/" +
                "\"plotArc\" as empty strings -- there is nothing to invent there. Each chapter should " +
                "be a distinct sub-topic that builds the book's overall thesis/premise in order.";
        }

        return "You are a professional book editor planning a full manuscript outline. Given a " +
               $"title, genre, and premise, plan exactly {chapterCount} chapters, each with a " +
               "concrete title and a 2-3 sentence summary of what actually happens/is covered in " +
               $"that chapter (specific, not vague filler). {genreGuidance} Respond ONLY as JSON: " +
               "{\"chapters\":[{\"number\":1,\"title\":...,\"summary\":...}],\"characters\":" +
               "[{\"name\":...,\"description\":...,\"role\":...}],\"setting\":...,\"plotArc\":...}";
    }

    private static string BuildUserContent(string title, BookGenre genre, string premise) =>
        $"Title: {title}\nGenre: {genre}\nPremise: {premise}";

    /// <summary>Never throws -- any provider failure falls through to the next tier, and if
    /// every configured tier fails (or none is configured), returns a minimal one-chapter
    /// outline naming the honest reason rather than silently pretending a real plan exists.
    /// Callers should check the returned outline's own Chapters.Count/Premise before treating it
    /// as a real, usable plan.</summary>
    public async Task<BookOutline> GenerateAsync(string title, BookGenre genre, string premise, int chapterCount, CancellationToken ct = default)
    {
        if (AnthropicConfigured)
        {
            try
            {
                BookOutline? outline = await GenerateViaAnthropicAsync(title, genre, premise, chapterCount, ct);
                if (outline is not null) return outline;
            }
            catch (OperationCanceledException) when (ct.IsCancellationRequested) { throw; }
            catch (Exception ex)
            {
                AppLog.Warning("BookOutlineGenerator: Claude call failed - {Error}, falling back to OpenAI.", ex.Message);
            }
        }

        if (!string.IsNullOrWhiteSpace(openAiApiKey))
        {
            try
            {
                BookOutline? outline = await GenerateViaOpenAiAsync(title, genre, premise, chapterCount, ct);
                if (outline is not null) return outline;
            }
            catch (OperationCanceledException) when (ct.IsCancellationRequested) { throw; }
            catch (Exception ex)
            {
                AppLog.Warning("BookOutlineGenerator: OpenAI call failed - {Error}, falling back to Yandex.", ex.Message);
            }
        }

        if (YandexConfigured)
        {
            try
            {
                BookOutline? outline = await GenerateViaYandexAsync(title, genre, premise, chapterCount, ct);
                if (outline is not null) return outline;
            }
            catch (OperationCanceledException) when (ct.IsCancellationRequested) { throw; }
            catch (Exception ex)
            {
                AppLog.Warning("BookOutlineGenerator: YandexGPT call failed - {Error}, falling back to a minimal outline.", ex.Message);
            }
        }

        return BuildFallbackOutline(title, genre, premise, chapterCount);
    }

    private async Task<BookOutline?> GenerateViaAnthropicAsync(string title, BookGenre genre, string premise, int chapterCount, CancellationToken ct)
    {
        var requestBody = new
        {
            model = AnthropicModel,
            max_tokens = 4096,
            system = BuildSystemPrompt(genre, chapterCount),
            messages = new object[] { new { role = "user", content = BuildUserContent(title, genre, premise) } },
            output_config = new
            {
                format = new
                {
                    type = "json_schema",
                    schema = new
                    {
                        type = "object",
                        properties = new
                        {
                            chapters = new
                            {
                                type = "array",
                                items = new
                                {
                                    type = "object",
                                    properties = new
                                    {
                                        number = new { type = "integer" },
                                        title = new { type = "string" },
                                        summary = new { type = "string" },
                                    },
                                    required = new[] { "number", "title", "summary" },
                                    additionalProperties = false,
                                },
                            },
                            characters = new
                            {
                                type = "array",
                                items = new
                                {
                                    type = "object",
                                    properties = new
                                    {
                                        name = new { type = "string" },
                                        description = new { type = "string" },
                                        role = new { type = "string" },
                                    },
                                    required = new[] { "name", "description", "role" },
                                    additionalProperties = false,
                                },
                            },
                            setting = new { type = "string" },
                            plotArc = new { type = "string" },
                        },
                        required = new[] { "chapters", "characters", "setting", "plotArc" },
                        additionalProperties = false,
                    },
                },
            },
        };

        using var request = new HttpRequestMessage(HttpMethod.Post, "https://api.anthropic.com/v1/messages");
        request.Headers.TryAddWithoutValidation("x-api-key", anthropicApiKey);
        request.Headers.TryAddWithoutValidation("anthropic-version", "2023-06-01");
        request.Content = new StringContent(JsonSerializer.Serialize(requestBody), Encoding.UTF8, "application/json");

        using HttpResponseMessage response = await Http.SendAsync(request, ct);
        response.EnsureSuccessStatusCode();

        string responseJson = await response.Content.ReadAsStringAsync(ct);
        using var envelope = JsonDocument.Parse(responseJson);

        var textBuilder = new StringBuilder();
        if (envelope.RootElement.TryGetProperty("content", out var contentEl) && contentEl.ValueKind == JsonValueKind.Array)
        {
            foreach (JsonElement block in contentEl.EnumerateArray())
            {
                if (block.TryGetProperty("type", out var typeEl) && typeEl.ValueKind == JsonValueKind.String && typeEl.GetString() == "text" &&
                    block.TryGetProperty("text", out var textEl) && textEl.ValueKind == JsonValueKind.String)
                {
                    textBuilder.Append(textEl.GetString());
                }
            }
        }

        var payload = JsonSerializer.Deserialize<OutlinePayload>(StripCodeFences(textBuilder.ToString()), JsonOptions);
        return BuildOutlineFromPayload(payload, title, genre, premise);
    }

    private async Task<BookOutline?> GenerateViaOpenAiAsync(string title, BookGenre genre, string premise, int chapterCount, CancellationToken ct)
    {
        var requestBody = new
        {
            model = Model,
            response_format = new { type = "json_object" },
            messages = new object[]
            {
                new { role = "system", content = BuildSystemPrompt(genre, chapterCount) },
                new { role = "user", content = BuildUserContent(title, genre, premise) },
            },
        };

        using var request = new HttpRequestMessage(HttpMethod.Post, OpenAiEndpoint)
        {
            Content = new StringContent(JsonSerializer.Serialize(requestBody), Encoding.UTF8, "application/json"),
        };
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", openAiApiKey);

        using HttpResponseMessage response = await Http.SendAsync(request, ct);
        response.EnsureSuccessStatusCode();

        string responseJson = await response.Content.ReadAsStringAsync(ct);
        using var envelope = JsonDocument.Parse(responseJson);
        string content = envelope.RootElement.GetProperty("choices")[0].GetProperty("message").GetProperty("content").GetString() ?? "";

        var payload = JsonSerializer.Deserialize<OutlinePayload>(StripCodeFences(content), JsonOptions);
        return BuildOutlineFromPayload(payload, title, genre, premise);
    }

    /// <summary>Same endpoint/auth/response-envelope shape MediaStar.GPT's own
    /// ScriptGenerator/MetadataGenerator Yandex tiers confirmed live: no outer "result" wrapper,
    /// alternatives at the top level.</summary>
    private async Task<BookOutline?> GenerateViaYandexAsync(string title, BookGenre genre, string premise, int chapterCount, CancellationToken ct)
    {
        var requestBody = new
        {
            modelUri = $"gpt://{yandexFolderId}/{YandexModel}",
            completionOptions = new { stream = false, temperature = 0.4, maxTokens = "4096" },
            messages = new object[]
            {
                new { role = "system", text = BuildSystemPrompt(genre, chapterCount) },
                new { role = "user", text = BuildUserContent(title, genre, premise) },
            },
        };

        using var request = new HttpRequestMessage(HttpMethod.Post, "https://llm.api.cloud.yandex.net/foundationModels/v1/completion")
        {
            Content = new StringContent(JsonSerializer.Serialize(requestBody), Encoding.UTF8, "application/json"),
        };
        request.Headers.TryAddWithoutValidation("Authorization", $"Api-Key {yandexApiKey}");

        using HttpResponseMessage response = await Http.SendAsync(request, ct);
        response.EnsureSuccessStatusCode();

        string responseJson = await response.Content.ReadAsStringAsync(ct);
        using var envelope = JsonDocument.Parse(responseJson);
        string content = envelope.RootElement.GetProperty("alternatives")[0].GetProperty("message").GetProperty("text").GetString() ?? "";

        var payload = JsonSerializer.Deserialize<OutlinePayload>(StripCodeFences(content), JsonOptions);
        return BuildOutlineFromPayload(payload, title, genre, premise);
    }

    private static BookOutline? BuildOutlineFromPayload(OutlinePayload? payload, string title, BookGenre genre, string premise)
    {
        if (payload?.Chapters is null || payload.Chapters.Count == 0) return null;

        var outline = new BookOutline { Title = title, Genre = genre, Premise = premise };
        foreach (ChapterPayload ch in payload.Chapters)
        {
            if (string.IsNullOrWhiteSpace(ch.Title)) continue;
            outline.Chapters.Add(new ChapterOutline
            {
                Number = ch.Number > 0 ? ch.Number : outline.Chapters.Count + 1,
                Title = ch.Title.Trim(),
                Summary = (ch.Summary ?? "").Trim(),
            });
        }
        if (outline.Chapters.Count == 0) return null;

        if (BookGenreRules.UsesStoryBible(genre) && payload.Characters is not null)
        {
            foreach (CharacterPayload c in payload.Characters)
            {
                if (string.IsNullOrWhiteSpace(c.Name)) continue;
                outline.Characters.Add(new BookCharacter { Name = c.Name.Trim(), Description = (c.Description ?? "").Trim(), Role = (c.Role ?? "").Trim() });
            }
            outline.Setting = (payload.Setting ?? "").Trim();
            outline.PlotArc = (payload.PlotArc ?? "").Trim();
        }

        return outline;
    }

    /// <summary>Every provider tier failed (or none configured) -- a single honest placeholder
    /// chapter rather than pretending a real multi-chapter plan exists. BookChapterGenerator can
    /// still expand this one chapter (its own honest-degrade path applies there too), but the
    /// caller should surface that this outline is not a real plan.</summary>
    private static BookOutline BuildFallbackOutline(string title, BookGenre genre, string premise, int chapterCount)
    {
        var outline = new BookOutline { Title = title, Genre = genre, Premise = premise };
        outline.Chapters.Add(new ChapterOutline
        {
            Number = 1,
            Title = "Chapter 1",
            Summary = $"No AI provider was configured or available to plan a real {chapterCount}-chapter outline - " +
                       "this single placeholder chapter covers the stated premise directly.",
        });
        return outline;
    }

    private static string StripCodeFences(string s)
    {
        s = s.Trim();
        if (!s.StartsWith("```")) return s;

        int firstNewline = s.IndexOf('\n');
        if (firstNewline >= 0) s = s[(firstNewline + 1)..];
        int lastFence = s.LastIndexOf("```", StringComparison.Ordinal);
        if (lastFence >= 0) s = s[..lastFence];
        return s.Trim();
    }

    private sealed class OutlinePayload
    {
        public List<ChapterPayload>? Chapters { get; set; }
        public List<CharacterPayload>? Characters { get; set; }
        public string? Setting { get; set; }
        public string? PlotArc { get; set; }
    }

    private sealed class ChapterPayload
    {
        public int Number { get; set; }
        public string? Title { get; set; }
        public string? Summary { get; set; }
    }

    private sealed class CharacterPayload
    {
        public string? Name { get; set; }
        public string? Description { get; set; }
        public string? Role { get; set; }
    }
}

