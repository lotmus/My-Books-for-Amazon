// A small .NET class library for LabVIEW (Constructor, Property, and Invoke Nodes) and for
// TestStand's .NET adapter: guard-banded limits with a log line that does not depend on the PC culture.
// Plain C# 7.3, so it builds for .NET Framework 4.x hosts as well as for .NET 8.
using System;
using System.Globalization;

namespace BenchLimits
{
    public sealed class LimitCheck
    {
        public LimitCheck(string name, double low, double high, double uncertainty)
        {
            if (low > high) throw new ArgumentException("low limit above high limit");
            if (uncertainty < 0 || 2 * uncertainty >= high - low)
                throw new ArgumentException("uncertainty leaves no test window");
            Name = name;
            TestLow = low + uncertainty;     // guard band: shrink the window on both sides
            TestHigh = high - uncertainty;
        }

        public string Name { get; private set; }
        public double TestLow { get; private set; }
        public double TestHigh { get; private set; }

        public bool Passes(double measured)
        {
            return !double.IsNaN(measured) && measured >= TestLow && measured <= TestHigh;
        }

        public string LogLine(string serial, double measured)
        {
            return string.Format(CultureInfo.InvariantCulture, "{0},{1},{2:G6},{3:G6},{4:G6},{5}",
                serial, Name, measured, TestLow, TestHigh, Passes(measured) ? "PASS" : "FAIL");
        }
    }
}
