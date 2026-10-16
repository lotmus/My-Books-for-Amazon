using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace BookWriter.Engine;

/// <summary>One AI-drafted starting point for the Write flow: everything the Setup form needs,
/// inferred from a single free-form prompt. Every field stays editable in the UI afterward --
/// this is a first draft to react to, not a commitment.</summary>
public sealed record BookStarter(string Title, BookGenre Genre, string Premise, int ChapterCount);

/// <summary>
/// Turns a one-line or one-paragraph idea ("a cosy mystery set in a lighthouse", "an
/// introduction to tide pools for curious ten-year-olds") into a filled-in
/// <see cref="BookStarter"/> -- a suggested title, genre, a proper one-paragraph premise, and a
/// sensible chapter count -- so the Write flow can start from a single sentence instead of the
/// author filling four fields cold.
///
/// Same provider chain, call shape and honest-degrade contract as
/// <see cref="BookOutlineGenerator"/>'s own planning call (Claude Structured Outputs first,
/// then OpenAI response_format json_object, then YandexGPT prompted JSON, then a minimal local
/// fallback that just reuses the prompt as the premise) -- this is the same kind of task
/// (schema-shaped JSON from a prompt) and is grounded against that class's already-verified
/// endpoint shapes rather than re-researching them.
/// </summary>
public sealed class BookStarterGenerator(string openAiApiKey, string anthropicApiKey = "", string yandexApiKey = "", string yandexFolderId = "")
{
    private const string OpenAiEndpoint = "https://api.openai.com/v1/chat/completions";
    private const string OpenAiModel = "gpt-4o-mini";
    private const string AnthropicModel = "claude-sonnet-5";
    private const string YandexModel = "yandexgpt/latest";

    private const int MinChapters = 3;
    private const int MaxChapters = 40;
    private const int DefaultChapters = 12;

    private static readonly HttpClient Http = new() { Timeout = TimeSpan.FromSeconds(60) };
    private static readonly JsonSerializerOptions JsonOptions = new() { PropertyNameCaseInsensitive = true };

    public bool AnthropicConfigured => !string.IsNullOrWhiteSpace(anthropicApiKey);
    public bool YandexConfigured => !string.IsNullOrWhiteSpace(yandexApiKey) && !string.IsNullOrWhiteSpace(yandexFolderId);

    private const string SystemPrompt =
        "You are a commissioning editor. Given a short free-form book idea, propose a concrete "
        + "starting point for it. Return a real working title (not a description), the single "
        + "best-fit genre, a vivid one-paragraph premise (3-5 sentences, concrete, no filler), "
        + "and a sensible whole-number chapter count for a book of that kind (most books land "
        + "between 8 and 20). genre MUST be exactly \"Fiction\" or \"NonFiction\". Respond ONLY "
        + "as JSON: {\"title\":...,\"genre\":\"Fiction|NonFiction\",\"premise\":...,\"chapterCount\":12}";

    /// <summary>Never throws for an ordinary provider failure -- each configured tier is tried
    /// in order, falling through on any error, and if every tier fails (or none is configured)
    /// this returns a local fallback that reuses <paramref name="prompt"/> as the premise plus
    /// an honest note. The note always says which tier produced the result, or why none
    /// did.</summary>
    public async Task<(BookStarter Starter, string Note)> GenerateAsync(string prompt, CancellationToken ct = default)
    {
        string idea = (prompt ?? "").Trim();
        if (idea.Length == 0)
            return (LocalFallback(""), "Enter an idea first -- even a single sentence is enough.");

        if (AnthropicConfigured)
        {
            try
            {
                BookStarter? s = await ViaAnthropicAsync(idea, ct);
                if (s is not null) return (s, "Draft setup suggested by Claude. Every field is editable.");
            }
            catch (OperationCanceledException) when (ct.IsCancellationRequested) { throw; }
            catch (Exception ex) { AppLog.Warning("BookStarterGenerator: Claude failed - {Error}, trying OpenAI.", ex.Message); }
        }

        if (!string.IsNullOrWhiteSpace(openAiApiKey))
        {
            try
            {
                BookStarter? s = await ViaOpenAiAsync(idea, ct);
                if (s is not null) return (s, "Draft setup suggested by OpenAI. Every field is editable.");
            }
            catch (OperationCanceledException) when (ct.IsCancellationRequested) { throw; }
            catch (Exception ex) { AppLog.Warning("BookStarterGenerator: OpenAI failed - {Error}, trying Yandex.", ex.Message); }
        }

        if (YandexConfigured)
        {
            try
            {
                BookStarter? s = await ViaYandexAsync(idea, ct);
                if (s is not null) return (s, "Draft setup suggested by YandexGPT. Every field is editable.");
            }
            catch (OperationCanceledException) when (ct.IsCancellationRequested) { throw; }
            catch (Exception ex) { AppLog.Warning("BookStarterGenerator: YandexGPT failed - {Error}, using a local fallback.", ex.Message); }
        }

        bool anyConfigured = AnthropicConfigured || !string.IsNullOrWhiteSpace(openAiApiKey) || YandexConfigured;
        string note = anyConfigured
            ? "No AI provider could draft a setup right now -- your idea has been dropped in as the premise. Fill in the rest, or try again."
            : "No AI provider is configured -- your idea has been dropped in as the premise. Fill in the title, genre and chapter count yourself.";
        return (LocalFallback(idea), note);
    }

    private async Task<BookStarter?> ViaAnthropicAsync(string idea, CancellationToken ct)
    {
        var requestBody = new
        {
            model = AnthropicModel,
            max_tokens = 1024,
            system = SystemPrompt,
            messages = new object[] { new { role = "user", content = idea } },
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
                            title = new { type = "string" },
                            genre = new { type = "string", @enum = new[] { "Fiction", "NonFiction" } },
                            premise = new { type = "string" },
                            chapterCount = new { type = "integer" },
                        },
                        required = new[] { "title", "genre", "premise", "chapterCount" },
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

        using var envelope = JsonDocument.Parse(await response.Content.ReadAsStringAsync(ct));
        var sb = new StringBuilder();
        if (envelope.RootElement.TryGetProperty("content", out var content) && content.ValueKind == JsonValueKind.Array)
        {
            foreach (JsonElement block in content.EnumerateArray())
            {
                if (block.TryGetProperty("type", out var t) && t.GetString() == "text" &&
                    block.TryGetProperty("text", out var txt) && txt.ValueKind == JsonValueKind.String)
                    sb.Append(txt.GetString());
            }
        }

        return Build(JsonSerializer.Deserialize<StarterPayload>(StripCodeFences(sb.ToString()), JsonOptions), idea);
    }

    private async Task<BookStarter?> ViaOpenAiAsync(string idea, CancellationToken ct)
    {
        var requestBody = new
        {
            model = OpenAiModel,
            response_format = new { type = "json_object" },
            messages = new object[]
            {
                new { role = "system", content = SystemPrompt },
                new { role = "user", content = idea },
            },
        };

        using var request = new HttpRequestMessage(HttpMethod.Post, OpenAiEndpoint)
        {
            Content = new StringContent(JsonSerializer.Serialize(requestBody), Encoding.UTF8, "application/json"),
        };
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", openAiApiKey);

        using HttpResponseMessage response = await Http.SendAsync(request, ct);
        response.EnsureSuccessStatusCode();

        using var envelope = JsonDocument.Parse(await response.Content.ReadAsStringAsync(ct));
        string content = envelope.RootElement.GetProperty("choices")[0].GetProperty("message").GetProperty("content").GetString() ?? "";
        return Build(JsonSerializer.Deserialize<StarterPayload>(StripCodeFences(content), JsonOptions), idea);
    }

    private async Task<BookStarter?> ViaYandexAsync(string idea, CancellationToken ct)
    {
        var requestBody = new
        {
            modelUri = $"gpt://{yandexFolderId}/{YandexModel}",
            completionOptions = new { stream = false, temperature = 0.5, maxTokens = "1024" },
            messages = new object[]
            {
                new { role = "system", text = SystemPrompt },
                new { role = "user", text = idea },
            },
        };

        using var request = new HttpRequestMessage(HttpMethod.Post, "https://llm.api.cloud.yandex.net/foundationModels/v1/completion")
        {
            Content = new StringContent(JsonSerializer.Serialize(requestBody), Encoding.UTF8, "application/json"),
        };
        request.Headers.TryAddWithoutValidation("Authorization", $"Api-Key {yandexApiKey}");

        using HttpResponseMessage response = await Http.SendAsync(request, ct);
        response.EnsureSuccessStatusCode();

        using var envelope = JsonDocument.Parse(await response.Content.ReadAsStringAsync(ct));
        string content = envelope.RootElement.GetProperty("alternatives")[0].GetProperty("message").GetProperty("text").GetString() ?? "";
        return Build(JsonSerializer.Deserialize<StarterPayload>(StripCodeFences(content), JsonOptions), idea);
    }

    private static BookStarter? Build(StarterPayload? payload, string idea)
    {
        if (payload is null) return null;

        string premise = (payload.Premise ?? "").Trim();
        if (premise.Length == 0) premise = idea;

        string title = (payload.Title ?? "").Trim();
        if (title.Length == 0) title = FirstLine(idea);

        BookGenre genre = string.Equals(payload.Genre?.Trim(), "Fiction", StringComparison.OrdinalIgnoreCase)
            ? BookGenre.Fiction
            : BookGenre.NonFiction;

        int chapters = payload.ChapterCount is > 0 ? Math.Clamp(payload.ChapterCount.Value, MinChapters, MaxChapters) : DefaultChapters;

        return new BookStarter(title, genre, premise, chapters);
    }

    private static BookStarter LocalFallback(string idea) =>
        new(FirstLine(idea), BookGenre.NonFiction, idea.Length > 0 ? idea : "", DefaultChapters);

    private static string FirstLine(string text)
    {
        string first = text.Replace("\r\n", "\n").Split('\n', 2)[0].Trim();
        if (first.Length == 0) return "Untitled Book";
        return first.Length <= 80 ? first : first[..80].TrimEnd() + "...";
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

    private sealed class StarterPayload
    {
        public string? Title { get; set; }
        public string? Genre { get; set; }
        public string? Premise { get; set; }
        public int? ChapterCount { get; set; }
    }
}
