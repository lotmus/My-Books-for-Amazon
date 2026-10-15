using System.IO;

namespace BookWriter.Engine;

/// <summary>
/// Minimal file+console logger, ported from MediaStar.GPT's own MediaMaker.Core.AppLog when
/// Book Writer was spun out into its own standalone app -- deliberately simplified to avoid
/// pulling in Serilog for one small app's worth of logging. Writes a plain timestamped line to
/// both the console and a rolling daily file under %LocalAppData%\BookWriter\logs; never throws
/// (a logging failure must never crash the feature that was trying to report a warning).
/// </summary>
public static class AppLog
{
    public static string LogDirectory { get; } = Path.Combine(
        Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
        "BookWriter", "logs");

    public static void Warning(string messageTemplate, params object?[] args) => Write("WRN", messageTemplate, args);

    public static void Info(string messageTemplate, params object?[] args) => Write("INF", messageTemplate, args);

    public static void Error(Exception? ex, string messageTemplate, params object?[] args) =>
        Write("ERR", messageTemplate + (ex is null ? "" : " -- " + ex), args);

    private static void Write(string level, string messageTemplate, object?[] args)
    {
        string message = FormatTemplate(messageTemplate, args);
        string line = $"{DateTime.Now:yyyy-MM-dd HH:mm:ss.fff} [{level}] {message}";

        try { Console.WriteLine(line); } catch { /* no console attached -- fine */ }

        try
        {
            Directory.CreateDirectory(LogDirectory);
            string filePath = Path.Combine(LogDirectory, $"log-{DateTime.Now:yyyyMMdd}.txt");
            File.AppendAllText(filePath, line + Environment.NewLine);
        }
        catch { /* best-effort -- a failed log write must never crash the caller */ }
    }

    /// <summary>Same "{Name}"-style message-template substitution the Serilog-based original
    /// used, without needing Serilog itself: positional, in order, missing/extra args are
    /// tolerated rather than throwing.</summary>
    private static string FormatTemplate(string template, object?[] args)
    {
        if (args.Length == 0) return template;

        int argIndex = 0;
        var result = new System.Text.StringBuilder(template.Length + 16);
        for (int i = 0; i < template.Length; i++)
        {
            if (template[i] == '{' && argIndex < args.Length)
            {
                int close = template.IndexOf('}', i);
                if (close > i)
                {
                    result.Append(args[argIndex++]);
                    i = close;
                    continue;
                }
            }
            result.Append(template[i]);
        }
        return result.ToString();
    }
}
