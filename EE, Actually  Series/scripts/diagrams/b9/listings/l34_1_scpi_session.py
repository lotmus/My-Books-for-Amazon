"""A robust SCPI session in Python: identify, reset, check the error queue after every configuration
block, synchronize with *OPC?, read IEEE 488.2 binary blocks, and always leave the instrument safe.

Works with any PyVISA resource (pip install pyvisa pyvisa-py; or a vendor VISA). The simulated DMM below
implements just enough SCPI to run the logic. Run:  python l34_1_scpi_session.py --sim
"""
import argparse
import struct
import time

class ScpiError(RuntimeError):
    pass

class Session:
    def __init__(self, inst, timeout_ms=5000):
        self.inst = inst
        self.inst.timeout = timeout_ms
        self.idn = self.query('*IDN?').strip()

    def write(self, cmd):
        self.inst.write(cmd)

    def query(self, cmd):
        return self.inst.query(cmd)

    def check(self, where=''):
        """Drain the error queue; raise if anything is in it (SYST:ERR? returns 0,"No error" when empty)."""
        errs = []
        for _ in range(20):
            e = self.query('SYST:ERR?').strip()
            if e.startswith('0') or e.startswith('+0'):
                break
            errs.append(e)
        if errs:
            raise ScpiError('%s: %s' % (where, '; '.join(errs)))

    def configure(self, *cmds, where='configure'):
        for c in cmds:
            self.write(c)
        self.query('*OPC?')                                            # wait until all are executed
        self.check(where)

    def read_block(self, cmd):
        """Query that returns a definite-length binary block #<n><len><data> of little-endian float32."""
        self.inst.write(cmd)
        raw = self.inst.read_raw()
        if raw[:1] != b'#':
            raise ScpiError('not a binary block: %r' % raw[:12])
        n = int(raw[1:2]); size = int(raw[2:2 + n]); data = raw[2 + n: 2 + n + size]
        if len(data) != size:
            raise ScpiError('block short: %d of %d bytes' % (len(data), size))
        return list(struct.unpack('<%df' % (size // 4), data))

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        try:
            self.write('OUTP OFF')                                       # leave the bench safe, even after an error
        finally:
            self.inst.close()

class SimDMM:
    """Enough SCPI to exercise Session: an error queue, *OPC?, and a binary trace of readings."""
    def __init__(self):
        self.errors, self.n, self.timeout, self.pending = [], 5, None, b''
    def write(self, cmd):
        head = cmd.split()[0].upper()
        if head == 'SAMP:COUN':
            self.n = int(cmd.split()[1])
        elif head == 'FETC?':
            vals = [1.0 + 1e-5 * k for k in range(self.n)]
            data = struct.pack('<%df' % self.n, *vals); ln = str(len(data))
            self.pending = b'#' + str(len(ln)).encode() + ln.encode() + data + b'\n'
        elif head not in ('*RST', '*CLS', 'CONF:VOLT:DC', 'VOLT:DC:NPLC', 'OUTP', 'FORM', 'FORM:BORD'):
            self.errors.append('-113,"Undefined header;%s"' % head)
    def query(self, cmd):
        if cmd == '*IDN?': return 'SIM,DMM,0,1.0\n'
        if cmd == '*OPC?': return '1\n'
        if cmd == 'SYST:ERR?': return (self.errors.pop(0) if self.errors else '+0,"No error"') + '\n'
        self.write(cmd); return '\n'
    def read_raw(self):
        return self.pending
    def close(self):
        pass

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('resource', nargs='?'); ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    inst = SimDMM() if a.sim else __import__('pyvisa').ResourceManager().open_resource(a.resource)
    with Session(inst) as s:
        print(s.idn)
        s.configure('*RST', '*CLS', 'CONF:VOLT:DC 10', 'VOLT:DC:NPLC 10', 'SAMP:COUN 5',
                    'FORM REAL,32', 'FORM:BORD SWAP', where='DMM setup')
        t0 = time.perf_counter(); vals = s.read_block('FETC?')              # FORM REAL,32 makes FETC? return a binary block
        print('%d readings in %.1f ms: %s' % (len(vals), 1e3 * (time.perf_counter() - t0), ', '.join('%.5f' % v for v in vals)))
        try:
            s.configure('VOLT:DC:RANG:AUTOO ON', where='typo test')     # deliberate typo: caught, not ignored
        except ScpiError as e:
            print('caught:', e)

if __name__ == '__main__':
    main()
