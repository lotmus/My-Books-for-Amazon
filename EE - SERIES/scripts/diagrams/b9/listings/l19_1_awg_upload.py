"""Build a 1 us pulse with 10 ns raised-cosine edges, scale it to signed 16-bit DAC codes, and upload it
as an IEEE 488.2 definite-length binary block with its sample rate and amplitude.

SCPI in the Keysight 33600A style (1 GSa/s) (DATA:ARB:DAC, FUNC:ARB, FUNC:ARB:SRAT); other AWGs name these differently.
Run:  python l19_1_awg_upload.py --sim
"""
import argparse
import struct
import numpy as np

def pulse(srate=1e9, width=1e-6, edge=10e-9, period=2e-6):
    t = np.arange(int(round(period * srate))) / srate
    up = np.clip(t / edge, 0, 1); down = np.clip((width + edge - t) / edge, 0, 1)
    shape = np.minimum(up, down)
    return 0.5 - 0.5 * np.cos(np.pi * shape)             # raised-cosine edges, 0..1

def to_block(codes):
    """IEEE 488.2 block: '#', number of length digits, length, then little-endian int16 bytes."""
    payload = struct.pack('<%dh' % codes.size, *codes)
    n = str(len(payload))
    return b'#' + str(len(n)).encode() + n.encode() + payload

class SimAWG:
    def write_raw(self, data):
        head = data.split(b'#', 1)
        nd = int(head[1][:1]); length = int(head[1][1:1 + nd])
        body = head[1][1 + nd:1 + nd + length]
        assert len(body) == length and length % 2 == 0, 'bad block'
        print('SIM: received %d samples in a %d-byte block (header %r)' % (length // 2, length, head[0][:30]))
    def write(self, cmd):
        print('SIM:', cmd)
    def query(self, cmd):
        return 'SIM,AWG,0,1.0' if cmd == '*IDN?' else '+0,"No error"'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('resource', nargs='?')
    ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    awg = SimAWG() if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    print(awg.query('*IDN?'))
    w = pulse()
    codes = np.round((w * 2 - 1) * 32767).astype('<i2')  # 0..1 -> -32767..+32767
    awg.write('DATA:VOL:CLE')
    awg.write_raw(b'DATA:ARB:DAC PULSE1,' + to_block(codes) + b'\n')
    for cmd in ('FUNC ARB', 'FUNC:ARB PULSE1', 'FUNC:ARB:SRAT 1E9', 'VOLT:LOW 0', 'VOLT:HIGH 3.3', 'OUTP:LOAD INF', 'OUTP ON'):
        awg.write(cmd)
    print(awg.query('SYST:ERR?'))
    print('%d points: %.0f ns per point, edge %d points' % (codes.size, 1.0, 10))

if __name__ == '__main__':
    main()
