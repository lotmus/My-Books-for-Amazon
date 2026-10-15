"""Regression check for the legacy Touchstone 1.x parser's format and unit paths.

Uses only the standard library and the included ATF-54143 sample. It writes
temporary equivalent files in MA, DB, and RI form with four frequency units
and 50/75-ohm references, then confirms that parsing recovers the original
S-parameters and noise rows.
"""
import cmath
import math
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from touchstone_atf import read_s2p

SAMPLE = HERE / 'ATF-54143_3V_60mA.s2p'
SCALE = {'HZ': 1.0, 'KHZ': 1e3, 'MHZ': 1e6, 'GHZ': 1e9}
FORMATS = ('MA', 'DB', 'RI')
REFERENCES = (50.0, 75.0)
TOL = 1e-11


def encode(value, form):
    if form == 'MA':
        return abs(value), math.degrees(cmath.phase(value))
    if form == 'DB':
        return 20 * math.log10(abs(value)), math.degrees(cmath.phase(value))
    return value.real, value.imag


def near(a, b, label):
    if abs(a - b) > TOL:
        raise AssertionError(f'{label}: {a!r} != {b!r}')


def main():
    source_s, source_noise, z0 = read_s2p(SAMPLE)
    if z0 != 50.0:
        raise AssertionError(f'expected 50 ohms, got {z0}')

    row_2g = next(row for row in source_s if abs(row[0] - 2e9) < 1)
    expected = (
        cmath.rect(0.62, math.radians(-168.3)),
        cmath.rect(7.31, math.radians(73.3)),
        cmath.rect(0.06, math.radians(33.3)),
        cmath.rect(0.17, math.radians(-117.0)),
    )
    for got, want in zip(row_2g[1:], expected):
        near(got, want, '2 GHz reference S-parameter')
    noise_2g = next(row for row in source_noise if abs(row[0] - 2e9) < 1)
    near(noise_2g[1], 0.45, '2 GHz NFmin')
    near(noise_2g[2], cmath.rect(0.27, math.radians(120.1)), '2 GHz Gamma-opt')
    near(noise_2g[3], 2.0, '2 GHz Rn')

    cases = 0
    with tempfile.TemporaryDirectory(prefix='b4_touchstone_') as temp:
        for unit, scale in SCALE.items():
            for form in FORMATS:
                for ref in REFERENCES:
                    path = Path(temp) / f'{unit}_{form}_{ref:g}.s2p'
                    lines = [f'# {unit} S {form} R {ref:g}']
                    for frequency, s11, s21, s12, s22 in source_s:
                        values = [frequency / scale]
                        for value in (s11, s21, s12, s22):
                            values.extend(encode(value, form))
                        lines.append(' '.join(f'{value:.14g}' for value in values))
                    for frequency, nfmin, gamma_opt, rn in source_noise:
                        lines.append(' '.join(f'{value:.14g}' for value in (
                            frequency / scale, nfmin, abs(gamma_opt),
                            math.degrees(cmath.phase(gamma_opt)), rn / ref)))
                    path.write_text('\n'.join(lines) + '\n', encoding='ascii')

                    got_s, got_noise, got_z0 = read_s2p(path)
                    if len(got_s) != len(source_s) or len(got_noise) != len(source_noise):
                        raise AssertionError(f'{unit}/{form}/R{ref:g}: row count changed')
                    near(got_z0, ref, f'{unit}/{form}/R{ref:g} reference impedance')
                    for got, want in zip(got_s, source_s):
                        near(got[0], want[0], f'{unit}/{form}/R{ref:g} S frequency')
                        for a, b in zip(got[1:], want[1:]):
                            near(a, b, f'{unit}/{form}/R{ref:g} S value')
                    for got, want in zip(got_noise, source_noise):
                        near(got[0], want[0], f'{unit}/{form}/R{ref:g} noise frequency')
                        near(got[1], want[1], f'{unit}/{form}/R{ref:g} NFmin')
                        near(got[2], want[2], f'{unit}/{form}/R{ref:g} Gamma-opt')
                        near(got[3], want[3], f'{unit}/{form}/R{ref:g} Rn')
                    cases += 1

    print(f'{cases} format/unit combinations passed; 2 GHz reference values verified')


if __name__ == '__main__':
    main()
