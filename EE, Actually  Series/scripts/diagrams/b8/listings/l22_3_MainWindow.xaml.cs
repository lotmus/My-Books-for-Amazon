// WPF dashboard: serial data arrives on a worker thread and is handed to the UI thread.
using System;
using System.Collections.Generic;
using System.IO.Ports;
using System.Linq;
using System.Windows;
using System.Windows.Media;

namespace GardenBench;

public partial class MainWindow : Window
{
    private SerialPort? _port;
    private readonly Queue<double> _temps = new();
    private const int MaxPoints = 300;               // 5 minutes at one reading per second

    public MainWindow()
    {
        InitializeComponent();
        PortBox.ItemsSource = SerialPort.GetPortNames();
        PortBox.SelectedIndex = 0;
        Closed += (_, _) => _port?.Close();
    }

    private void Connect_Click(object sender, RoutedEventArgs e)
    {
        if (PortBox.SelectedItem is not string name) return;
        _port?.Close();
        _port = new SerialPort(name, 115200) { NewLine = "\r\n", ReadTimeout = 2000 };
        _port.DataReceived += OnData;                // raised on a thread-pool thread
        try { _port.Open(); StatusText.Text = $"connected to {name}"; }
        catch (Exception ex) { StatusText.Text = ex.Message; }
    }

    private void OnData(object sender, SerialDataReceivedEventArgs e)
    {
        var port = (SerialPort)sender;
        while (port.IsOpen && port.BytesToRead > 0)
        {
            string line;
            try { line = port.ReadLine(); } catch (TimeoutException) { return; }
            bool ok = ReadingParser.TryParse(line, out var r, out string error);
            // Never touch a control from this thread: queue the update on the UI thread.
            Dispatcher.BeginInvoke(() =>
            {
                if (ok) Show(r); else StatusText.Text = "bad line: " + error;
            });
        }
    }

    private void Show(Reading r)
    {
        ValueText.Text = $"{r.TempC:F2} °C   {r.HumidityPct:F1} %   {r.PressureHPa:F1} hPa";
        _temps.Enqueue(r.TempC);
        if (_temps.Count > MaxPoints) _temps.Dequeue();
        double lo = _temps.Min() - 0.5, hi = _temps.Max() + 0.5;
        double w = Plot.ActualWidth, h = Plot.ActualHeight;
        TempLine.Points = new PointCollection(_temps.Select((t, i) =>
            new Point(i * w / (MaxPoints - 1), h - (t - lo) / (hi - lo) * h)));
    }
}
