// .NET console app: read "t,h,p" lines from the ESP32-S3 and print them with checks.
// Project: dotnet new console; dotnet add package System.IO.Ports
using System;
using System.Globalization;
using System.IO.Ports;

class SerialConsole
{
    static void Main(string[] args)
    {
        string portName = args.Length > 0 ? args[0] : "COM5";
        using var port = new SerialPort(portName, 115200, Parity.None, 8, StopBits.One)
        {
            NewLine = "\r\n",
            ReadTimeout = 2000           // ms; never wait forever
        };
        port.Open();
        Console.WriteLine($"Listening on {portName}. Ctrl+C to stop.");
        while (true)
        {
            try
            {
                string line = port.ReadLine();
                string[] f = line.Split(',');
                if (f.Length == 3 &&
                    double.TryParse(f[0], NumberStyles.Float, CultureInfo.InvariantCulture, out double t) &&
                    double.TryParse(f[1], NumberStyles.Float, CultureInfo.InvariantCulture, out double h) &&
                    double.TryParse(f[2], NumberStyles.Float, CultureInfo.InvariantCulture, out double p))
                    Console.WriteLine($"{DateTime.Now:HH:mm:ss}  {t,6:F2} °C  {h,5:F1} %  {p,7:F2} hPa");
                else
                    Console.WriteLine($"bad line: {line}");
            }
            catch (TimeoutException)
            {
                Console.WriteLine("no data for 2 s - is the board running?");
            }
        }
    }
}
