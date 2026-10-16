using System.Windows;

namespace BookWriter.App;

/// <summary>
/// Book Writer's own top-level window -- unlike MediaStar.GPT's MainWindow, there is no
/// multi-workspace sidebar; just two tabs for the app's two jobs: "Write a Book"
/// (<see cref="BookWriterView"/> -- plan and generate a book from a prompt or a full setup) and
/// "Edit a Manuscript" (<see cref="BookEditorView"/> -- import an existing manuscript and run
/// editorial passes over it). Both hand their finished <see cref="Engine.Book"/> to a shared
/// <see cref="BookOutputControls"/> for cover art and EPUB/Word/PDF export.
/// </summary>
public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }
}
