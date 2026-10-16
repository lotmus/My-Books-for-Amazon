using System.IO;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using BookWriter.Engine;
using Microsoft.Win32;

namespace BookWriter.App;

/// <summary>
/// The "Edit a Manuscript" tab: open an existing <c>.txt</c> / <c>.md</c> / <c>.docx</c>
/// manuscript (<see cref="ManuscriptImporter"/> splits it into chapters), pick which
/// <see cref="EditPass"/>es to run, then revise one chapter or the whole book with
/// <see cref="BookChapterEditor"/>. Edits apply straight to the working copy, but the
/// as-imported text of every chapter is kept so the Original / Current panes always show a real
/// before-and-after and any chapter (or the whole book) can be reverted. The revised
/// <see cref="Book"/> is handed to the shared <see cref="BookOutputControls"/> for cover art
/// and EPUB/Word/PDF export -- exactly the same output path as a book written from scratch.
/// </summary>
public partial class BookEditorView : UserControl
{
    private readonly ApiKeys _apiKeys = ApiKeys.Load();
    private readonly Dictionary<EditPass, CheckBox> _passChecks = new();
    private readonly bool _providerConfigured;

    private Book? _book;
    private List<string> _baseline = new();      // chapter text exactly as imported, never mutated
    private List<string> _changeLog = new();     // per-chapter running "what changed" text ("" = untouched)
    private CancellationTokenSource? _editCts;
    private bool _refreshingList;
    private bool _busy;

    public BookEditorView()
    {
        InitializeComponent();

        _providerConfigured = new BookChapterEditor(
            _apiKeys.OpenAiKey, _apiKeys.AnthropicApiKey, _apiKeys.GeminiApiKey,
            _apiKeys.XaiApiKey, _apiKeys.YandexApiKey, _apiKeys.YandexFolderId).AnyProviderConfigured;

        GenreCombo.DisplayMemberPath = "Name";
        GenreCombo.SelectedValuePath = "Value";
        GenreCombo.ItemsSource = Enum.GetValues<BookGenre>()
            .Select(g => new { Value = g, Name = BookGenreRules.DisplayName(g) })
            .ToList();
        GenreCombo.SelectedValue = BookGenre.Fiction;

        foreach (EditPass pass in EditPassInfo.All)
        {
            var check = new CheckBox
            {
                Content = EditPassInfo.DisplayName(pass),
                IsChecked = pass is EditPass.Bugs,
                Margin = new Thickness(0, 0, 16, 0),
                ToolTip = EditPassInfo.Description(pass),
            };
            _passChecks[pass] = check;
            PassCheckboxPanel.Children.Add(check);
        }

        if (!_providerConfigured)
            StatusText.Text = "No AI provider key is configured — editing needs at least one. See the manual (\"Setting up API keys\").";
    }

    // ==================== Opening a manuscript ====================

    private void BtnOpenManuscript_Click(object sender, RoutedEventArgs e)
    {
        if (GenreCombo.SelectedValue is not BookGenre genre) genre = BookGenre.Fiction;

        var dlg = new OpenFileDialog
        {
            Filter = ManuscriptImporter.OpenFileDialogFilter,
            Title = "Open a manuscript to edit",
            InitialDirectory = RecentFolderMemory.GetLastFolder("import-manuscript") ?? "",
        };
        if (dlg.ShowDialog() != true) return;

        RecentFolderMemory.RememberPath("import-manuscript", dlg.FileName);

        (Book? book, string error) = ManuscriptImporter.Import(dlg.FileName, genre);
        if (book is null)
        {
            StatusText.Text = "Could not open that manuscript: " + error;
            return;
        }

        _book = book;
        _baseline = new List<string>(book.ChapterContents);
        _changeLog = Enumerable.Repeat("", book.ChapterContents.Count).ToList();

        LoadedFileText.Text = $"{Path.GetFileName(dlg.FileName)}  ·  {book.ChapterContents.Count} chapter(s)";
        RefreshChapterList();
        if (ChaptersListBox.Items.Count > 0) ChaptersListBox.SelectedIndex = 0;

        OutputControls.SetBook(book);
        RefreshButtons();
        StatusText.Text = $"Imported \"{book.Outline.Title}\". Pick your passes, then edit a chapter or the whole book.";
    }

    private void GenreCombo_SelectionChanged(object sender, SelectionChangedEventArgs e)
    {
        if (_book is not null && GenreCombo.SelectedValue is BookGenre genre)
            _book.Outline.Genre = genre;
    }

    // ==================== Chapter list / selection ====================

    private void RefreshChapterList()
    {
        if (_book is null) return;

        int previous = ChaptersListBox.SelectedIndex;
        _refreshingList = true;

        ChaptersListBox.ItemsSource = _book.Outline.Chapters
            .Select((chapter, i) =>
            {
                string mark = i < _changeLog.Count && _changeLog[i].Length > 0 ? "✎ " : "    ";
                return $"{mark}Chapter {chapter.Number}: {chapter.Title}";
            })
            .ToList();

        _refreshingList = false;
        ChaptersListBox.SelectedIndex = previous >= 0 && previous < ChaptersListBox.Items.Count
            ? previous
            : (ChaptersListBox.Items.Count > 0 ? 0 : -1);
    }

    private void ChaptersListBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
    {
        if (_refreshingList) return;
        RefreshChapterView();
        RefreshButtons();
    }

    private void RefreshChapterView()
    {
        int index = ChaptersListBox.SelectedIndex;
        if (_book is null || index < 0 || index >= _book.ChapterContents.Count)
        {
            OriginalBox.Text = CurrentBox.Text = ChangeLogBox.Text = "";
            CurrentHeader.Text = "Current";
            return;
        }

        OriginalBox.Text = index < _baseline.Count ? _baseline[index] : "";
        CurrentBox.Text = _book.ChapterContents[index];

        bool edited = index < _changeLog.Count && _changeLog[index].Length > 0;
        CurrentHeader.Text = edited ? "Current (edited)" : "Current (unchanged)";
        ChangeLogBox.Text = edited ? _changeLog[index] : "(no edits to this chapter yet)";
    }

    // ==================== Editing ====================

    private List<EditPass> SelectedPasses() =>
        EditPassInfo.All.Where(p => _passChecks[p].IsChecked == true).ToList();

    private async void BtnEditChapter_Click(object sender, RoutedEventArgs e)
    {
        int index = ChaptersListBox.SelectedIndex;
        if (_book is null || index < 0) return;

        List<EditPass> passes = SelectedPasses();
        if (passes.Count == 0) { StatusText.Text = "Tick at least one editorial pass first."; return; }

        _editCts = new CancellationTokenSource();
        SetBusy(true);
        StatusText.Text = $"Editing chapter {_book.Outline.Chapters[index].Number}...";

        try
        {
            (bool ok, string message) = await RunEditAsync(index, passes, _editCts.Token);
            StatusText.Text = message;
            RefreshChapterList();
            ChaptersListBox.SelectedIndex = index;
            RefreshChapterView();
        }
        catch (OperationCanceledException)
        {
            StatusText.Text = "Edit cancelled.";
        }
        finally
        {
            SetBusy(false);
            _editCts?.Dispose();
            _editCts = null;
            RefreshButtons();
        }
    }

    private async void BtnEditAll_Click(object sender, RoutedEventArgs e)
    {
        if (_book is null) return;

        List<EditPass> passes = SelectedPasses();
        if (passes.Count == 0) { StatusText.Text = "Tick at least one editorial pass first."; return; }

        _editCts = new CancellationTokenSource();
        CancellationToken ct = _editCts.Token;
        SetBusy(true);

        int edited = 0, failed = 0;
        try
        {
            for (int i = 0; i < _book.Outline.Chapters.Count; i++)
            {
                ct.ThrowIfCancellationRequested();
                StatusText.Text = $"Editing chapter {_book.Outline.Chapters[i].Number} of {_book.Outline.Chapters.Count}...";
                (bool ok, string _) = await RunEditAsync(i, passes, ct);
                if (ok) edited++; else failed++;
                RefreshChapterList();
                ChaptersListBox.SelectedIndex = i;
                RefreshChapterView();
            }

            StatusText.Text = failed == 0
                ? $"Edited all {edited} chapter(s). Review each, then export."
                : $"Edited {edited} chapter(s); {failed} could not be edited and were left as-is (see each chapter's log).";
        }
        catch (OperationCanceledException)
        {
            StatusText.Text = $"Stopped after editing {edited} chapter(s).";
        }
        finally
        {
            SetBusy(false);
            _editCts?.Dispose();
            _editCts = null;
            RefreshButtons();
        }
    }

    /// <summary>Runs the selected passes on one chapter and, on success, applies the revised
    /// text to the working copy and appends to that chapter's log. Returns (didChange, message).
    /// A provider failure is not thrown -- it comes back as (false, honest reason) and the
    /// chapter keeps its current text.</summary>
    private async Task<(bool Changed, string Message)> RunEditAsync(int index, List<EditPass> passes, CancellationToken ct)
    {
        Book book = _book!;
        ChapterOutline chapter = book.Outline.Chapters[index];

        var context = new BookEditContext
        {
            Title = book.Outline.Title,
            Genre = book.Outline.Genre,
            AllChapters = book.Outline.Chapters.Select(c => (c.Number, c.Title)).ToList(),
        };

        ChapterEditResult result = await new BookChapterEditor(
                _apiKeys.OpenAiKey, _apiKeys.AnthropicApiKey, _apiKeys.GeminiApiKey,
                _apiKeys.XaiApiKey, _apiKeys.YandexApiKey, _apiKeys.YandexFolderId)
            .EditChapterAsync(context, book.ChapterContents[index], chapter.Number, chapter.Title,
                passes, EditorNotesBox.Text.Trim(), ct);

        if (result.Error.Length > 0)
        {
            AppendLog(index, $"[{DateTime.Now:HH:mm}] Edit failed: {result.Error}");
            return (false, $"Chapter {chapter.Number}: {result.Error}");
        }

        if (!result.Changed)
        {
            AppendLog(index, $"[{DateTime.Now:HH:mm}] {PassList(passes)} — editor reported no changes needed.");
            return (false, $"Chapter {chapter.Number}: the editor found nothing to change for the selected passes.");
        }

        book.ChapterContents[index] = result.RevisedText;
        string summary = result.ChangeSummary.Length > 0 ? result.ChangeSummary : "(no change list returned)";
        AppendLog(index, $"[{DateTime.Now:HH:mm}] {PassList(passes)}\n{summary}");
        OutputControls.SetBook(book);
        return (true, $"Chapter {chapter.Number} edited.");
    }

    private void AppendLog(int index, string entry)
    {
        if (index < 0 || index >= _changeLog.Count) return;
        _changeLog[index] = _changeLog[index].Length == 0 ? entry : _changeLog[index] + "\n\n" + entry;
    }

    private static string PassList(IEnumerable<EditPass> passes) =>
        "Passes: " + string.Join(", ", passes.Select(EditPassInfo.DisplayName));

    // ==================== Revert ====================

    private void BtnRevertChapter_Click(object sender, RoutedEventArgs e)
    {
        int index = ChaptersListBox.SelectedIndex;
        if (_book is null || index < 0 || index >= _book.ChapterContents.Count) return;

        _book.ChapterContents[index] = _baseline[index];
        _changeLog[index] = "";
        OutputControls.SetBook(_book);
        RefreshChapterList();
        ChaptersListBox.SelectedIndex = index;
        RefreshChapterView();
        RefreshButtons();
        StatusText.Text = $"Chapter {_book.Outline.Chapters[index].Number} reverted to the imported text.";
    }

    private void BtnRevertAll_Click(object sender, RoutedEventArgs e)
    {
        if (_book is null) return;

        for (int i = 0; i < _book.ChapterContents.Count; i++)
        {
            _book.ChapterContents[i] = _baseline[i];
            _changeLog[i] = "";
        }
        OutputControls.SetBook(_book);
        RefreshChapterList();
        RefreshChapterView();
        RefreshButtons();
        StatusText.Text = "All chapters reverted to the imported text.";
    }

    // ==================== Busy / button state ====================

    private void BtnCancelEdit_Click(object sender, RoutedEventArgs e)
    {
        _editCts?.Cancel();
        StatusText.Text = "Cancelling...";
    }

    private void SetBusy(bool busy)
    {
        _busy = busy;
        BusyBar.Visibility = busy ? Visibility.Visible : Visibility.Collapsed;
        BtnCancelEdit.Visibility = busy ? Visibility.Visible : Visibility.Collapsed;
        OutputControls.IsEnabled = !busy;
        BtnOpenManuscript.IsEnabled = !busy;
        RefreshButtons();
    }

    private void RefreshButtons()
    {
        if (_busy)
        {
            BtnEditChapter.IsEnabled = BtnEditAll.IsEnabled = BtnRevertChapter.IsEnabled = BtnRevertAll.IsEnabled = false;
            return;
        }

        bool hasBook = _book is not null;
        bool provider = _providerConfigured;
        bool chapterSelected = ChaptersListBox.SelectedIndex >= 0;
        int index = ChaptersListBox.SelectedIndex;
        bool chapterEdited = hasBook && index >= 0 && index < _changeLog.Count && _changeLog[index].Length > 0;
        bool anyEdited = hasBook && _changeLog.Any(l => l.Length > 0);

        BtnEditChapter.IsEnabled = hasBook && provider && chapterSelected;
        BtnEditAll.IsEnabled = hasBook && provider;
        BtnRevertChapter.IsEnabled = chapterEdited;
        BtnRevertAll.IsEnabled = anyEdited;
    }
}
