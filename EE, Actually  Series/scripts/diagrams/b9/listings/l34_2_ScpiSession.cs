// A SCPI session in C#: the same pattern as Listing 34.1 (error queue, *OPC?, binary blocks, safe exit).
// IScpiIo hides the transport. With a vendor VISA installed, wrap IVI VISA.NET:
//   var s = (Ivi.Visa.IMessageBasedSession)Ivi.Visa.GlobalResourceManager.Open("TCPIP0::192.168.1.50::hislip0::INSTR");
//   Write -> s.RawIO.Write(cmd + "\n");  ReadLine -> s.RawIO.ReadString();  ReadBytes -> s.RawIO.Read()
// The simulated DMM below lets the logic run anywhere:  dotnet run
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Text;

public interface IScpiIo : IDisposable
{
    void Write(string cmd);
    string ReadLine();
    byte[] ReadBytes();
}

public sealed class ScpiException : Exception
{
    public ScpiException(string msg) : base(msg) { }
}

public sealed class ScpiSession : IDisposable
{
    private readonly IScpiIo io;
    public string Idn { get; }

    public ScpiSession(IScpiIo io)
    {
        this.io = io;
        Idn = Query("*IDN?");
    }

    public string Query(string cmd) { io.Write(cmd); return io.ReadLine().Trim(); }

    public void CheckErrors(string where)
    {
        var errs = new List<string>();
        for (int i = 0; i < 20; i++)
        {
            string e = Query("SYST:ERR?");
            if (e.StartsWith("0") || e.StartsWith("+0")) break;
            errs.Add(e);
        }
        if (errs.Count > 0) throw new ScpiException(where + ": " + string.Join("; ", errs));
    }

    public void Configure(string where, params string[] cmds)
    {
        foreach (var c in cmds) io.Write(c);
        Query("*OPC?");
        CheckErrors(where);
    }

    public float[] ReadBlock(string cmd)
    {
        io.Write(cmd);
        byte[] raw = io.ReadBytes();
        if (raw.Length < 2 || raw[0] != (byte)'#') throw new ScpiException("not a binary block");
        int n = raw[1] - '0';
        int size = int.Parse(Encoding.ASCII.GetString(raw, 2, n), CultureInfo.InvariantCulture);
        if (raw.Length < 2 + n + size) throw new ScpiException("block short");
        var vals = new float[size / 4];
        for (int k = 0; k < vals.Length; k++)
            vals[k] = BitConverter.ToSingle(raw, 2 + n + 4 * k);     // little-endian, as set by FORM:BORD SWAP
        return vals;
    }

    public void Dispose()
    {
        try { io.Write("OUTP OFF"); }                                // leave the bench safe
        finally { io.Dispose(); }
    }
}

public sealed class SimDmm : IScpiIo
{
    private readonly Queue<string> errors = new Queue<string>();
    private string reply = "";
    private byte[] block = new byte[0];
    private int count = 5;
    private static readonly HashSet<string> Known = new HashSet<string>
        { "*RST", "*CLS", "CONF:VOLT:DC", "VOLT:DC:NPLC", "SAMP:COUN", "FORM", "FORM:BORD", "OUTP" };

    public void Write(string cmd)
    {
        string head = cmd.Split(' ')[0].ToUpperInvariant();
        switch (head)
        {
            case "*IDN?": reply = "SIM,DMM,0,1.0"; return;
            case "*OPC?": reply = "1"; return;
            case "SYST:ERR?": reply = errors.Count > 0 ? errors.Dequeue() : "+0,\"No error\""; return;
            case "FETC?":
                var data = new byte[4 * count];
                for (int k = 0; k < count; k++) BitConverter.GetBytes(1.0f + 1e-5f * k).CopyTo(data, 4 * k);
                string len = data.Length.ToString(CultureInfo.InvariantCulture);
                var head2 = Encoding.ASCII.GetBytes("#" + len.Length + len);
                block = new byte[head2.Length + data.Length];
                head2.CopyTo(block, 0); data.CopyTo(block, head2.Length);
                return;
        }
        if (head == "SAMP:COUN") count = int.Parse(cmd.Split(' ')[1], CultureInfo.InvariantCulture);
        if (!Known.Contains(head)) errors.Enqueue("-113,\"Undefined header;" + head + "\"");
    }

    public string ReadLine() => reply;
    public byte[] ReadBytes() => block;
    public void Dispose() { }
}

public static class Program
{
    public static int Main()
    {
        using (var s = new ScpiSession(new SimDmm()))
        {
            Console.WriteLine(s.Idn);
            s.Configure("DMM setup", "*RST", "*CLS", "CONF:VOLT:DC 10", "VOLT:DC:NPLC 10", "SAMP:COUN 5",
                        "FORM REAL,32", "FORM:BORD SWAP");
            float[] v = s.ReadBlock("FETC?");
            Console.WriteLine(v.Length + " readings: " + string.Join(", ",
                Array.ConvertAll(v, x => x.ToString("F5", CultureInfo.InvariantCulture))));
            try { s.Configure("typo test", "VOLT:DC:RANG:AUTOO ON"); }
            catch (ScpiException e) { Console.WriteLine("caught: " + e.Message); }
            return v.Length == 5 ? 0 : 1;
        }
    }
}
