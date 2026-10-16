using System.Text;
using DocumentFormat.OpenXml.Packaging;
using UglyToad.PdfPig;
using UglyToad.PdfPig.Content;

namespace BookWriter.Engine.Reimagining;

/// <summary>Which raw form a <see cref="SourceDocument"/> came from -- carried through to the
/// rights/provenance note the Book Study and Reimagining Manual's own workflow calls for (see
/// its "2. Establish rights and provenance" section), not used for any behavioural branching
/// later in the pipeline.</summary>
public enum SourceKind
{
    Pdf,
    Word,
    PastedText,
}

/// <summary>One raw source document read into this pipeline, before any chunking, rewording, or
/// de-identification has happened -- <see cref="RawText"/> is the source's own original wording,
/// kept only long enough for <see cref="Reimagining.SourceChunker"/>/<see cref="ChunkRewriter"/>
/// to work from and for the later similarity audits to compare a finished draft back against;
/// it is never itself the thing handed to a drafting model (see those classes' own doc
/// comments).</summary>
public sealed class SourceDocument
{
    public string Title { get; init; } = "";
    public string RawText { get; init; } = "";
    public SourceKind Kind { get; init; }

    /// <summary>A short, human-readable provenance note (source file name, page/word count) --
    /// not a legal rights determination. The Reimagining Manual's own "Establish rights and
    /// provenance" step (author, death year, edition, lawful-access) is a human research task
    /// this app cannot perform automatically; this note exists so that step has something
    /// concrete to attach to, not to replace it.</summary>
    public string ProvenanceNote { get; init; } = "";
}

/// <summary>
/// Reads a source document -- <c>.pdf</c>, <c>.docx</c>, or plain <c>.txt</c>/<c>.md</c> -- or
/// wraps directly pasted text, into a <see cref="SourceDocument"/> for the reimagining pipeline
/// (<see cref="SourceChunker"/> next). This is deliberately a separate, simpler reader from
/// <see cref="ManuscriptImporter"/>: that class's whole job is splitting a manuscript into
/// numbered chapters for editing; this one only needs one long, reasonably paragraph-structured
/// wall of text per source, since chunking-by-subtopic is <see cref="SourceChunker"/>'s own,
/// separate, AI-driven job.
///
/// PDF EXTRACTION QUALITY, disclosed honestly rather than assumed: PdfPig's own page.Text
/// concatenates every word on a page with no paragraph or even line-break structure at all
/// (verified directly -- a two-paragraph, two-heading test page round-tripped as one run-on
/// string with headings glued straight onto the following paragraph). This class instead groups
/// each page's own Word list (Word.BoundingBox positions) into lines by vertical position, then
/// lines into paragraphs by detecting a larger-than-normal vertical gap between consecutive
/// lines -- a standard, reasonable layout heuristic, not a claim of pixel-perfect reconstruction.
/// Common ligature glyphs (fi/fl/ffi/ffl/ff/st) are expanded back to plain letters, since PdfPig
/// decodes those as single Unicode ligature code points rather than the two-or-three separate
/// letters a chunking/rewording AI call would expect to read. A PDF whose font embeds custom,
/// non-standard ligature glyphs with no Unicode mapping at all can still lose an internal letter
/// or two in a rare word -- an honest, disclosed limitation of PDF text extraction in general,
/// not something this class silently papers over.
///
/// Never throws for an ordinary problem (missing file, empty/unreadable document, unsupported
/// extension) -- returns (null, reason) instead, same convention as ManuscriptImporter.Import.
/// </summary>
public static class SourceDocumentReader
{
    public static IReadOnlyList<string> SupportedExtensions { get; } = new[] { ".pdf", ".docx", ".txt", ".md" };

    public const string OpenFileDialogFilter =
        "Source documents (*.pdf;*.docx;*.txt;*.md)|*.pdf;*.docx;*.txt;*.md|" +
        "PDF (*.pdf)|*.pdf|Word document (*.docx)|*.docx|Text/Markdown (*.txt;*.md)|*.txt;*.md|All files (*.*)|*.*";

    /// <summary>Reads a source file into a <see cref="SourceDocument"/>. Returns
    /// <c>(null, reason)</c> on any ordinary failure rather than throwing.</summary>
    public static (SourceDocument? Document, string Error) ReadFile(string path)
    {
        if (string.IsNullOrWhiteSpace(path))
            return (null, "No file was supplied.");
        if (!File.Exists(path))
            return (null, $"File not found: \"{path}\".");

        string extension = Path.GetExtension(path).ToLowerInvariant();
        if (!SupportedExtensions.Contains(extension))
            return (null, $"Unsupported file type \"{extension}\". This can read {string.Join(", ", SupportedExtensions)}.");

        string title = Path.GetFileNameWithoutExtension(path).Trim();

        try
        {
            return extension switch
            {
                ".pdf" => ReadPdf(path, title),
                ".docx" => ReadDocx(path, title),
                _ => ReadPlainTextFile(path, title),
            };
        }
        catch (Exception ex)
        {
            AppLog.Warning("SourceDocumentReader: failed to read \"{Path}\" - {Error}", path, ex.Message);
            return (null, $"Could not read that file: {ex.Message}");
        }
    }

    /// <summary>Wraps text the author pasted directly (no file) into a <see cref="SourceDocument"/>.
    /// Returns null when the text is blank -- nothing to distill.</summary>
    public static SourceDocument? FromPastedText(string text, string title)
    {
        if (string.IsNullOrWhiteSpace(text)) return null;

        string trimmed = text.Trim();
        int wordCount = trimmed.Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries).Length;
        return new SourceDocument
        {
            Title = string.IsNullOrWhiteSpace(title) ? "Pasted text" : title.Trim(),
            RawText = trimmed,
            Kind = SourceKind.PastedText,
            ProvenanceNote = $"Pasted directly into the app ({wordCount:N0} word(s)).",
        };
    }

    // ==================== PDF ====================

    private static (SourceDocument?, string) ReadPdf(string path, string title)
    {
        using PdfDocument document = PdfDocument.Open(path);
        var pageTexts = new List<string>();
        foreach (Page page in document.GetPages())
            pageTexts.Add(ReconstructPageText(page));

        string combined = NormalizeLigatures(string.Join("\n\n", pageTexts.Where(p => p.Length > 0)));
        if (string.IsNullOrWhiteSpace(combined))
            return (null, "That PDF has no extractable text (it may be a scanned image with no text layer).");

        int wordCount = combined.Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries).Length;
        var doc = new SourceDocument
        {
            Title = title,
            RawText = combined,
            Kind = SourceKind.Pdf,
            ProvenanceNote = $"PDF \"{Path.GetFileName(path)}\", {document.NumberOfPages} page(s), {wordCount:N0} word(s) extracted.",
        };
        return (doc, "");
    }

    /// <summary>Groups one page's words into lines by vertical position, then lines into
    /// paragraphs by vertical gap -- see this class's own top doc comment for why, and for the
    /// honest limits of this approach.</summary>
    private static string ReconstructPageText(Page page)
    {
        List<Word> words = page.GetWords().ToList();
        if (words.Count == 0) return "";

        // Group into lines: a new line starts when a word's vertical center is not within half
        // a typical word-height of the current line's own running vertical center. PdfPig's own
        // GetWords() enumeration order is already reading order (left-to-right, top-to-bottom)
        // for the ordinary single-column layout this app expects to read.
        var lines = new List<List<Word>> { new() { words[0] } };
        foreach (Word word in words.Skip(1))
        {
            List<Word> currentLine = lines[^1];
            Word lastWord = currentLine[^1];
            double lineHeight = Math.Max(lastWord.BoundingBox.Height, word.BoundingBox.Height);
            double verticalShift = Math.Abs(word.BoundingBox.Bottom - lastWord.BoundingBox.Bottom);

            if (verticalShift <= lineHeight * 0.6)
                currentLine.Add(word);
            else
                lines.Add(new List<Word> { word });
        }

        // Paragraph breaks: a gap between consecutive lines noticeably larger than the typical
        // single-line-to-next-line gap reads as a real paragraph/heading boundary, not just
        // ordinary line spacing within one paragraph.
        var lineTexts = lines.Select(line => string.Join(" ", line.Select(w => w.Text))).ToList();
        var gaps = new List<double>();
        for (int i = 1; i < lines.Count; i++)
            gaps.Add(lines[i - 1][0].BoundingBox.Bottom - lines[i][0].BoundingBox.Top);
        double typicalGap = gaps.Count > 0 ? gaps.OrderBy(g => g).ElementAt(gaps.Count / 2) : 0; // median, robust to a few large outliers

        var sb = new StringBuilder();
        sb.Append(lineTexts[0]);
        for (int i = 1; i < lineTexts.Count; i++)
        {
            bool isParagraphBreak = gaps[i - 1] > Math.Max(typicalGap * 1.6, typicalGap + 2);
            sb.Append(isParagraphBreak ? "\n\n" : " ").Append(lineTexts[i]);
        }
        return sb.ToString();
    }

    /// <summary>Expands the common ligature code points PdfPig decodes as a single character
    /// (contraction, not word-loss) back to their plain letters, so downstream chunking/reword
    /// AI calls see ordinary spelling rather than "ﬁrst"/"ﬂow"/etc.</summary>
    private static string NormalizeLigatures(string text) => text
        .Replace("ﬀ", "ff")
        .Replace("ﬁ", "fi")
        .Replace("ﬂ", "fl")
        .Replace("ﬃ", "ffi")
        .Replace("ﬄ", "ffl")
        .Replace("ﬅ", "st")
        .Replace("ﬆ", "st");

    // ==================== Word / plain text ====================

    private static (SourceDocument?, string) ReadDocx(string path, string title)
    {
        using WordprocessingDocument doc = WordprocessingDocument.Open(path, false);
        var body = doc.MainDocumentPart?.Document?.Body;
        if (body is null) return (null, "That .docx file has no document body.");

        var paragraphs = body.Descendants<DocumentFormat.OpenXml.Wordprocessing.Paragraph>()
            .Select(p => p.InnerText.Trim())
            .Where(t => t.Length > 0)
            .ToList();

        if (paragraphs.Count == 0)
            return (null, "That .docx file has no readable text in it.");

        string combined = string.Join("\n\n", paragraphs);
        int wordCount = combined.Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries).Length;
        var source = new SourceDocument
        {
            Title = title,
            RawText = combined,
            Kind = SourceKind.Word,
            ProvenanceNote = $"Word document \"{Path.GetFileName(path)}\", {paragraphs.Count} paragraph(s), {wordCount:N0} word(s).",
        };
        return (source, "");
    }

    private static (SourceDocument?, string) ReadPlainTextFile(string path, string title)
    {
        string text = File.ReadAllText(path).Trim();
        if (text.Length == 0) return (null, "That file has no text in it.");

        int wordCount = text.Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries).Length;
        var source = new SourceDocument
        {
            Title = title,
            RawText = text,
            Kind = SourceKind.PastedText,
            ProvenanceNote = $"Text file \"{Path.GetFileName(path)}\", {wordCount:N0} word(s).",
        };
        return (source, "");
    }
}
