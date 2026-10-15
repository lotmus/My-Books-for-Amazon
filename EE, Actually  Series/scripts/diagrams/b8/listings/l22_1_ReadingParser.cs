// Parse and validate one "t,h,p" line from the garden node. No I/O here, so it can be unit-tested.
using System.Globalization;

namespace GardenBench;

public readonly record struct Reading(double TempC, double HumidityPct, double PressureHPa);

public static class ReadingParser
{
    // BME280 operating ranges from the datasheet: -40..85 degC, 0..100 %RH, 300..1100 hPa.
    public static bool TryParse(string? line, out Reading reading, out string error)
    {
        reading = default;
        error = "";
        if (string.IsNullOrWhiteSpace(line)) { error = "empty line"; return false; }
        string[] f = line.Trim().Split(',');
        if (f.Length != 3) { error = $"expected 3 fields, got {f.Length}"; return false; }

        var inv = CultureInfo.InvariantCulture;      // "23.41" on every PC, German or not
        if (!double.TryParse(f[0], NumberStyles.Float, inv, out double t) ||
            !double.TryParse(f[1], NumberStyles.Float, inv, out double h) ||
            !double.TryParse(f[2], NumberStyles.Float, inv, out double p))
        { error = "not a number"; return false; }

        if (t is < -40 or > 85)    { error = $"temperature {t} out of range"; return false; }
        if (h is < 0 or > 100)     { error = $"humidity {h} out of range"; return false; }
        if (p is < 300 or > 1100)  { error = $"pressure {p} out of range"; return false; }

        reading = new Reading(t, h, p);
        return true;
    }
}
