namespace BookWriter.Engine;

/// <summary>Which generation architecture BookOutlineGenerator/BookChapterGenerator use --
/// Fiction and FictionWithScienceAppendix carry a <see cref="BookOutline.Characters"/>/<see cref="BookOutline.Setting"/>/
/// <see cref="BookOutline.PlotArc"/> "book bible" into every chapter call for continuity
/// (names, relationships, and plot events must stay consistent across the whole manuscript);
/// NonFiction has none of that -- each chapter is a self-contained sub-topic building the
/// book's overall thesis, so no character/plot continuity state is needed. FictionWithScienceAppendix
/// additionally reserves the last 20-30% of chapters as "Appendix:" science explainers.</summary>
public enum BookGenre
{
    NonFiction,
    Fiction,
    FictionWithScienceAppendix,

    /// <summary>A self-paced exam-prep course book (lessons, Praxis Tips, original practice); see <see cref="ExamPrepRules"/>.</summary>
    ExamPrep,
}

/// <summary>Central place for genre-specific behaviour (story bible, science appendix, UI labels,
/// EPUB subject) so generators/exporters/UI do not each re-encode the same Fiction-vs-NonFiction
/// branching as the genre list grows.</summary>
public static class BookGenreRules
{
    public static bool UsesStoryBible(BookGenre genre) =>
        genre is BookGenre.Fiction or BookGenre.FictionWithScienceAppendix;

    public static bool IsExamPrep(BookGenre genre) => genre == BookGenre.ExamPrep;

    public static bool HasScienceAppendix(BookGenre genre) =>
        genre == BookGenre.FictionWithScienceAppendix;

    public static string DisplayName(BookGenre genre) => genre switch
    {
        BookGenre.NonFiction => "Non-Fiction",
        BookGenre.Fiction => "Fiction",
        BookGenre.FictionWithScienceAppendix => "Fiction + Science Appendix",
        BookGenre.ExamPrep => "Exam Prep Course",
        _ => genre.ToString(),
    };

    /// <summary>dc:subject value for EPUB metadata -- a short bookstore-style subject string.</summary>
    public static string EpubSubject(BookGenre genre) => genre switch
    {
        BookGenre.NonFiction => "Non-Fiction",
        BookGenre.Fiction => "Fiction",
        BookGenre.FictionWithScienceAppendix => "Fiction / Science",
        BookGenre.ExamPrep => "Education / Test Preparation",
        _ => genre.ToString(),
    };

    /// <summary>First words (case-insensitive) that mark a chapter as backmatter-style
    /// expository content -- science/reference material to be edited and labelled as such,
    /// not narrative fiction -- when they are the WHOLE first word of the title, not merely
    /// contained in it. Kept short and specific on purpose: each entry here was observed as a
    /// real title convention (this app's own "Appendix: <topic>" generation, and "COURSE -
    /// Spacetime for Investigators" / bare "Appendix A" seen importing real manuscripts via
    /// <see cref="ManuscriptImporter"/>), not a guess -- a narrower list means a narrative
    /// chapter that happens to be called, say, "The Bibliography of a Broken Man" is never
    /// mistaken for backmatter. Ordinary backmatter that ISN'T science/reference content
    /// (Acknowledgements, About the Author, Bibliography) is deliberately left out: this flag
    /// also drives BookChapterEditor's "treat as expository, not narrative" instruction, which
    /// would be the wrong call for a personal thank-you note.</summary>
    private static readonly string[] AppendixLikeFirstWords = { "appendix", "course", "glossary" };

    /// <summary>True when a chapter title is (or should be treated as) a science-appendix
    /// section: this app's own "Appendix: <topic>" convention, or a title whose first word is
    /// one of <see cref="AppendixLikeFirstWords"/> (a bare/lettered/numbered "Appendix", a
    /// "Course - ..." section, a "Glossary") -- the other real-world ways the same kind of
    /// backmatter shows up in a manuscript this app did not itself generate.</summary>
    public static bool LooksLikeAppendixChapter(string? title)
    {
        if (string.IsNullOrWhiteSpace(title)) return false;

        string trimmed = title.Trim();
        if (trimmed.StartsWith("Appendix:", StringComparison.OrdinalIgnoreCase)) return true;

        string firstWord = trimmed.Split(SectionWordSeparators, 2, StringSplitOptions.RemoveEmptyEntries) is [var w, ..]
            ? w
            : "";
        return Array.Exists(AppendixLikeFirstWords, word => word.Equals(firstWord, StringComparison.OrdinalIgnoreCase));
    }

    private static readonly char[] SectionWordSeparators = { ' ', '\t', ':', '-', '–', '—' };
}

/// <summary>One character in a Fiction book's "book bible" -- carried into every chapter's own
/// generation call (see BookChapterGenerator) so names/descriptions/roles stay consistent
/// across chapters written by separate AI calls that don't otherwise share memory of each
/// other.</summary>
public sealed class BookCharacter
{
    public string Name { get; set; } = "";
    public string Description { get; set; } = "";
    public string Role { get; set; } = "";
}

/// <summary>One chapter's planned title + summary, generated up front by BookOutlineGenerator
/// before any chapter's actual prose is written -- BookChapterGenerator later expands each of
/// these into full chapter text, one at a time.</summary>
public sealed class ChapterOutline
{
    public int Number { get; set; }
    public string Title { get; set; } = "";
    public string Summary { get; set; } = "";
}

/// <summary>
/// The planned shape of an entire book, before any chapter's actual prose exists yet --
/// BookOutlineGenerator's own output, and the fixed context every later BookChapterGenerator
/// call reads from. Characters/Setting/PlotArc are populated only when
/// <see cref="BookGenreRules.UsesStoryBible"/> is true for the genre (Fiction and
/// FictionWithScienceAppendix; BookOutlineGenerator leaves them empty for NonFiction, since
/// there is nothing there to invent) -- this is the "book bible" every chapter's own generation
/// call is grounded against, so a character introduced in chapter 2 doesn't get a different
/// backstory in chapter 7's own, separately-generated text.
/// </summary>
public sealed class BookOutline
{
    public string Title { get; set; } = "";
    public BookGenre Genre { get; set; }
    public string Premise { get; set; } = "";
    public List<ChapterOutline> Chapters { get; } = new();

    /// <summary>Story-bible genres only (Fiction / FictionWithScienceAppendix) -- empty for NonFiction.</summary>
    public List<BookCharacter> Characters { get; } = new();

    /// <summary>Story-bible genres only -- where/when the story takes place. Empty for NonFiction.</summary>
    public string Setting { get; set; } = "";

    /// <summary>Story-bible genres only -- the overall story arc/structure (e.g. a 3-act summary) every
    /// chapter's own generation is meant to serve. Empty for NonFiction.</summary>
    public string PlotArc { get; set; } = "";
}

/// <summary>
/// A fully (or partially) generated book -- Outline is fixed once BookOutlineGenerator runs;
/// ChapterContents fills in one entry at a time as BookChapterGenerator writes each chapter,
/// in the same order as Outline.Chapters (ChapterContents[i] is the prose for
/// Outline.Chapters[i]). CoverImagePath is set once a cover generator (built separately) has
/// produced one.
/// </summary>
public sealed class Book
{
    public BookOutline Outline { get; }
    public List<string> ChapterContents { get; } = new();
    public string? CoverImagePath { get; set; }

    public Book(BookOutline outline) => Outline = outline;
}
