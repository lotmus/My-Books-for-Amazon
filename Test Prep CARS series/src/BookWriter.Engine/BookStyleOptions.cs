namespace BookWriter.Engine;

/// <summary>
/// Typography choices for an exported book, set independently for headings (the book title and
/// every chapter heading) and body prose. Threaded as an optional parameter through
/// <see cref="BookEpubExporter.ExportToEpub"/> and <see cref="BookDocumentExporter"/>'s Word and
/// PDF paths, so all three formats render the same choices consistently -- font family, bold,
/// and color, matching exactly the three things a user can set per role.
///
/// Every export method treats a missing (null) <see cref="BookStyleOptions"/> as
/// <see cref="Default"/>, which reproduces exactly what these exporters hard-coded before this
/// type existed (Georgia body text, bold headings, no color override) -- existing callers that
/// don't pass one keep behaving identically.
/// </summary>
public sealed class BookStyleOptions
{
    public string HeadingFontFamily { get; set; } = "Georgia";
    public bool HeadingBold { get; set; } = true;

    /// <summary>Bare hex ("1A2B3C" or "abc"), with or without a leading '#'. Empty means "no
    /// override -- use the reader/viewer's normal text color" rather than forcing black, since
    /// forcing black would fight a reader's own dark-mode/night theme.</summary>
    public string HeadingColor { get; set; } = "";

    public string BodyFontFamily { get; set; } = "Georgia";
    public bool BodyBold { get; set; }
    public string BodyColor { get; set; } = "";

    public static BookStyleOptions Default => new();

    /// <summary>The font-family fallback chain every exporter already hard-coded (Georgia, then
    /// Cambria, then Times New Roman) for whichever role is still left at the built-in "Georgia"
    /// default -- preserves that existing fallback quality unchanged. A font the user actually
    /// typed in gets used on its own: a browser/e-reader/Word's own font substitution already
    /// handles "not installed" sensibly, so a second-guessed fallback list for an arbitrary user
    /// font would just be guessing at what they wanted.</summary>
    private static readonly string[] GeorgiaFallbackChain = { "Georgia", "Cambria", "Times New Roman" };

    public string[] HeadingFontFamilyChain => FallbackChainFor(HeadingFontFamily);
    public string[] BodyFontFamilyChain => FallbackChainFor(BodyFontFamily);

    private static string[] FallbackChainFor(string fontFamily) =>
        string.IsNullOrWhiteSpace(fontFamily) || fontFamily.Equals("Georgia", StringComparison.OrdinalIgnoreCase)
            ? GeorgiaFallbackChain
            : new[] { fontFamily.Trim() };

    /// <summary>Normalizes a user-typed hex color ("1a2b3c", "#1A2B3C", "abc") to a bare 6-digit
    /// uppercase hex string with no '#', or "" if the input is blank or not a valid 3/6-digit
    /// hex value. Callers treat "" as "no override" rather than failing an entire export over a
    /// typo in a color box.</summary>
    public static string NormalizeHex(string? input)
    {
        if (string.IsNullOrWhiteSpace(input)) return "";

        string s = input.Trim().TrimStart('#');
        if (s.Length == 3 && s.All(Uri.IsHexDigit))
            s = string.Concat(s.Select(c => new string(c, 2)));

        return s.Length == 6 && s.All(Uri.IsHexDigit) ? s.ToUpperInvariant() : "";
    }
}
