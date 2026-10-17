using System.Text.RegularExpressions;
using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;
using QuestPDF.Fluent;
using QuestPDF.Helpers;
using QuestPDF.Infrastructure;

namespace BookWriter.Engine;

/// <summary>
/// Exports a <see cref="Book"/> (BookWriter's own output: a fixed Outline plus whatever
/// chapters have been written into ChapterContents so far) as a real, KDP-ready manuscript -
/// a Word (.docx) file via the OpenXml SDK and a print-trim PDF via QuestPDF. Both formats
/// render the same content: a centered title page, then one page-break-separated section per
/// chapter (heading "Chapter N: Title", then the chapter's prose split into real paragraphs on
/// blank-line boundaries).
///
/// DELIBERATE DEVIATION from ScriptDocumentExporter.cs's own .docx approach: that file
/// intentionally emits only plain paragraphs with explicit RunProperties and no Styles.xml
/// stylesheet at all, which is a fine, disposable shape for an internal script-review document
/// nobody but this app's own users ever opens elsewhere. A KDP-bound manuscript is different:
/// Kindle Create's and KDP's own DOCX-to-ebook ingestion pipeline, and Word's own "Insert Table
/// of Contents" feature, both key off real named paragraph styles (specifically the standard
/// built-in "Title" and "Heading1" style ids, the same ones Word itself writes for those built-
/// in styles) to find chapter/section breaks for e-reader navigation and TOC generation - not
/// off plain bold text that happens to look like a heading. So this file, unlike
/// ScriptDocumentExporter, builds a minimal StyleDefinitionsPart with real "Title"/"Heading1"
/// w:style elements and applies them via ParagraphProperties/ParagraphStyleId, instead of
/// relying only on ad hoc RunProperties. Body paragraphs still use direct RunProperties/
/// ParagraphProperties (no "Normal" override) since KDP's own recognition only cares about the
/// heading/title styles, not the body text's own style id.
///
/// The exact required child-element order inside a w:style element (w:name, then w:pPr, then
/// w:rPr - StyleName before StyleParagraphProperties before StyleRunProperties, per OOXML's own
/// CT_Style sequence) and inside StyleParagraphProperties/ParagraphProperties (spacing, then
/// indentation, then justification, then outline level) was not assumed from memory: it was
/// confirmed by loading the actual installed DocumentFormat.OpenXml 3.3.0 package DLL via .NET
/// reflection (property declaration order on Style/StyleParagraphProperties/
/// StyleRunProperties/ParagraphProperties mirrors OOXML's own schema sequence in this SDK) and
/// then by building real .docx files both ways in a throwaway console harness and running
/// DocumentFormat.OpenXml.Validation.OpenXmlValidator against them - the correct order produced
/// zero validation errors, and a deliberately reversed order (w:rPr before w:pPr) produced real
/// "unexpected child element" schema errors, the same way ScriptDocumentExporter.cs's own doc
/// comment already verified RunProperties' required CT_RPr child order.
///
/// QuestPDF's page.Size(width, height, Unit) raw overload (as opposed to only the named
/// PageSizes.* constants ScriptDocumentExporter.cs uses) was likewise confirmed against the
/// installed QuestPDF 2024.12.3 package DLL - both via reflection (PageDescriptor.Size(float,
/// float, Unit) and PageSize's own (float, float, Unit) constructor both exist) and by actually
/// generating a PDF with page.Size(6, 9, Unit.Inch) and reading its raw bytes back: the
/// resulting page object's own /MediaBox entry is "[0 0 432 648]" - exactly 6 x 9 inches at 72
/// points/inch, confirming this is a real trim size, not a mis-parsed no-op. 6x9 inches is
/// Amazon KDP's single most common print/PDF trim size.
///
/// QuestPDF requires accepting a license once per process before generating its first document
/// (see the static constructor below) - same Community-tier rationale as
/// ScriptDocumentExporter.cs's own doc comment already covers; setting it again here is
/// idempotent and harmless if that class's static constructor already ran first in this
/// process.
/// </summary>
public static class BookDocumentExporter
{
    static BookDocumentExporter()
    {
        QuestPDF.Settings.License = LicenseType.Community;
    }


    /// <summary>Renders <paramref name="book"/> as a Word (.docx) manuscript at
    /// <paramref name="outputPath"/>, using real named "Title"/"Heading1" paragraph styles (see
    /// this class's own doc comment for why - a deliberate deviation from
    /// ScriptDocumentExporter's plain-paragraph approach). "" on success, a clear honest error
    /// string on failure (bad path, an OpenXml write exception, disk full, etc.) - never throws
    /// for an ordinary I/O problem. When the book is only partially written (ChapterContents is
    /// shorter than Outline.Chapters, e.g. a chapter generation failed and was skipped, or the
    /// book simply is not finished yet), this still succeeds and exports every chapter that
    /// actually has both a planned outline entry and written prose - the return value then
    /// honestly names the first omitted trailing chapter instead of silently exporting a
    /// shorter book with no explanation, and instead of failing outright over an ordinary,
    /// expected partial-book state. The document is built to a temp file next to the real
    /// target and only moved into place once the OpenXml writer has fully finished, so a
    /// failure partway through never leaves a truncated or corrupt .docx at outputPath.</summary>
    public static string ExportToDocx(Book book, string outputPath, BookStyleOptions? style = null)
    {
        if (book is null)
            return "No book supplied to export.";
        if (book.Outline is null)
            return "The book has no outline to export.";

        (List<(ChapterOutline Outline, List<string> Paragraphs)> chapters, string completionNote) = PrepareChapters(book);

        string prepError = PrepareOutputPaths(outputPath, out string tempPath);
        if (prepError.Length > 0) return prepError;

        try
        {
            BuildDocxDocument(book, tempPath, chapters, style ?? BookStyleOptions.Default);

            if (!File.Exists(tempPath) || new FileInfo(tempPath).Length == 0)
            {
                TryDelete(tempPath);
                AppLog.Warning("BookDocumentExporter.ExportToDocx produced no output for {Path}", outputPath);
                return "The Word document was not written (OpenXml produced no output).";
            }

            File.Move(tempPath, outputPath, overwrite: true);
            AppLog.Info("BookDocumentExporter.ExportToDocx wrote {Path}", outputPath);
            return completionNote;
        }
        catch (Exception ex)
        {
            TryDelete(tempPath);
            AppLog.Warning("BookDocumentExporter.ExportToDocx failed for {Path}: {Error}", outputPath, ex.Message);
            return "Could not create the book Word document: " + ex.Message;
        }
    }

    /// <summary>Renders <paramref name="book"/> as a 6x9-inch (Amazon KDP's most common print/
    /// PDF trim size) PDF at <paramref name="outputPath"/>. Same "" / honest-error-string
    /// contract, same build-to-a-temp-file-then-move safety, and the same honest partial-book
    /// completion note in place of a bare "" as <see cref="ExportToDocx"/> - see that method's
    /// own doc comment for both.</summary>
    public static string ExportToPdf(Book book, string outputPath, BookStyleOptions? style = null)
    {
        if (book is null)
            return "No book supplied to export.";
        if (book.Outline is null)
            return "The book has no outline to export.";

        (List<(ChapterOutline Outline, List<string> Paragraphs)> chapters, string completionNote) = PrepareChapters(book);

        string prepError = PrepareOutputPaths(outputPath, out string tempPath);
        if (prepError.Length > 0) return prepError;

        try
        {
            BuildPdfDocument(book, chapters, style ?? BookStyleOptions.Default).GeneratePdf(tempPath);

            if (!File.Exists(tempPath) || new FileInfo(tempPath).Length == 0)
            {
                TryDelete(tempPath);
                AppLog.Warning("BookDocumentExporter.ExportToPdf produced no PDF output for {Path}", outputPath);
                return "QuestPDF ran but produced no PDF output.";
            }

            File.Move(tempPath, outputPath, overwrite: true);
            AppLog.Info("BookDocumentExporter.ExportToPdf wrote {Path}", outputPath);
            return completionNote;
        }
        catch (Exception ex)
        {
            TryDelete(tempPath);
            AppLog.Warning("BookDocumentExporter.ExportToPdf failed for {Path}: {Error}", outputPath, ex.Message);
            return "Could not create the book PDF: " + ex.Message;
        }
    }

    // ==== Shared content preparation ====

    /// <summary>Pairs each chapter that has BOTH a planned outline entry AND already-written
    /// prose (guarding the case where ChapterContents is shorter than Outline.Chapters - a
    /// partially-written book, e.g. mid-generation or missing a chapter that failed and was
    /// left out) with that chapter's prose split into real paragraphs. Returns alongside it an
    /// honest completion note: "" when every outline chapter had matching prose, or a short
    /// message naming the first omitted trailing chapter otherwise - callers return this note
    /// as their own success value instead of a bare "" so a partial export is never silently
    /// indistinguishable from a complete one.</summary>
    private static (List<(ChapterOutline Outline, List<string> Paragraphs)> Chapters, string CompletionNote) PrepareChapters(Book book)
    {
        int totalOutlineChapters = book.Outline.Chapters.Count;
        int renderableCount = Math.Min(totalOutlineChapters, book.ChapterContents.Count);

        var chapters = new List<(ChapterOutline Outline, List<string> Paragraphs)>(renderableCount);
        for (int i = 0; i < renderableCount; i++)
            chapters.Add((book.Outline.Chapters[i], SplitIntoParagraphs(book.ChapterContents[i])));

        int omittedCount = totalOutlineChapters - renderableCount;
        if (omittedCount == 0)
            return (chapters, "");

        int firstOmittedChapterNumber = book.Outline.Chapters[renderableCount].Number;
        string note = $"Exported {renderableCount} of {totalOutlineChapters} chapter(s); chapter {firstOmittedChapterNumber} onward has no written content yet and was omitted.";
        return (chapters, note);
    }

    /// <summary>Splits one chapter's raw prose into real paragraphs on blank-line boundaries
    /// (one or more blank lines, either \n or \r\n), joining any single-newline-wrapped lines
    /// within a paragraph back into one flowing line first - a chapter generator's own raw text
    /// may hard-wrap lines that were never meant to be separate paragraphs.</summary>
    private static List<string> SplitIntoParagraphs(string chapterText)
    {
        var paragraphs = new List<string>();
        if (string.IsNullOrWhiteSpace(chapterText))
            return paragraphs;

        string normalized = chapterText.Replace("\r\n", "\n").Replace("\r", "\n");
        foreach (string block in Regex.Split(normalized, @"\n[ \t]*\n+"))
        {
            string joined = string.Join(" ", block.Split('\n').Select(line => line.Trim()).Where(line => line.Length > 0));
            if (joined.Length > 0)
                paragraphs.Add(joined);
        }

        return paragraphs;
    }

    /// <summary>Validates outputPath, creates its parent directory if missing, and hands back a
    /// same-directory temp path to build into first - same rationale as
    /// ScriptDocumentExporter's own identical private helper (duplicated here rather than
    /// shared, since that method is private to that class): building next to the real target
    /// keeps the final File.Move a same-volume rename, atomic on every filesystem this app
    /// actually runs on.</summary>
    private static string PrepareOutputPaths(string outputPath, out string tempPath)
    {
        tempPath = "";
        if (string.IsNullOrWhiteSpace(outputPath))
            return "No output path supplied.";

        try
        {
            string fullPath = Path.GetFullPath(outputPath);
            string? dir = Path.GetDirectoryName(fullPath);
            if (!string.IsNullOrEmpty(dir))
                Directory.CreateDirectory(dir);

            string dirForTemp = string.IsNullOrEmpty(dir) ? "." : dir;
            tempPath = Path.Combine(dirForTemp, $"~{Path.GetFileName(fullPath)}.{Guid.NewGuid():N}.tmp");
            return "";
        }
        catch (Exception ex)
        {
            AppLog.Warning("BookDocumentExporter could not prepare output path {Path}: {Error}", outputPath, ex.Message);
            return $"Could not prepare output path \"{outputPath}\": {ex.Message}";
        }
    }

    /// <summary>Best-effort cleanup of a leftover temp file after a failed export - deliberately
    /// swallows any exception of its own (a locked/already-gone file here must never mask the
    /// real failure the caller is already reporting).</summary>
    private static void TryDelete(string path)
    {
        try
        {
            if (path.Length > 0 && File.Exists(path))
                File.Delete(path);
        }
        catch
        {
            // Best-effort only - a failure to delete a temp file is not worth surfacing.
        }
    }

    // ==== DOCX (DocumentFormat.OpenXml) ====

    private static void BuildDocxDocument(Book book, string path, List<(ChapterOutline Outline, List<string> Paragraphs)> chapters, BookStyleOptions style)
    {
        using WordprocessingDocument wordDocument = WordprocessingDocument.Create(path, WordprocessingDocumentType.Document);
        MainDocumentPart mainPart = wordDocument.AddMainDocumentPart();
        mainPart.Document = new DocumentFormat.OpenXml.Wordprocessing.Document();
        Body body = mainPart.Document.AppendChild(new Body());

        StyleDefinitionsPart stylesPart = mainPart.AddNewPart<StyleDefinitionsPart>();
        stylesPart.Styles = BuildStylesheet(style);
        stylesPart.Styles.Save();

        var links = new DocxInlineContext(mainPart, chapters.Count);

        string title = book.Outline.Title.Length > 0 ? book.Outline.Title : "Untitled Book";
        var titleParagraph = new Paragraph(
            new ParagraphProperties(new ParagraphStyleId { Val = "Title" }),
            new Run(new Text(title)));
        body.AppendChild(titleParagraph);
        body.AppendChild(BuildTableOfContentsField());

        foreach ((ChapterOutline outline, List<string> paragraphs) in chapters)
        {
            // A bookmark named "chapterN" wraps the heading run so an internal
            // [text](chapter:N) link elsewhere in the book resolves to a real Word bookmark
            // (Hyperlink w:anchor) rather than a dead cross-reference.
            string bookmarkId = links.NextBookmarkId();
            var headingParagraph = new Paragraph(
                new ParagraphProperties(new ParagraphStyleId { Val = "Heading1" }, new PageBreakBefore()),
                new BookmarkStart { Name = $"chapter{outline.Number}", Id = bookmarkId },
                new Run(new Text(ChapterHeadingLabel(outline))),
                new BookmarkEnd { Id = bookmarkId });
            body.AppendChild(headingParagraph);

            foreach (string paragraphText in paragraphs)
            {
                Match subheading = SubheadingPattern.Match(paragraphText.Trim());
                body.AppendChild(subheading.Success
                    ? BuildSubheadingParagraph(subheading.Groups[1].Value)
                    : BuildBodyParagraph(paragraphText, links, style));
            }
        }

        mainPart.Document.Save();
    }

    /// <summary>A body paragraph whose ENTIRE text is one <c>**bold**</c> span and nothing else
    /// -- this project's own convention (used throughout every hand-written guide chapter) for a
    /// sub-section heading inside a chapter, one level below the chapter's own Heading1. Matched
    /// before <see cref="InlineMarkup"/> ever sees the paragraph, since a real Heading2 paragraph
    /// needs a named style Word can index, not just a bold run sitting inside an ordinary Normal
    /// paragraph.</summary>
    private static readonly Regex SubheadingPattern = new(@"^\*\*(.+)\*\*$", RegexOptions.Compiled);

    /// <summary>Renders a matched <see cref="SubheadingPattern"/> line as a real "Heading2"
    /// paragraph -- <see cref="InlineMarkup.ToPlainText"/> strips any further inline markup
    /// (there should not normally be any inside a heading) so Word's own Navigation Pane and a
    /// "Insert Table of Contents" both show clean heading text, not literal asterisks.</summary>
    private static Paragraph BuildSubheadingParagraph(string text) =>
        new(new ParagraphProperties(new ParagraphStyleId { Val = "Heading2" }),
            new Run(new Text(InlineMarkup.ToPlainText(text))));

    /// <summary>A real Word TOC field (the same <c>{ TOC }</c> field Word's own "References →
    /// Table of Contents" ribbon button inserts) driven off the Heading1/Heading2 styles this
    /// exporter already applies -- so Word's left-hand Navigation Pane and an actual in-document
    /// contents page show the identical outline, both built from the same paragraph styles rather
    /// than two separately-maintained lists. <c>Dirty = true</c> tells Word this field's cached
    /// result is stale so it prompts to update on open; the placeholder run underneath is what a
    /// reader sees if they dismiss that prompt without updating, so it reads as an instruction
    /// rather than as blank, broken-looking space.</summary>
    private static Paragraph BuildTableOfContentsField()
    {
        var beginRun = new Run(new FieldChar { FieldCharType = FieldCharValues.Begin, Dirty = OnOffValue.FromBoolean(true) });
        var instructionRun = new Run(new FieldCode(" TOC \\o \"1-2\" \\h \\z \\u ") { Space = SpaceProcessingModeValues.Preserve });
        var separateRun = new Run(new FieldChar { FieldCharType = FieldCharValues.Separate });
        var placeholderRun = new Run(new Text("Right-click here and choose \"Update Field\" (or press F9) to build the table of contents."));
        var endRun = new Run(new FieldChar { FieldCharType = FieldCharValues.End });

        return new Paragraph(new ParagraphProperties(new SpacingBetweenLines { After = "480" }),
            beginRun, instructionRun, separateRun, placeholderRun, endRun);
    }

    /// <summary>"Chapter N: Title", or the raw "Appendix: ..." title kept as-is for a
    /// science-appendix chapter (matching <see cref="BookEpubExporter"/>'s own label rule), or
    /// just "Chapter N" when the outline entry has no title.</summary>
    private static string ChapterHeadingLabel(ChapterOutline outline)
    {
        string chapterTitle = string.IsNullOrWhiteSpace(outline.Title) ? "" : outline.Title.Trim();
        if (BookGenreRules.LooksLikeAppendixChapter(chapterTitle)) return chapterTitle;
        return chapterTitle.Length > 0 ? $"Chapter {outline.Number}: {chapterTitle}" : $"Chapter {outline.Number}";
    }

    /// <summary>Per-document state for rendering inline links in the Word export: the
    /// <see cref="MainDocumentPart"/> that owns external hyperlink relationships, how many
    /// chapters this export contains (an internal link past that has no bookmark and is drawn as
    /// plain text), and a running unique id for the <c>chapterN</c> heading bookmarks.</summary>
    private sealed class DocxInlineContext(MainDocumentPart mainPart, int exportedChapterCount)
    {
        private int _nextBookmarkId = 1;

        public MainDocumentPart MainPart => mainPart;
        public int ExportedChapterCount => exportedChapterCount;
        public string NextBookmarkId() => (_nextBookmarkId++).ToString();
    }

    /// <summary>Builds the two real named paragraph styles a KDP-bound manuscript needs -
    /// "Title" and "Heading1", the same StyleIds Word itself writes for its own built-in
    /// styles of those names - so Kindle Create/KDP's own DOCX ingestion and Word's "Insert
    /// Table of Contents" both recognize this document's own structure instead of seeing plain
    /// paragraphs. Child element order inside each w:style (w:name, then w:pPr, then w:rPr) and
    /// inside each w:pPr (spacing, then justification, then outline level) follows OOXML's own
    /// required CT_Style/CT_PPrBase sequence - confirmed via reflection and a real
    /// OpenXmlValidator run against the installed package before writing this method; see this
    /// class's own top doc comment for how.</summary>
    private static Styles BuildStylesheet(BookStyleOptions style)
    {
        var titleStyle = new Style
        {
            Type = StyleValues.Paragraph,
            StyleId = "Title",
        };
        titleStyle.Append(new StyleName { Val = "Title" });
        titleStyle.Append(new StyleParagraphProperties(
            new SpacingBetweenLines { After = "480" },
            new Justification { Val = JustificationValues.Center }));
        titleStyle.Append(BuildHeadingRunProperties(style, "72"));

        var heading1Style = new Style
        {
            Type = StyleValues.Paragraph,
            StyleId = "Heading1",
        };
        heading1Style.Append(new StyleName { Val = "heading 1" });
        heading1Style.Append(new StyleParagraphProperties(
            new SpacingBetweenLines { Before = "480", After = "240" },
            new OutlineLevel { Val = 0 }));
        heading1Style.Append(BuildHeadingRunProperties(style, "32"));

        var heading2Style = new Style
        {
            Type = StyleValues.Paragraph,
            StyleId = "Heading2",
        };
        heading2Style.Append(new StyleName { Val = "heading 2" });
        heading2Style.Append(new StyleParagraphProperties(
            new SpacingBetweenLines { Before = "240", After = "120" },
            new OutlineLevel { Val = 1 }));
        heading2Style.Append(BuildHeadingRunProperties(style, "26"));

        return new Styles(titleStyle, heading1Style, heading2Style);
    }

    /// <summary>Builds the Title/Heading1 styles' shared w:rPr -- font, bold, and color from
    /// <see cref="BookStyleOptions.HeadingFontFamily"/>/<c>HeadingBold</c>/<c>HeadingColor</c> --
    /// in OOXML's required CT_RPr child order (rFonts, b, color, sz; see this class's own top
    /// doc comment for how that order was verified).</summary>
    private static StyleRunProperties BuildHeadingRunProperties(BookStyleOptions style, string fontSizeHalfPoints)
    {
        var props = new StyleRunProperties();
        props.Append(new RunFonts { Ascii = style.HeadingFontFamily, HighAnsi = style.HeadingFontFamily });
        if (style.HeadingBold) props.Append(new Bold());
        string headingColor = BookStyleOptions.NormalizeHex(style.HeadingColor);
        if (headingColor.Length > 0) props.Append(new DocumentFormat.OpenXml.Wordprocessing.Color { Val = headingColor });
        props.Append(new FontSize { Val = fontSizeHalfPoints });
        return props;
    }

    /// <summary>Builds one body-text paragraph: justified, first-line-indented like real book
    /// typesetting, using direct ParagraphProperties/RunProperties rather than a "Normal" named
    /// style override - KDP's/Word's own style-based recognition only cares about the Title/
    /// Heading1 styles above, not the body text's own style id, so a named style here would add
    /// complexity without adding any real navigational value.
    ///
    /// The paragraph's text is run through <see cref="InlineMarkup"/> so <c>**bold**</c> /
    /// <c>*italic*</c> become real run properties and a Markdown link becomes a real Word
    /// hyperlink - an external <c>[text](https://...)</c> as a <c>w:hyperlink r:id</c> with an
    /// external relationship, an internal <c>[text](chapter:N)</c> as a <c>w:hyperlink w:anchor</c>
    /// pointing at that chapter's heading bookmark (see <see cref="BuildDocxDocument"/>).</summary>
    private static Paragraph BuildBodyParagraph(string text, DocxInlineContext links, BookStyleOptions style)
    {
        var paragraph = new Paragraph(new ParagraphProperties(
            new Indentation { FirstLine = "360" },
            new Justification { Val = JustificationValues.Both }));

        foreach (InlineRun run in InlineMarkup.Parse(text))
            paragraph.AppendChild(BuildInlineElement(run, links, style));

        return paragraph;
    }

    /// <summary>One <see cref="InlineRun"/> as either a bare <c>w:r</c> or a <c>w:hyperlink</c>
    /// wrapping one, styled from <see cref="BookStyleOptions.BodyFontFamily"/>/<c>BodyBold</c>/
    /// <c>BodyColor</c> as the base, with the run's own markdown bold/italic layered on top and
    /// a link's color/underline always winning over <c>BodyColor</c> (a link should still look
    /// like a link regardless of the chosen body color). RunProperties children are appended in
    /// OOXML's required CT_RPr order (rFonts, b, i, color, sz, u) - the same "child-element order
    /// was verified, not assumed" discipline this class's own top doc comment documents for the
    /// stylesheet.</summary>
    private static OpenXmlElement BuildInlineElement(InlineRun run, DocxInlineContext links, BookStyleOptions style)
    {
        bool isExternal = run.LinkKind == InlineLinkKind.External;
        bool isInternal = run.LinkKind == InlineLinkKind.InternalChapter &&
            int.TryParse(run.LinkTarget, out int n) && n >= 1 && n <= links.ExportedChapterCount;
        bool linked = isExternal || isInternal;

        var runProperties = new RunProperties();
        runProperties.AppendChild(new RunFonts { Ascii = style.BodyFontFamily, HighAnsi = style.BodyFontFamily });
        if (run.Bold || style.BodyBold) runProperties.AppendChild(new Bold());
        if (run.Italic) runProperties.AppendChild(new Italic());
        string bodyColor = linked ? "0563C1" : BookStyleOptions.NormalizeHex(style.BodyColor);
        if (bodyColor.Length > 0) runProperties.AppendChild(new DocumentFormat.OpenXml.Wordprocessing.Color { Val = bodyColor });
        runProperties.AppendChild(new FontSize { Val = "24" });
        if (linked) runProperties.AppendChild(new Underline { Val = UnderlineValues.Single });

        var wordRun = new Run(runProperties, new Text(run.Text) { Space = SpaceProcessingModeValues.Preserve });

        if (isExternal && TryMakeUri(run.LinkTarget, out Uri uri))
        {
            string relationshipId = links.MainPart.AddHyperlinkRelationship(uri, true).Id;
            return new Hyperlink(wordRun) { Id = relationshipId };
        }
        if (isInternal)
        {
            int.TryParse(run.LinkTarget, out int chapterNumber);
            return new Hyperlink(wordRun) { Anchor = $"chapter{chapterNumber}" };
        }
        return wordRun;
    }

    private static bool TryMakeUri(string value, out Uri uri)
    {
        try
        {
            uri = new Uri(value, UriKind.Absolute);
            return true;
        }
        catch
        {
            uri = null!;
            return false;
        }
    }

    // ==== PDF (QuestPDF) ====

    private static IDocument BuildPdfDocument(Book book, List<(ChapterOutline Outline, List<string> Paragraphs)> chapters, BookStyleOptions style)
    {
        string title = book.Outline.Title.Length > 0 ? book.Outline.Title : "Untitled Book";
        string bodyColor = BookStyleOptions.NormalizeHex(style.BodyColor);

        return QuestPDF.Fluent.Document.Create(container =>
        {
            container.Page(page =>
            {
                // 6x9 inches: Amazon KDP's single most common print/PDF trim size. Confirmed
                // via reflection (PageDescriptor.Size(float, float, Unit) exists on the
                // installed QuestPDF 2024.12.3 package, not only the named PageSizes.*
                // constants ScriptDocumentExporter.cs uses) and by reading a generated PDF's
                // own raw /MediaBox back ("[0 0 432 648]" = exactly 6 x 9in at 72pt/in).
                page.Size(6, 9, Unit.Inch);
                page.Margin(0.9f, Unit.Inch);
                // The page-wide default IS the body style -- headings below explicitly
                // override font family/weight/color on top of this, same cascade QuestPDF
                // already uses for every other per-span override (a link's color, a markdown
                // bold run) elsewhere in this file.
                page.DefaultTextStyle(text =>
                {
                    text = text.FontSize(12).FontFamily(style.BodyFontFamilyChain);
                    text = style.BodyBold ? text.Bold() : text;
                    return bodyColor.Length > 0 ? text.FontColor("#" + bodyColor) : text;
                });

                page.Content().Column(column =>
                {
                    column.Spacing(10);

                    column.Item().AlignCenter().PaddingTop(2.5f, Unit.Inch)
                        .Text(text => ApplyHeadingSpan(text.Span(title), style).FontSize(30));

                    foreach ((ChapterOutline outline, List<string> paragraphs) in chapters)
                    {
                        column.Item().PageBreak();
                        // Section("chapterN") is the internal-link target a [text](chapter:N)
                        // link elsewhere in the book resolves to via TextDescriptor.SectionLink.
                        column.Item().Section($"chapter{outline.Number}")
                            .Text(text => ApplyHeadingSpan(text.Span(ChapterHeadingLabel(outline)), style).FontSize(18));

                        foreach (string paragraphText in paragraphs)
                        {
                            column.Item().Text(text =>
                            {
                                text.Justify();
                                text.ParagraphFirstLineIndentation(0.25f, Unit.Inch);
                                AppendPdfRuns(text, paragraphText, chapters.Count);
                            });
                        }
                    }
                });

                page.Footer().AlignCenter().Text(footer =>
                {
                    footer.CurrentPageNumber();
                    footer.Span(" / ");
                    footer.TotalPages();
                });
            });
        });
    }

    /// <summary>Applies <see cref="BookStyleOptions.HeadingFontFamily"/>/<c>HeadingBold</c>/
    /// <c>HeadingColor</c> to one heading span (the book title or a chapter heading) -- the PDF
    /// equivalent of <see cref="BuildHeadingRunProperties"/> for the Word export. Font size is
    /// left to the caller (title and chapter headings use different sizes).</summary>
    private static TextSpanDescriptor ApplyHeadingSpan(TextSpanDescriptor span, BookStyleOptions style)
    {
        span = span.FontFamily(style.HeadingFontFamilyChain);
        span = style.HeadingBold ? span.Bold() : span.NormalWeight();
        string headingColor = BookStyleOptions.NormalizeHex(style.HeadingColor);
        return headingColor.Length > 0 ? span.FontColor("#" + headingColor) : span;
    }

    /// <summary>Blue used for link text in the PDF, close to the Word export's own <c>0563C1</c>.</summary>
    private const string PdfLinkColor = "#0563C1";

    /// <summary>Renders one paragraph's <see cref="InlineMarkup"/> runs into an open QuestPDF
    /// text block: <c>**bold**</c>/<c>*italic*</c> as span styles, an external link as a real
    /// clickable <see cref="TextDescriptor.Hyperlink(string,string)"/>, and an internal
    /// <c>[text](chapter:N)</c> link (when N is in this export) as a clickable
    /// <see cref="TextDescriptor.SectionLink(string,string)"/> to that chapter's
    /// <c>Section("chapterN")</c>.</summary>
    private static void AppendPdfRuns(TextDescriptor text, string paragraph, int exportedChapterCount)
    {
        foreach (InlineRun run in InlineMarkup.Parse(paragraph))
        {
            bool isExternal = run.LinkKind == InlineLinkKind.External;
            bool isInternal = run.LinkKind == InlineLinkKind.InternalChapter &&
                int.TryParse(run.LinkTarget, out int n) && n >= 1 && n <= exportedChapterCount;

            TextSpanDescriptor span;
            if (isExternal)
                span = text.Hyperlink(run.Text, run.LinkTarget).FontColor(PdfLinkColor);
            else if (isInternal)
                span = text.SectionLink(run.Text, $"chapter{run.LinkTarget}").FontColor(PdfLinkColor);
            else
                span = text.Span(run.Text);

            if (run.Bold) span = span.Bold();
            if (run.Italic) span = span.Italic();
        }
    }
}
