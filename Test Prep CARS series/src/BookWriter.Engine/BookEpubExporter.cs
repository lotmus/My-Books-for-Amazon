using System.Globalization;
using System.IO.Compression;
using System.Text;
using System.Text.RegularExpressions;

namespace BookWriter.Engine;

/// <summary>
/// Exports a (possibly partially-written) <see cref="Book"/> as a real, spec-valid EPUB 3 file
/// - hand-rolled directly against System.IO.Compression.ZipArchive (already in the BCL) rather
/// than a third-party EPUB package, since the whole format is just a strict-shape zip plus a
/// handful of small, fixed XML documents - the same "small per-domain wrapper written directly
/// in this file rather than referencing a cross-project/third-party helper for ~30-100 lines of
/// plumbing" precedent MediaMaker.ScriptToVideo.ThumbnailAI.ThumbnailVariantGenerator's own doc
/// comment (and, in turn, MediaMaker.VideoEditor.FfmpegProcess's) already establishes for this
/// codebase.
///
/// The zip-level shape was hand-verified (not assumed) in an isolated throwaway console project
/// against this solution's actual installed net10.0 runtime: ZipArchive.CreateEntry(name,
/// CompressionLevel.NoCompression) really does write a true STORED local file header
/// (compression method field = 0, general-purpose bit 3 clear so no trailing data descriptor is
/// used, zero-length extra field, exact byte-for-byte content) rather than merely a low deflate
/// level - see this class's own ExportToEpub doc comment for what that guarantees for the
/// mandatory first "mimetype" entry.
///
/// Every public method here returns "" on success or a clear, honest, human-readable error
/// string on failure, and never throws for an ordinary failure (bad path, missing/locked cover
/// image file, disk full) - same convention as ScriptDocumentExporter/ShotListExporter/
/// SeoMetadataSpreadsheetExporter elsewhere in this project. The whole archive is assembled at a
/// same-directory temp path first and only File.Move'd into place once confirmed non-empty, so a
/// failure partway through zip-writing never leaves a truncated/corrupt .epub sitting at the
/// real output path.
/// </summary>
public static class BookEpubExporter
{
    private const string XhtmlNamespace = "http://www.w3.org/1999/xhtml";
    private const string EpubOpsNamespace = "http://www.idpf.org/2007/ops";
    private const string OpfNamespace = "http://www.idpf.org/2007/opf";
    private const string DcNamespace = "http://purl.org/dc/elements/1.1/";
    private const string ContainerNamespace = "urn:oasis:names:tc:opendocument:xmlns:container";

    /// <summary>
    /// Writes <paramref name="book"/> as a real EPUB 3 file at <paramref name="outputPath"/>:
    /// the mandatory first "mimetype" entry (stored, uncompressed, exactly "application/epub
    /// +zip"), META-INF/container.xml, OEBPS/content.opf (the OPF 3.0 package document), OEBPS/
    /// nav.xhtml (the required EPUB 3 navigation document), one title-page XHTML file, one XHTML
    /// file per generated chapter, and - when <see cref="Book.CoverImagePath"/> is set and the
    /// file actually exists - the cover image's own bytes, referenced from the manifest with
    /// properties="cover-image" plus the legacy OPF2-style
    /// meta name="cover" declaration real-world readers (Kindle Previewer/KDP among them) still
    /// look for alongside EPUB 3's own convention.
    ///
    /// Only chapters that have BOTH a planned outline entry AND already-generated prose are
    /// exported - book.Outline.Chapters.Count and book.ChapterContents.Count are allowed to
    /// differ (a partially-written book), and this exports exactly min(both counts) chapters
    /// rather than indexing out of range. That is not itself treated as a failure: this still
    /// returns "" once every chapter that DOES have content has been written out; the omission
    /// is only ever recorded honestly via AppLog.Info, never silently hidden and never promoted
    /// into a fabricated failure. A book with zero generated chapters (nothing has been written
    /// yet) is the one case this treats as a real failure, since there would be nothing but an
    /// empty shell to export.
    ///
    /// Returns "" on success, or a clear, honest error string on failure (no book supplied, no
    /// chapters generated yet, a bad output path, a locked/full disk, or any other ordinary I/O
    /// problem) - never throws.
    /// </summary>
    public static string ExportToEpub(Book book, string outputPath, BookStyleOptions? style = null)
    {
        if (book is null)
            return "No book was supplied to export.";

        int chapterCount = Math.Min(book.Outline.Chapters.Count, book.ChapterContents.Count);
        if (chapterCount == 0)
            return "This book has no generated chapter content yet - there is nothing to export.";

        string prepError = PrepareOutputPaths(outputPath, out string tempPath);
        if (prepError.Length > 0) return prepError;

        try
        {
            BuildEpubFile(book, chapterCount, tempPath, style ?? BookStyleOptions.Default);

            if (!File.Exists(tempPath) || new FileInfo(tempPath).Length == 0)
            {
                TryDelete(tempPath);
                AppLog.Warning("BookEpubExporter.ExportToEpub produced no output for {Path}", outputPath);
                return "The EPUB file was not written (no output was produced).";
            }

            File.Move(tempPath, outputPath, overwrite: true);

            int plannedChapters = book.Outline.Chapters.Count;
            if (chapterCount < plannedChapters)
            {
                AppLog.Info(
                    "BookEpubExporter.ExportToEpub wrote {Path} with {Written} of {Planned} planned chapter(s) - the remaining chapter(s) have not been generated yet and were omitted.",
                    outputPath, chapterCount, plannedChapters);
            }
            else
            {
                AppLog.Info("BookEpubExporter.ExportToEpub wrote {Path} ({Chapters} chapter(s)).", outputPath, chapterCount);
            }

            return "";
        }
        catch (Exception ex)
        {
            TryDelete(tempPath);
            AppLog.Warning("BookEpubExporter.ExportToEpub failed for {Path}: {Error}", outputPath, ex.Message);
            return "Could not create the EPUB file: " + ex.Message;
        }
    }

    // ==================== Zip assembly ====================

    /// <summary>Builds the whole archive at tempPath in one pass, in the exact entry order the
    /// EPUB spec (and real, strict readers) require: mimetype first, then everything else.</summary>
    private static void BuildEpubFile(Book book, int chapterCount, string tempPath, BookStyleOptions style)
    {
        string? dir = Path.GetDirectoryName(tempPath);
        if (!string.IsNullOrEmpty(dir)) Directory.CreateDirectory(dir);

        string title = string.IsNullOrWhiteSpace(book.Outline.Title) ? "Untitled Book" : book.Outline.Title.Trim();
        string uuid = "urn:uuid:" + Guid.NewGuid();
        (string Href, string MediaType)? cover = ResolveCoverImage(book.CoverImagePath);

        using var fileStream = new FileStream(tempPath, FileMode.Create);
        using var archive = new ZipArchive(fileStream, ZipArchiveMode.Create);

        // 1. "mimetype" MUST be the first entry, stored (no compression), exactly these 20
        // ASCII bytes, no trailing newline, no zip "extra field" - confirmed by reflection/live
        // test against this solution's actual runtime, see this class's own top doc comment.
        WriteStoredAsciiEntry(archive, "mimetype", "application/epub+zip");

        // 2. META-INF/container.xml - points readers at the package document below.
        WriteTextEntry(archive, "META-INF/container.xml", BuildContainerXml());

        // 3. OEBPS/content.opf - the OPF 3.0 package document (metadata/manifest/spine).
        WriteTextEntry(archive, "OEBPS/content.opf", BuildContentOpf(book, title, uuid, chapterCount, cover));

        // 4. OEBPS/nav.xhtml - the EPUB 3 required navigation document.
        WriteTextEntry(archive, "OEBPS/nav.xhtml", BuildNavXhtml(title, book, chapterCount));

        // 5. Title page, then one XHTML file per already-generated chapter, in reading order.
        WriteTextEntry(archive, "OEBPS/titlepage.xhtml", BuildTitlePageXhtml(book, title, chapterCount, style));

        for (int i = 0; i < chapterCount; i++)
        {
            ChapterOutline chapterOutline = book.Outline.Chapters[i];
            string chapterText = book.ChapterContents[i];
            WriteTextEntry(archive, $"OEBPS/chapter{i + 1}.xhtml", BuildChapterXhtml(book, chapterOutline, chapterText, chapterCount, style));
        }

        // 6. The cover image's own bytes, only when a real, existing file was supplied.
        if (cover is { } coverInfo)
        {
            byte[] coverBytes = File.ReadAllBytes(book.CoverImagePath!);
            WriteBinaryEntry(archive, "OEBPS/" + coverInfo.Href, coverBytes);
        }
    }

    /// <summary>Writes entryName stored (CompressionLevel.NoCompression - a true STORED entry,
    /// not merely a low deflate level, per this class's own top doc comment) with content's
    /// exact ASCII bytes - the shape the EPUB spec's own mandatory first "mimetype" entry
    /// requires.</summary>
    private static void WriteStoredAsciiEntry(ZipArchive archive, string entryName, string content)
    {
        ZipArchiveEntry entry = archive.CreateEntry(entryName, CompressionLevel.NoCompression);
        byte[] bytes = Encoding.ASCII.GetBytes(content);
        using Stream entryStream = entry.Open();
        entryStream.Write(bytes, 0, bytes.Length);
    }

    /// <summary>Writes one UTF-8 (no byte-order mark - Encoding.UTF8.GetBytes never emits one)
    /// text entry, normally compressed - every XHTML/XML document in this archive goes through
    /// this, only the mimetype entry above needs the special stored/uncompressed treatment.</summary>
    private static void WriteTextEntry(ZipArchive archive, string entryName, string content)
    {
        ZipArchiveEntry entry = archive.CreateEntry(entryName, CompressionLevel.Optimal);
        byte[] bytes = Encoding.UTF8.GetBytes(content);
        using Stream entryStream = entry.Open();
        entryStream.Write(bytes, 0, bytes.Length);
    }

    /// <summary>Writes one binary (cover image) entry, normally compressed.</summary>
    private static void WriteBinaryEntry(ZipArchive archive, string entryName, byte[] bytes)
    {
        ZipArchiveEntry entry = archive.CreateEntry(entryName, CompressionLevel.Optimal);
        using Stream entryStream = entry.Open();
        entryStream.Write(bytes, 0, bytes.Length);
    }

    /// <summary>Resolves book.CoverImagePath into the destination filename (its own real
    /// extension is kept, rather than blindly forcing ".jpg", so the manifest's media-type
    /// always actually matches the bytes on disk) plus the matching manifest media-type - or
    /// null when no cover is set or the file no longer exists, in which case the EPUB simply has
    /// no cover rather than this failing the whole export.</summary>
    private static (string Href, string MediaType)? ResolveCoverImage(string? coverImagePath)
    {
        if (string.IsNullOrWhiteSpace(coverImagePath) || !File.Exists(coverImagePath))
            return null;

        string ext = Path.GetExtension(coverImagePath).ToLowerInvariant();
        string mediaType = ext switch
        {
            ".jpg" or ".jpeg" => "image/jpeg",
            ".png" => "image/png",
            ".gif" => "image/gif",
            ".webp" => "image/webp",
            _ => "image/jpeg",
        };
        // Unrecognized extensions default to a plain ".jpg" destination name paired with the
        // image/jpeg guess above - an honest best effort, not a claim the bytes are verified.
        string safeExt = ext is ".jpg" or ".jpeg" or ".png" or ".gif" or ".webp" ? ext : ".jpg";
        return ($"cover{safeExt}", mediaType);
    }

    // ==================== XML document builders ====================

    /// <summary>META-INF/container.xml - the fixed-format document every EPUB reader opens
    /// first, pointing at the real package document's path.</summary>
    private static string BuildContainerXml()
    {
        var sb = new StringBuilder();
        sb.Append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
        sb.Append("<container xmlns=\"").Append(ContainerNamespace).Append("\" version=\"1.0\">\n");
        sb.Append("  <rootfiles>\n");
        sb.Append("    <rootfile full-path=\"OEBPS/content.opf\" media-type=\"application/oebps-package+xml\"/>\n");
        sb.Append("  </rootfiles>\n");
        sb.Append("</container>\n");
        return sb.ToString();
    }

    /// <summary>OEBPS/content.opf - the OPF 3.0 package document: metadata (dc:title/
    /// dc:language/dc:identifier/the required dcterms:modified timestamp; dc:creator is
    /// deliberately omitted since Book has no author field to source it from), manifest (nav +
    /// title page + one item per exported chapter + the cover image when present), and spine
    /// (title page then every exported chapter, in reading order).</summary>
    private static string BuildContentOpf(Book book, string title, string uuid, int chapterCount, (string Href, string MediaType)? cover)
    {
        string modified = DateTime.UtcNow.ToString("yyyy-MM-dd'T'HH:mm:ss'Z'", CultureInfo.InvariantCulture);
        string safeTitle = EscapeXmlText(title);

        var sb = new StringBuilder();
        sb.Append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
        sb.Append("<package xmlns=\"").Append(OpfNamespace).Append("\" version=\"3.0\" unique-identifier=\"pub-id\" xml:lang=\"en\">\n");

        sb.Append("  <metadata xmlns:dc=\"").Append(DcNamespace).Append("\">\n");
        sb.Append("    <dc:identifier id=\"pub-id\">").Append(EscapeXmlText(uuid)).Append("</dc:identifier>\n");
        sb.Append("    <dc:title>").Append(safeTitle).Append("</dc:title>\n");
        sb.Append("    <dc:language>en</dc:language>\n");
        sb.Append("    <dc:subject>").Append(EscapeXmlText(BookGenreRules.EpubSubject(book.Outline.Genre))).Append("</dc:subject>\n");
        sb.Append("    <meta property=\"dcterms:modified\">").Append(modified).Append("</meta>\n");
        if (cover is not null)
            sb.Append("    <meta name=\"cover\" content=\"cover-image\"/>\n");
        sb.Append("  </metadata>\n");

        sb.Append("  <manifest>\n");
        sb.Append("    <item id=\"nav\" href=\"nav.xhtml\" media-type=\"application/xhtml+xml\" properties=\"nav\"/>\n");
        sb.Append("    <item id=\"titlepage\" href=\"titlepage.xhtml\" media-type=\"application/xhtml+xml\"/>\n");
        for (int i = 0; i < chapterCount; i++)
        {
            string n = (i + 1).ToString(CultureInfo.InvariantCulture);
            sb.Append("    <item id=\"chapter").Append(n).Append("\" href=\"chapter").Append(n).Append(".xhtml\" media-type=\"application/xhtml+xml\"/>\n");
        }
        if (cover is { } coverItem)
        {
            sb.Append("    <item id=\"cover-image\" href=\"").Append(coverItem.Href)
              .Append("\" media-type=\"").Append(coverItem.MediaType).Append("\" properties=\"cover-image\"/>\n");
        }
        sb.Append("  </manifest>\n");

        sb.Append("  <spine>\n");
        sb.Append("    <itemref idref=\"titlepage\"/>\n");
        for (int i = 0; i < chapterCount; i++)
            sb.Append("    <itemref idref=\"chapter").Append((i + 1).ToString(CultureInfo.InvariantCulture)).Append("\"/>\n");
        sb.Append("  </spine>\n");

        sb.Append("</package>\n");
        return sb.ToString();
    }

    /// <summary>OEBPS/nav.xhtml - the EPUB 3 required navigation document: a real XHTML file
    /// with a nav element of epub:type="toc" containing an ordered list of links, one per
    /// exported chapter (plus the title page).</summary>
    private static string BuildNavXhtml(string title, Book book, int chapterCount)
    {
        var sb = new StringBuilder();
        sb.Append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
        sb.Append("<!DOCTYPE html>\n");
        sb.Append("<html xmlns=\"").Append(XhtmlNamespace).Append("\" xmlns:epub=\"").Append(EpubOpsNamespace).Append("\">\n");
        sb.Append("<head>\n");
        sb.Append("  <title>").Append(EscapeXmlText(title)).Append(" - Table of Contents</title>\n");
        sb.Append("  <meta charset=\"utf-8\"/>\n");
        sb.Append("</head>\n");
        sb.Append("<body>\n");
        sb.Append("  <nav epub:type=\"toc\" id=\"toc\">\n");
        sb.Append("    <h1>Table of Contents</h1>\n");
        sb.Append("    <ol>\n");
        sb.Append("      <li><a href=\"titlepage.xhtml\">Title Page</a></li>\n");
        for (int i = 0; i < chapterCount; i++)
        {
            string label = EscapeXmlText(BuildChapterLabel(book.Outline.Chapters[i]));
            sb.Append("      <li><a href=\"chapter").Append((i + 1).ToString(CultureInfo.InvariantCulture)).Append(".xhtml\">").Append(label).Append("</a></li>\n");
        }
        sb.Append("    </ol>\n");
        sb.Append("  </nav>\n");
        sb.Append("</body>\n");
        sb.Append("</html>\n");
        return sb.ToString();
    }

    /// <summary>OEBPS/titlepage.xhtml - the book's title, its genre label, and its premise
    /// (split into real paragraphs the same way every chapter is).</summary>
    private static string BuildTitlePageXhtml(Book book, string title, int exportedChapterCount, BookStyleOptions style)
    {
        string genreLabel = BookGenreRules.DisplayName(book.Outline.Genre);
        List<string> premiseParagraphs = SplitIntoParagraphs(book.Outline.Premise);

        var sb = new StringBuilder();
        AppendXhtmlHead(sb, title, "Title Page", style);
        sb.Append("<body>\n");
        sb.Append("  <h1>").Append(EscapeXmlText(title)).Append("</h1>\n");
        sb.Append("  <p><em>").Append(EscapeXmlText(genreLabel)).Append("</em></p>\n");
        foreach (string paragraph in premiseParagraphs)
        {
            sb.Append("  <p>");
            AppendInlineRuns(sb, paragraph, exportedChapterCount);
            sb.Append("</p>\n");
        }
        sb.Append("</body>\n");
        sb.Append("</html>\n");
        return sb.ToString();
    }

    /// <summary>OEBPS/chapterN.xhtml - one chapter's heading plus its prose, split into real
    /// paragraph elements on blank-line boundaries (see <see cref="SplitIntoParagraphs"/>), with
    /// each paragraph's inline Markdown (links, bold, italic) rendered via
    /// <see cref="AppendInlineRuns"/>. <paramref name="exportedChapterCount"/> is how many
    /// chapters this EPUB actually contains: an internal <c>[text](chapter:N)</c> link whose N is
    /// outside that range has no file to point at and is rendered as plain text instead of a
    /// dead link.</summary>
    private static string BuildChapterXhtml(Book book, ChapterOutline chapterOutline, string chapterText, int exportedChapterCount, BookStyleOptions style)
    {
        string chapterLabel = BuildChapterLabel(chapterOutline);
        List<string> paragraphs = SplitIntoParagraphs(chapterText);

        var sb = new StringBuilder();
        AppendXhtmlHead(sb, book.Outline.Title, chapterLabel, style);
        sb.Append("<body>\n");
        sb.Append("  <h1>").Append(EscapeXmlText(chapterLabel)).Append("</h1>\n");
        foreach (string paragraph in paragraphs)
        {
            sb.Append("  <p>");
            AppendInlineRuns(sb, paragraph, exportedChapterCount);
            sb.Append("</p>\n");
        }
        sb.Append("</body>\n");
        sb.Append("</html>\n");
        return sb.ToString();
    }

    /// <summary>Renders one paragraph's <see cref="InlineMarkup"/> runs into an open
    /// <c>&lt;p&gt;</c>: plain text is XML-escaped, <c>**bold**</c>/<c>*italic*</c> become
    /// <c>&lt;strong&gt;</c>/<c>&lt;em&gt;</c>, an external link becomes
    /// <c>&lt;a href="https://..."&gt;</c>, and an internal <c>chapter:N</c> link becomes
    /// <c>&lt;a href="chapterN.xhtml"&gt;</c> - but only when chapter N is actually in this
    /// export (<paramref name="exportedChapterCount"/>); otherwise that run is emitted as plain
    /// styled text so the book never carries a link to a file that isn't there.</summary>
    private static void AppendInlineRuns(StringBuilder sb, string paragraph, int exportedChapterCount)
    {
        foreach (InlineRun run in InlineMarkup.Parse(paragraph))
        {
            string open = "", close = "";

            if (run.LinkKind == InlineLinkKind.External)
            {
                open = $"<a href=\"{EscapeXmlAttribute(run.LinkTarget)}\">";
                close = "</a>";
            }
            else if (run.LinkKind == InlineLinkKind.InternalChapter &&
                     int.TryParse(run.LinkTarget, out int n) && n >= 1 && n <= exportedChapterCount)
            {
                open = $"<a href=\"chapter{n}.xhtml\">";
                close = "</a>";
            }

            if (run.Bold) { open += "<strong>"; close = "</strong>" + close; }
            if (run.Italic) { open += "<em>"; close = "</em>" + close; }

            sb.Append(open).Append(EscapeXmlText(run.Text)).Append(close);
        }
    }

    /// <summary>Shared XML declaration/doctype/head opening every chapter and the title page
    /// use, so both always produce identically-shaped well-formed XHTML - a real xml
    /// declaration, the html element carrying the required XHTML namespace, and a plain
    /// HTML5-style doctype (the EPUB 3 Content Documents specification's own permitted, and in
    /// practice standard, XHTML5 doctype for EPUB 3 content - see this class's own uncertainties
    /// disclosure for how this compares to a literal XHTML 1.1 DOCTYPE declaration).</summary>
    private static void AppendXhtmlHead(StringBuilder sb, string bookTitle, string pageLabel, BookStyleOptions style)
    {
        sb.Append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
        sb.Append("<!DOCTYPE html>\n");
        sb.Append("<html xmlns=\"").Append(XhtmlNamespace).Append("\">\n");
        sb.Append("<head>\n");
        sb.Append("  <title>").Append(EscapeXmlText(bookTitle)).Append(" - ").Append(EscapeXmlText(pageLabel)).Append("</title>\n");
        sb.Append("  <meta charset=\"utf-8\"/>\n");
        AppendStyleBlock(sb, style);
        sb.Append("</head>\n");
    }

    /// <summary>Emits the &lt;style&gt; block carrying <see cref="BookStyleOptions"/>'s
    /// heading/body font family, bold, and color choices as plain CSS -- the EPUB equivalent of
    /// the Title/Heading1 styles (Word) and the heading/body span styling (PDF) elsewhere in this
    /// app. Font family names are reduced to letters/digits/spaces/hyphens before embedding (no
    /// escaping logic to get right, no way for a stray quote or angle bracket typed into a font
    /// name box to break out of the &lt;style&gt; text node or the surrounding XHTML) - color
    /// values are already pure hex digits by the time they reach here
    /// (<see cref="BookStyleOptions.NormalizeHex"/>), so need no further sanitizing.
    ///
    /// h1's font-weight is always stated explicitly (bold or normal), not merely omitted when
    /// not bold, because most reader/browser stylesheets already bold h1 by default -- an
    /// omitted declaration wouldn't actually turn heading bold off. Body's font-weight is only
    /// emitted when bold is requested, since normal is already every reader's own default.</summary>
    private static void AppendStyleBlock(StringBuilder sb, BookStyleOptions style)
    {
        string bodyFont = SanitizeFontFamilyForCss(style.BodyFontFamily);
        string headingFont = SanitizeFontFamilyForCss(style.HeadingFontFamily);
        string bodyColor = BookStyleOptions.NormalizeHex(style.BodyColor);
        string headingColor = BookStyleOptions.NormalizeHex(style.HeadingColor);

        sb.Append("  <style type=\"text/css\">\n");
        sb.Append("    body { font-family: '").Append(bodyFont).Append("', Georgia, serif; ");
        if (style.BodyBold) sb.Append("font-weight: bold; ");
        if (bodyColor.Length > 0) sb.Append("color: #").Append(bodyColor).Append("; ");
        sb.Append("}\n");
        sb.Append("    h1 { font-family: '").Append(headingFont).Append("', Georgia, serif; ");
        sb.Append("font-weight: ").Append(style.HeadingBold ? "bold" : "normal").Append("; ");
        if (headingColor.Length > 0) sb.Append("color: #").Append(headingColor).Append("; ");
        sb.Append("}\n");
        sb.Append("  </style>\n");
    }

    /// <summary>Keeps only letters/digits/spaces/hyphens from a user-typed font family name --
    /// see <see cref="AppendStyleBlock"/> for why this is simpler and safer than escaping.
    /// Falls back to "Georgia" for a blank/fully-stripped result so the CSS is never left with
    /// an empty font-family value.</summary>
    private static string SanitizeFontFamilyForCss(string? fontFamily)
    {
        if (string.IsNullOrWhiteSpace(fontFamily)) return "Georgia";

        var sb = new StringBuilder(fontFamily.Length);
        foreach (char c in fontFamily)
        {
            if (char.IsLetterOrDigit(c) || c is ' ' or '-') sb.Append(c);
        }

        string cleaned = sb.ToString().Trim();
        return cleaned.Length > 0 ? cleaned : "Georgia";
    }

    /// <summary>"Chapter N: Title", or just "Chapter N" when the outline entry has no title -
    /// used identically for the nav link text and the chapter file's own on-page heading, so
    /// both always agree.</summary>
    private static string BuildChapterLabel(ChapterOutline chapterOutline)
    {
        string chapterTitle = string.IsNullOrWhiteSpace(chapterOutline.Title) ? "" : chapterOutline.Title.Trim();
        // Appendix chapters keep their "Appendix: ..." title as the heading/nav label rather than
        // being prefixed with "Chapter N:", so the science-appendix sections read as appendices.
        if (BookGenreRules.LooksLikeAppendixChapter(chapterTitle))
            return chapterTitle;

        string number = chapterOutline.Number.ToString(CultureInfo.InvariantCulture);
        return chapterTitle.Length > 0 ? $"Chapter {number}: {chapterTitle}" : $"Chapter {number}";
    }

    // ==================== Text helpers ====================

    /// <summary>Splits raw chapter/premise prose into real paragraphs on blank-line (double
    /// newline, optionally with trailing whitespace on the blank line itself) boundaries, then
    /// collapses any remaining internal whitespace (single newlines, tabs, runs of spaces)
    /// within each paragraph down to single spaces. Text with no blank-line structure at all
    /// (no double-newline boundary anywhere) comes back as exactly one paragraph rather than
    /// this throwing or producing nothing; empty/whitespace-only input comes back as an empty
    /// list (the caller simply emits no &lt;p&gt; elements) rather than one hollow
    /// paragraph.</summary>
    private static List<string> SplitIntoParagraphs(string? text)
    {
        var result = new List<string>();
        if (string.IsNullOrWhiteSpace(text)) return result;

        string normalized = text.Replace("\r\n", "\n").Replace('\r', '\n');
        string[] rawBlocks = Regex.Split(normalized, @"\n[ \t]*\n+");

        foreach (string rawBlock in rawBlocks)
        {
            string collapsed = Regex.Replace(rawBlock.Trim(), @"\s+", " ");
            if (collapsed.Length > 0) result.Add(collapsed);
        }

        // Defensive fallback only - reachable in practice only if every "block" above somehow
        // collapsed to nothing despite the top IsNullOrWhiteSpace guard already passing.
        if (result.Count == 0)
        {
            string whole = Regex.Replace(normalized.Trim(), @"\s+", " ");
            if (whole.Length > 0) result.Add(whole);
        }

        return result;
    }

    /// <summary>Escapes '&amp;', '&lt;', and '&gt;' in one pass for safe placement inside an XML
    /// text node - '&amp;' first, so its own escape sequence is never re-escaped.</summary>
    private static string EscapeXmlText(string? text)
    {
        if (string.IsNullOrEmpty(text)) return "";

        var sb = new StringBuilder(text.Length + 16);
        foreach (char c in text)
        {
            switch (c)
            {
                case '&': sb.Append("&amp;"); break;
                case '<': sb.Append("&lt;"); break;
                case '>': sb.Append("&gt;"); break;
                default: sb.Append(c); break;
            }
        }
        return sb.ToString();
    }

    /// <summary>Escapes a string for use inside a double-quoted XML attribute value (an
    /// <c>href</c>): everything <see cref="EscapeXmlText"/> handles, plus <c>"</c>. Link targets
    /// reaching here have already been validated by <see cref="InlineMarkup"/> as
    /// <c>http(s)://</c> absolute URIs, so this is defence-in-depth for an odd character in a
    /// query string, not the primary scheme check.</summary>
    private static string EscapeXmlAttribute(string? text)
    {
        if (string.IsNullOrEmpty(text)) return "";

        var sb = new StringBuilder(text.Length + 16);
        foreach (char c in text)
        {
            switch (c)
            {
                case '&': sb.Append("&amp;"); break;
                case '<': sb.Append("&lt;"); break;
                case '>': sb.Append("&gt;"); break;
                case '"': sb.Append("&quot;"); break;
                default: sb.Append(c); break;
            }
        }
        return sb.ToString();
    }

    // ==================== Output-path plumbing (same pattern as ScriptDocumentExporter) ====================

    /// <summary>Validates outputPath, creates its parent directory if missing, and hands back a
    /// same-directory temp path to build the whole archive into first. Building next to the
    /// real target keeps the final File.Move a same-volume rename (atomic on every filesystem
    /// this app runs on) - a mid-write failure is caught before the move ever happens, so
    /// outputPath itself is never touched until the new .epub is fully, successfully
    /// written.</summary>
    private static string PrepareOutputPaths(string outputPath, out string tempPath)
    {
        tempPath = "";
        if (string.IsNullOrWhiteSpace(outputPath))
            return "No output path was supplied.";

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
            AppLog.Warning("BookEpubExporter could not prepare output path {Path}: {Error}", outputPath, ex.Message);
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
}

