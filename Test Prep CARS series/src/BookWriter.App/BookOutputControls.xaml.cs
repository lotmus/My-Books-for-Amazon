using System.IO;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media.Imaging;
using BookWriter.Engine;
using Microsoft.Win32;

namespace BookWriter.App;

/// <summary>
/// The "you have a finished (or partial) <see cref="Book"/> -- now make something out of it"
/// panel: generate KDP cover art, and export to EPUB / Word / PDF. Shared by both
/// <see cref="BookWriterView"/> (a book written from scratch) and <see cref="BookEditorView"/>
/// (a manuscript imported and revised) so the cover-art call and the Save-dialog-then-export
/// flow live in exactly one place.
///
/// The host view owns the <see cref="Book"/> and calls <see cref="SetBook"/> whenever it
/// changes (a re-write, a fresh import, an accepted edit); this control never mutates the book
/// except to set <see cref="Book.CoverImagePath"/> once cover art is generated. While the host
/// is busy doing its own thing (writing, editing), it sets <c>IsEnabled = false</c> on this
/// whole control so an in-flight export can't race a book being replaced underneath it.
/// </summary>
public partial class BookOutputControls : UserControl
{
    private readonly ApiKeys _apiKeys = ApiKeys.Load();
    private Book? _book;

    public BookOutputControls()
    {
        InitializeComponent();
    }

    /// <summary>Point this panel at the current book (or <c>null</c> to disable it). Clears any
    /// previously shown cover thumbnail when the book instance actually changes, since a cover
    /// belongs to one specific book.</summary>
    public void SetBook(Book? book)
    {
        bool changed = !ReferenceEquals(_book, book);
        _book = book;

        bool hasBook = book is not null;
        BtnGenerateCoverArt.IsEnabled = hasBook;
        BtnExportEpub.IsEnabled = hasBook;
        BtnExportDocx.IsEnabled = hasBook;
        BtnExportPdf.IsEnabled = hasBook;

        if (changed)
        {
            CoverArtImage.Source = book?.CoverImagePath is { Length: > 0 } path && File.Exists(path)
                ? LoadFrozenBitmap(path)
                : null;
            OutputStatusText.Text = "";
        }
    }

    private async void BtnGenerateCoverArt_Click(object sender, RoutedEventArgs e)
    {
        // Captured into a local rather than read from _book after the await below: nullable-flow
        // narrowing on a field doesn't survive an await, and a local keeps this specific call
        // acting on the exact book it started with even if _book moves on meanwhile.
        Book? book = _book;
        if (book is null) return;

        BtnGenerateCoverArt.IsEnabled = false;
        OutputStatusText.Text = "Generating cover art...";

        try
        {
            var generator = new BookCoverArtGenerator(
                AppPaths.FfmpegExe, _apiKeys.OpenAiKey, _apiKeys.GeminiApiKey,
                _apiKeys.YandexApiKey, _apiKeys.YandexFolderId);
            (string? coverPath, string note) = await generator.GenerateAsync(book.Outline, AppPaths.WorkFolder("BookWriter"));

            if (coverPath is not null)
            {
                book.CoverImagePath = coverPath;
                if (ReferenceEquals(book, _book))
                    CoverArtImage.Source = LoadFrozenBitmap(coverPath);
            }

            // GenerateAsync never throws: its Note is already the honest, human-readable outcome.
            OutputStatusText.Text = note;
        }
        catch (Exception ex)
        {
            AppLog.Warning("BookOutputControls: cover art generation failed - {Error}", ex.Message);
            OutputStatusText.Text = "Cover art generation failed: " + ex.Message;
        }
        finally
        {
            BtnGenerateCoverArt.IsEnabled = _book is not null;
        }
    }

    private void BtnExportEpub_Click(object sender, RoutedEventArgs e) =>
        ExportBook(BookEpubExporter.ExportToEpub, "EPUB", ".epub", "EPUB File (*.epub)|*.epub");

    private void BtnExportDocx_Click(object sender, RoutedEventArgs e) =>
        ExportBook(BookDocumentExporter.ExportToDocx, "Word Document", ".docx", "Word Document (*.docx)|*.docx");

    private void BtnExportPdf_Click(object sender, RoutedEventArgs e) =>
        ExportBook(BookDocumentExporter.ExportToPdf, "PDF Document", ".pdf", "PDF Document (*.pdf)|*.pdf");

    private delegate string StyledExporter(Book book, string outputPath, BookStyleOptions? style);

    /// <summary>Reads the Style group's six boxes into a <see cref="BookStyleOptions"/> for the
    /// export about to run. Blank font-name boxes fall back to the "Georgia" default rather than
    /// an empty font-family string; an invalid color box is silently treated as "no override" by
    /// <see cref="BookStyleOptions.NormalizeHex"/> itself, so a typo here never blocks an
    /// export.</summary>
    private BookStyleOptions ReadStyleOptions() => new()
    {
        HeadingFontFamily = string.IsNullOrWhiteSpace(HeadingFontBox.Text) ? "Georgia" : HeadingFontBox.Text.Trim(),
        HeadingBold = HeadingBoldCheck.IsChecked == true,
        HeadingColor = HeadingColorBox.Text,
        BodyFontFamily = string.IsNullOrWhiteSpace(BodyFontBox.Text) ? "Georgia" : BodyFontBox.Text.Trim(),
        BodyBold = BodyBoldCheck.IsChecked == true,
        BodyColor = BodyColorBox.Text,
    };

    /// <summary>
    /// Shared Save-dialog-then-export flow for all three export buttons. Defaults to
    /// AppPaths.ExportsFolder\Books (created on demand) with a filename sanitized from the
    /// book's own title, and remembers the last folder used.
    ///
    /// The three exporters don't share one simple success/failure return contract:
    /// BookEpubExporter.ExportToEpub returns "" for a real success and only ever a real error
    /// string otherwise, but BookDocumentExporter.ExportToDocx/ExportToPdf can also return a
    /// non-empty but still-a-success "partial book" note. A bare `result.Length == 0` check
    /// can't tell that note apart from an error, so this compares the destination file's own
    /// existence/last-write-time from just before the call to just after it.
    /// </summary>
    private void ExportBook(StyledExporter exporter, string label, string extension, string filter)
    {
        Book? book = _book;
        if (book is null) return;

        string booksFolder = Path.Combine(AppPaths.ExportsFolder, "Books");
        Directory.CreateDirectory(booksFolder);
        string baseName = book.Outline.Title.Trim().Length > 0 ? SanitizeFileName(book.Outline.Title.Trim()) : "Book";

        var dlg = new SaveFileDialog
        {
            Filter = filter,
            Title = "Export as " + label,
            FileName = baseName + extension,
            InitialDirectory = RecentFolderMemory.GetLastFolder("export-book") ?? booksFolder,
        };
        if (dlg.ShowDialog() != true) return;

        RecentFolderMemory.RememberPath("export-book", dlg.FileName);

        bool existedBefore = File.Exists(dlg.FileName);
        DateTime beforeWriteTimeUtc = existedBefore ? File.GetLastWriteTimeUtc(dlg.FileName) : default;

        string result = exporter(book, dlg.FileName, ReadStyleOptions());

        bool fileWasWritten = File.Exists(dlg.FileName) &&
            (!existedBefore || File.GetLastWriteTimeUtc(dlg.FileName) != beforeWriteTimeUtc);

        if (result.Length == 0)
            OutputStatusText.Text = $"Exported {label}: {dlg.FileName}";
        else if (fileWasWritten)
            OutputStatusText.Text = $"Exported {label}: {dlg.FileName} -- {result}";
        else
            OutputStatusText.Text = $"Could not export {label}: {result}";
    }

    private static string SanitizeFileName(string name)
    {
        foreach (char c in Path.GetInvalidFileNameChars())
            name = name.Replace(c, '_');
        return name;
    }

    /// <summary>Same ReadAllBytes-then-MemoryStream-then-Freeze load MediaStar.GPT's own
    /// thumbnail-loading helpers use: avoids holding a file lock on the loaded cover image,
    /// which matters because a later "Generate Cover Art" click can overwrite it.</summary>
    private static BitmapImage LoadFrozenBitmap(string path)
    {
        byte[] bytes = File.ReadAllBytes(path);
        var bmp = new BitmapImage();
        using var ms = new MemoryStream(bytes);
        bmp.BeginInit();
        bmp.CacheOption = BitmapCacheOption.OnLoad;
        bmp.StreamSource = ms;
        bmp.EndInit();
        bmp.Freeze();
        return bmp;
    }
}
