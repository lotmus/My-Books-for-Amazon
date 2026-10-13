// Test the test bench itself with fake instruments: no board, no DMM, runs in CI.
using System.Linq;
using GardenBench;
using Xunit;

class FakeDmm : IDmm { public double V; public double ReadVoltage() => V; }
class FakeDut : IDut { public string SerialNumber => "GN-0001"; public string? Line; public string? ReadLine() => Line; }

public class TestBenchTests
{
    [Theory]
    [InlineData(3.30, true)]
    [InlineData(3.205, true)]      // just above the low limit 3.201
    [InlineData(3.19, false)]
    [InlineData(3.41, false)]
    public void RailLimits(double volts, bool pass)
    {
        var bench = new TestBench(new FakeDmm { V = volts }, new FakeDut { Line = "23.41,45.2,1013.25" });
        Assert.Equal(pass, bench.Run().Single(s => s.Name == "3V3 rail").Pass);
    }

    [Fact]
    public void SilentSensor_FailsAndSkipsTemperature()
    {
        var steps = new TestBench(new FakeDmm { V = 3.30 }, new FakeDut { Line = null }).Run();
        Assert.False(steps.Single(s => s.Name == "sensor answers").Pass);
        Assert.DoesNotContain(steps, s => s.Name == "room temperature");
    }
}
