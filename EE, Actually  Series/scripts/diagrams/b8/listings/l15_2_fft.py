"""Plan an FFT on the PC before writing it for the MCU: bin width, leakage, and the window."""
import numpy as np

FS = 10_000          # sample rate, Hz
N = 1024             # FFT length
F_TONE = 1000.0      # test tone, Hz

t = np.arange(N) / FS
x = np.sin(2 * np.pi * F_TONE * t)

print(f"bin width {FS / N:.2f} Hz, frame {N / FS * 1000:.1f} ms, tone at bin {F_TONE * N / FS:.1f}")
for name, w in (("rectangular", np.ones(N)), ("Hann", np.hanning(N))):
    spec = np.abs(np.fft.rfft(x * w))
    spec_db = 20 * np.log10(spec / spec.max() + 1e-12)
    far = spec_db[int(1500 * N / FS):]           # everything above 1.5 kHz
    print(f"{name:12s} peak at {np.argmax(spec) * FS / N:7.1f} Hz, leakage above 1.5 kHz {far.max():6.1f} dB")
