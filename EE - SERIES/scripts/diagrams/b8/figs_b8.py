"""Figures for Book 8, Firmware and Software for Electronics.

Every figure is computed or drawn here from the numbers in the worked examples; CHECK lines
print the values that the captions quote. Run: python figs_b8.py [name ...]  (output in ./fig)
Style: the series' eestyle helpers (imported read-only), 800 px wide, 64-color PNG.
"""
import math
import os
import sys

import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'common'))   # series helpers, read-only
sys.path.insert(0, HERE)
from eestyle import BLUE, RED, GREEN, GRAY, ORANGE, INK, fig, save, plt   # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle  # noqa: E402

OUT = os.path.join(HERE, 'fig')
os.makedirs(OUT, exist_ok=True)
LIGHT = {'blue': '#dce8f5', 'green': '#dff0e5', 'orange': '#f8e6d2', 'gray': '#eeeeee', 'red': '#f6d9d5'}
FIGS = {}

def figure(fn):
    FIGS[fn.__name__] = fn
    return fn

def check(msg, cond=True):
    print(('CHECK ' if cond else 'CHECK FAILED ') + msg)
    if not cond:
        raise SystemExit('check failed: ' + msg)

def canvas(w=8, h=4.5, xmax=100, ymax=56):
    f, ax = fig(w, h)
    ax.set_xlim(0, xmax); ax.set_ylim(0, ymax); ax.axis('off')
    return f, ax

def box(ax, x, y, w, h, text, fc=None, ec=INK, fs=10, bold=False, color=INK, ls='-'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.4,rounding_size=1.2',
                                fc=fc or 'white', ec=ec, lw=1.2, ls=ls))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs,
            fontweight='bold' if bold else 'normal', color=color, wrap=True)

def arrow(ax, x0, y0, x1, y1, text=None, color=INK, fs=9, off=(0, 1.2), ls='-', rad=0.0, lw=1.3):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=12,
                                 color=color, lw=lw, ls=ls, connectionstyle='arc3,rad=%g' % rad))
    if text:
        ax.text((x0 + x1) / 2 + off[0], (y0 + y1) / 2 + off[1], text, ha='center', va='bottom',
                fontsize=fs, color=color)

def digital(ax, t, v, y0, h=1.0, color=BLUE, lw=1.6):
    """Step waveform: v[i] holds from t[i] to t[i+1]."""
    tt = np.repeat(t, 2)[1:]
    vv = np.repeat(v, 2)[:-1]
    ax.plot(tt, y0 + h * np.asarray(vv, float), color=color, lw=lw, drawstyle='default')

def finish(f, name):
    path = os.path.join(OUT, name + '.png')
    save(f, path)
    from PIL import Image
    w, h = Image.open(path).size
    check('%s.png %dx%d px' % (name, w, h), w == 800)

# ---------------------------------------------------------------- Part I
@figure
def b8_languages():
    f, ax = canvas(8, 4.6)
    box(ax, 2, 18, 26, 30, '', fc=LIGHT['blue'])
    ax.text(15, 44.5, 'ESP32-S3, Pico, STM32', ha='center', fontsize=9, fontweight='bold')
    box(ax, 5, 30, 20, 9, 'C / C++ firmware\nESP-IDF, Arduino, SDKs', fc='white', fs=9)
    box(ax, 5, 20, 20, 7, 'MicroPython /\nCircuitPython', fc=LIGHT['green'], fs=9)
    box(ax, 38, 18, 26, 30, '', fc=LIGHT['orange'])
    ax.text(51, 45, 'PC', ha='center', fontsize=10, fontweight='bold')
    box(ax, 41, 31, 20, 9, 'Python: instruments,\nlogging, plots, tests', fs=9)
    box(ax, 41, 20, 20, 8, 'C#: dashboards,\ntest benches, xUnit', fs=9)
    box(ax, 74, 30, 22, 14, 'FPGA\nVerilog becomes logic', fc=LIGHT['gray'], fs=9)
    box(ax, 74, 6, 22, 10, 'Bench instrument\n(SCPI)', fc='white', fs=9)
    arrow(ax, 29, 37, 37.5, 37, 'USB serial', fs=8)
    arrow(ax, 29, 25, 37.5, 25, 'Wi-Fi, MQTT', fs=8)
    arrow(ax, 65, 38, 73.5, 38, 'program', fs=8)
    arrow(ax, 65, 22, 76, 16.5)
    ax.text(73, 21, 'SCPI over\nUSB/LAN', fontsize=8)
    finish(f, 'b8_languages')

@figure
def b8_method():
    f, ax = canvas(8, 5.2, 100, 64)
    steps = ['1 Spec', '2 Modules', '3 Write or\nprompt', '4 Review', '5 Build and\nunit test',
             '6 Hardware\ntest', '7 Commit', '8 Iterate with\nbug report', '9 Document']
    cx, cy, r = 50, 31, 24
    pos = []
    for k, s in enumerate(steps):
        a = math.pi / 2 - 2 * math.pi * k / 9
        x, y = cx + 1.55 * r * math.cos(a), cy + r * math.sin(a)
        pos.append((x, y))
        fc = LIGHT['green'] if k in (3, 4) else (LIGHT['blue'] if k in (0, 1, 8) else 'white')
        box(ax, x - 8, y - 3.6, 16, 7.2, s, fc=fc, fs=8.5)
    for k in range(8):
        (x0, y0), (x1, y1) = pos[k], pos[k + 1]
        d = math.hypot(x1 - x0, y1 - y0)
        ux, uy = (x1 - x0) / d, (y1 - y0) / d
        arrow(ax, x0 + ux * 9, y0 + uy * 5, x1 - ux * 9, y1 - uy * 5, rad=-0.15)
    arrow(ax, pos[7][0] + 8.5, pos[7][1] + 1, pos[2][0] - 8.5, pos[2][1] + 1, color=RED, rad=-0.3, ls='--')
    ax.text(cx, cy - 6, 'steps 3 to 8 repeat\nper module', ha='center', fontsize=9, color=RED)
    ax.text(cx, cy - 15, 'shaded green: cheap bug gates\n(review, PC test)', ha='center', fontsize=8, color=GREEN)
    finish(f, 'b8_method')

@figure
def b8_spec_card():
    spec = ['Purpose', 'Hardware', 'Pins', 'Interfaces', 'Timing', 'Power', 'Error handling',
            'Acceptance tests', 'Out of scope']
    rev = ['Pins and addresses match spec', 'Bus speed, baud, mode, byte order', 'Every wait has a timeout',
           'ISRs short: flag or queue only', 'Shared variables protected', 'Return codes checked',
           'Units and scaling tested', 'No secrets in source', 'Library calls exist in this version',
           'Watchdog or recovery path']
    f, ax = canvas(8, 5.0, 100, 60)
    ax.add_patch(Rectangle((1, 1), 47, 57, fc=LIGHT['blue'], ec=INK, lw=1.2))
    ax.add_patch(Rectangle((52, 1), 47, 57, fc=LIGHT['green'], ec=INK, lw=1.2))
    ax.text(24.5, 54, 'SPEC (one page per module)', ha='center', fontweight='bold', fontsize=11)
    ax.text(75.5, 54, 'REVIEW (before the first run)', ha='center', fontweight='bold', fontsize=11)
    for k, s in enumerate(spec):
        ax.text(4, 48 - k * 5.2, '%d. %s: ____________' % (k + 1, s), fontsize=9.5, va='center')
    for k, s in enumerate(rev):
        ax.text(54, 48 - k * 4.7, '\u2610 ' + s, fontsize=9.2, va='center')
    check('spec card: %d spec fields, %d review checks' % (len(spec), len(rev)), len(spec) == 9 and len(rev) == 10)
    finish(f, 'b8_spec_card')

@figure
def b8_build():
    f, ax = canvas(8, 4.2, 100, 50)
    stages = [(1, 'main.c\nsensor.c\n*.h', 'white'), (17, 'Pre-\nprocessor', LIGHT['blue']),
              (31, 'Compiler', LIGHT['blue']), (45, 'Linker\n+ libs\n+ linker script', LIGHT['blue']),
              (63, 'Converter', LIGHT['blue']), (79, 'Flasher\n\u2192 chip', LIGHT['green'])]
    for x, t, c in stages:
        box(ax, x, 26, 13, 15, t, fc=c, fs=9)
    for k in range(len(stages) - 1):
        arrow(ax, stages[k][0] + 13.6, 33.5, stages[k + 1][0] - 0.6, 33.5)
    ax.text(30.5, 44, '.o files', fontsize=8, ha='center')
    ax.text(61, 44, '.elf + .map', fontsize=8, ha='center')
    ax.text(77, 44, '.bin/.hex/.uf2', fontsize=8, ha='center')
    errs = [(23.5, '"fatal error:\nno such file"'), (37.5, '"expected \';\'"'),
            (51.5, '"undefined reference"\n"region overflowed"')]
    for x, e in errs:
        ax.text(x, 18, e, ha='center', va='top', fontsize=8, color=RED)
    finish(f, 'b8_build')

@figure
def b8_size():
    flash_total, ram_total = 524288, 131072
    text, data, bss, stack, heap = 38412, 1204, 6880, 1024, 512
    fl = (text + data) / flash_total * 100
    ram = (data + bss + stack + heap) / ram_total * 100
    check('flash %.1f %% (7.6), RAM %.1f %% (7.3)' % (fl, ram), round(fl, 1) == 7.6 and round(ram, 1) == 7.3)
    f, ax = fig(8, 3.6)
    ax.barh([1], [text / 1024], color=BLUE, label='text (code)')
    ax.barh([1], [data / 1024], left=[text / 1024], color=ORANGE, label='data (initial values / variables)')
    ax.barh([1], [(flash_total - text - data) / 1024], left=[(text + data) / 1024], color='#eeeeee')
    x = 0
    for v, c, lab in ((data, ORANGE, None), (bss, GREEN, 'bss'), (stack, RED, 'stack'), (heap, GRAY, 'heap')):
        ax.barh([0], [v / 1024], left=[x / 1024], color=c, label=lab)
        x += v
    ax.barh([0], [(ram_total - x) / 1024], left=[x / 1024], color='#eeeeee')
    ax.set_yticks([0, 1]); ax.set_yticklabels(['RAM 128 KB\n7.3 % used', 'Flash 512 KB\n7.6 % used'])
    ax.set_xlabel('kilobytes'); ax.set_xlim(0, 520); ax.grid(axis='y', visible=False)
    ax.legend(loc='lower right', fontsize=8, ncol=2, frameon=True)
    finish(f, 'b8_size')

@figure
def b8_memmap():
    f, ax = canvas(8, 5.0, 100, 60)
    ax.text(25, 57, 'Flash', ha='center', fontweight='bold'); ax.text(72, 57, 'RAM', ha='center', fontweight='bold')
    fl = [('vector table', 4, LIGHT['gray']), ('.text (code)', 16, LIGHT['blue']), ('.rodata (constants)', 8, LIGHT['blue']),
          ('initial values of .data', 6, LIGHT['orange']), ('free', 18, 'white')]
    y = 2
    for t, h, c in fl:
        ax.add_patch(Rectangle((12, y), 26, h, fc=c, ec=INK)); ax.text(25, y + h / 2, t, ha='center', va='center', fontsize=9)
        y += h
    rm = [('.data', 6, LIGHT['orange']), ('.bss (zeroed)', 8, LIGHT['green']), ('heap \u2191', 7, LIGHT['gray']),
          ('free gap (the only margin)', 14, 'white'), ('stack \u2193', 10, LIGHT['red']), ('', 7, 'white')]
    y = 2
    for t, h, c in rm:
        ax.add_patch(Rectangle((59, y), 26, h, fc=c, ec=INK, ls='--' if not t else '-'))
        ax.text(72, y + h / 2, t, ha='center', va='center', fontsize=9)
        y += h
    arrow(ax, 38.5, 27, 58.5, 5, 'copied at start-up', fs=8, off=(2, 1), color=ORANGE)
    finish(f, 'b8_memmap')

@figure
def b8_padding():
    f, ax = canvas(8, 3.4, 100, 40)
    rows = [('rec_a (12 bytes)', [('id', 1, LIGHT['blue']), ('pad', 3, LIGHT['gray']), ('time', 4, LIGHT['orange']),
                                  ('hum', 2, LIGHT['green']), ('flags', 1, LIGHT['red']), ('pad', 1, LIGHT['gray'])], 24),
            ('rec_b (8 bytes)', [('time', 4, LIGHT['orange']), ('hum', 2, LIGHT['green']), ('id', 1, LIGHT['blue']),
                                 ('flags', 1, LIGHT['red'])], 8)]
    cw = 6.5
    for name, fields, y in rows:
        ax.text(1, y + 3, name, fontsize=10, va='center')
        x = 20; n = 0
        for t, w, c in fields:
            for b in range(w):
                ax.add_patch(Rectangle((x + (n + b) * cw, y), cw, 6, fc=c, ec=INK, lw=0.8))
            ax.text(x + (n + w / 2) * cw, y + 3, t, ha='center', va='center', fontsize=9)
            n += w
        check('%s: %d bytes' % (name, n), n in (12, 8))
    for b in range(12):
        ax.text(20 + (b + 0.5) * cw, 34, str(b), ha='center', fontsize=8, color=GRAY)
    finish(f, 'b8_padding')

@figure
def b8_linerate():
    bauds = [9600, 115200, 921600]
    rates = [b / 10 / 20 for b in bauds]
    check('line rates %s (48, 576, 4608)' % rates, rates == [48, 576, 4608])
    f, ax = fig(8, 4.2)
    ax.bar(['9 600', '115 200', '921 600'], rates, color=[GRAY, BLUE, GREEN])
    ax.set_yscale('log'); ax.set_ylim(0.5, 2e4)
    for i, r in enumerate(rates):
        ax.text(i, r * 1.25, '%d lines/s' % r, ha='center', fontsize=10)
    ax.axhline(1, ls='--', color=RED); ax.text(2.3, 1.15, '1 line/s logger', color=RED, ha='right', fontsize=9)
    ax.set_xlabel('baud rate (8N1, 20-byte lines)'); ax.set_ylabel('lines per second')
    finish(f, 'b8_linerate')

@figure
def b8_dotnet():
    f, ax = canvas(8, 4.6)
    box(ax, 2, 6, 40, 44, '', fc=LIGHT['orange'])
    ax.text(22, 46.5, 'PC: .NET', ha='center', fontweight='bold')
    box(ax, 5, 33, 34, 8, 'System.IO.Ports \u00b7 WPF / WinUI / MAUI \u00b7 xUnit', fs=8.5)
    box(ax, 5, 21, 34, 8, 'Apps: dashboard, test bench,\ncalibration tool', fs=9)
    box(ax, 5, 9, 34, 8, '.NET runtime', fc=LIGHT['gray'], fs=9)
    box(ax, 58, 34, 38, 14, 'C firmware\nESP-IDF, Pico SDK, STM32 HAL', fc=LIGHT['blue'], fs=9)
    box(ax, 58, 15, 38, 13, 'nanoFramework C#\non ESP32-S3 or STM32', fc=LIGHT['green'], fs=9)
    box(ax, 70, 2, 18, 8, 'Meadow F7', fc='white', fs=9)
    arrow(ax, 43, 38, 57, 40, 'USB serial / Wi-Fi', fs=8)
    arrow(ax, 43, 25, 57, 22, 'documented line protocol', fs=8, off=(0, -4))
    finish(f, 'b8_dotnet')

@figure
def b8_timer():
    req = np.arange(0, 101, 10.0)
    tick = 15.625
    deliv = [math.ceil(t / tick) * tick for t in req]
    per_s = 1000 / tick
    check('tick 15.625 ms -> %.0f callbacks/s (64)' % per_s, round(per_s) == 64)
    f, ax = fig(8, 3.4)
    for t in req:
        ax.plot([t, t], [1.2, 1.9], color=BLUE, lw=2)
    for t in sorted(set(deliv)):
        ax.plot([t, t], [0.1, 0.8], color=RED, lw=2)
    for a, b in zip(req, deliv):
        ax.plot([a, b], [1.2, 0.8], color=GRAY, ls=':', lw=0.8)
    ax.set_yticks([0.45, 1.55]); ax.set_yticklabels(['delivered\n(15.625 ms tick)', 'requested\n(every 10 ms)'])
    ax.set_xlabel('time (ms)'); ax.set_xlim(-3, 110); ax.set_ylim(0, 2.1); ax.grid(axis='y', visible=False)
    finish(f, 'b8_timer')

@figure
def b8_debounce():
    raw = np.array([1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1])   # Listing 6.1's test sequence
    t = np.arange(len(raw)) * 5
    state, cnt, deb, cnts = 1, 0, [], []
    for r in raw:
        if r != state:
            cnt += 1
            if cnt >= 4:
                state, cnt = r, 0
        else:
            cnt = 0
        deb.append(state); cnts.append(cnt)
    changes = [int(t[i]) for i in range(1, len(t)) if deb[i] != deb[i - 1]]
    check('debounced changes at %s ms (35, 75)' % changes, changes == [35, 75])
    f, ax = fig(8, 4.2)
    tt = np.append(t, t[-1] + 5)
    digital(ax, tt, np.append(raw, 1), 4.0, 1.0, color=GRAY)
    ax.plot(t, 4.0 + raw, 'o', color=GRAY, ms=3)
    digital(ax, tt, np.append(cnts, 0) / 4.0, 2.0, 1.2, color=ORANGE)
    digital(ax, tt, np.append(deb, 1), 0.0, 1.0, color=BLUE)
    ax.set_yticks([0.5, 2.6, 4.5]); ax.set_yticklabels(['debounced', 'count (0..4)', 'raw pin'])
    ax.set_xlabel('time (ms), sampled every 5 ms'); ax.grid(axis='y', visible=False)
    for c in changes:
        ax.axvline(c, color=BLUE, ls=':', lw=0.8)
    finish(f, 'b8_debounce')

@figure
def b8_pwm_counter():
    psc, arr, ccr, fclk = 83, 19999, 1500, 84e6
    tick = (psc + 1) / fclk
    period_ms = (arr + 1) * tick * 1e3
    pulse_ms = ccr * tick * 1e3
    check('PWM period %.1f ms (20), pulse %.2f ms (1.5)' % (period_ms, pulse_ms), abs(period_ms - 20) < 1e-9 and abs(pulse_ms - 1.5) < 1e-9)
    t = np.linspace(0, 60, 6001)
    cnt = ((t / 1e3) / tick) % (arr + 1)
    f, (a1, a2) = plt.subplots(2, 1, figsize=(8, 4.4), dpi=100, sharex=True)
    a1.plot(t, cnt, color=BLUE); a1.axhline(ccr, ls='--', color=RED); a1.text(61, ccr, 'CCR = 1500', color=RED, va='center', fontsize=8)
    a1.set_ylabel('counter'); a1.set_ylim(0, 21000)
    a2.plot(t, (cnt < ccr).astype(int), color=GREEN, drawstyle='steps-post'); a2.set_ylabel('output'); a2.set_yticks([0, 1])
    a2.set_xlabel('time (ms)')
    finish(f, 'b8_pwm_counter')

@figure
def b8_servo():
    res = 2 ** 14
    duties = [round(ms / 20 * res) for ms in (1.0, 1.5, 2.0)]
    step_us = 20000 / res
    check('servo duties %s (819, 1229, 1638), step %.2f us (1.22)' % (duties, step_us), duties == [819, 1229, 1638] and round(step_us, 2) == 1.22)
    f, ax = fig(8, 3.8)
    for k, (ms, d, ang) in enumerate(zip((1.0, 1.5, 2.0), duties, (0, 90, 180))):
        t = np.linspace(0, 60, 12001)
        v = ((t % 20) < ms).astype(int)
        ax.plot(t, 2.0 * k + v, color=[BLUE, GREEN, ORANGE][k], drawstyle='steps-post')
        ax.text(61, 2.0 * k + 0.4, '%.1f ms = %d\u00b0 (duty %d)' % (ms, ang, d), fontsize=9, va='center')
    ax.set_xlim(-1, 80); ax.set_yticks([]); ax.set_xlabel('time (ms), 20 ms frames at 50 Hz')
    finish(f, 'b8_servo')

@figure
def b8_ultrasonic():
    c = 331.3 + 0.606 * 20
    echo_ms = 2 * 1.0 / c * 1e3
    check('echo %.3f ms at 20 C for 1.000 m (5.824)' % echo_ms, round(echo_ms, 3) == 5.824)
    f, ax = fig(8, 3.8)
    t = np.linspace(-0.2, 7, 20000)
    trig = ((t >= 0) & (t < 0.010)).astype(float)
    burst = np.where((t >= 0.02) & (t < 0.22), 0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 40 * (t - 0.02))), 0)
    echo = ((t >= 0.22) & (t < 0.22 + echo_ms)).astype(float)
    ax.plot(t, 4 + trig, color=BLUE, lw=1.4); ax.plot(t, 2 + burst, color=ORANGE, lw=0.8); ax.plot(t, echo, color=GREEN, lw=1.4)
    ax.annotate('', xy=(0.22, 1.25), xytext=(0.22 + echo_ms, 1.25), arrowprops=dict(arrowstyle='<->', color=INK))
    ax.text(0.22 + echo_ms / 2, 1.4, '%.3f ms = 1.000 m at 20 \u00b0C' % echo_ms, ha='center', fontsize=9)
    ax.set_yticks([0.5, 2.5, 4.5]); ax.set_yticklabels(['echo', '40 kHz burst\n(8 cycles)', 'trigger 10 \u00b5s'])
    ax.set_xlabel('time (ms)'); ax.grid(axis='y', visible=False)
    finish(f, 'b8_ultrasonic')

@figure
def b8_averaging():
    lsb = 3.3 / 4096 * 1e3
    rng = np.random.default_rng(8)
    single = 1850 + rng.normal(0, 3 * lsb, 2000)
    avg8 = 1850 + rng.normal(0, 3 * lsb, (2000, 8)).mean(axis=1)
    s1, s8 = single.std(), avg8.std()
    check('sigma single %.2f mV (2.4), avg8 %.2f mV (0.85)' % (s1, s8), abs(s1 - 2.42) < 0.15 and abs(s8 - 0.855) < 0.06)
    f, ax = fig(8, 4.0)
    bins = np.linspace(1840, 1860, 81)
    ax.hist(single, bins, color=GRAY, alpha=0.6, label='single readings, \u03c3 = %.1f mV' % s1)
    ax.hist(avg8, bins, color=BLUE, alpha=0.7, label='averages of 8, \u03c3 = %.2f mV' % s8)
    ax.set_xlabel('reading (mV)'); ax.set_ylabel('count'); ax.legend(fontsize=9)
    finish(f, 'b8_averaging')

@figure
def b8_adccal():
    c1, v1, c2, v2 = 412, 0.500, 3690, 3.000
    gain = (v2 - v1) / (c2 - c1); off = v1 - gain * c1
    v2400 = gain * 2400 + off; ideal = 2400 * 3.3 / 4096
    check('gain %.1f uV, offset %.4f V, 2400 -> %.4f vs %.4f' % (gain * 1e6, off, v2400, ideal),
          round(gain * 1e6, 1) == 762.7 and round(off, 3) == 0.186 and round(v2400, 3) == 2.016 and round(ideal, 3) == 1.934)
    f, ax = fig(8, 4.4)
    c = np.array([0, 4095])
    ax.plot(c, c * 3.3 / 4096, '--', color=GRAY, label='ideal: 3.3 V/4096')
    ax.plot(c, gain * c + off, color=BLUE, label='calibrated: 762.7 \u00b5V/code + 0.186 V')
    ax.plot([c1, c2], [v1, v2], 'o', color=RED)
    ax.axvline(2400, color=INK, lw=0.7, ls=':')
    ax.text(2450, v2400 + 0.05, '2.016 V', fontsize=9); ax.text(2450, ideal - 0.2, '1.934 V', fontsize=9, color=GRAY)
    ax.set_xlabel('ADC code'); ax.set_ylabel('volts'); ax.legend(fontsize=9, loc='upper left')
    finish(f, 'b8_adccal')

@figure
def b8_uart():
    bit_us = 1e6 / 115200
    bits = [0] + [(0x41 >> i) & 1 for i in range(8)] + [1]
    check('UART bit %.2f us, frame %.1f us, data %s' % (bit_us, 10 * bit_us, bits[1:9]),
          round(bit_us, 2) == 8.68 and bits[1:9] == [1, 0, 0, 0, 0, 0, 1, 0])
    t = np.concatenate([[-bit_us], np.arange(12) * bit_us])   # edges; digital() takes equal lengths
    v = [1] + bits + [1, 1]
    f, ax = fig(8, 3.0)
    digital(ax, t, v, 0)
    labels = ['start'] + ['D%d' % i for i in range(8)] + ['stop']
    for i, lab in enumerate(labels):
        ax.text((i + 0.5) * bit_us, 1.25, lab, ha='center', fontsize=8)
        ax.text((i + 0.5) * bit_us, -0.35, str(bits[i]), ha='center', fontsize=9, color=BLUE)
    ax.set_ylim(-0.6, 1.6); ax.set_yticks([]); ax.set_xlabel('time (\u00b5s): 8.68 \u00b5s per bit, 86.8 \u00b5s per frame')
    finish(f, 'b8_uart')

@figure
def b8_i2c():
    f, ax = canvas(8, 3.6, 100, 40)
    segs = [('S', 4, LIGHT['gray']), ('0x76 + W', 14, LIGHT['blue']), ('A', 3, LIGHT['green']), ('0xD0', 11, LIGHT['blue']),
            ('A', 3, LIGHT['green']), ('Sr', 4, LIGHT['gray']), ('0x76 + R', 14, LIGHT['blue']), ('A', 3, LIGHT['green']),
            ('0x60', 11, LIGHT['orange']), ('N', 3, LIGHT['red']), ('P', 4, LIGHT['gray'])]
    x = 6
    for t, w, c in segs:
        ax.add_patch(Rectangle((x, 26), w, 8, fc=c, ec=INK)); ax.text(x + w / 2, 30, t, ha='center', va='center', fontsize=9)
        x += w
    ax.text(6, 37, 'controller sends: blue    sensor sends: orange data, green ACK', fontsize=8.5)
    # SCL/SDA for the first byte 0x76 + W = 0xEC
    byte = 0x76 << 1
    sb = [(byte >> (7 - i)) & 1 for i in range(8)] + [0]
    t0 = 10
    sclx, scly, sdax, sday = [6, t0], [1, 1], [6, 8], [1, 0]
    for i in range(9):
        a = t0 + i * 8
        sclx += [a, a + 2, a + 2, a + 6, a + 6, a + 8]; scly += [0, 0, 1, 1, 0, 0]
        sdax += [a + 1, a + 1, a + 8]; sday += [sday[-1], sb[i], sb[i]]
    ax.plot(sclx, np.array(scly) * 6 + 13, color=INK); ax.plot(sdax, np.array(sday) * 6 + 3, color=BLUE)
    ax.text(1, 16, 'SCL', fontsize=9); ax.text(1, 6, 'SDA', fontsize=9)
    for i, b in enumerate(sb):
        ax.text(t0 + i * 8 + 4, 10.5, str(b) if i < 8 else 'ACK', ha='center', fontsize=7, color=BLUE)
    check('first byte 0x%02X = %s + ACK' % (byte, ''.join(map(str, sb[:8]))), byte == 0xEC)
    finish(f, 'b8_i2c')

@figure
def b8_spi():
    byte = 0xA5
    bits = [(byte >> (7 - i)) & 1 for i in range(8)]
    check('SPI 0xA5 bits %s, 1 us at 8 MHz' % bits, bits == [1, 0, 1, 0, 0, 1, 0, 1] and 8 / 8e6 == 1e-6)
    f, ax = fig(8, 3.6)
    T = 125.0   # ns per bit at 8 MHz
    t0 = 100
    cs_t = [0, t0 - 50, t0 + 8 * T + 50, t0 + 8 * T + 150]
    digital(ax, np.array(cs_t), [1, 0, 1, 1], 4.0, color=INK)
    sck_t, sck_v = [0, t0], [0, 0]
    for i in range(8):
        a = t0 + i * T
        sck_t += [a + T / 2, a + T]; sck_v += [1, 0]
    digital(ax, np.array(sck_t + [t0 + 8 * T + 150]), sck_v + [0], 2.0, color=BLUE)
    mo_t, mo_v = [0], [0]
    for i, b in enumerate(bits):
        mo_t.append(t0 + i * T); mo_v.append(b)
    mo_t.append(t0 + 8 * T); mo_v.append(0); mo_t.append(t0 + 8 * T + 150); mo_v.append(0)
    digital(ax, np.array(mo_t), mo_v, 0.0, color=GREEN)
    for i, b in enumerate(bits):
        x = t0 + i * T + T / 2
        ax.axvline(x, color=GRAY, ls=':', lw=0.8); ax.text(x, -0.45, str(b), ha='center', fontsize=9, color=GREEN)
    ax.set_yticks([0.5, 2.5, 4.5]); ax.set_yticklabels(['MOSI', 'SCK', 'CS']); ax.grid(axis='y', visible=False)
    ax.set_xlabel('time (ns): mode 0, sampled on rising edges (dotted), 8 MHz'); ax.set_ylim(-0.8, 5.3)
    finish(f, 'b8_spi')

@figure
def b8_can():
    segs = [('SOF', 1), ('ID', 11), ('RTR IDE r0', 3), ('DLC', 4), ('data', 64), ('CRC', 15), ('del', 1),
            ('ACK', 2), ('EOF', 7), ('IFS', 3)]
    n = sum(w for _, w in segs)
    stuffed = n + 24
    check('CAN frame %d bits (111), with stuffing up to %d (135); %.0f-%.0f us at 500k' % (n, stuffed, n * 2, stuffed * 2),
          n == 111 and stuffed == 135)
    f, ax = canvas(8, 3.2, 140, 40)
    x = 2
    cols = [LIGHT['gray'], LIGHT['blue'], LIGHT['gray'], LIGHT['gray'], LIGHT['orange'], LIGHT['green'], LIGHT['gray'],
            LIGHT['red'], LIGHT['gray'], 'white']
    for (t, w), c in zip(segs, cols):
        ax.add_patch(Rectangle((x, 24), w, 8, fc=c, ec=INK, lw=0.8))
        if w >= 3:
            ax.text(x + w / 2, 28, t if w > 6 else t.split()[0], ha='center', va='center', fontsize=7 if w < 10 else 9)
        x += w
    ax.text(2, 35, '111 bits = 222 \u00b5s at 500 kbit/s', fontsize=9)
    ax.add_patch(Rectangle((2, 8), n, 8, fc=LIGHT['blue'], ec=INK, lw=0.8)); ax.add_patch(Rectangle((2 + n, 8), 24, 8, fc=LIGHT['red'], ec=INK, lw=0.8, hatch='//'))
    ax.text(2 + n / 2, 12, 'frame bits', ha='center', fontsize=9); ax.text(2 + n + 12, 12, '+24 stuff', ha='center', fontsize=8)
    ax.text(2, 19, 'worst case 135 bits = 270 \u00b5s', fontsize=9)
    finish(f, 'b8_can')

@figure
def b8_layers():
    f, ax = canvas(8, 5.0, 100, 60)
    layers = ['silicon peripherals', 'registers at fixed addresses', 'CMSIS device headers (register names)',
              'vendor drivers: HAL, LL, Pico SDK, ESP-IDF', 'your drivers', 'application']
    cols = [LIGHT['gray'], LIGHT['gray'], LIGHT['blue'], LIGHT['blue'], LIGHT['green'], LIGHT['orange']]
    for k, (t, c) in enumerate(zip(layers, cols)):
        box(ax, 18, 3 + k * 9, 52, 7, t, fc=c, fs=9.5)
    box(ax, 75, 30, 20, 25, 'Arduino,\nMicroPython', fc='white', fs=9, ls='--')
    arrow(ax, 8, 6, 8, 55, color=GREEN)
    ax.text(5, 30, 'more portable,\nmore convenient', rotation=90, va='center', ha='center', fontsize=8, color=GREEN)
    arrow(ax, 13, 55, 13, 6, color=BLUE)
    ax.text(15.5, 30, 'faster, more transparent', rotation=90, va='center', ha='center', fontsize=8, color=BLUE)
    finish(f, 'b8_layers')

@figure
def b8_bsrr():
    val = (1 << 22) | (1 << 5)
    check('BSRR value 0x%08X (0x00400020)' % val, val == 0x00400020)
    f, ax = canvas(8, 2.8, 100, 30)
    cw = 96 / 32
    for i in range(32):
        bit = 31 - i
        on = (val >> bit) & 1
        ax.add_patch(Rectangle((2 + i * cw, 12), cw, 7, fc=(RED if bit >= 16 else BLUE) if on else (LIGHT['red'] if bit >= 16 else LIGHT['blue']), ec=INK, lw=0.6))
        ax.text(2 + (i + 0.5) * cw, 10.5, str(bit), ha='center', va='top', fontsize=6)
    ax.text(26, 22, 'BR15 ... BR0 (reset pins)', ha='center', fontsize=9, color=RED)
    ax.text(74, 22, 'BS15 ... BS0 (set pins)', ha='center', fontsize=9, color=BLUE)
    ax.text(2 + 9.5 * cw, 26.5, 'bit 22: reset PA6', ha='center', fontsize=8.5)
    ax.text(2 + 26.5 * cw, 26.5, 'bit 5: set PA5', ha='center', fontsize=8.5)
    ax.text(50, 2, 'BSRR = 0x00400020', ha='center', fontsize=11, fontweight='bold')
    finish(f, 'b8_bsrr')

@figure
def b8_superloop():
    a = 2 + 5 + 12; b = 2 + 5 + 1.5
    check('loop %g ms -> worst %g ms; split %g ms -> %g ms' % (a, 5 * a, b, 5 * b), a == 19 and 5 * a == 95 and b == 8.5 and 5 * b == 42.5)
    f, ax = fig(8, 3.4)
    for row, jobs in ((1, (2, 5, 12)), (0, (2, 5, 1.5))):
        t = 0
        while t < 100:
            for d, c in zip(jobs, (GREEN, BLUE, ORANGE)):
                ax.barh(row, min(d, 100 - t), left=t, color=c, height=0.5, edgecolor='white')
                t += d
                if t >= 100:
                    break
        L = sum(jobs)
        for k in range(int(100 // L) + 1):
            ax.plot(k * L, row + 0.33, 'v', color=INK, ms=4)
    ax.axvline(50, color=RED, ls='--'); ax.text(51, 1.45, '50 ms spec', color=RED, fontsize=9)
    ax.set_yticks([0, 1]); ax.set_yticklabels(['one OLED page\nper loop: 8.5 ms', 'full redraw:\n19 ms per loop'])
    ax.set_xlim(0, 100); ax.set_xlabel('time (ms)   green: sensor, blue: logic, orange: display, \u25bc button sample')
    ax.grid(axis='y', visible=False)
    finish(f, 'b8_superloop')

@figure
def b8_fsm():
    f, ax = canvas(8, 4.6, 100, 56)
    S = {'SLEEP': (11, 30), 'CAPTURE': (36, 30), 'SAVE': (64, 42), 'COOLDOWN': (64, 14), 'LOWBATT': (88, 46)}
    for k, (x, y) in S.items():
        box(ax, x - 8, y - 4, 16, 8, k, fc=LIGHT['red'] if k == 'LOWBATT' else LIGHT['blue'], fs=9, bold=True)
    arrow(ax, 19.5, 31, 27.5, 31, 'motion', fs=8)
    arrow(ax, 44.5, 33, 55.5, 41, 'capture OK', fs=8, off=(-3, 1))
    arrow(ax, 44.5, 27, 55.5, 16, 'fail: errors+1', fs=8, off=(-5, -4))
    arrow(ax, 64, 37.5, 64, 18.5, 'saved:\nphotos+1', fs=8, off=(7, -2))
    arrow(ax, 55.5, 12, 11, 25.5, '30 ticks of 1 s', fs=8, off=(0, -6), rad=-0.2)
    ax.text(74, 8, 'motion ignored', fontsize=8, color=GRAY)
    ax.text(70, 54, 'battery low from any state \u2192 LOWBATT', fontsize=8, color=RED, ha='center')
    finish(f, 'b8_fsm')

@figure
def b8_rtos():
    loads = (0.4 / 10, 8 / 100, 60 / 60000)
    tot = sum(loads) * 100
    check('RTOS load %.1f %% (12.1)' % tot, round(tot, 1) == 12.1)
    f, ax = fig(8, 3.2)
    sensor = [(k * 10, 0.4) for k in range(10)]
    ax.broken_barh(sensor, (2, 0.6), color=RED)
    disp, t, left = [], 0.4, 8.0
    while left > 0:
        nxt = (math.floor(t / 10) + 1) * 10
        run = min(left, nxt - t)
        disp.append((t, run)); left -= run; t = nxt + 0.4
    ax.broken_barh(disp, (1, 0.6), color=BLUE)
    busy = sorted(sensor + disp)
    idle, t = [], 0
    for s, d in busy:
        if s > t:
            idle.append((t, s - t))
        t = max(t, s + d)
    idle.append((t, 100 - t))
    ax.broken_barh(idle, (0, 0.6), color='#cccccc')
    ax.set_yticks([0.3, 1.3, 2.3]); ax.set_yticklabels(['idle', 'display (8 ms / 100 ms)', 'sensor (0.4 ms / 10 ms)'])
    ax.set_xlim(0, 100); ax.set_xlabel('time (ms)'); ax.grid(axis='y', visible=False)
    finish(f, 'b8_rtos')

@figure
def b8_inversion():
    f, (a1, a2) = plt.subplots(2, 1, figsize=(8, 4.4), dpi=100, sharex=True)
    def row(ax, segs):
        for r, s, d, c in segs:
            ax.broken_barh([(s, d)], (r, 0.6), color=c)
        ax.set_yticks([0.3, 1.3, 2.3]); ax.set_yticklabels(['L', 'M', 'H']); ax.grid(axis='y', visible=False)
    row(a1, [(0, 0, 2, GRAY), (2, 2, 0.4, RED), (0, 2.4, 0.6, GRAY), (1, 3, 10, ORANGE), (0, 13, 1, GRAY), (2, 14, 3, RED)])
    a1.text(2.3, 2.75, 'H blocks on mutex', fontsize=8); a1.text(14.2, 2.75, 'H runs late', fontsize=8, color=RED)
    a1.set_title('without priority inheritance', fontsize=10)
    row(a2, [(0, 0, 2, GRAY), (2, 2, 0.4, RED), (0, 2.4, 1.6, GREEN), (2, 4, 3, RED), (1, 7, 10, ORANGE)])
    a2.text(2.5, 0.75, 'L boosted to H', fontsize=8, color=GREEN); a2.text(4.2, 2.75, 'H on time', fontsize=8, color=RED)
    a2.set_title('with priority inheritance', fontsize=10); a2.set_xlabel('time (ms)'); a2.set_xlim(0, 18)
    finish(f, 'b8_inversion')

# ---------------------------------------------------------------- Part III-IV
def iavg(i_act, t_act, i_sleep, T):
    return (i_act * t_act + i_sleep * (T - t_act)) / T

@figure
def b8_power_profile():
    a_mod = iavg(80, 3, 0.020, 600); a_dev = iavg(80, 3, 13.5, 600)
    check('averages %.3f mA (0.42), %.2f mA (13.8)' % (a_mod, a_dev), round(a_mod, 2) == 0.42 and round(a_dev, 1) == 13.8)
    f, ax = fig(8, 4.0)
    t = np.array([0, 3, 600])
    ax.step(t, [80, 0.020, 0.020], where='post', color=BLUE, lw=1.6, label='bare module: sleep 20 \u00b5A')
    ax.step(t, [80, 13.5, 13.5], where='post', color=RED, lw=1.6, label='development board: sleep 13.5 mA')
    ax.axhline(a_mod, color=BLUE, ls='--', lw=1); ax.axhline(a_dev, color=RED, ls='--', lw=1)
    ax.text(300, a_mod * 1.25, 'average 0.42 mA', color=BLUE, fontsize=9); ax.text(300, a_dev * 1.25, 'average 13.8 mA', color=RED, fontsize=9)
    ax.set_yscale('log'); ax.set_ylim(0.01, 200); ax.set_xlim(-5, 600)
    ax.set_xlabel('time in one 10-minute cycle (s); 3 s active at 80 mA'); ax.set_ylabel('current (mA)')
    ax.legend(fontsize=9, loc='upper right')
    finish(f, 'b8_power_profile')

@figure
def b8_life():
    T = np.logspace(math.log10(60), math.log10(86400), 200)
    life = lambda ta: 3000 / iavg(80, ta, 0.020, T) / 24
    l3 = 3000 / iavg(80, 3, 0.020, 600) / 24; l08 = 3000 / iavg(80, 0.8, 0.020, 600) / 24
    check('life at 10 min: %.0f d (298), %.0f d (987); ceiling %.0f d' % (l3, l08, 3000 / 0.02 / 24),
          round(l3) == 298 and round(l08) == 987)
    f, ax = fig(8, 4.2)
    ax.loglog(T / 60, life(3), color=RED, label='3 s active')
    ax.loglog(T / 60, life(0.8), color=BLUE, label='0.8 s active')
    ax.axhline(6250, color=GRAY, ls='--'); ax.text(1.1, 7000, 'sleep-current ceiling 6250 days', fontsize=9, color=GRAY)
    ax.plot([10, 10], [l3, l08], 'o', color=INK)
    ax.text(11, l3 * 0.8, '298 d', fontsize=9); ax.text(11, l08 * 0.8, '987 d', fontsize=9)
    ax.set_xlabel('wake interval (minutes)'); ax.set_ylabel('life on 3000 mAh (days)'); ax.legend(fontsize=9, loc='lower right')
    finish(f, 'b8_life')

@figure
def b8_iir():
    n = np.arange(0, 151)
    fl = 1000 * (1 - (15 / 16) ** n)
    yn, acc, naive, scaled = 0, 0, [0], [0]
    for _ in n[1:]:
        yn += (1000 - yn) >> 4; acc += ((1000 << 8) - acc) >> 4
        naive.append(yn); scaled.append((acc + 128) >> 8)
    tau = -1 / math.log(15 / 16)
    check('IIR after 16: %d (644); naive end %d (985); scaled end %d; tau %.1f samples' % (scaled[16], naive[-1], scaled[-1], tau),
          scaled[16] == 644 and naive[-1] == 985 and scaled[-1] == 1000 and round(tau, 1) == 15.5)
    f, ax = fig(8, 4.0)
    t = n / 100
    ax.plot(t, fl, color=GRAY, lw=3, alpha=0.5, label='float')
    ax.plot(t, scaled, color=BLUE, label='integer, 8 fractional bits')
    ax.plot(t, naive, color=RED, label='naive integer (stops at 985)')
    ax.axhline(632, color=INK, ls=':', lw=0.8); ax.axvline(0.155, color=INK, ls=':', lw=0.8)
    ax.text(0.17, 560, '63.2 % at \u03c4 = 0.155 s', fontsize=9)
    ax.set_xlabel('time (s) at 100 Hz'); ax.set_ylabel('output (counts)'); ax.legend(fontsize=9, loc='lower right')
    ax.set_ylim(0, 1050)
    finish(f, 'b8_iir')

@figure
def b8_fft():
    FS, N = 10000, 1024
    x = np.sin(2 * np.pi * 1000 * np.arange(N) / FS)
    fr = np.fft.rfftfreq(N, 1 / FS)
    out = {}
    f, ax = fig(8, 4.0)
    for name, w, c in (('rectangular', np.ones(N), RED), ('Hann', np.hanning(N), BLUE)):
        s = np.abs(np.fft.rfft(x * w)); db = 20 * np.log10(s / s.max() + 1e-12)
        out[name] = db[int(1500 * N / FS):].max()
        ax.plot(fr, db, color=c, lw=1, label=name)
    check('leakage above 1.5 kHz: rect %.1f dB (-42.4), Hann %.1f dB (-111.4)' % (out['rectangular'], out['Hann']),
          round(out['rectangular'], 1) == -42.4 and round(out['Hann'], 1) == -111.4)
    ax.set_ylim(-140, 5); ax.set_xlim(0, 5000)
    ax.set_xlabel('frequency (Hz), bins of 9.77 Hz'); ax.set_ylabel('magnitude (dB)'); ax.legend(fontsize=9)
    finish(f, 'b8_fft')

def fusion_sim():
    """Python mirror of Listing 16.2, including its LCG noise generator (seed 12345)."""
    st = {'seed': 12345}
    def noise():
        acc = 0.0
        for _ in range(12):
            st['seed'] = (st['seed'] * 1664525 + 1013904223) & 0xFFFFFFFF
            acc += (st['seed'] >> 8) / 16777216.0
        return acc - 6.0
    dt, truth, bias = 0.01, 10.0, 0.5
    gyro_only, comp = truth, None
    ang, b, P = None, 0.0, np.zeros((2, 2))
    Qa, Qb, R = 0.001, 0.003, 4.0
    out = []
    for i in range(2000):
        g = bias + 0.1 * noise(); a = truth + 2.0 * noise()
        if i == 0:
            comp = a; ang = a
        gyro_only += g * dt
        comp = 0.98 * (comp + g * dt) + 0.02 * a
        ang += (g - b) * dt
        P[0, 0] += dt * (dt * P[1, 1] - P[0, 1] - P[1, 0] + Qa); P[0, 1] -= dt * P[1, 1]; P[1, 0] -= dt * P[1, 1]; P[1, 1] += Qb * dt
        S = P[0, 0] + R; K0, K1 = P[0, 0] / S, P[1, 0] / S; y = a - ang
        ang += K0 * y; b += K1 * y
        P00, P01 = P[0, 0], P[0, 1]
        P[0, 0] -= K0 * P00; P[0, 1] -= K0 * P01; P[1, 0] -= K1 * P00; P[1, 1] -= K1 * P01
        out.append((i * dt, a, gyro_only, comp, ang))
    return np.array(out)

@figure
def b8_fusion():
    d = fusion_sim()
    last = d[1000:]
    rms = lambda col: math.sqrt(np.mean((last[:, col] - 10) ** 2))
    drift = d[-1, 2] - 10
    check('fusion: drift %.2f (9.94), rms acc %.2f (1.96), comp %.2f (0.33), kalman %.2f (0.19)' % (drift, rms(1), rms(3), rms(4)),
          round(drift, 1) == 9.9 and round(rms(1), 2) == 1.96 and round(rms(3), 2) == 0.33 and round(rms(4), 2) == 0.19)
    f, ax = fig(8, 4.2)
    ax.plot(d[:, 0], d[:, 1], color=GRAY, lw=0.5, alpha=0.6, label='accelerometer only')
    ax.plot(d[:, 0], d[:, 2], color=RED, label='gyro only (drifts)')
    ax.plot(d[:, 0], d[:, 3], color=BLUE, label='complementary, \u03b1 = 0.98')
    ax.plot(d[:, 0], d[:, 4], color=GREEN, label='Kalman (angle + bias)')
    ax.set_xlabel('time (s)'); ax.set_ylabel('tilt (degrees)'); ax.set_ylim(0, 25); ax.legend(fontsize=9, loc='upper left')
    finish(f, 'b8_fusion')

@figure
def b8_grid():
    CELL, SIZE = 0.05, 40
    lh, lm = math.log(0.7 / 0.3), math.log(0.4 / 0.6)
    g = np.zeros((SIZE, SIZE))
    def occupied(x, y):
        return x < 0.1 or x > 1.9 or y < 0.1 or y > 1.9 or (1.1 < x < 1.4 and 1.1 < y < 1.4)
    path = [(0.4 + 0.05 * k, 0.5 + 0.02 * k) for k in range(20)]
    for (px, py) in path:
        for hd in range(0, 360, 6):
            h = math.radians(hd)
            for s in range(1, 60):
                x, y = px + s * CELL * math.cos(h), py + s * CELL * math.sin(h)
                cx, cy = int(x / CELL), int(y / CELL)
                if not (0 <= cx < SIZE and 0 <= cy < SIZE):
                    break
                if occupied(x, y):
                    g[cy, cx] += lh
                    break
                g[cy, cx] += lm
    p = 1 - 1 / (1 + np.exp(np.clip(g, -20, 20)))
    check('grid: %d cells occupied (p>0.9), %d free (p<0.1)' % ((p > 0.9).sum(), (p < 0.1).sum()), (p > 0.9).sum() > 50)
    check('three hits -> p = %.3f (0.927), three misses -> %.3f (0.229)' % (1 - 1 / (1 + math.exp(3 * lh)), 1 - 1 / (1 + math.exp(3 * lm))), True)
    f, ax = fig(8, 5.4)
    ax.imshow(1 - p, cmap='gray', origin='lower', extent=(0, 2, 0, 2), vmin=0, vmax=1)
    ax.plot([q[0] for q in path], [q[1] for q in path], color=BLUE, lw=2)
    ax.set_xlabel('x (m)'); ax.set_ylabel('y (m)'); ax.grid(False)
    finish(f, 'b8_grid')

@figure
def b8_mqtt():
    f, ax = canvas(8, 4.2, 100, 52)
    box(ax, 2, 20, 20, 12, 'ESP32-S3\ngarden node', fc=LIGHT['blue'], fs=9)
    box(ax, 38, 18, 22, 16, 'Broker\nMosquitto on Pi 5', fc=LIGHT['orange'], fs=9, bold=True)
    for k, t in enumerate(('CSV logger\n(Listing 17.4)', 'C# dashboard\n(Chapter 22)', 'phone app')):
        box(ax, 76, 38 - k * 15, 22, 10, t, fc=LIGHT['green'], fs=9)
        arrow(ax, 60.5, 26, 75.5, 43 - k * 15)
    arrow(ax, 22.5, 26, 37.5, 26, 'publish\nlab/garden/bme280', fs=8)
    ax.text(68, 48, 'subscribe lab/garden/#', fontsize=8, ha='center')
    arrow(ax, 49, 17.5, 49, 6, ls='--', color=RED)
    ax.text(51, 7, 'last will: lab/garden/status = offline', fontsize=8, color=RED)
    finish(f, 'b8_mqtt')

@figure
def b8_backoff():
    base = [min(1 << a, 60) if a < 6 else 60 for a in range(10)]
    base = [min(2 ** a, 60) for a in range(10)]
    jit = [0.8, 1.6, 3.2, 8.0, 13.5, 30.7, 57.6, 49.5, 58.1, 57.9]     # Listing 17.3 output
    check('back-off total without jitter %d s (303)' % sum(base), sum(base) == 303)
    f, ax = fig(8, 4.0)
    x = np.arange(1, 11)
    ax.bar(x - 0.2, base, 0.4, color=GRAY, label='no jitter')
    ax.bar(x + 0.2, jit, 0.4, color=BLUE, label='25 % jitter (Listing 17.3)')
    ax.axhspan(45, 60, color=LIGHT['orange'], alpha=0.6, zorder=0); ax.text(0.6, 52, 'jittered waits at the cap: 45 to 60 s', fontsize=9)
    ax.set_xticks(x); ax.set_xlabel('attempt'); ax.set_ylabel('wait (s)'); ax.legend(fontsize=9, loc='upper left', bbox_to_anchor=(0, 0.85))
    finish(f, 'b8_backoff')

def lora_toa(PL, SF, BW=125e3, CR=1, npre=8, crc=1, H=0):
    DE = 1 if (SF >= 11 and BW == 125e3) else 0
    Ts = 2 ** SF / BW
    n = 8 + max(math.ceil((8 * PL - 4 * SF + 28 + 16 * crc - 20 * H) / (4 * (SF - 2 * DE))) * (CR + 4), 0)
    return (npre + 4.25) * Ts + n * Ts

@figure
def b8_airtime():
    a8, a32 = lora_toa(8, 9) * 1e3, lora_toa(32, 9) * 1e3
    check('LoRa SF9: 8 B %.1f ms (123.9), 32 B %.1f ms (246.8); SF7 8 B %.1f ms (36.1)' % (a8, a32, lora_toa(8, 7) * 1e3),
          round(a8, 1) == 123.9 and round(a32, 1) == 246.8 and round(lora_toa(8, 7) * 1e3, 1) == 36.1)
    f, ax = fig(8, 4.2)
    pl = np.arange(1, 65)
    for sf, c in ((7, GREEN), (9, BLUE), (12, RED)):
        ax.step(pl, [lora_toa(p, sf) * 1e3 for p in pl], where='mid', color=c, label='SF%d' % sf)
    ax.plot([8, 32], [a8, a32], 'o', color=INK)
    ax.text(9, a8 * 0.75, '8 B: 123.9 ms', fontsize=9); ax.text(33, a32 * 0.75, '32 B JSON: 246.8 ms', fontsize=9)
    ax.set_yscale('log'); ax.set_xlabel('payload (bytes)'); ax.set_ylabel('airtime (ms)'); ax.legend(fontsize=9)
    finish(f, 'b8_airtime')

@figure
def b8_payload():
    payload = bytes.fromhex('012A09255A279544')
    t = int.from_bytes(payload[2:4], 'big', signed=True) / 100
    p = int.from_bytes(payload[5:7], 'big') / 10
    v = 2.5 + payload[7] / 50
    check('payload -> %.2f C, %.1f %%, %.1f hPa, %.2f V' % (t, payload[4] / 2, p, v), t == 23.41 and p == 1013.3 and abs(v - 3.86) < 1e-9)
    f, ax = canvas(8, 2.8, 100, 30)
    fields = [('version', 1, '01', '1'), ('seq', 1, '2A', '42'), ('temp int16', 2, '09 25', '0.01 \u00b0C\n23.41'),
              ('hum', 1, '5A', '0.5 %\n45.0'), ('pressure uint16', 2, '27 95', '0.1 hPa\n1013.3'), ('battery', 1, '44', '2.5 V + 20 mV\n3.86 V')]
    x, cw = 4, 11.5
    for name, w, hx, sc in fields:
        ax.add_patch(Rectangle((x, 12), w * cw, 8, fc=LIGHT['blue'] if w == 2 else LIGHT['green'], ec=INK))
        ax.text(x + w * cw / 2, 16, hx, ha='center', va='center', fontsize=11, family='monospace')
        ax.text(x + w * cw / 2, 22, name, ha='center', fontsize=8.5)
        ax.text(x + w * cw / 2, 10, sc, ha='center', va='top', fontsize=8, color=GRAY)
        x += w * cw
    for b in range(8):
        ax.text(4 + (b + 0.5) * cw, 27, 'byte %d' % b, ha='center', fontsize=7, color=GRAY)
    finish(f, 'b8_payload')

@figure
def b8_ota():
    f, ax = canvas(8, 5.0, 100, 60)
    parts = [('boot', 8), ('nvs', 7), ('otadata', 10), ('ota_0', 25), ('ota_1', 25)]
    rows = [('1 run ota_0, download into ota_1', {'ota_0': BLUE, 'ota_1': ORANGE}),
            ('2 verify, mark ota_1 to boot', {'ota_0': BLUE, 'ota_1': ORANGE, 'otadata': ORANGE}),
            ('3 restart into ota_1 (pending verify)', {'ota_1': BLUE}),
            ('4 self-test OK: confirm / fail: roll back', {'ota_1': GREEN})]
    for r, (lab, col) in enumerate(rows):
        y = 48 - r * 13
        x = 3
        ax.text(3, y + 8.5, lab, fontsize=9)
        for name, w in parts:
            c = col.get(name)
            ax.add_patch(Rectangle((x, y), w, 7, fc=c if c else 'white', ec=INK, alpha=0.55 if c else 1))
            ax.text(x + w / 2, y + 3.5, name, ha='center', va='center', fontsize=8.5)
            x += w
    arrow(ax, 82, 10, 82, 50, color=RED, rad=0.4)
    ax.text(86, 30, 'rollback\nto ota_0', color=RED, fontsize=9)
    finish(f, 'b8_ota')

@figure
def b8_datarates():
    rates = [('VGA RGB, 30 fps', 640 * 480 * 3 * 30), ('gray 320\u00d7240, 100 fps', 320 * 240 * 100),
             ('QVGA RGB565, 30 fps', 320 * 240 * 2 * 30), ('event stream (synthetic)', 240000 * 8),
             ('QVGA JPEG, 25 fps', 10000 * 25), ('VL53L1X, 20 Hz', 2 * 20)]
    check('rates: VGA %.1f MB/s (27.6), QVGA565 %.1f (4.6), events %.2f (1.92)' % (rates[0][1] / 1e6, rates[2][1] / 1e6, rates[3][1] / 1e6),
          round(rates[0][1] / 1e6, 1) == 27.6 and round(rates[2][1] / 1e6, 1) == 4.6)
    f, ax = fig(8, 4.0)
    names = [r[0] for r in rates][::-1]; vals = [r[1] for r in rates][::-1]
    ax.barh(names, vals, color=[GREEN, ORANGE, BLUE, BLUE, BLUE, RED])
    ax.set_xscale('log'); ax.set_xlim(10, 3e8); ax.set_xlabel('bytes per second')
    for i, v in enumerate(vals):
        ax.text(v * 1.3, i, ('%.3g MB/s' % (v / 1e6)) if v >= 1e5 else ('%.0f B/s' % v if v < 1e3 else '%.0f kB/s' % (v / 1e3)), va='center', fontsize=9)
    ax.grid(axis='y', visible=False)
    finish(f, 'b8_datarates')

@figure
def b8_pointcloud():
    Z, FOV = 8, 45.0
    step = math.radians(FOV) / Z
    a = (np.arange(Z) - (Z - 1) / 2) * step
    corner = 1 / (math.cos(a[0]) ** 2)
    check('corner zone %.0f mm (1128), off-axis %.2f deg (19.69)' % (corner * 1000, math.degrees(-a[0])), round(corner * 1000) == 1128)
    f, ax = fig(8, 4.4)
    el0 = a[3]   # a middle row, side view of the elevation fan
    for el in a:
        r = 1 / (math.cos(el) * math.cos(a[0]))
        ax.plot([0, math.cos(el) * 1.0 / math.cos(el)], [0, math.tan(el)], color=GRAY, lw=0.8)
        ax.plot(1.0, math.tan(el), 'o', color=BLUE)
    ax.axvline(1.0, color=BLUE, lw=2, alpha=0.4)
    ax.text(1.02, math.tan(a[-1]) + 0.03, 'corner zones: 1128 mm', fontsize=9)
    ax.text(1.02, 0.02, 'center zones: about 1000 mm', fontsize=9)
    ax.plot(0, 0, 's', color=INK, ms=8); ax.text(0.02, -0.07, 'sensor', fontsize=9)
    ax.set_xlim(-0.05, 1.45); ax.set_ylim(-0.5, 0.5); ax.set_aspect('equal')
    ax.set_xlabel('z, distance ahead (m)'); ax.set_ylabel('y (m)')
    finish(f, 'b8_pointcloud')

@figure
def b8_events():
    W, H, v = 320, 240, 1000.0
    rng = np.random.default_rng(2)
    xs = np.arange(100); xx, yy = np.meshgrid(xs, np.arange(H))
    t = (xx / v * 1e6 + rng.normal(0, 50, xx.shape)).clip(0)
    n = xx.size
    win = (t >= 50000) & (t < 60000)
    cols = np.unique(xx[win])
    check('events %d in 100 ms (24000); window columns %d..%d (50..60)' % (n, cols.min(), cols.max()), n == 24000 and cols.min() == 50 and cols.max() == 60)
    f, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.6), dpi=100)
    a1.plot(t[120] / 1000, xx[120], '.', ms=2, color=BLUE)
    a1.set_xlabel('time (ms)'); a1.set_ylabel('pixel column (row 120)'); a1.set_title('events: slope = 1000 px/s', fontsize=10)
    img = np.zeros((H, W)); np.add.at(img, (yy[win], xx[win]), 1)
    a2.imshow(img, cmap='gray', origin='upper'); a2.set_title('10 ms window at 50 ms', fontsize=10); a2.grid(False)
    a2.set_xlabel('x'); a2.set_ylabel('y')
    finish(f, 'b8_events')

@figure
def b8_quant():
    s = 8 / 255; zp = int(round(-128 - (-2.0) / s))
    x = np.linspace(-2, 6, 4001)
    q = np.clip(np.round(x / s) + zp, -128, 127)
    err = s * (q - zp) - x
    check('scale %.5f, zp %d (-64), max |err| inside %.4f (0.0157)' % (s, zp, np.abs(err[200:-200]).max()), zp == -64 and np.abs(err[200:-200]).max() < 0.0158)
    f, (a1, a2) = plt.subplots(2, 1, figsize=(8, 4.4), dpi=100, sharex=True, gridspec_kw={'height_ratios': [2, 1]})
    a1.plot(x, q, color=BLUE, drawstyle='steps-mid'); a1.set_ylabel('q (int8)')
    a1.plot([1.0, 3.3], [-32, 41], 'o', color=RED); a1.text(1.1, -45, '1.0 \u2192 \u221232', fontsize=9); a1.text(3.4, 30, '3.3 \u2192 41', fontsize=9)
    a2.plot(x, err, color=ORANGE, lw=0.8); a2.axhline(s / 2, color=GRAY, ls='--'); a2.axhline(-s / 2, color=GRAY, ls='--')
    a2.set_ylabel('error'); a2.set_xlabel('real value')
    finish(f, 'b8_quant')

# ---------------------------------------------------------------- Part V
@figure
def b8_bench():
    f, ax = canvas(8, 4.2, 100, 52)
    box(ax, 36, 38, 28, 10, 'PC: Python + PyVISA', fc=LIGHT['orange'], fs=10, bold=True)
    box(ax, 4, 16, 26, 10, 'function generator', fc=LIGHT['blue'], fs=9)
    box(ax, 70, 16, 26, 10, 'oscilloscope\nCH1 in, CH2 out', fc=LIGHT['blue'], fs=9)
    box(ax, 38, 2, 24, 9, 'RC low-pass\n10 k\u03a9, 10 nF', fc=LIGHT['green'], fs=9)
    arrow(ax, 40, 37.5, 20, 26.5, 'USB (SCPI)', fs=8, off=(-6, 0))
    arrow(ax, 60, 37.5, 80, 26.5, 'Ethernet (SCPI)', fs=8, off=(7, 0))
    arrow(ax, 17, 15.5, 37.5, 7, 'signal', fs=8, off=(-4, -3))
    arrow(ax, 62.5, 7, 76, 15.5, 'CH2', fs=8, off=(3, -3))
    arrow(ax, 30, 17, 69.5, 18.5, 'CH1', fs=8, ls='--')
    finish(f, 'b8_bench')

@figure
def b8_bode():
    R, C = 10e3, 10e-9
    fr = np.logspace(2, 5, 61)
    g = -10 * np.log10(1 + (2 * np.pi * fr * R * C) ** 2)
    i = np.where(g < -3.0103)[0][0]
    x = (-3.0103 - g[i - 1]) / (g[i] - g[i - 1])
    fc = 10 ** (np.log10(fr[i - 1]) + x * (np.log10(fr[i]) - np.log10(fr[i - 1])))
    check('sweep 61 points, corner %.1f Hz (1591.2), theory %.1f' % (fc, 1 / (2 * np.pi * R * C)), round(fc, 1) == 1591.2)
    f, ax = fig(8, 4.0)
    ax.semilogx(fr, g, 'o-', ms=3, color=BLUE)
    ax.axhline(-3.01, ls='--', color=GRAY); ax.axvline(fc, ls=':', color=RED)
    ax.text(fc * 1.1, -8, 'f_c = 1591 Hz', color=RED, fontsize=9)
    ax.set_xlabel('frequency (Hz)'); ax.set_ylabel('gain (dB)'); ax.grid(True, which='both', alpha=0.3)
    finish(f, 'b8_bode')

@figure
def b8_calib():
    ref = np.array([5.02, 10.11, 15.05, 20.00, 24.98, 30.04, 35.10])
    dut = np.array([5.61, 10.69, 15.52, 20.49, 25.38, 30.44, 35.43])
    gain, off = np.polyfit(dut, ref, 1)
    res = gain * dut + off - ref
    check('fit %.5f x %+.4f (1.00871, -0.6443); max resid %.3f (0.039)' % (gain, off, np.abs(res).max()),
          round(gain, 5) == 1.00871 and round(off, 4) == -0.6443 and round(np.abs(res).max(), 3) == 0.039)
    f, ax = fig(8, 4.0)
    ax.plot(ref, dut - ref, 'o', color=RED, label='raw error (mean +0.47 \u00b0C)')
    ax.plot(ref, res, 's', color=BLUE, label='after gain-and-offset correction')
    ax.axhline(0, color=GRAY, ls='--')
    ax.set_xlabel('reference temperature (\u00b0C)'); ax.set_ylabel('error (\u00b0C)'); ax.set_ylim(-0.1, 0.7); ax.legend(fontsize=9)
    finish(f, 'b8_calib')

@figure
def b8_threads():
    f, ax = canvas(8, 3.8, 100, 46)
    ax.add_patch(Rectangle((1, 25), 98, 18, fc=LIGHT['gray'], ec=GRAY)); ax.text(2, 40, 'thread-pool thread', fontsize=9, color=GRAY)
    ax.add_patch(Rectangle((1, 2), 98, 18, fc=LIGHT['blue'], ec=GRAY)); ax.text(2, 17, 'UI thread', fontsize=9, color=GRAY)
    box(ax, 6, 28, 18, 8, 'DataReceived', fs=9); box(ax, 30, 28, 16, 8, 'ReadLine', fs=9); box(ax, 52, 28, 16, 8, 'TryParse', fs=9)
    arrow(ax, 24.5, 32, 29.5, 32); arrow(ax, 46.5, 32, 51.5, 32)
    box(ax, 66, 5, 28, 8, 'Show: text + plot', fs=9, fc='white')
    arrow(ax, 68.5, 31, 78, 13.5, 'Dispatcher.BeginInvoke', fs=8, off=(8, 2), color=GREEN)
    arrow(ax, 60, 27.5, 42, 9, color=RED, ls='--')
    ax.text(38, 9, 'TextBlock.Text = ...', fontsize=8, color=RED, ha='right')
    ax.text(51, 17, '\u2716', fontsize=16, color=RED, ha='center', va='center')
    finish(f, 'b8_threads')

@figure
def b8_guardband():
    lo, hi = 3.30 * 0.97, 3.30 * 1.03
    check('limits %.3f..%.3f (3.201..3.399), guard %.3f..%.3f' % (lo, hi, lo + 0.01, hi - 0.01), round(lo, 3) == 3.201 and round(hi, 3) == 3.399)
    f, ax = fig(8, 2.8)
    ax.axvspan(lo, hi, ymin=0.15, ymax=0.85, color='#dddddd', label='specification 3.201 to 3.399 V')
    ax.axvspan(lo + 0.01, hi - 0.01, ymin=0.3, ymax=0.7, color=LIGHT['blue'], label='test limits 3.211 to 3.389 V')
    ax.errorbar([3.205], [0.5], xerr=[0.010], fmt='o', color=RED, capsize=4, label='reading 3.205 \u00b1 0.010 V')
    ax.set_xlim(3.17, 3.43); ax.set_ylim(0, 1); ax.set_yticks([]); ax.set_xlabel('rail voltage (V)')
    ax.legend(fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.32), ncol=3, frameon=False); ax.grid(axis='y', visible=False)
    finish(f, 'b8_guardband')

@figure
def b8_intrusion():
    pt = 40 * 10 / 115200 * 1e3
    check('printf 40 chars = %.2f ms (3.47)' % pt, round(pt, 2) == 3.47)
    f, ax = fig(8, 2.8)
    ax.barh(1, pt, color=RED, height=0.4); ax.text(pt + 0.05, 1, 'printf, 40 chars: 3.47 ms', va='center', fontsize=9)
    ax.text(0.02, 0.4, 'RAM trace / GPIO: measure target overhead', va='center', fontsize=9, color=BLUE)
    for k in range(5):
        ax.axvline(k, color=GRAY, ls='--', lw=0.8)
    ax.text(0.02, 1.45, 'loop deadlines every 1 ms', fontsize=8, color=GRAY)
    ax.set_xlim(0, 5.2); ax.set_ylim(0, 1.6); ax.set_yticks([]); ax.set_xlabel('time (ms)')
    finish(f, 'b8_intrusion')

@figure
def b8_sampling():
    T = 2.5
    t = np.linspace(0, 20, 20001)
    clk = ((t % T) < T / 2).astype(int)
    f, (a1, a2) = plt.subplots(2, 1, figsize=(8, 3.6), dpi=100, sharex=True)
    for ax, fs, c in ((a1, 1.0, RED), (a2, 8.0, BLUE)):
        ts = np.arange(0.3, 20, 1 / fs)
        cs = ((ts % T) < T / 2).astype(int)
        ax.plot(t, clk, color='#cccccc', lw=1)
        ax.step(ts, cs, where='post', color=c, lw=1.6)
        ax.set_yticks([]); ax.set_title('%g MS/s: %.1f samples per bit' % (fs, fs * T), fontsize=10)
    check('samples per bit at 1 and 8 MS/s: %.1f, %.0f' % (1 * T, 8 * T), True)
    a2.set_xlabel('time (\u00b5s), 400 kHz clock in gray')
    finish(f, 'b8_sampling')

@figure
def b8_pyramid():
    f, ax = canvas(8, 4.6, 100, 56)
    layers = [('host unit tests: ~400 checks, < 1 s', LIGHT['green'], 90), ('xUnit and integration tests: seconds', LIGHT['blue'], 68),
              ('HIL tests on the real board: ~11 s', LIGHT['orange'], 46), ('system test: days', LIGHT['red'], 24)]
    for k, (t, c, w) in enumerate(layers):
        y = 3 + k * 12
        ax.add_patch(Rectangle((50 - w / 2, y), w, 11, fc=c, ec=INK)); ax.text(50, y + 5.5, t, ha='center', va='center', fontsize=9.5)
    arrow(ax, 96, 5, 96, 50, color=RED); ax.text(93, 28, 'slower, more\nexpensive', rotation=90, ha='center', va='center', fontsize=8, color=RED)
    finish(f, 'b8_pyramid')

# ---------------------------------------------------------------- Part VI
@figure
def b8_ai_loop():
    f, ax = canvas(8, 4.6, 100, 56)
    nodes = [(12, 44, 'spec = prompt', LIGHT['blue']), (40, 44, 'assistant drafts\none module', LIGHT['gray']),
             (68, 44, 'review against\nchecklist', LIGHT['green']), (82, 24, 'build and\nunit test', LIGHT['green']),
             (60, 6, 'bench test\nwith scope', 'white'), (28, 6, 'commit', 'white'), (11, 24, 'document', LIGHT['blue'])]
    for x, y, t, c in nodes:
        w = 16 if 'assistant' not in t else 13
        box(ax, x - w / 2, y - 4, w, 8, t, fc=c, fs=8.5)
    seq = [0, 1, 2, 3, 4, 5, 6]
    for a, b in zip(seq, seq[1:]):
        (x0, y0, _, _), (x1, y1, _, _) = nodes[a], nodes[b]
        d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
        arrow(ax, x0 + ux * 9.5, y0 + uy * 5, x1 - ux * 9.5, y1 - uy * 5)
    box(ax, 30, 22, 22, 8, 'precise bug report', fc=LIGHT['red'], fs=8.5)
    arrow(ax, 55, 10.5, 47, 21.5, 'failure', color=RED, fs=8, off=(4, 0))
    arrow(ax, 41, 30.5, 40, 39.5, 'next prompt', color=RED, fs=8, off=(-6, 0))
    finish(f, 'b8_ai_loop')

@figure
def b8_trust():
    f, ax = canvas(8, 4.8, 100, 60)
    q = [(10, 30, 'review and test', LIGHT['orange'], 'UI logic, state machines'),
         (55, 30, 'check every line\nand measure', LIGHT['red'], 'pin map, I2C address, ISR,\nOTA security, charger, motor duty'),
         (10, 4, 'trust and run', LIGHT['green'], 'plot labels, test scaffolding'),
         (55, 4, 'test it', LIGHT['blue'], 'parser, log format, MQTT topic')]
    for x, y, t, c, ex in q:
        ax.add_patch(Rectangle((x, y), 43, 24, fc=c, ec=INK))
        ax.text(x + 21.5, y + 17, t, ha='center', va='center', fontsize=11, fontweight='bold')
        ax.text(x + 21.5, y + 6.5, ex, ha='center', va='center', fontsize=8.5)
    ax.text(54, 0.5, 'failure visible  \u2190  \u2192  failure silent', ha='center', fontsize=9)
    ax.text(5, 30, 'consequence low \u2192 high', rotation=90, ha='center', va='center', fontsize=9)
    finish(f, 'b8_trust')

def vcd_signals(path, names):
    """Minimal VCD reader: {name: [(time_ps, value_str), ...]} for the given reference names."""
    ids, out, t = {}, {n: [] for n in names}, 0
    with open(path) as fh:
        for line in fh:
            p = line.split()
            if not p:
                continue
            if p[0] == '$var' and p[4] in names and p[3] not in ids:
                ids[p[3]] = p[4]
            elif p[0].startswith('#'):
                t = int(p[0][1:])
            elif p[0][0] in '01xz' and len(p) == 1 and p[0][1:] in ids:
                out[ids[p[0][1:]]].append((t, p[0][0]))
            elif p[0][0] == 'b' and len(p) == 2 and p[1] in ids:
                out[ids[p[1]]].append((t, p[0][1:]))
    return out

VCD_DIR = os.path.join(HERE, 'vcd')   # written by the Chapter 26 testbenches

@figure
def b8_pwm_wave():
    s = vcd_signals(os.path.join(VCD_DIR, 'pwm.vcd'), ['duty', 'count', 'out'])
    def val(lst, t):
        v = '0'
        for tt, x in lst:
            if tt > t:
                break
            v = x
        return int(v, 2) if set(v) <= set('01') else 0
    starts = {}
    for tt, v in s['duty']:
        starts.setdefault(int(v, 2), tt)
    T = 37036   # ps per clock in the testbench
    f, (a1, a2) = plt.subplots(2, 1, figsize=(8, 4.0), dpi=100, sharex=True)
    def wrap_after(t):
        return next(tt for tt, v in s['count'] if tt > t and set(v) <= set('01') and int(v, 2) == 0)
    t0s = {64: wrap_after(starts[64] + T), 128: wrap_after(starts[128] + T)}
    xs = []
    for k, d in enumerate((64, 128)):
        base = t0s[d]
        ts = base + np.arange(0, 256 * T, T // 4)
        cnt = [val(s['count'], t) for t in ts]
        out = [val(s['out'], t) for t in ts]
        x = (ts - base) / 1e6 + k * (256 * T / 1e6 + 1.0)
        a1.plot(x, cnt, color=BLUE, lw=1); a2.step(x, out, where='post', color=GREEN)
        frac = sum(out) / len(out)
        xs.append(frac)
        a2.text(x[0] + 0.3, 1.1, 'duty %d: %.1f %%' % (d, frac * 100), fontsize=9)
        if k: a1.axvline(x[0] - 0.5, color=GRAY, ls=':'); a2.axvline(x[0] - 0.5, color=GRAY, ls=':')
    check('VCD PWM duty fractions %.3f (0.25), %.3f (0.50)' % tuple(xs), abs(xs[0] - 0.25) < 0.01 and abs(xs[1] - 0.5) < 0.01)
    a1.set_ylabel('count'); a2.set_ylabel('out'); a2.set_ylim(-0.2, 1.4); a2.set_yticks([0, 1])
    a2.set_xlabel('time (\u00b5s), 27 MHz clock, period 9.48 \u00b5s')
    finish(f, 'b8_pwm_wave')

@figure
def b8_uart_wave():
    s = vcd_signals(os.path.join(VCD_DIR, 'uart.vcd'), ['tx', 'data'])
    tx = [(t, v) for t, v in s['tx']]
    # find the frame for 0xA3: data changes to a3 then the next falling edge of tx
    t_data = next(t for t, v in s['data'] if set(v) <= set('01') and int(v, 2) == 0xA3)
    fall = next(t for (t, v) in tx if t >= t_data and v == '0')
    edges = [(t, int(v)) for t, v in tx if fall - 20e6 <= t <= fall + 100e6]
    bit = 234 * 37036
    samples = []
    for k in range(10):
        tm = fall + bit // 2 + k * bit
        v = 1
        for t, x in tx:
            if t > tm:
                break
            v = int(x) if x in '01' else v
        samples.append(v)
    data = sum(b << i for i, b in enumerate(samples[1:9]))
    check('VCD frame: start %d, data 0x%02X (0xA3), stop %d, bit %.3f us' % (samples[0], data, samples[9], bit / 1e6),
          samples[0] == 0 and data == 0xA3 and samples[9] == 1)
    f, ax = fig(8, 3.0)
    t0 = fall - 10e6
    tend = fall + 10 * bit
    ts = [t0] + [t for t, _ in edges if t0 < t < fall + 9.5 * bit] + [tend]
    vs = [1] + [v for t, v in edges if t0 < t < fall + 9.5 * bit]
    vs.append(vs[-1])
    ax.step((np.array(ts) - fall) / 1e6, vs, where='post', color=BLUE, lw=1.6)
    labels = ['start'] + ['D%d=%d' % (i, samples[i + 1]) for i in range(8)] + ['stop']
    for k, lab in enumerate(labels):
        ax.text((k + 0.5) * bit / 1e6, 1.2, lab, ha='center', fontsize=7.5)
    ax.set_ylim(-0.3, 1.5); ax.set_yticks([]); ax.set_xlabel('time from start bit (\u00b5s), 8.667 \u00b5s per bit, byte 0xA3')
    finish(f, 'b8_uart_wave')

@figure
def b8_hdl_flow():
    f, ax = canvas(8, 4.0, 100, 50)
    ax.text(1, 45, 'Firmware', fontweight='bold', fontsize=10)
    fw = ['write C', 'compile', 'flash', 'test', 'update in field']
    for k, t in enumerate(fw):
        box(ax, 2 + k * 19, 33, 15, 7, t, fc=LIGHT['blue'], fs=9)
        if k:
            arrow(ax, 2 + k * 19 - 3.6, 36.5, 2 + k * 19 - 0.6, 36.5)
    arrow(ax, 85, 32.5, 10, 32.5, color=GRAY, rad=-0.08, ls='--'); ax.text(47, 23.5, 'minutes per loop', fontsize=8, color=GRAY, ha='center')
    ax.text(1, 21, 'HDL', fontweight='bold', fontsize=10)
    hd = [('write\nVerilog', LIGHT['green']), ('simulate', LIGHT['green']), ('synthesize', LIGHT['green']), ('FPGA\nprototype', LIGHT['green']),
          ('place, route,\nsign-off', LIGHT['orange']), ('tapeout', LIGHT['orange']), ('fab\n6-9 months', LIGHT['orange'])]
    for k, (t, c) in enumerate(hd):
        box(ax, 1.5 + k * 14, 6, 11.5, 10, t, fc=c, fs=8)
        if k:
            arrow(ax, 1.5 + k * 14 - 2.2, 11, 1.5 + k * 14 - 0.4, 11)
    ax.axvline(70.5, ymin=0.05, ymax=0.38, color=RED, lw=3)
    ax.text(70.5, 1, 'no patches after this point', color=RED, fontsize=8, ha='center')
    finish(f, 'b8_hdl_flow')

if __name__ == '__main__':
    names = sys.argv[1:] or list(FIGS)
    for n in names:
        FIGS[n]()
    print('%d figures written to %s' % (len(names), OUT))
