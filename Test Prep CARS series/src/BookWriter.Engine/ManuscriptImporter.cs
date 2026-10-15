using System.Text;
using System.Text.RegularExpressions;
using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;

namespace BookWriter.Engine;

/// <summary>
/// Reads an existing manuscript off disk into the same <see cref="Book"/> shape the Write flow
/// produces, so the Edit workspace, the cover generator and all three exporters can act on a
/// book this app never wrote. Supports plain text (<c>.txt</c>), Markdown (<c>.md</c> /
/// <c>.markdown</c>) and Word (<c>.docx</c>).
///
/// The whole job is splitting one long document into chapters. The detector looks, in order,
/// for: Markdown ATX headings (<c># ...</c>), "Chapter N" / "Part N" / stand-alone
/// Prologue/Epilogue/Introduction lines, numbered headings (<c>1. ...</c>), and Markdown
/// setext <c>===</c> underlines; for <c>.docx</c> it also treats any paragraph in a built-in
/// Title/Heading style as a break. If it finds none of those, it falls back to "a short
/// ALL-CAPS line fenced by blank lines", and if that finds nothing either, the whole file
/// becomes a single chapter rather than failing -- a one-chapter import the author can still
/// edit and re-export beats a hard error.
///
/// Nothing in the source text is dropped: any front matter before the first detected chapter
/// heading is folded into the first chapter, and an unrecognised structure just yields fewer,
/// longer chapters. A <c>.docx</c> body paragraph's bold/italic runs and external hyperlinks
/// survive import too -- re-encoded as the same <c>**bold**</c>/<c>_italic_</c>/<c>[label](url)</c>
/// Markdown the <see cref="EditPass.Hyperlinks"/> pass and a <c>.md</c> import already produce, so
/// every exporter renders it identically via <see cref="InlineMarkup"/>. What does NOT survive:
/// formatting that comes from a character/paragraph style rather than a direct bold/italic toggle
/// on the run, and a hyperlink whose target has no clean Markdown encoding (contains whitespace or
/// a literal ')') -- both fall back to plain (never dropped) text, an honest, documented
/// limitation rather than silent corruption.
///
/// <see cref="Import"/> never throws for an ordinary problem (missing file, unreadable
/// document, unsupported extension, a file with no text in it) -- it returns
/// <c>(null, reason)</c> instead.
/// </summary>
public static partial class ManuscriptImporter
{
    public static IReadOnlyList<string> SupportedExtensions { get; } =
        new[] { ".txt", ".md", ".markdown", ".docx" };

    /// <summary>Open-file-dialog filter string covering exactly <see cref="SupportedExtensions"/>.</summary>
    public const string OpenFileDialogFilter =
        "Manuscripts (*.txt;*.md;*.markdown;*.docx)|*.txt;*.md;*.markdown;*.docx|" +
        "Text and Markdown (*.txt;*.md;*.markdown)|*.txt;*.md;*.markdown|" +
        "Word document (*.docx)|*.docx|All files (*.*)|*.*";

    [GeneratedRegex(@"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")]
    private static partial Regex AtxHeading();

    [GeneratedRegex(@"^\s*(chapter|part|book)\s+([0-9]+|[ivxlcdm]+|[a-z]+)\b\s*[:.–\-]?\s*(.*)$", RegexOptions.IgnoreCase)]
    private static partial Regex ChapterWord();

    [GeneratedRegex(@"^\s*(prologue|epilogue|introduction|foreword|preface|afterword|acknowledgements?|appendix)\b\s*[:.–\-]?\s*(.*)$", RegexOptions.IgnoreCase)]
    private static partial Regex StandaloneSection();

    [GeneratedRegex(@"^\s*(\d{1,3})[.)]\s+(\S.*)$")]
    private static partial Regex NumberedHeading();

    [GeneratedRegex(@"^[A-Z0-9][A-Z0-9 '""!?:;,.()–\-]{2,59}$")]
    private static partial Regex AllCapsLine();

    /// <summary>Upper bound on a "Chapter N"/"Prologue"/"Appendix"/numbered-style heading line,
    /// used together with <see cref="PrecededByBlank"/> in <see cref="IsStrongHeading"/> to tell
    /// a real (if verbose) title from an ordinary paragraph that merely opens with one of the
    /// same words. Generous on purpose: real non-fiction and science-appendix chapter titles
    /// ("Appendix: The Impossible Origami Trick of Folding 2 Meters of DNA Into a Microscopic
    /// Nucleus") regularly run past 90 characters.</summary>
    private const int MaxNaturalHeadingLength = 140;

    /// <summary>Parses the manuscript at <paramref name="path"/> into a <see cref="Book"/> of
    /// the given <paramref name="genre"/> (the file itself carries no genre, so the caller --
    /// the Edit UI -- supplies it). Returns <c>(null, reason)</c> on any ordinary failure.</summary>
    public static (Book? Book, string Error) Import(string path, BookGenre genre)
    {
        if (string.IsNullOrWhiteSpace(path))
            return (null, "No file was supplied.");
        if (!File.Exists(path))
            return (null, $"File not found: \"{path}\".");

        string extension = Path.GetExtension(path).ToLowerInvariant();
        if (!SupportedExtensions.Contains(extension))
            return (null, $"Unsupported file type \"{extension}\". Book Writer can import {string.Join(", ", SupportedExtensions)}.");

        string fallbackTitle = Path.GetFileNameWithoutExtension(path).Trim();

        try
        {
            (string? titleFromDoc, List<string> lines, string readError) = extension == ".docx"
                ? ReadDocxLines(path)
                : ReadPlainLines(path);

            if (readError.Length > 0)
                return (null, readError);
            if (lines.Count == 0 || lines.All(string.IsNullOrWhiteSpace))
                return (null, "That file has no readable text in it.");

            (string detectedTitle, List<RawChapter> rawChapters) = SplitIntoChapters(lines, titleFromDoc);
            string title = FirstNonEmpty(detectedTitle, titleFromDoc, fallbackTitle, "Imported Manuscript");

            if (rawChapters.Count == 0)
                return (null, "That file has no readable text in it.");

            var outline = new BookOutline { Title = title, Genre = genre, Premise = "" };
            var book = new Book(outline);

            for (int i = 0; i < rawChapters.Count; i++)
            {
                RawChapter raw = rawChapters[i];
                string chapterTitle = string.IsNullOrWhiteSpace(raw.Title) ? $"Chapter {i + 1}" : raw.Title.Trim();
                outline.Chapters.Add(new ChapterOutline { Number = i + 1, Title = chapterTitle, Summary = "" });
                book.ChapterContents.Add(raw.Body.ToString().Trim());
            }

            AppLog.Info("ManuscriptImporter: imported \"{Path}\" as {Chapters} chapter(s), title \"{Title}\".",
                path, book.ChapterContents.Count, title);
            return (book, "");
        }
        catch (Exception ex)
        {
            AppLog.Warning("ManuscriptImporter: failed to import \"{Path}\" - {Error}", path, ex.Message);
            return (null, $"Could not read that file: {ex.Message}");
        }
    }

    // ==================== Readers ====================

    private static (string? Title, List<string> Lines, string Error) ReadPlainLines(string path)
    {
        string text = File.ReadAllText(path);
        string normalized = text.Replace("\r\n", "\n").Replace('\r', '\n');
        return (null, normalized.Split('\n').ToList(), "");
    }

    /// <summary>Flattens a .docx body to lines the shared splitter can work on: one line per
    /// Word paragraph, with a marker prefix on any paragraph carrying a built-in Title/Heading
    /// style so <see cref="SplitIntoChapters"/> treats it as a break even when its text has no
    /// "Chapter N" wording. Returns the text of the first Title-styled paragraph as the book
    /// title when there is one.
    ///
    /// Title/Heading paragraphs are read as plain text -- <see cref="BookOutline.Title"/> and
    /// <see cref="ChapterOutline.Title"/> are plain strings nothing ever re-parses as Markdown,
    /// so encoding bold/italic markers into one would leak literal "**" into a book or chapter
    /// title. Every other (body) paragraph goes through <see cref="ExtractFormattedParagraphText"/>
    /// instead, which preserves bold/italic runs and external hyperlinks by re-encoding them in
    /// the same Markdown convention <see cref="InlineMarkup"/> already parses at every export
    /// path, rather than flattening them to plain text.</summary>
    private static (string? Title, List<string> Lines, string Error) ReadDocxLines(string path)
    {
        using WordprocessingDocument doc = WordprocessingDocument.Open(path, false);
        Body? body = doc.MainDocumentPart?.Document?.Body;
        if (body is null)
            return (null, new List<string>(), "That .docx file has no document body.");

        var lines = new List<string>();
        string? title = null;

        foreach (Paragraph paragraph in body.Descendants<Paragraph>())
        {
            string? styleId = paragraph.ParagraphProperties?.ParagraphStyleId?.Val?.Value;
            bool isTitleStyle = string.Equals(styleId, "Title", StringComparison.OrdinalIgnoreCase);
            bool isHeadingStyle = styleId is not null && styleId.StartsWith("Heading", StringComparison.OrdinalIgnoreCase);

            if (isTitleStyle)
            {
                string plainText = paragraph.InnerText.Replace('\t', ' ').Trim();
                if (title is null && plainText.Length > 0) title = plainText;
                continue; // the title line is not itself a chapter and not body text
            }

            if (isHeadingStyle)
            {
                string plainText = paragraph.InnerText.Replace('\t', ' ').Trim();
                if (plainText.Length > 0) lines.Add(HeadingMarker + plainText);
                continue;
            }

            lines.Add(ExtractFormattedParagraphText(paragraph, doc)); // may be "" -- a blank line, which is a paragraph boundary
        }

        return (title, lines, "");
    }

    /// <summary>Prefix ReadDocxLines stamps on a Heading-styled paragraph so the shared line
    /// splitter recognises it as a break. A control-char prefix that cannot occur in real
    /// document text.</summary>
    private const string HeadingMarker = "\u0001";

    // ==================== Formatting-preserving body-paragraph extraction ====================

    /// <summary>One run of a body paragraph after Word's own arbitrary run-splitting has been
    /// collapsed away (see <see cref="CoalesceRunSegments"/>): a stretch of text that is entirely
    /// plain, entirely bold/italic, and/or entirely one external hyperlink.</summary>
    private readonly record struct DocxRunSegment(string Text, bool Bold, bool Italic, string? LinkUrl);

    /// <summary>Renders one body paragraph's runs to a single line, re-encoding bold/italic runs
    /// (and external hyperlinks) as <c>**bold**</c> / <c>_italic_</c> / <c>[label](url)</c> --
    /// see the class-level doc comment on <see cref="ReadDocxLines"/> for why only body
    /// paragraphs get this treatment. Italic deliberately renders with <c>_..._</c> rather than
    /// <c>*...*</c>: it is the same valid syntax as far as <see cref="InlineMarkup"/> is
    /// concerned, but keeping bold's <c>*</c> and italic's <c>_</c> visually distinct means a
    /// bold run sitting directly against an italic run (no space between them, which real .docx
    /// files do produce) never leaves three-plus <c>*</c> characters in a row for the parser to
    /// puzzle over.</summary>
    private static string ExtractFormattedParagraphText(Paragraph paragraph, WordprocessingDocument doc)
    {
        var segments = new List<DocxRunSegment>();
        CollectRunSegments(paragraph, doc, linkUrl: null, segments);
        segments = CoalesceRunSegments(segments);

        var sb = new StringBuilder();
        foreach (DocxRunSegment segment in segments)
            sb.Append(RenderSegment(segment));

        return sb.ToString().Trim();
    }

    /// <summary>Walks a paragraph's children looking for <see cref="Run"/>s (each contributing
    /// one segment) and <see cref="Hyperlink"/>s (recursed into with their resolved external URL
    /// attached to every segment found inside). Anything else that carries child content --
    /// tracked-change wrappers, content controls, smart tags -- is recursed into generically too,
    /// so a Run buried inside one of those still contributes its text rather than silently
    /// vanishing (this importer's whole design promises nothing in the source text is dropped).
    /// Structural, non-text children (bookmarks, proofing-error markers, paragraph properties)
    /// are skipped.</summary>
    private static void CollectRunSegments(OpenXmlElement container, WordprocessingDocument doc, string? linkUrl, List<DocxRunSegment> segments)
    {
        foreach (OpenXmlElement child in container.ChildElements)
        {
            switch (child)
            {
                case Run run:
                    string text = ExtractRunText(run);
                    if (text.Length > 0)
                    {
                        bool bold = IsOn(run.RunProperties?.Bold);
                        bool italic = IsOn(run.RunProperties?.Italic);
                        segments.Add(new DocxRunSegment(text, bold, italic, linkUrl));
                    }
                    break;

                case Hyperlink hyperlink:
                    string? url = ResolveExternalHyperlinkUrl(hyperlink, doc);
                    CollectRunSegments(hyperlink, doc, url ?? linkUrl, segments);
                    break;

                case ParagraphProperties:
                case BookmarkStart:
                case BookmarkEnd:
                case ProofError:
                case CommentRangeStart:
                case CommentRangeEnd:
                    break; // no visible text

                default:
                    if (child.HasChildren)
                        CollectRunSegments(child, doc, linkUrl, segments);
                    break;
            }
        }
    }

    /// <summary>A run's own visible text, flattened to a single line: literal text plus tabs and
    /// line/page breaks each normalised to one space, matching the single-line-per-Word-paragraph
    /// shape the rest of this importer expects.</summary>
    private static string ExtractRunText(Run run)
    {
        var sb = new StringBuilder();
        foreach (OpenXmlElement child in run.ChildElements)
        {
            switch (child)
            {
                case Text t: sb.Append(t.Text); break;
                case TabChar: sb.Append(' '); break;
                case Break: sb.Append(' '); break;
                case CarriageReturn: sb.Append(' '); break;
            }
        }
        return sb.ToString();
    }

    /// <summary>An OOXML on/off toggle (<c>&lt;w:b/&gt;</c>, <c>&lt;w:i/&gt;</c>, ...) is "on" when
    /// present with no <c>w:val</c> at all, or an explicit true-ish <c>w:val</c> -- and "off" only
    /// when <c>w:val</c> is explicitly false/0. Absence of the element itself (not passed here --
    /// callers pass <c>run.RunProperties?.Bold</c>, which is null when there's no such element)
    /// means off.</summary>
    private static bool IsOn(OnOffType? toggle) => toggle is not null && (toggle.Val is null || toggle.Val.Value);

    /// <summary>The absolute URL a hyperlink run points to, or null when it isn't an external
    /// link this importer can carry forward (an internal bookmark/cross-reference via
    /// <c>w:anchor</c>, or a relationship id that doesn't resolve) -- in which case the run's
    /// text still comes through via <see cref="CollectRunSegments"/>, just without a link
    /// wrapped around it, the same "keep the words, drop only what can't be represented"
    /// degrade this whole importer uses elsewhere.</summary>
    private static string? ResolveExternalHyperlinkUrl(Hyperlink hyperlink, WordprocessingDocument doc)
    {
        string? id = hyperlink.Id?.Value;
        if (id is null) return null;

        HyperlinkRelationship? rel = doc.MainDocumentPart?.HyperlinkRelationships.FirstOrDefault(r => r.Id == id);
        return rel is { IsExternal: true } ? rel.Uri.AbsoluteUri : null;
    }

    /// <summary>Merges adjacent segments with identical styling/link -- real .docx files
    /// routinely split one visually-uniform bold sentence into several runs (spell-check,
    /// autocorrect and revision history all do this), and without merging first, each run would
    /// get its own marker pair (<c>**Hello** **world**</c> instead of <c>**Hello world**</c>).
    /// Harmless either way once re-parsed, but noisier to read if a user opens the raw chapter
    /// text before export.</summary>
    private static List<DocxRunSegment> CoalesceRunSegments(List<DocxRunSegment> segments)
    {
        var merged = new List<DocxRunSegment>(segments.Count);
        foreach (DocxRunSegment segment in segments)
        {
            if (segment.Text.Length == 0) continue;
            if (merged.Count > 0)
            {
                DocxRunSegment prev = merged[^1];
                if (prev.Bold == segment.Bold && prev.Italic == segment.Italic && prev.LinkUrl == segment.LinkUrl)
                {
                    merged[^1] = prev with { Text = prev.Text + segment.Text };
                    continue;
                }
            }
            merged.Add(segment);
        }
        return merged;
    }

    /// <summary>Encodes one coalesced segment as Markdown. Leading/trailing whitespace is moved
    /// outside the <c>**</c>/<c>_</c> markers (<see cref="InlineMarkup"/>'s emphasis patterns
    /// require a non-whitespace character on the inside of each marker, so "**hello **" would not
    /// parse as bold at all) but left inside a <c>[label](url)</c> link, which has no such
    /// requirement.</summary>
    private static string RenderSegment(DocxRunSegment segment)
    {
        string trimmedStart = segment.Text.TrimStart();
        string leading = segment.Text[..(segment.Text.Length - trimmedStart.Length)];
        string core = trimmedStart.TrimEnd();
        string trailing = trimmedStart[core.Length..];

        if (core.Length == 0) return segment.Text; // whitespace-only run -- nothing to mark up

        string emphasized = ApplyEmphasisMarkers(core, segment.Bold, segment.Italic);

        return segment.LinkUrl is not null && IsSafeLinkTarget(segment.LinkUrl)
            ? leading + "[" + emphasized + "](" + segment.LinkUrl + ")" + trailing
            : leading + emphasized + trailing;
    }

    private static string ApplyEmphasisMarkers(string core, bool bold, bool italic) =>
        (bold, italic) switch
        {
            (true, true) => "**_" + core + "_**",
            (true, false) => "**" + core + "**",
            (false, true) => "_" + core + "_",
            _ => core,
        };

    /// <summary>True when <paramref name="url"/> can round-trip through <c>[label](url)</c>:
    /// <see cref="InlineMarkup"/>'s link target cannot contain whitespace or ')' (both end the
    /// <c>(...)</c> early), which a real-world URL only very rarely does. Rather than emit a link
    /// that would parse back out truncated, an unsafe target is dropped and the run falls back to
    /// plain (still bold/italic, just unlinked) text -- the label itself is never lost.</summary>
    private static bool IsSafeLinkTarget(string url) => url.Length > 0 && !url.Any(char.IsWhiteSpace) && !url.Contains(')');

    // ==================== Chapter splitting ====================

    private sealed class RawChapter
    {
        public string Title = "";
        public readonly StringBuilder Body = new();
    }

    private static (string Title, List<RawChapter> Chapters) SplitIntoChapters(List<string> lines, string? knownTitle)
    {
        // Pass 1: structural headings (Markdown, "Chapter N", numbered, docx Heading style, setext ===).
        var chapters = SplitOnHeadings(lines, out string atxTitle, requireStrong: true);
        if (chapters.Count >= 2 || (chapters.Count == 1 && HasAnyStrongHeading(lines)))
            return (atxTitle, chapters);

        // Pass 2: nothing structural -- try "short ALL-CAPS line fenced by blanks".
        var capsChapters = SplitOnAllCapsLines(lines);
        if (capsChapters.Count >= 2)
            return (atxTitle, capsChapters);

        // Pass 3: give up splitting -- the whole document is one chapter.
        var single = new RawChapter { Title = FirstNonEmpty(atxTitle, knownTitle ?? "", "Chapter 1") };
        foreach (string line in lines) single.Body.Append(line).Append('\n');
        return (atxTitle, new List<RawChapter> { single });
    }

    private static bool HasAnyStrongHeading(List<string> lines)
    {
        for (int i = 0; i < lines.Count; i++)
        {
            if (IsStrongHeading(lines, i, out _, out _)) return true;
        }
        return false;
    }

    private static List<RawChapter> SplitOnHeadings(List<string> lines, out string bookTitle, bool requireStrong)
    {
        bookTitle = "";
        var chapters = new List<RawChapter>();
        RawChapter? current = null;
        var frontMatter = new StringBuilder(); // content before the first heading, if any

        for (int i = 0; i < lines.Count; i++)
        {
            string line = lines[i];

            // A top-level "# Title" before the first chapter names the book, not a chapter.
            Match atx = AtxHeading().Match(line);
            if (atx.Success && atx.Groups[1].Value.Length == 1 && chapters.Count == 0 && current is null && bookTitle.Length == 0)
            {
                bookTitle = atx.Groups[2].Value.Trim();
                continue;
            }

            if (IsStrongHeading(lines, i, out string headingTitle, out int consumedNextLine))
            {
                current = new RawChapter { Title = headingTitle };
                if (chapters.Count == 0) AbsorbFrontMatter(frontMatter, current, ref bookTitle);
                chapters.Add(current);
                if (consumedNextLine > 0) i += consumedNextLine; // skip a setext underline
                continue;
            }

            if (current is null)
            {
                // Pre-first-heading content -- buffered, then folded into chapter 1 (or, when
                // it is a single short line and no title is known yet, taken as the title)
                // rather than becoming a phantom untitled chapter that shifts every real
                // chapter's number by one.
                if (frontMatter.Length == 0 && line.Trim().Length == 0) continue;
                frontMatter.Append(StripHeadingMarker(line)).Append('\n');
                continue;
            }

            current.Body.Append(StripHeadingMarker(line)).Append('\n');
        }

        return chapters;
    }

    /// <summary>Folds any buffered pre-first-heading text into the first chapter's body -- or,
    /// when it is a single line of at most 80 characters and the book has no title yet, adopts
    /// it as the title instead.</summary>
    private static void AbsorbFrontMatter(StringBuilder frontMatter, RawChapter firstChapter, ref string bookTitle)
    {
        if (frontMatter.Length == 0) return;

        string text = frontMatter.ToString().Trim();
        string[] nonEmpty = text.Split('\n', StringSplitOptions.RemoveEmptyEntries);

        if (bookTitle.Length == 0 && nonEmpty.Length == 1 && nonEmpty[0].Trim().Length is > 0 and <= 80)
        {
            bookTitle = nonEmpty[0].Trim();
            return;
        }

        firstChapter.Body.Append(text).Append("\n\n");
    }

    private static bool IsStrongHeading(List<string> lines, int index, out string title, out int consumedNextLine)
    {
        title = "";
        consumedNextLine = 0;
        string line = lines[index];

        if (line.StartsWith(HeadingMarker, StringComparison.Ordinal))
        {
            title = line[HeadingMarker.Length..].Trim();
            return true;
        }

        Match atx = AtxHeading().Match(line);
        if (atx.Success)
        {
            // "# " alone (a single hash) at the very top is the book title, handled by the caller;
            // here, any ATX heading that is not that first h1 is a chapter break.
            title = atx.Groups[2].Value.Trim();
            return true;
        }

        Match chapterWord = ChapterWord().Match(line);
        if (chapterWord.Success && line.Trim().Length <= MaxNaturalHeadingLength && PrecededByBlank(lines, index) && !EndsLikeASentence(line))
        {
            string trailing = chapterWord.Groups[3].Value.Trim();
            title = trailing.Length > 0
                ? $"{Capitalize(chapterWord.Groups[1].Value)} {chapterWord.Groups[2].Value}: {trailing}"
                : $"{Capitalize(chapterWord.Groups[1].Value)} {chapterWord.Groups[2].Value}";
            return true;
        }

        // Real non-fiction/appendix titles run long -- e.g. a science-appendix chapter's own
        // "Appendix: <topic>" title (BookGenreRules/BookOutlineGenerator impose no length limit
        // when generating one) can comfortably run past 90 characters. MaxNaturalHeadingLength
        // is calibrated to that, not to the older, stricter 60-character cap this used to have,
        // which silently dropped exactly this kind of long appendix heading during re-import.
        Match standalone = StandaloneSection().Match(line);
        if (standalone.Success && line.Trim().Length <= MaxNaturalHeadingLength && PrecededByBlank(lines, index) && !EndsLikeASentence(line))
        {
            string trailing = standalone.Groups[2].Value.Trim();
            title = trailing.Length > 0 ? $"{Capitalize(standalone.Groups[1].Value)}: {trailing}" : Capitalize(standalone.Groups[1].Value);
            return true;
        }

        Match numbered = NumberedHeading().Match(line);
        if (numbered.Success && line.Trim().Length <= MaxNaturalHeadingLength && PrecededByBlank(lines, index) && !EndsLikeASentence(line))
        {
            title = $"{numbered.Groups[1].Value}. {numbered.Groups[2].Value.Trim()}";
            return true;
        }

        // Setext: this line has text, the next is all '=' (h1). '-' underlines are ignored
        // because they collide with '---' rules and YAML front-matter fences.
        if (line.Trim().Length > 0 && index + 1 < lines.Count && Regex.IsMatch(lines[index + 1], @"^\s*={3,}\s*$"))
        {
            title = line.Trim();
            consumedNextLine = 1;
            return true;
        }

        return false;
    }

    private static List<RawChapter> SplitOnAllCapsLines(List<string> lines)
    {
        var chapters = new List<RawChapter>();
        RawChapter? current = null;

        for (int i = 0; i < lines.Count; i++)
        {
            string trimmed = lines[i].Trim();
            bool isBreak = trimmed.Length > 0
                && AllCapsLine().IsMatch(trimmed)
                && trimmed.Any(char.IsLetter)
                && PrecededByBlank(lines, i)
                && FollowedByBlank(lines, i);

            if (isBreak)
            {
                current = new RawChapter { Title = Capitalize(trimmed.ToLowerInvariant()) };
                chapters.Add(current);
                continue;
            }

            if (current is null)
            {
                if (trimmed.Length == 0) continue;
                current = new RawChapter { Title = "" };
                chapters.Add(current);
            }
            current.Body.Append(lines[i]).Append('\n');
        }

        return chapters;
    }

    // ==================== Helpers ====================

    /// <summary>True when the line immediately before <paramref name="index"/> is blank, or
    /// <paramref name="index"/> is the first line -- the "this heading stands on its own, not
    /// mid-paragraph" check.</summary>
    private static bool PrecededByBlank(List<string> lines, int index) =>
        index - 1 < 0 || lines[index - 1].Trim().Length == 0;

    /// <summary>True when the line immediately after <paramref name="index"/> is blank, or
    /// <paramref name="index"/> is the last line.</summary>
    private static bool FollowedByBlank(List<string> lines, int index) =>
        index + 1 >= lines.Count || lines[index + 1].Trim().Length == 0;

    /// <summary>True when a line ends with a sentence-terminal period -- the cheap, effective
    /// signal that distinguishes an ordinary prose sentence from a title, used alongside the
    /// length cap and <see cref="PrecededByBlank"/> in <see cref="IsStrongHeading"/>. Without
    /// it, a body paragraph that simply opens with one of the same keywords (e.g. an appendix's
    /// own first sentence, "Appendix body text goes here.", right after the real "Appendix"
    /// heading) would itself be misread as a second heading. A title ending in '?' or '!' is
    /// deliberately still allowed through -- only a plain terminal '.' is treated as "this reads
    /// like a finished sentence, not a title".</summary>
    private static bool EndsLikeASentence(string line) => line.TrimEnd().EndsWith('.');

    private static string StripHeadingMarker(string line) =>
        line.StartsWith(HeadingMarker, StringComparison.Ordinal) ? line[HeadingMarker.Length..] : line;

    private static string Capitalize(string word) =>
        word.Length == 0 ? word : char.ToUpperInvariant(word[0]) + word[1..];

    private static string FirstNonEmpty(params string?[] candidates) =>
        candidates.FirstOrDefault(c => !string.IsNullOrWhiteSpace(c))?.Trim() ?? "";
}
