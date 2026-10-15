using System.Text.Json;
using System.Text.Json.Serialization;

namespace BookWriter.Engine;

/// <summary>
/// A saved snapshot of an in-progress or finished <see cref="Book"/> -- title, genre, premise,
/// story bible, chapter outline, chapter text, and cover path -- written to and read back from a
/// single JSON file, so a book no longer has to be exported before closing the app to avoid
/// losing it (the "no project save/load" limitation the manual used to list).
///
/// A plain serialization DTO, not <see cref="Book"/>/<see cref="BookOutline"/> themselves:
/// <see cref="Book"/> has no parameterless constructor and <see cref="BookOutline.Chapters"/>/
/// <c>Characters</c> are get-only collections filled after construction, both deliberate for
/// every OTHER caller in this codebase (an outline is meant to be fixed once planned) -- rather
/// than loosen that shape for one serializer's convenience, this type exists purely to give
/// System.Text.Json something with a normal, mutable shape to work with, and converts to/from a
/// real <see cref="Book"/> on either side.
/// </summary>
public sealed class BookProjectFile
{
    public int FormatVersion { get; set; } = 1;
    public string Title { get; set; } = "";
    public BookGenre Genre { get; set; }
    public string Premise { get; set; } = "";
    public string Setting { get; set; } = "";
    public string PlotArc { get; set; } = "";
    public List<BookCharacter> Characters { get; set; } = new();
    public List<ChapterOutline> Chapters { get; set; } = new();
    public List<string> ChapterContents { get; set; } = new();
    public string? CoverImagePath { get; set; }

    public static BookProjectFile FromBook(Book book) => new()
    {
        Title = book.Outline.Title,
        Genre = book.Outline.Genre,
        Premise = book.Outline.Premise,
        Setting = book.Outline.Setting,
        PlotArc = book.Outline.PlotArc,
        Characters = new List<BookCharacter>(book.Outline.Characters),
        Chapters = new List<ChapterOutline>(book.Outline.Chapters),
        ChapterContents = new List<string>(book.ChapterContents),
        CoverImagePath = book.CoverImagePath,
    };

    public Book ToBook()
    {
        var outline = new BookOutline { Title = Title, Genre = Genre, Premise = Premise, Setting = Setting, PlotArc = PlotArc };
        outline.Characters.AddRange(Characters);
        outline.Chapters.AddRange(Chapters);

        var book = new Book(outline) { CoverImagePath = CoverImagePath };
        book.ChapterContents.AddRange(ChapterContents);
        return book;
    }
}

/// <summary>Saves/loads a <see cref="Book"/> as one indented, human-readable JSON file. Never
/// throws for an ordinary I/O problem (bad path, disk full, corrupt/foreign JSON) -- returns an
/// honest error string instead, same convention as every exporter in this project. Unlike the
/// exporters, this does not need the temp-file-then-move dance: a save that fails partway (e.g.
/// disk full) is caught by the same try/catch before anything is reported as successful, and a
/// half-written project file is no worse an outcome than the save having been reported as failed
/// in the first place -- the previous save (if any) at that same path may already be
/// overwritten, but there was nothing at stake there that export-before-closing wouldn't already
/// have carried the same risk for.</summary>
public static class BookProjectStore
{
    public const string FileExtension = ".bookproject.json";
    public const string OpenFileDialogFilter = "Book Writer project (*.bookproject.json)|*.bookproject.json|All files (*.*)|*.*";

    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        WriteIndented = true,
        PropertyNameCaseInsensitive = true,
        Converters = { new JsonStringEnumConverter() },
    };

    public static string Save(Book book, string path)
    {
        if (book is null) return "No book to save.";
        if (string.IsNullOrWhiteSpace(path)) return "No output path supplied.";

        try
        {
            string json = JsonSerializer.Serialize(BookProjectFile.FromBook(book), JsonOptions);
            string? dir = Path.GetDirectoryName(Path.GetFullPath(path));
            if (!string.IsNullOrEmpty(dir)) Directory.CreateDirectory(dir);
            File.WriteAllText(path, json);
            AppLog.Info("BookProjectStore: saved {Path}", path);
            return "";
        }
        catch (Exception ex)
        {
            AppLog.Warning("BookProjectStore: save failed for {Path} - {Error}", path, ex.Message);
            return "Could not save the project: " + ex.Message;
        }
    }

    public static (Book? Book, string Error) Load(string path)
    {
        if (string.IsNullOrWhiteSpace(path)) return (null, "No file was supplied.");
        if (!File.Exists(path)) return (null, $"File not found: \"{path}\".");

        try
        {
            string json = File.ReadAllText(path);
            BookProjectFile? file = JsonSerializer.Deserialize<BookProjectFile>(json, JsonOptions);
            if (file is null || file.Chapters.Count == 0 && file.Title.Length == 0)
                return (null, "That file is not a valid Book Writer project.");

            AppLog.Info("BookProjectStore: loaded {Path} ({Chapters} chapter(s))", path, file.Chapters.Count);
            return (file.ToBook(), "");
        }
        catch (Exception ex)
        {
            AppLog.Warning("BookProjectStore: load failed for {Path} - {Error}", path, ex.Message);
            return (null, "Could not open that project file: " + ex.Message);
        }
    }
}
