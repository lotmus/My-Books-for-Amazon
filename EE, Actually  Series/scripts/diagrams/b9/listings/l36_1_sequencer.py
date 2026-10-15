"""A minimal test executive: steps with guard-banded limits, one retest on failure, results and metadata
in SQLite, and the production statistics (first-pass yield, Cpk per step, and the failure Pareto).

Each step is a function returning a value; on a real station it calls the instruments (Listing 34.1).
Here a simulated regulator board stands in. Run:  python l36_1_sequencer.py [units]
"""
import math
import sqlite3
import statistics
import sys
import time
import uuid
import numpy as np

STEPS = [  # name, unit, lower, upper, guard band (measurement uncertainty, Chapter 2)
    ('vout', 'V', 3.201, 3.399, 0.010),
    ('ripple', 'mV', 0.0, 30.0, 1.0),
    ('eff', '%', 88.0, 100.0, 0.3),
]

class SimBoard:
    def __init__(self, rng):
        self.v = rng.normal(3.302, 0.022); self.r = abs(rng.normal(14, 4)); self.e = rng.normal(90.2, 0.9)
        self.rng = rng; self.contact_ok = rng.random() > 0.02     # 2 % of insertions: a bad pogo-pin contact
    def measure(self, name):                                   # repeatability noise on every reading
        n = self.rng.normal(0, 1)
        if name == 'vout' and not self.contact_ok:
            self.contact_ok = True                             # the retest reseats the contact
            return 0.0
        return {'vout': self.v + 0.004 * n, 'ripple': self.r + 0.5 * n, 'eff': self.e + 0.1 * n}[name]

def run_unit(db, run_id, serial, board):
    passed_all, first_pass = True, True
    for name, unit, lo, hi, gb in STEPS:
        for attempt in (1, 2):                                 # one retest: catches contact problems, not bad parts
            v = board.measure(name)
            ok = lo + gb <= v <= hi - gb
            db.execute('INSERT INTO result VALUES (?,?,?,?,?,?,?,?)', (run_id, serial, name, attempt, v, lo + gb, hi - gb, int(ok)))
            if ok:
                break
            first_pass = False
        passed_all &= ok
    return passed_all, first_pass

def cpk(values, lo, hi):
    m, s = statistics.mean(values), statistics.stdev(values)
    return min(hi - m, m - lo) / (3 * s)

def main(units=500):
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE run (run_id TEXT, station TEXT, sw_version TEXT, instruments TEXT, started REAL)')
    db.execute('CREATE TABLE result (run_id TEXT, serial TEXT, step TEXT, attempt INT, value REAL, lo REAL, hi REAL, pass INT)')
    run_id = str(uuid.uuid4())
    db.execute('INSERT INTO run VALUES (?,?,?,?,?)', (run_id, 'ST-07', 'seq 1.4.2', 'SIM,DMM,0,1.0', time.time()))
    rng = np.random.default_rng(36)
    final = fpy = 0
    for k in range(units):
        p, fp = run_unit(db, run_id, 'SN%06d' % k, SimBoard(rng))
        final += p; fpy += fp
    print('units %d: first-pass yield %.1f %%, final yield %.1f %%' % (units, 100 * fpy / units, 100 * final / units))
    for name, unit, lo, hi, gb in STEPS:
        vals = [r[0] for r in db.execute('SELECT value FROM result r WHERE step=? AND attempt=(SELECT MAX(attempt) FROM '
                                          'result WHERE serial=r.serial AND step=r.step)', (name,))]   # last attempt: no contact faults
        print('%-6s mean %8.4f %s  sd %.4f  Cpk %.2f (to spec limits)' % (name, statistics.mean(vals), unit, statistics.stdev(vals), cpk(vals, lo, hi)))
    pareto = db.execute('SELECT step, COUNT(DISTINCT serial) FROM result WHERE pass=0 GROUP BY step ORDER BY 2 DESC').fetchall()
    print('failures (any attempt) by step:', pareto)
    return db

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 500)
