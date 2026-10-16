using System.Text;

namespace BookWriter.Engine;

/// <summary>
/// The ONE correct way to embed arbitrary user text into an ffmpeg drawtext filter's "text"
/// option. Ported verbatim from MediaStar.GPT's own MediaMaker.Core.DrawtextEscaping when Book
/// Writer was spun out into its own standalone app -- this logic is empirically verified against
/// real ffmpeg output (see rules below), not derived from ffmpeg's own documentation, which gets
/// several of these wrong for this specific parser build.
///
/// EMPIRICALLY VERIFIED RULES (tested against a real bundled ffmpeg 6.0-essentials build by
/// rendering real PNGs and reading the pixels back):
///
///  - '%' must be left COMPLETELY UNESCAPED, and the filter must carry ":expansion=none".
///    Doubling it or backslash-escaping it both make drawtext's parser drop the ENTIRE overlay
///    silently: exit 0, "Stray % near ..." on stderr, output byte-identical to a render with no
///    overlay at all.
///  - ':' MUST still be backslash-escaped ("\:") even though the whole value is wrapped in
///    single quotes below -- this build's key=value tokenizer still treats an unescaped ':' as
///    the option-list separator even inside single quotes, silently truncating the text there.
///  - '\' must be doubled ("\\") so a raw backslash round-trips as one literal backslash.
///  - An embedded single quote can NOT be represented by any backslash escape sequence on this
///    build -- substitute a typographic right single quotation mark (U+2019) instead.
///  - An embedded double quote breaks the OUTER Win32 command-line double-quoted argument the
///    whole filter string is wrapped in -- substitute a typographic right double quotation mark
///    (U+201D), same reasoning as the single-quote case.
///  - ',' ';' '[' ']' '&amp;' need NO escaping inside the single-quoted value.
/// </summary>
public static class DrawtextEscaping
{
    /// <summary>The clause every drawtext filter using <see cref="TextClause"/> must carry
    /// alongside it (TextClause already appends this) -- disables drawtext's own %{...}/strftime
    /// text expansion so a bare '%' in the escaped text is just a printable character.</summary>
    public const string ExpansionNoneClause = "expansion=none";

    /// <summary>Returns the complete, safe "text='&lt;escaped&gt;':expansion=none" fragment for
    /// a drawtext filter. Collapses embedded CR/LF to a single space first.</summary>
    public static string TextClause(string text)
    {
        string oneLine = (text ?? "").Replace("\r\n", " ").Replace('\r', ' ').Replace('\n', ' ');
        return "text='" + EscapeText(oneLine) + "':" + ExpansionNoneClause;
    }

    /// <summary>Escapes/substitutes one drawtext text value per-character in a single pass
    /// (order-independent, unlike sequential String.Replace calls where an earlier escape's own
    /// backslash could get re-escaped by a later one).</summary>
    public static string EscapeText(string? text)
    {
        text ??= "";
        var sb = new StringBuilder(text.Length + 8);
        foreach (char c in text)
        {
            switch (c)
            {
                case '\\': sb.Append("\\\\"); break;
                case ':': sb.Append("\\:"); break;
                case '\'': sb.Append('’'); break; // typographic right single quote
                case '"': sb.Append('”'); break; // typographic right double quote
                // '%' is intentionally left unescaped -- see class doc comment. Requires the
                // caller's filter to also carry ":expansion=none" (TextClause adds it).
                default: sb.Append(c); break;
            }
        }
        return sb.ToString();
    }
}
