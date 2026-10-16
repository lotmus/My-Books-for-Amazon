
namespace BookWriter.Engine;

/// <summary>
/// Orchestrates a full, fully-automatic book generation run: outline once, then every chapter
/// in order, with no per-chapter review checkpoint (per explicit instruction -- unlike
/// AiVideoPromptReviewDialog's per-segment review, this pipeline runs straight through). A
/// chapter that fails to generate (every provider tier failed) gets an honest placeholder
/// paragraph naming the real reason, rather than silently producing a shorter book or throwing
/// and losing every chapter already written -- the caller can see exactly which chapter(s), if
/// any, need a manual retry afterward by checking for that placeholder text.
/// </summary>
public sealed class BookWritingPipeline(
    string openAiApiKey, string anthropicApiKey = "", string geminiApiKey = "", string xaiApiKey = "",
    string yandexApiKey = "", string yandexFolderId = "")
{
    private readonly BookOutlineGenerator _outlineGenerator = new(openAiApiKey, anthropicApiKey, yandexApiKey, yandexFolderId);
    private readonly BookChapterGenerator _chapterGenerator = new(openAiApiKey, anthropicApiKey, geminiApiKey, xaiApiKey, yandexApiKey, yandexFolderId);

    /// <summary>Runs the whole pipeline: one outline call, then one chapter call per planned
    /// chapter, in order. Never throws for an ordinary provider failure on any single chapter --
    /// see this class's own doc comment for why a failed chapter becomes an honest placeholder
    /// instead of aborting the whole book.</summary>
    public async Task<Book> WriteAsync(string title, BookGenre genre, string premise, int chapterCount, IProgress<string>? progress = null, CancellationToken ct = default)
    {
        progress?.Report($"Planning outline for \"{title}\"...");
        BookOutline outline = await _outlineGenerator.GenerateAsync(title, genre, premise, chapterCount, ct);
        var book = new Book(outline);

        for (int i = 0; i < outline.Chapters.Count; i++)
        {
            ct.ThrowIfCancellationRequested();
            ChapterOutline chapterOutline = outline.Chapters[i];
            progress?.Report($"Writing chapter {chapterOutline.Number} of {outline.Chapters.Count}: \"{chapterOutline.Title}\"...");

            (string chapterText, string error) = await _chapterGenerator.GenerateChapterAsync(outline, i, ct);
            if (chapterText.Length > 0)
            {
                book.ChapterContents.Add(chapterText);
            }
            else
            {
                AppLog.Warning("BookWriter: chapter {Number} (\"{Title}\") failed to generate - {Error}", chapterOutline.Number, chapterOutline.Title, error);
                book.ChapterContents.Add(
                    $"[This chapter could not be generated: {error} You can retry it individually, or write it manually and replace this placeholder before exporting.]");
            }
        }

        progress?.Report($"Finished writing \"{title}\" ({book.ChapterContents.Count} chapter(s)).");
        return book;
    }
}
