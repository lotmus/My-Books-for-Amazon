using System.IO;

namespace BookWriter.App;

/// <summary>
/// Reads config/asset_api.ini -- a flat key=value format, trimmed down from MediaStar.GPT's own
/// MediaMaker.Core.ApiKeys when Book Writer was spun out into its own standalone app to just the
/// 5 providers the book engine actually calls (OpenAI, Anthropic, Gemini, xAI/Grok, Yandex).
/// Uses the SAME ini key names as the original app on purpose, so a user who already has an
/// asset_api.ini for MediaStar.GPT can copy the relevant lines straight across.
/// </summary>
public sealed class ApiKeys
{
    public const string DefaultConfigPath = @"D:\My_C#_Apps\Book Writer\config\asset_api.ini";

    public string OpenAiKey { get; private set; } = "";
    public string AnthropicApiKey { get; private set; } = "";
    public string GeminiApiKey { get; private set; } = "";
    public string XaiApiKey { get; private set; } = "";
    public string YandexApiKey { get; private set; } = "";
    public string YandexFolderId { get; private set; } = "";

    public static ApiKeys Load(string? path = null)
    {
        path ??= DefaultConfigPath;
        var keys = new ApiKeys();
        if (!File.Exists(path)) return keys;

        foreach (string rawLine in File.ReadAllLines(path))
        {
            string line = rawLine.Trim();
            if (line.Length == 0 || line.StartsWith('#') || line.StartsWith(';') || line.StartsWith('[')) continue;

            int eq = line.IndexOf('=');
            if (eq < 0) continue;

            string key = line[..eq].Trim().ToLowerInvariant();
            string value = line[(eq + 1)..].Trim();
            if (value.Length == 0) continue;

            switch (key)
            {
                case "openai_key" or "openai_api_key" or "openai": keys.OpenAiKey = value; break;
                case "anthropic_key" or "anthropic_api_key" or "claude_key": keys.AnthropicApiKey = value; break;
                case "gemini_key" or "google_ai_key": keys.GeminiApiKey = value; break;
                case "xai_key" or "xai_api_key" or "grok_key" or "grok_api_key": keys.XaiApiKey = value; break;
                case "yandex_api_key" or "yandex_cloud_api_key": keys.YandexApiKey = value; break;
                case "yandex_folder_id": keys.YandexFolderId = value; break;
            }
        }

        return keys;
    }
}
