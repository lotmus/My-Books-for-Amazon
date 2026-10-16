using System.IO;
using System.Windows;
using System.Windows.Controls;
using BookWriter.Engine;
using Microsoft.Win32;

namespace BookWriter.App;

/// <summary>
/// The "Write a Book" tab: an optional free-form Starter prompt (BookStarterGenerator drafts
/// title/genre/premise/chapter-count from one sentence), then Setup (those same four fields, by
/// hand or edited from the draft), then Write Book (BookWritingPipeline.WriteAsync, fully
/// automatic start to finish, with no per-chapter review checkpoint -- an explicit product
/// decision, see BookWritingPipeline's own doc comment). The finished book is browsed here and
/// handed to the shared <see cref="BookOutputControls"/> for cover art and export.
///
/// Ported from MediaStar.GPT's MediaMaker.BookWriter.Wpf.BookWriterView when Book Writer was
/// spun out; the Starter prompt, the genre-rules combo and the shared output panel were added
/// afterward.
/// </summary>
public partial class BookWriterView : UserControl
{
    private readonly ApiKeys _apiKeys;

    private Book? _book;
    private CancellationTokenSource? _writeCts;
    private CancellationTokenSource? _draftCts;

    public BookWriterView()
    {
        InitializeComponent();

        _apiKeys = ApiKeys.Load();

        GenreCombo.DisplayMemberPath = "Name";
        GenreCombo.SelectedValuePath = "Value";
        GenreCombo.ItemsSource = Enum.GetValues<BookGenre>()
            .Select(g => new { Value = g, Name = BookGenreRules.DisplayName(g) })
            .ToList();
        GenreCombo.SelectedValue = BookGenre.FictionWithScienceAppendix;
    }

    private async void BtnDraftFromPrompt_Click(object sender, RoutedEventArgs e)
    {
        string prompt = StarterPromptBox.Text.Trim();
        if (prompt.Length == 0)
        {
            StatusText.Text = "Type a sentence or two describing the book first.";
            return;
        }

        _draftCts?.Cancel();
        _draftCts?.Dispose();
        _draftCts = new CancellationTokenSource();
        CancellationToken ct = _draftCts.Token;

        BtnDraftFromPrompt.IsEnabled = false;
        BusyBar.Visibility = Visibility.Visible;
        StatusText.Text = "Drafting a setup from your prompt...";

        try
        {
            var drafter = new BookStarterGenerator(
                _apiKeys.OpenAiKey, _apiKeys.AnthropicApiKey, _apiKeys.YandexApiKey, _apiKeys.YandexFolderId);
            (BookStarter starter, string note) = await drafter.GenerateAsync(prompt, ct);

            TitleBox.Text = starter.Title;
            GenreCombo.SelectedValue = starter.Genre;
            PremiseBox.Text = starter.Premise;
            ChapterCountBox.Text = starter.ChapterCount.ToString();
            StatusText.Text = note;
        }
        catch (OperationCanceledException)
        {
            StatusText.Text = "Draft cancelled.";
        }
        catch (Exception ex)
        {
            AppLog.Warning("BookWriterView: drafting setup failed - {Error}", ex.Message);
            StatusText.Text = "Could not draft a setup: " + ex.Message;
        }
        finally
        {
            BtnDraftFromPrompt.IsEnabled = true;
            if (BtnWriteBook.IsEnabled) BusyBar.Visibility = Visibility.Collapsed;
        }
    }

    private async void BtnWriteBook_Click(object sender, RoutedEventArgs e)
    {
        string title = TitleBox.Text.Trim();
        if (title.Length == 0)
        {
            StatusText.Text = "Enter a title first (or draft one from a starter prompt).";
            return;
        }

        if (GenreCombo.SelectedValue is not BookGenre genre)
        {
            StatusText.Text = "Select a genre first.";
            return;
        }

        if (!int.TryParse(ChapterCountBox.Text.Trim(), out int chapterCount) || chapterCount <= 0)
        {
            StatusText.Text = "Chapter count must be a positive whole number.";
            return;
        }

        string premise = PremiseBox.Text.Trim();

        _writeCts?.Cancel();
        _writeCts?.Dispose();
        _writeCts = new CancellationTokenSource();
        CancellationToken ct = _writeCts.Token;

        BtnWriteBook.IsEnabled = false;
        // The shared output panel is disabled wholesale while a (re-)write is in flight: a
        // re-write can replace _book out from under an in-flight cover-art/export call.
        OutputControls.IsEnabled = false;
        BtnCancelWrite.Visibility = Visibility.Visible;
        BusyBar.Visibility = Visibility.Visible;
        StatusText.Text = "Starting book generation...";

        // Progress<T> captures the current (UI-thread) SynchronizationContext at construction,
        // so every Report() from the background work is marshalled back here automatically.
        var progress = new Progress<string>(msg => StatusText.Text = msg);

        try
        {
            var writer = new BookWritingPipeline(
                _apiKeys.OpenAiKey, _apiKeys.AnthropicApiKey, _apiKeys.GeminiApiKey,
                _apiKeys.XaiApiKey, _apiKeys.YandexApiKey, _apiKeys.YandexFolderId);
            Book book = await writer.WriteAsync(title, genre, premise, chapterCount, progress, ct);
            ApplyBook(book);
        }
        catch (OperationCanceledException)
        {
            StatusText.Text = "Book generation cancelled.";
        }
        catch (Exception ex)
        {
            AppLog.Warning("BookWriterView: writing \"{Title}\" failed - {Error}", title, ex.Message);
            StatusText.Text = "Writing the book failed: " + ex.Message;
        }
        finally
        {
            BusyBar.Visibility = Visibility.Collapsed;
            BtnCancelWrite.Visibility = Visibility.Collapsed;
            BtnWriteBook.IsEnabled = true;
            OutputControls.IsEnabled = true;
            // Reflects whichever book (if any) most recently finished writing successfully: a
            // cancelled/failed re-write must not wipe out a still-good prior book in _book.
            OutputControls.SetBook(_book);
        }
    }

    private void BtnCancelWrite_Click(object sender, RoutedEventArgs e)
    {
        _writeCts?.Cancel();
        StatusText.Text = "Cancelling...";
    }

    /// <summary>Wires a freshly-written (or re-written) Book into the chapter list and the
    /// shared output panel. The final "Finished writing..." status is left to
    /// BookWritingPipeline.WriteAsync's own last IProgress report rather than repeated here.</summary>
    private void ApplyBook(Book book)
    {
        _book = book;
        RefreshChapterList();
        ChapterContentBox.Text = "";
        OutputControls.SetBook(book);
        BtnSaveProject.IsEnabled = true;
        RefreshRetryButtons();
    }

    /// <summary>The exact placeholder text BookWritingPipeline.WriteAsync writes into
    /// ChapterContents for a chapter every configured provider tier failed on -- see that
    /// class's own doc comment. Checked here (and in BookChapterEditor indirectly via the same
    /// convention) purely by its fixed opening words, not by any separate "did this fail" flag,
    /// since the placeholder text IS the book's own honest record of the failure.</summary>
    private static bool IsFailedPlaceholder(string chapterText) =>
        chapterText.StartsWith("[This chapter could not be generated:", StringComparison.Ordinal);

    /// <summary>Rebuilds the chapter list from the current _book, marking every chapter whose
    /// content is still a failure placeholder with a "⚠" prefix (same "mark it in the list, don't
    /// make the author hunt for it" convention BookEditorView uses for edited chapters), and
    /// restores the previous selection when it's still valid.</summary>
    private void RefreshChapterList()
    {
        if (_book is null) return;

        int previousIndex = ChaptersListBox.SelectedIndex;
        ChaptersListBox.ItemsSource = _book.Outline.Chapters
            .Select((chapter, i) =>
            {
                bool failed = i < _book.ChapterContents.Count && IsFailedPlaceholder(_book.ChapterContents[i]);
                string mark = failed ? "⚠ " : "    ";
                return $"{mark}Chapter {chapter.Number}: {chapter.Title}";
            })
            .ToList();

        ChaptersListBox.SelectedIndex = previousIndex >= 0 && previousIndex < ChaptersListBox.Items.Count ? previousIndex : -1;
    }

    private void ChaptersListBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
    {
        RefreshSelectedChapterText();
        RefreshRetryButtons();
    }

    private void RefreshSelectedChapterText()
    {
        int index = ChaptersListBox.SelectedIndex;
        if (index < 0 || _book is null)
        {
            ChapterContentBox.Text = "";
            return;
        }

        // Outline.Chapters.Count and ChapterContents.Count are allowed to differ for a
        // partially-written book: an honest placeholder for a missing index instead of an
        // IndexOutOfRangeException.
        ChapterContentBox.Text = index < _book.ChapterContents.Count
            ? _book.ChapterContents[index]
            : "(This chapter has not been written yet.)";
    }

    // ==================== Per-chapter retry ====================

    private void RefreshRetryButtons()
    {
        bool hasBook = _book is not null;
        bool chapterSelected = hasBook && ChaptersListBox.SelectedIndex >= 0;
        bool anyFailed = hasBook && _book!.ChapterContents.Any(IsFailedPlaceholder);
        BtnRetryChapter.IsEnabled = chapterSelected;
        BtnRetryAllFailed.IsEnabled = anyFailed;
    }

    private async void BtnRetryChapter_Click(object sender, RoutedEventArgs e)
    {
        int index = ChaptersListBox.SelectedIndex;
        if (_book is null || index < 0) return;
        await RetryChaptersAsync(new[] { index });
    }

    private async void BtnRetryAllFailed_Click(object sender, RoutedEventArgs e)
    {
        if (_book is null) return;
        List<int> failedIndices = Enumerable.Range(0, _book.ChapterContents.Count)
            .Where(i => IsFailedPlaceholder(_book.ChapterContents[i]))
            .ToList();
        if (failedIndices.Count == 0)
        {
            StatusText.Text = "No failed chapters to retry.";
            return;
        }
        await RetryChaptersAsync(failedIndices);
    }

    /// <summary>Regenerates just the given chapters in place, via a fresh BookChapterGenerator
    /// call per chapter (the same one-chapter call BookWritingPipeline.WriteAsync itself uses) --
    /// never a full-book rewrite. Each chapter still gets the whole outline as context, per
    /// BookChapterGenerator's own continuity design, so a retried chapter stays consistent with
    /// the rest of the book. A chapter that fails again keeps its (possibly updated) honest
    /// placeholder rather than the run stopping outright, matching the original write's own
    /// honest-degrade contract.</summary>
    private async Task RetryChaptersAsync(IReadOnlyList<int> indices)
    {
        Book book = _book!;

        _writeCts?.Cancel();
        _writeCts?.Dispose();
        _writeCts = new CancellationTokenSource();
        CancellationToken ct = _writeCts.Token;

        BtnWriteBook.IsEnabled = false;
        BtnRetryChapter.IsEnabled = false;
        BtnRetryAllFailed.IsEnabled = false;
        OutputControls.IsEnabled = false;
        BtnCancelWrite.Visibility = Visibility.Visible;
        BusyBar.Visibility = Visibility.Visible;

        var generator = new BookChapterGenerator(
            _apiKeys.OpenAiKey, _apiKeys.AnthropicApiKey, _apiKeys.GeminiApiKey,
            _apiKeys.XaiApiKey, _apiKeys.YandexApiKey, _apiKeys.YandexFolderId);

        int succeeded = 0, stillFailed = 0;
        try
        {
            foreach (int index in indices)
            {
                ct.ThrowIfCancellationRequested();
                ChapterOutline chapterOutline = book.Outline.Chapters[index];
                StatusText.Text = $"Retrying chapter {chapterOutline.Number}: \"{chapterOutline.Title}\"...";

                (string text, string error) = await generator.GenerateChapterAsync(book.Outline, index, ct);
                if (text.Length > 0)
                {
                    book.ChapterContents[index] = text;
                    succeeded++;
                }
                else
                {
                    book.ChapterContents[index] =
                        $"[This chapter could not be generated: {error} You can retry it individually, or write it manually and replace this placeholder before exporting.]";
                    stillFailed++;
                    AppLog.Warning("BookWriterView: retry failed for chapter {Number} - {Error}", chapterOutline.Number, error);
                }
            }

            StatusText.Text = stillFailed == 0
                ? $"Retried {succeeded} chapter(s) successfully."
                : $"Retried {indices.Count} chapter(s): {succeeded} succeeded, {stillFailed} still failed.";
        }
        catch (OperationCanceledException)
        {
            StatusText.Text = $"Retry cancelled after {succeeded} of {indices.Count} chapter(s).";
        }
        finally
        {
            BusyBar.Visibility = Visibility.Collapsed;
            BtnCancelWrite.Visibility = Visibility.Collapsed;
            BtnWriteBook.IsEnabled = true;
            OutputControls.IsEnabled = true;
            RefreshChapterList();
            RefreshSelectedChapterText();
            RefreshRetryButtons();
            OutputControls.SetBook(book);
        }
    }

    // ==================== Project save/load ====================

    private void BtnSaveProject_Click(object sender, RoutedEventArgs e)
    {
        if (_book is null) return;

        string projectsFolder = Path.Combine(AppPaths.ExportsFolder, "Books");
        Directory.CreateDirectory(projectsFolder);
        string baseName = _book.Outline.Title.Trim().Length > 0
            ? string.Concat(_book.Outline.Title.Trim().Select(c => Path.GetInvalidFileNameChars().Contains(c) ? '_' : c))
            : "Book";

        var dlg = new SaveFileDialog
        {
            Filter = BookProjectStore.OpenFileDialogFilter,
            Title = "Save Project",
            FileName = baseName + BookProjectStore.FileExtension,
            InitialDirectory = RecentFolderMemory.GetLastFolder("book-project") ?? projectsFolder,
        };
        if (dlg.ShowDialog() != true) return;

        RecentFolderMemory.RememberPath("book-project", dlg.FileName);
        string result = BookProjectStore.Save(_book, dlg.FileName);
        StatusText.Text = result.Length == 0 ? $"Saved project: {dlg.FileName}" : $"Could not save project: {result}";
    }

    private void BtnLoadProject_Click(object sender, RoutedEventArgs e)
    {
        var dlg = new OpenFileDialog
        {
            Filter = BookProjectStore.OpenFileDialogFilter,
            Title = "Load Project",
            InitialDirectory = RecentFolderMemory.GetLastFolder("book-project") ?? "",
        };
        if (dlg.ShowDialog() != true) return;

        RecentFolderMemory.RememberPath("book-project", dlg.FileName);
        (Book? book, string error) = BookProjectStore.Load(dlg.FileName);
        if (book is null)
        {
            StatusText.Text = "Could not load project: " + error;
            return;
        }

        TitleBox.Text = book.Outline.Title;
        GenreCombo.SelectedValue = book.Outline.Genre;
        PremiseBox.Text = book.Outline.Premise;
        ChapterCountBox.Text = book.Outline.Chapters.Count.ToString();
        ApplyBook(book);
        StatusText.Text = $"Loaded project: {dlg.FileName}";
    }
}
