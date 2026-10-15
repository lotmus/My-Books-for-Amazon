using System.Text.RegularExpressions;

namespace BookWriter.Engine;

/// <summary>What a single <see cref="InlineRun"/> links to (if anything).</summary>
public enum InlineLinkKind
{
    /// <summary>Plain text -- no link.</summary>
    None,

    /// <summary>An external URL. <see cref="InlineRun.LinkTarget"/> is the full <c>http(s)://</c> address.</summary>
    External,

    /// <summary>A cross-reference to another chapter of this same book.
    /// <see cref="InlineRun.LinkTarget"/> is that chapter's number as a string.</summary>
    InternalChapter,
}

/// <summary>One styled span of a paragraph: a stretch of text that is entirely plain, entirely
/// one link, and/or entirely bold/italic. <see cref="InlineMarkup.Parse"/> turns a raw
/// paragraph string into an ordered list of these, which every exporter then renders in its own
/// format (an EPUB <c>&lt;a&gt;</c>/<c>&lt;strong&gt;</c>, a Word hyperlink run, a QuestPDF
/// span).</summary>
public readonly record struct InlineRun(string Text, bool Bold, bool Italic, InlineLinkKind LinkKind, string LinkTarget)
{
    public static InlineRun Plain(string text) => new(text, false, false, InlineLinkKind.None, "");

    public bool IsLink => LinkKind != InlineLinkKind.None;
}

/// <summary>
/// The single place that understands the small slice of Markdown Book Writer's chapter text can
/// carry: links (<c>[label](https://example.com)</c> for an external source, and
/// <c>[label](chapter:N)</c> for a cross-reference to chapter N of this same book -- a private
/// convention this app resolves at export time), plus <c>**bold**</c> and <c>*italic*</c> /
/// <c>_italic_</c> emphasis.
///
/// It exists because two of the app's flows now put Markdown into chapter text -- the
/// <see cref="EditPass.Hyperlinks"/> edit pass adds links, and <see cref="ManuscriptImporter"/>
/// can import a real <c>.md</c> manuscript -- and all three exporters
/// (<see cref="BookEpubExporter"/>, <see cref="BookDocumentExporter"/>'s Word and PDF paths)
/// need to render that identically rather than each re-parsing it slightly differently or
/// leaking raw <c>[..](..)</c> into the finished book.
///
/// Anything it does not recognise (an unmatched bracket, a bare URL, a link whose target is
/// neither <c>http(s)://</c> nor <c>chapter:N</c>, a stray <c>*</c>) is passed through as
/// literal text rather than dropped -- a book must never lose an author's actual words to a
/// parser being strict. Parsing is deliberately non-nested and single-pass: <c>**_x_**</c>
/// renders as bold text with literal underscores, which is a fine, rare degradation and far
/// simpler to keep correct than a full Markdown inline grammar.
/// </summary>
public static partial class InlineMarkup
{
    // [label](target) -- label has no ']' or newline; target has no whitespace or ')'.
    [GeneratedRegex(@"\[([^\]\r\n]+?)\]\(\s*([^)\s]+?)\s*\)", RegexOptions.Compiled)]
    private static partial Regex LinkPattern();

    [GeneratedRegex(@"\*\*(?=\S)(.+?)(?<=\S)\*\*", RegexOptions.Compiled)]
    private static partial Regex BoldPattern();

    // A single '*' or '_' pair, not touching another marker of the same kind. '_' only counts
    // when it is on a word boundary, so snake_case identifiers and file_names survive intact.
    [GeneratedRegex(@"(?<!\*)\*(?=\S)([^*\r\n]+?)(?<=\S)\*(?!\*)|(?<![\w_])_(?=\S)([^_\r\n]+?)(?<=\S)_(?![\w_])", RegexOptions.Compiled)]
    private static partial Regex ItalicPattern();

    /// <summary>Turns one raw paragraph into ordered styled runs. Never returns null; an
    /// empty/whitespace paragraph comes back as a single plain run with that exact text so the
    /// caller's paragraph count and spacing are unchanged.</summary>
    public static List<InlineRun> Parse(string? paragraph)
    {
        string text = paragraph ?? "";
        var runs = new List<InlineRun>();
        if (text.Length == 0)
        {
            runs.Add(InlineRun.Plain(""));
            return runs;
        }

        int cursor = 0;
        foreach (Match link in LinkPattern().Matches(text))
        {
            if (link.Index > cursor)
                AddStyledText(runs, text[cursor..link.Index]);

            string label = link.Groups[1].Value;
            string target = link.Groups[2].Value;
            (InlineLinkKind kind, string resolvedTarget) = ClassifyTarget(target);

            if (kind == InlineLinkKind.None)
            {
                // Not a link shape we understand -- keep the author's literal characters.
                AddStyledText(runs, link.Value);
            }
            else
            {
                foreach (InlineRun styled in ParseEmphasis(label))
                    runs.Add(styled with { LinkKind = kind, LinkTarget = resolvedTarget });
            }

            cursor = link.Index + link.Length;
        }

        if (cursor < text.Length)
            AddStyledText(runs, text[cursor..]);

        if (runs.Count == 0)
            runs.Add(InlineRun.Plain(text));

        return Coalesce(runs);
    }

    /// <summary>True when <paramref name="paragraph"/> contains at least one link this parser
    /// would resolve -- lets an exporter skip all per-run machinery for the common case of a
    /// paragraph with no links at all (emphasis alone still goes through the normal path).</summary>
    public static bool HasResolvableLink(string? paragraph)
    {
        if (string.IsNullOrEmpty(paragraph)) return false;
        foreach (Match link in LinkPattern().Matches(paragraph))
        {
            if (ClassifyTarget(link.Groups[2].Value).Kind != InlineLinkKind.None)
                return true;
        }
        return false;
    }

    /// <summary>Flattens every run of a paragraph back to plain text with the link/emphasis
    /// markup removed -- used where a format genuinely cannot carry a link (e.g. a nav-label or
    /// a cover prompt) so it shows "the term" rather than "[the term](chapter:3)".</summary>
    public static string ToPlainText(string? paragraph)
    {
        var sb = new System.Text.StringBuilder();
        foreach (InlineRun run in Parse(paragraph))
            sb.Append(run.Text);
        return sb.ToString();
    }

    private static (InlineLinkKind Kind, string Target) ClassifyTarget(string rawTarget)
    {
        string target = rawTarget.Trim();

        if (target.StartsWith("chapter:", StringComparison.OrdinalIgnoreCase))
        {
            string number = target["chapter:".Length..].Trim();
            return int.TryParse(number, out int n) && n > 0
                ? (InlineLinkKind.InternalChapter, n.ToString())
                : (InlineLinkKind.None, "");
        }

        if ((target.StartsWith("http://", StringComparison.OrdinalIgnoreCase) ||
             target.StartsWith("https://", StringComparison.OrdinalIgnoreCase)) &&
            Uri.TryCreate(target, UriKind.Absolute, out _))
        {
            return (InlineLinkKind.External, target);
        }

        return (InlineLinkKind.None, "");
    }

    private static void AddStyledText(List<InlineRun> runs, string segment)
    {
        if (segment.Length == 0) return;
        runs.AddRange(ParseEmphasis(segment));
    }

    /// <summary>One non-nested pass of <c>**bold**</c> then <c>*italic*</c>/<c>_italic_</c> over
    /// a plain (already link-free) string. Bold is resolved first; the italic pass then runs
    /// over EVERY resulting span, bold ones included -- so <c>**_text_**</c> (bold wrapping an
    /// italic inner span) comes back as one run with both Bold and Italic set, not "bold text
    /// with literal underscores" the way a bold-excludes-italic pass would leave it. A marker
    /// that isn't nested this specific way (e.g. italic wrapping bold, or three-plus nesting
    /// levels) is still left literal -- this remains a deliberately non-nested, single-pass
    /// parser (see this class's own top doc comment), just one step less naive than
    /// bold-or-italic-but-never-both.</summary>
    private static IEnumerable<InlineRun> ParseEmphasis(string segment)
    {
        var afterBold = new List<InlineRun>();
        int cursor = 0;
        foreach (Match m in BoldPattern().Matches(segment))
        {
            if (m.Index > cursor)
                afterBold.Add(InlineRun.Plain(segment[cursor..m.Index]));
            afterBold.Add(new InlineRun(m.Groups[1].Value, true, false, InlineLinkKind.None, ""));
            cursor = m.Index + m.Length;
        }
        if (cursor < segment.Length)
            afterBold.Add(InlineRun.Plain(segment[cursor..]));

        foreach (InlineRun run in afterBold)
        {
            if (run.Text.Length == 0) continue;

            int innerCursor = 0;
            foreach (Match m in ItalicPattern().Matches(run.Text))
            {
                if (m.Index > innerCursor)
                    yield return run with { Text = run.Text[innerCursor..m.Index] };
                string inner = m.Groups[1].Success ? m.Groups[1].Value : m.Groups[2].Value;
                yield return run with { Text = inner, Italic = true };
                innerCursor = m.Index + m.Length;
            }
            if (innerCursor < run.Text.Length)
                yield return run with { Text = run.Text[innerCursor..] };
        }
    }

    /// <summary>Merges adjacent runs that carry identical styling/linking so an exporter emits
    /// one <c>&lt;a&gt;</c>/hyperlink/span instead of several touching ones.</summary>
    private static List<InlineRun> Coalesce(List<InlineRun> runs)
    {
        var merged = new List<InlineRun>(runs.Count);
        foreach (InlineRun run in runs)
        {
            if (run.Text.Length == 0) continue;
            if (merged.Count > 0)
            {
                InlineRun prev = merged[^1];
                if (prev.Bold == run.Bold && prev.Italic == run.Italic &&
                    prev.LinkKind == run.LinkKind && prev.LinkTarget == run.LinkTarget)
                {
                    merged[^1] = prev with { Text = prev.Text + run.Text };
                    continue;
                }
            }
            merged.Add(run);
        }
        if (merged.Count == 0)
            merged.Add(InlineRun.Plain(""));
        return merged;
    }
}
