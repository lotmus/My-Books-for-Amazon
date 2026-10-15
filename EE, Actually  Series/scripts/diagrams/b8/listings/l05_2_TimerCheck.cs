// Measure what a 10 ms System.Threading.Timer really delivers on this PC.
using System;
using System.Diagnostics;
using System.Threading;

class TimerCheck
{
    static void Main()
    {
        const int N = 200;
        var stamps = new double[N];
        int n = 0;
        var sw = Stopwatch.StartNew();
        using var done = new ManualResetEventSlim(false);
        using var timer = new Timer(_ =>
        {
            if (n < N) stamps[n++] = sw.Elapsed.TotalMilliseconds;
            if (n == N) done.Set();
        }, null, 0, 10);              // ask for one tick every 10 ms
        done.Wait();
        double mean = (stamps[N - 1] - stamps[0]) / (N - 1);
        Console.WriteLine($"requested 10.0 ms, measured mean {mean:F2} ms ({1000 / mean:F1} Hz)");
    }
}
