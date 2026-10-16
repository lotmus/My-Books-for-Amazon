using System.IO;
using System.Text.Json;

namespace BookWriter.App;

/// <summary>
/// Remembers the last folder used for a given file-dialog purpose, ported verbatim from
/// MediaStar.GPT's own MediaMaker.Core.RecentFolderMemory when Book Writer was spun out into
/// its own standalone app. Persisted as one small shared JSON dictionary (purpose key -> last
/// folder path) under %LocalAppData%\BookWriter\recent-folders.json.
/// </summary>
public static class RecentFolderMemory
{
    private static readonly string FilePath = Path.Combine(
        Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
        "BookWriter", "recent-folders.json");

    private static Dictionary<string, string>? _cache;

    /// <summary>Null if this purpose has never been used before, or its remembered folder no
    /// longer exists.</summary>
    public static string? GetLastFolder(string purposeKey)
    {
        Dictionary<string, string> map = Load();
        return map.TryGetValue(purposeKey, out string? folder) && Directory.Exists(folder) ? folder : null;
    }

    /// <summary>Pass either a full file path (its containing directory is remembered) or a
    /// folder path directly.</summary>
    public static void RememberPath(string purposeKey, string fileOrFolderPath)
    {
        string? folder = Directory.Exists(fileOrFolderPath) ? fileOrFolderPath : Path.GetDirectoryName(fileOrFolderPath);
        if (string.IsNullOrWhiteSpace(folder)) return;

        Dictionary<string, string> map = Load();
        map[purposeKey] = folder;
        Save(map);
    }

    private static Dictionary<string, string> Load()
    {
        if (_cache is not null) return _cache;
        if (!File.Exists(FilePath)) return _cache = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);

        try
        {
            string json = File.ReadAllText(FilePath);
            _cache = JsonSerializer.Deserialize<Dictionary<string, string>>(json) ?? new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        }
        catch
        {
            _cache = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        }
        return _cache;
    }

    private static void Save(Dictionary<string, string> map)
    {
        try
        {
            string? dir = Path.GetDirectoryName(FilePath);
            if (dir is not null) Directory.CreateDirectory(dir);
            File.WriteAllText(FilePath, JsonSerializer.Serialize(map));
        }
        catch (Exception ex)
        {
            Engine.AppLog.Error(ex, "RecentFolderMemory: could not save {Path}", FilePath);
        }
    }
}
