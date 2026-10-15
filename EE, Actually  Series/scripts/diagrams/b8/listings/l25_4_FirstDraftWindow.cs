// The assistant's first C# answer for the dashboard, before review. It compiles and runs on the
// developer's English-language PC. Find the two bugs before reading on.
using System.IO.Ports;
using System.Windows;
using System.Windows.Controls;

namespace GardenBench;

public class FirstDraftWindow : Window
{
    private readonly TextBlock _value = new() { FontSize = 28 };
    private readonly SerialPort _port = new("COM5", 115200);

    public FirstDraftWindow()
    {
        Content = _value;
        _port.DataReceived += (s, e) =>
        {
            string[] f = _port.ReadLine().Split(',');
            double t = double.Parse(f[0]);
            _value.Text = $"{t:F2} °C";
        };
        _port.Open();
    }
}
