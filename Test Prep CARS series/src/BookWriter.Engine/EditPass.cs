namespace BookWriter.Engine;

/// <summary>
/// One kind of editorial improvement <see cref="BookChapterEditor"/> can apply to a chapter.
/// A single <see cref="BookChapterEditor.EditChapterAsync"/> call carries every selected pass
/// at once -- they are listed together in one prompt rather than run as separate AI calls, so
/// a 3-pass edit of one chapter is one provider call, not three (same cost/failure-surface
/// reasoning as BookChapterGenerator passing the whole outline in one call rather than a
/// per-chapter running summary).
/// </summary>
public enum EditPass
{
    /// <summary>Spelling, grammar, punctuation, tense/agreement slips, internal continuity
    /// errors (a detail that contradicts earlier in the same chapter or the chapter list) and
    /// plainly wrong facts -- the "is this correct" pass. Does not rewrite for style.</summary>
    Bugs,

    /// <summary>Sharpen, and sparingly add, wit and comic timing where it already suits the
    /// voice -- never forced into a beat that needs to stay serious.</summary>
    Humor,

    /// <summary>Scrutinise every scientific, technical, medical or historical claim: correct
    /// what is wrong, make vague hand-waving precise, without turning prose into a lecture or
    /// inventing citations.</summary>
    Science,

    /// <summary>Add genuinely useful links in Markdown syntax: internal cross-references to
    /// other chapters of this same book (<c>[text](chapter:N)</c>) and external links to
    /// stable, authoritative sources (<c>[text](https://...)</c>). See
    /// <see cref="BookChapterEditor"/>'s prompt for the exact contract and the "don't
    /// over-link / don't guess URLs" rules.</summary>
    Hyperlinks,

    /// <summary>Pacing, tension, hooks, stronger openings and closings, show-don't-tell,
    /// trimming filler -- the "is this compelling" pass. Preserves every plot event and the
    /// author's voice.</summary>
    Storytelling,
}

/// <summary>Display names and prompt fragments for each <see cref="EditPass"/>, kept next to
/// the enum rather than scattered through the UI and the editor so a pass's user-facing label
/// and the instruction the model actually receives always change together.</summary>
public static class EditPassInfo
{
    /// <summary>Every pass, in the order they are shown in the UI and listed in the prompt.</summary>
    public static IReadOnlyList<EditPass> All { get; } = new[]
    {
        EditPass.Bugs, EditPass.Humor, EditPass.Science, EditPass.Hyperlinks, EditPass.Storytelling,
    };

    public static string DisplayName(EditPass pass) => pass switch
    {
        EditPass.Bugs => "Bugs & errors",
        EditPass.Humor => "Humor",
        EditPass.Science => "Science accuracy",
        EditPass.Hyperlinks => "Hyperlinks",
        EditPass.Storytelling => "Storytelling",
        _ => pass.ToString(),
    };

    public static string Description(EditPass pass) => pass switch
    {
        EditPass.Bugs => "Typos, grammar, punctuation, continuity slips and wrong facts.",
        EditPass.Humor => "Sharpen wit and comic timing where it fits the voice.",
        EditPass.Science => "Check and correct every scientific or technical claim.",
        EditPass.Hyperlinks => "Add internal chapter cross-references and external source links.",
        EditPass.Storytelling => "Pacing, tension, hooks, show-don't-tell, cut filler.",
        _ => "",
    };

    /// <summary>The instruction line added to the editor prompt for this pass.</summary>
    public static string PromptInstruction(EditPass pass) => pass switch
    {
        EditPass.Bugs =>
            "BUGS & ERRORS: Fix spelling, grammar, punctuation and word-choice mistakes. Fix "
            + "internal continuity slips (details that contradict earlier in THIS chapter or the "
            + "chapter list above) and plainly incorrect facts. Under this pass do not rewrite "
            + "sentences purely for style.",
        EditPass.Humor =>
            "HUMOR: Where it fits the established voice and does not undercut the scene's "
            + "purpose, sharpen existing wit and comic timing and add the occasional light "
            + "touch. Do not force jokes into beats that need to land seriously.",
        EditPass.Science =>
            "SCIENCE ACCURACY: Scrutinise every scientific, technical, medical or historical "
            + "claim. Correct anything inaccurate and make vague or hand-wavy statements "
            + "precise. Keep it readable prose -- no lecturing, and never invent a citation or "
            + "a statistic.",
        EditPass.Hyperlinks =>
            "HYPERLINKS: Add genuinely useful links using Markdown link syntax ONLY. For a "
            + "reference to another chapter of this book, write the linked phrase as "
            + "[text](chapter:N) where N is that chapter's number from the list above. For an "
            + "external source, write [text](https://...), and only for well-known, stable, "
            + "authoritative pages (Wikipedia articles, official organisation sites, DOI "
            + "links). If you are not certain a URL is real and durable, do not add it. Do not "
            + "over-link: at most a few high-value links in the whole chapter, and never link "
            + "the same target twice.",
        EditPass.Storytelling =>
            "STORYTELLING: Improve momentum -- tighten slack passages, strengthen the opening "
            + "hook and the final line, turn tell-y summary into shown action or dialogue where "
            + "it matters, and cut filler. Preserve every plot event, fact and the author's "
            + "voice; this is a sharpening pass, not a rewrite.",
        _ => "",
    };
}
