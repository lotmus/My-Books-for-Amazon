// Production test: check the 3.3 V rail and the sensor of each garden-node board, log pass/fail.
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;

namespace GardenBench;

public interface IDmm { double ReadVoltage(); }                 // real: SCPI over USB; tests: a fake
public interface IDut { string SerialNumber { get; } string? ReadLine(); }

public record StepResult(string Name, double Value, double Low, double High)
{
    public bool Pass => Value >= Low && Value <= High;
}

public class TestBench
{
    private readonly IDmm _dmm;
    private readonly IDut _dut;
    public TestBench(IDmm dmm, IDut dut) { _dmm = dmm; _dut = dut; }

    public List<StepResult> Run()
    {
        var results = new List<StepResult>();
        const double nominal = 3.30, tol = 0.03;                  // 3.30 V +-3 %
        results.Add(new StepResult("3V3 rail", _dmm.ReadVoltage(), nominal * (1 - tol), nominal * (1 + tol)));

        bool ok = ReadingParser.TryParse(_dut.ReadLine(), out var r, out _);
        results.Add(new StepResult("sensor answers", ok ? 1 : 0, 1, 1));
        if (ok) results.Add(new StepResult("room temperature", r.TempC, 15, 35));
        return results;
    }

    public static void Log(string path, string serial, IEnumerable<StepResult> steps)
    {
        using var w = new StreamWriter(path, append: true);
        string stamp = DateTime.UtcNow.ToString("yyyy-MM-ddTHH:mm:ssZ", CultureInfo.InvariantCulture);
        foreach (var s in steps)
            w.WriteLine(string.Join(",", stamp, serial, s.Name,
                s.Value.ToString("F3", CultureInfo.InvariantCulture),
                s.Low.ToString("F3", CultureInfo.InvariantCulture),
                s.High.ToString("F3", CultureInfo.InvariantCulture), s.Pass ? "PASS" : "FAIL"));
    }
}
