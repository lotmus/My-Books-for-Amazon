// Compile-check stub for System.IO.Ports (the NuGet package is not in the offline cache).
// Only the members the listings use; signatures follow the real API.
namespace System.IO.Ports
{
    public enum Parity { None, Odd, Even, Mark, Space }
    public enum StopBits { None, One, Two, OnePointFive }
    public enum SerialData { Chars = 1, Eof = 2 }
    public class SerialDataReceivedEventArgs : EventArgs { public SerialData EventType => SerialData.Chars; }
    public delegate void SerialDataReceivedEventHandler(object sender, SerialDataReceivedEventArgs e);
    public class SerialPort : IDisposable
    {
        public SerialPort() { }
        public SerialPort(string portName, int baudRate) { }
        public SerialPort(string portName, int baudRate, Parity parity, int dataBits, StopBits stopBits) { }
        public string NewLine { get; set; } = "\n";
        public int ReadTimeout { get; set; } = -1;
        public int WriteTimeout { get; set; } = -1;
        public int ReadBufferSize { get; set; } = 4096;
        public bool IsOpen => false;
        public int BytesToRead => 0;
        public bool DtrEnable { get; set; }
        public event SerialDataReceivedEventHandler? DataReceived { add { } remove { } }
        public static string[] GetPortNames() => Array.Empty<string>();
        public void Open() { }
        public void Close() { }
        public string ReadLine() => throw new TimeoutException();
        public string ReadExisting() => "";
        public void WriteLine(string text) { }
        public void Write(string text) { }
        public void DiscardInBuffer() { }
        public void Dispose() { }
    }
}
