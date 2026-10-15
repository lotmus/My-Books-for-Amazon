using System.IO;

namespace BookWriter.App;

/// <summary>
/// Trimmed down from MediaStar.GPT's own MediaMaker.Core.AppPaths when Book Writer was spun out
/// into its own standalone app -- keeps only the handful of paths this app actually uses
/// (ffmpeg for cover-art finishing, a scratch work folder, a durable exports folder), following
/// the same "hardcoded absolute path to this app's own install root, Tools/ never redistributed
/// or auto-installed" convention the original established for a personal, locally-run tool.
/// </summary>
public static class AppPaths
{
    /// <summary>This app's own bundled-tools root -- currently just ffmpeg.exe, copied in
    /// manually (not committed to git, not auto-installed) the same way MediaStar.GPT's own
    /// Tools/ never redistributes ffmpeg either.</summary>
    public const string ToolsRoot = @"D:\My_C#_Apps\Book Writer\Tools";

    public static string FfmpegExe { get; } = Path.Combine(ToolsRoot, "ffmpeg.exe");

    /// <summary>Durable, user-browsable home for exported books -- BookWriterView's own
    /// export flow creates an "Exports\Books" subfolder under this on first use.</summary>
    public const string ExportsFolder = @"D:\My_C#_Apps\Book Writer\Exports";

    /// <summary>Scratch folder for in-progress work (e.g. cover-art generation's own temp
    /// files before the finished cover is written back into a durable location).</summary>
    public static string WorkFolder(string subsystem) =>
        Path.Combine(Path.GetTempPath(), "BookWriter", subsystem);
}
