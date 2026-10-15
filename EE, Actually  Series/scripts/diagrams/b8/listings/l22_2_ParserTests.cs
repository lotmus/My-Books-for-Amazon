// xUnit tests for ReadingParser: dotnet test runs them in about a second, no hardware needed.
using GardenBench;
using Xunit;

public class ReadingParserTests
{
    [Fact]
    public void ValidLine_IsParsed()
    {
        Assert.True(ReadingParser.TryParse("23.41,45.2,1013.25\r\n", out var r, out _));
        Assert.Equal(23.41, r.TempC, 3);
        Assert.Equal(45.2, r.HumidityPct, 3);
        Assert.Equal(1013.25, r.PressureHPa, 3);
    }

    [Theory]
    [InlineData("", "empty line")]
    [InlineData("23.41,45.2", "expected 3 fields, got 2")]
    [InlineData("23,41;45,2;1013,25", "expected 3 fields, got 4")]    // German decimal commas
    [InlineData("23.41,abc,1013.25", "not a number")]
    [InlineData("123.0,45.2,1013.25", "temperature 123 out of range")]
    [InlineData("23.41,45.2,0", "pressure 0 out of range")]
    public void BadLine_IsRejectedWithReason(string line, string expected)
    {
        Assert.False(ReadingParser.TryParse(line, out _, out string error));
        Assert.Equal(expected, error);
    }

    [Fact]
    public void ParsingDoesNotDependOnPcCulture()
    {
        var saved = System.Globalization.CultureInfo.CurrentCulture;
        try
        {
            System.Globalization.CultureInfo.CurrentCulture = new System.Globalization.CultureInfo("de-DE");
            Assert.True(ReadingParser.TryParse("23.41,45.2,1013.25", out var r, out _));
            Assert.Equal(23.41, r.TempC, 3);
        }
        finally { System.Globalization.CultureInfo.CurrentCulture = saved; }
    }
}
