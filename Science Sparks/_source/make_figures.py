# -*- coding: utf-8 -*-
"""Draw the book's line figures into _source/figures/ (grayscale, 300 dpi, print-safe).

Usage: python make_figures.py
"""
import os
from math import comb

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Georgia', 'DejaVu Serif'],
    'font.size': 10,
    'axes.edgecolor': '#333333',
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.6,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})
INK, MID, LIGHT = '#111111', '#666666', '#bbbbbb'


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + '.png'), facecolor='white')
    plt.close(fig)
    print('wrote', name)


def light_cone():
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    x = np.linspace(-1, 1, 2)
    ax.plot(x, x, color=INK)
    ax.plot(x, -x, color=INK)
    ax.fill_between([-1, 0, 1], [1, 0, 1], [1, 1, 1], color=LIGHT, alpha=0.5)
    ax.fill_between([-1, 0, 1], [-1, 0, -1], [-1, -1, -1], color=LIGHT, alpha=0.5)
    ax.plot([0], [0], 'o', color=INK)
    ax.text(0.05, -0.08, 'here, now', fontsize=9)
    ax.text(0, 0.72, 'future\n(can be affected)', ha='center', fontsize=9)
    ax.text(0, -0.82, 'past\n(could have affected you)', ha='center', fontsize=9)
    ax.text(0.62, 0.05, 'elsewhere', ha='center', fontsize=9, color=MID)
    ax.text(-0.62, 0.05, 'elsewhere', ha='center', fontsize=9, color=MID)
    ax.text(0.78, 0.86, 'light', rotation=45, fontsize=8, color=MID)
    ax.set_xlim(-1, 1); ax.set_ylim(-1, 1)
    ax.set_xlabel('space'); ax.set_ylabel('time')
    ax.set_xticks([]); ax.set_yticks([])
    save(fig, 'light_cone')


def simultaneity():
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    v = 0.5
    s = np.linspace(-0.2, 1.6, 2)
    for c in (0.8, 0.3):
        ax.plot(s, v * s + c, color=MID, ls='--', lw=1.1)
    ax.axhline(1.0, color=INK, lw=1.2)
    ax.plot([0.4, 1.4], [1.0, 1.0], 'o', color=INK)
    ax.text(0.33, 1.05, 'A', fontsize=10); ax.text(1.36, 1.05, 'B', fontsize=10)
    ax.text(0.95, 0.52, "the moving observer's\n'same moment' lines:\nB comes first", fontsize=8, color=MID)
    ax.text(0.98, 1.17, "your 'same moment':\nA and B together", fontsize=8)
    ax.plot([0, 0.55], [0, 1.1], color=MID, lw=1)
    ax.text(0.52, 1.13, 'moving observer', fontsize=8, color=MID)
    ax.set_xlim(-0.2, 1.6); ax.set_ylim(-0.1, 1.42)
    ax.set_xlabel('space'); ax.set_ylabel('time')
    ax.set_xticks([]); ax.set_yticks([])
    save(fig, 'simultaneity')


def entropy_coins():
    k = np.arange(101)
    ways = np.array([comb(100, int(i)) for i in k], dtype=float)
    fig, ax = plt.subplots(figsize=(5.6, 3.0))
    ax.bar(k, ways / ways.max(), width=1.0, color=MID)
    ax.set_xlabel('number of heads among 100 coins')
    ax.set_ylabel('ways to get it\n(relative to the peak)')
    ax.annotate('all heads: exactly 1 way', xy=(100, 0.01), xytext=(68, 0.6), fontsize=8,
                arrowprops=dict(arrowstyle='->', color=INK, lw=0.8))
    ax.annotate('50 heads: about 10^29 ways', xy=(50, 1.0), xytext=(4, 0.85), fontsize=8,
                arrowprops=dict(arrowstyle='->', color=INK, lw=0.8))
    save(fig, 'entropy_coins')


def hubble():
    rng = np.random.default_rng(3)
    d = np.sort(rng.uniform(20, 400, 26))
    v = 70 * d * (1 + rng.normal(0, 0.07, d.size))
    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    ax.plot(d, v / 1000, 'o', color=MID, ms=4)
    dd = np.linspace(0, 420, 2)
    ax.plot(dd, 70 * dd / 1000, color=INK)
    ax.set_xlabel('distance (millions of parsecs)')
    ax.set_ylabel('recession speed\n(thousands of km/s)')
    ax.text(30, 25, 'slope: about 70 km/s for every megaparsec', fontsize=8)
    ax.text(250, 3, 'schematic data', fontsize=7, color=MID)
    save(fig, 'hubble')


def cosmic_timeline():
    yr = 3.156e7
    events = [(1, 'neutrinos\nstop interacting\n(1 second)'),
              (180, 'first nuclei\n(3 minutes)'),
              (380000 * yr, 'light set free:\nthe microwave\nbackground\n(380,000 years)'),
              (2e8 * yr, 'first stars\n(~200 million\nyears)'),
              (9.2e9 * yr, 'the Sun\n(9.2 billion\nyears)'),
              (13.8e9 * yr, 'now\n(13.8 billion\nyears)')]
    fig, ax = plt.subplots(figsize=(6.2, 2.4))
    ax.set_xscale('log')
    ax.axhline(0, color=INK, lw=1)
    for i, (t, label) in enumerate(events):
        ax.plot([t], [0], 'o', color=INK, ms=5)
        y = 0.25 if i % 2 == 0 else -0.25
        ax.text(t, y, label, ha='center', va='bottom' if y > 0 else 'top', fontsize=7.5)
    ax.set_ylim(-1.2, 1.2); ax.set_xlim(0.3, 3e18)
    ax.set_yticks([]); ax.spines['left'].set_visible(False)
    ax.set_xlabel('time since the hot Big Bang (seconds, logarithmic)')
    save(fig, 'cosmic_timeline')


def double_slit():
    x = np.linspace(-1, 1, 2000)
    env = np.sinc(2.2 * x) ** 2
    fringes = env * np.cos(np.pi * 9 * x) ** 2
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 3.6), sharex=True)
    a1.plot(x, fringes, color=INK, lw=1.1)
    a1.set_title('no record of which opening: stripes', fontsize=9, loc='left')
    a2.plot(x, env / 2, color=INK, lw=1.1)
    a2.set_title('which-opening record kept: the stripes are gone', fontsize=9, loc='left')
    for a in (a1, a2):
        a.set_yticks([]); a.set_ylabel('hits')
    a2.set_xlabel('position on the screen')
    a2.set_xticks([])
    fig.tight_layout()
    save(fig, 'double_slit')


def fourier_budget():
    t = np.linspace(-6, 6, 3000)
    w = np.linspace(-12, 12, 3000)
    fig, ax = plt.subplots(2, 2, figsize=(5.8, 3.6))
    for row, (sig, name) in enumerate([(0.35, 'a click'), (2.5, 'a long note')]):
        wave = np.exp(-t ** 2 / (2 * sig ** 2)) * np.cos(5 * t)
        spec = np.exp(-((w - 5) ** 2) * sig ** 2 / 2) + np.exp(-((w + 5) ** 2) * sig ** 2 / 2)
        ax[row, 0].plot(t, wave, color=INK, lw=0.9)
        ax[row, 1].plot(w[w > 0], spec[w > 0], color=INK)
        ax[row, 0].set_ylabel(name, fontsize=9)
        for a in ax[row]:
            a.set_yticks([]); a.set_xticks([])
    ax[0, 0].set_title('in time (or position)', fontsize=9)
    ax[0, 1].set_title('in pitch (or momentum)', fontsize=9)
    ax[1, 0].set_xlabel('narrow here ...'); ax[1, 1].set_xlabel('... means wide there')
    fig.tight_layout()
    save(fig, 'fourier_budget')


def stern_gerlach():
    rng = np.random.default_rng(7)
    smear = rng.uniform(-1, 1, 6000)
    spots = np.concatenate([rng.normal(-0.6, 0.06, 3000), rng.normal(0.6, 0.06, 3000)])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(5.6, 2.4), sharey=True)
    a1.hist(smear, bins=60, color=LIGHT, edgecolor=MID, lw=0.3)
    a1.set_title('expected: a smear', fontsize=9)
    a2.hist(spots, bins=60, color=MID)
    a2.set_title('found in 1922: two spots', fontsize=9)
    for a in (a1, a2):
        a.set_yticks([]); a.set_xticks([]); a.set_xlabel('deflection')
    a1.set_ylabel('silver atoms')
    fig.tight_layout()
    save(fig, 'stern_gerlach')


def bell_ceiling():
    fig, ax = plt.subplots(figsize=(4.8, 3.0))
    names = ['local prewritten\nanswers (max)', 'quantum mechanics\n(max)', 'pure algebra\n(max)']
    vals = [2, 2 * np.sqrt(2), 4]
    bars = ax.bar(names, vals, color=[LIGHT, MID, 'white'], edgecolor=INK, lw=0.8)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.07, '%.2f' % v, ha='center', fontsize=9)
    ax.set_ylabel('CHSH score')
    ax.set_ylim(0, 4.5)
    ax.text(1, 3.35, 'about 41% above\nthe local ceiling', ha='center', fontsize=8)
    save(fig, 'bell_ceiling')


def decoherence():
    t = np.linspace(0, 5, 400)
    fig, ax = plt.subplots(figsize=(5.0, 2.9))
    for tau, ls, lab in [(3.0, '-', 'well isolated'), (1.0, '--', 'a few stray photons'),
                         (0.15, ':', 'a warm, crowded room')]:
        ax.plot(t, np.exp(-t / tau), color=INK, ls=ls, label=lab)
    ax.set_xlabel('time (arbitrary units)')
    ax.set_ylabel('stripe contrast')
    ax.legend(frameon=False, fontsize=8)
    ax.text(3.6, 0.9, 'schematic', fontsize=7, color=MID)
    save(fig, 'decoherence')


def zeno():
    n = np.arange(1, 41)
    p = np.cos(np.pi / (2 * n)) ** (2 * n)
    fig, ax = plt.subplots(figsize=(5.0, 2.9))
    ax.plot(n, p, 'o-', color=INK, ms=3, lw=1)
    ax.set_xlabel('number of checks during the change')
    ax.set_ylabel('chance the system\nhas not changed')
    ax.set_ylim(0, 1.02)
    ax.text(12, 0.3, 'one check at the end: it has always changed.\nforty checks: it almost never has.', fontsize=8)
    save(fig, 'zeno')


def hawking():
    m = np.logspace(-10, 2, 200)
    T = 6.17e-8 / m
    fig, ax = plt.subplots(figsize=(5.2, 3.2))
    ax.loglog(m, T, color=INK)
    ax.axhline(2.725, color=MID, ls='--', lw=1)
    ax.text(2e-5, 6.0, 'temperature of the microwave sky, 2.7 K', fontsize=8, color=MID)
    ax.plot([1], [6.17e-8], 'o', color=INK)
    ax.text(1.5, 1.2e-7, 'one Sun: 0.00000006 K', fontsize=8)
    ax.plot([3.7e-8], [6.17e-8 / 3.7e-8], 'o', color=INK)
    ax.text(8e-8, 0.25, 'one Moon: 1.7 K', fontsize=8)
    ax.set_xlabel('mass of the black hole (in Suns)')
    ax.set_ylabel('Hawking temperature (kelvin)')
    save(fig, 'hawking')


def bands():
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    cols = [('insulator', 0.0, 5.5), ('semiconductor', 1.6, 1.1), ('conductor', 3.2, -0.4)]
    for name, x0, gap in cols:
        ax.add_patch(plt.Rectangle((x0, 0), 1.0, 1.0, color=MID))
        top = 1.0 + max(gap, 0) * 0.35 if gap > 0 else 0.86
        ax.add_patch(plt.Rectangle((x0, top), 1.0, 1.0, fill=False, edgecolor=INK, lw=1))
        if gap > 0:
            ax.annotate('', xy=(x0 + 0.5, top), xytext=(x0 + 0.5, 1.0),
                        arrowprops=dict(arrowstyle='<->', color=INK, lw=0.8))
            ax.text(x0 + 0.55, 1.0 + (top - 1.0) / 2, '%s eV' % ('~5.5' if gap > 2 else '1.1'),
                    fontsize=8, va='center')
        ax.text(x0 + 0.5, -0.25, name, ha='center', fontsize=9)
    ax.text(4.35, 0.5, 'filled', fontsize=8, va='center')
    ax.text(4.35, 1.4, 'empty', fontsize=8, va='center')
    ax.set_xlim(-0.1, 5.0); ax.set_ylim(-0.4, 4.05)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_ylabel('electron energy')
    ax.spines['bottom'].set_visible(False)
    save(fig, 'bands')


def feynman():
    fig, ax = plt.subplots(figsize=(3.6, 3.4))
    ax.plot([0.2, 0.4, 0.2], [0.0, 0.5, 1.0], color=INK)
    ax.plot([1.0, 0.8, 1.0], [0.0, 0.5, 1.0], color=INK)
    for x0, y0, x1, y1 in [(0.2, 0.0, 0.3, 0.25), (0.4, 0.5, 0.3, 0.75), (1.0, 0.0, 0.9, 0.25), (0.8, 0.5, 0.9, 0.75)]:
        ax.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle='->', color=INK, lw=1))
    xs = np.linspace(0.4, 0.8, 200)
    ax.plot(xs, 0.5 + 0.03 * np.sin((xs - 0.4) * 2 * np.pi * 7.5), color=INK, lw=1.2)
    ax.text(0.6, 0.57, 'photon', ha='center', fontsize=9)
    ax.text(0.12, 0.02, 'electron', fontsize=8); ax.text(0.86, 0.02, 'electron', fontsize=8)
    ax.annotate('time', xy=(0.05, 0.95), xytext=(0.05, 0.55), fontsize=8,
                arrowprops=dict(arrowstyle='->', color=MID, lw=0.8))
    ax.set_xlim(0, 1.1); ax.set_ylim(-0.08, 1.05)
    ax.axis('off')
    save(fig, 'feynman')


def drift_selection():
    rng = np.random.default_rng(11)
    gens = 200
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.0, 2.8), sharey=True)
    for _ in range(8):
        p, path = 0.5, []
        for _g in range(gens):
            p = rng.binomial(50, p) / 50
            path.append(p)
        a1.plot(path, color=MID, lw=0.9)
    a1.set_title('no advantage, 50 individuals:\nluck decides', fontsize=9)
    for _ in range(8):
        p, path, s = 0.05, [], 0.05
        for _g in range(gens):
            p = p * (1 + s) / (1 + s * p)
            p = rng.binomial(5000, p) / 5000
            path.append(p)
        a2.plot(path, color=INK, lw=0.9)
    a2.set_title('5% advantage, 5,000 individuals:\nselection decides', fontsize=9)
    for a in (a1, a2):
        a.set_xlabel('generations')
    a1.set_ylabel('share of the population\ncarrying the variant')
    fig.tight_layout()
    save(fig, 'drift_selection')


def codons():
    counts = [('Leu', 6), ('Ser', 6), ('Arg', 6), ('Ala', 4), ('Gly', 4), ('Pro', 4), ('Thr', 4),
              ('Val', 4), ('Ile', 3), ('stop', 3), ('Asn', 2), ('Asp', 2), ('Cys', 2), ('Gln', 2),
              ('Glu', 2), ('His', 2), ('Lys', 2), ('Phe', 2), ('Tyr', 2), ('Met', 1), ('Trp', 1)]
    assert sum(c for _, c in counts) == 64
    fig, ax = plt.subplots(figsize=(6.0, 2.8))
    ax.bar([n for n, _ in counts], [c for _, c in counts],
           color=[MID if n != 'stop' else 'white' for n, _ in counts], edgecolor=INK, lw=0.6)
    ax.set_ylabel('three-letter words\nthat mean it')
    ax.set_xlabel('amino acid (and the stop signal)')
    plt.setp(ax.get_xticklabels(), rotation=60, fontsize=8)
    ax.text(10.5, 5.3, '64 words, 20 meanings plus "stop"', fontsize=8)
    save(fig, 'codons')


def unit_circle():
    th = np.linspace(0, 2 * np.pi, 400)
    a = np.deg2rad(35)
    fig, ax = plt.subplots(figsize=(3.8, 3.8))
    ax.plot(np.cos(th), np.sin(th), color=INK, lw=1)
    ax.axhline(0, color=LIGHT, lw=0.8); ax.axvline(0, color=LIGHT, lw=0.8)
    ax.plot([0, np.cos(a)], [0, np.sin(a)], color=INK)
    ax.plot([np.cos(a), np.cos(a)], [0, np.sin(a)], color=MID, ls='--')
    ax.text(np.cos(a) / 2, -0.12, 'cos', ha='center', fontsize=9)
    ax.text(np.cos(a) + 0.05, np.sin(a) / 2, 'sin', fontsize=9)
    ax.text(0.5, 0.42, '1', fontsize=9)
    ax.text(0.17, 0.04, 'angle', fontsize=8)
    ax.set_aspect('equal'); ax.axis('off')
    save(fig, 'unit_circle')


def tangent():
    x = np.linspace(-0.5, 2.2, 300)
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    ax.plot(x, x ** 2, color=INK, label='y = x squared')
    ax.plot(x, 2 * x - 1, color=MID, ls='--', label='tangent at x = 1, slope 2')
    ax.plot([1], [1], 'o', color=INK)
    ax.legend(frameon=False, fontsize=8)
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save(fig, 'tangent')


def area():
    x = np.linspace(0, 3.4, 300)
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    ax.plot(x, x ** 2, color=INK)
    xs = np.linspace(0, 3, 300)
    ax.fill_between(xs, xs ** 2, color=LIGHT)
    ax.text(2.0, 1.2, 'area = 9', fontsize=10)
    ax.set_xlabel('x'); ax.set_ylabel('y = x squared')
    save(fig, 'area')


def square_wave():
    x = np.linspace(0, 2 * np.pi, 2000)
    fig, ax = plt.subplots(figsize=(5.6, 3.0))
    ax.plot(x, np.sign(np.sin(x)), color=LIGHT, lw=2.5, label='target: a square wave')
    for n, ls in [(1, ':'), (3, '--'), (15, '-')]:
        y = sum(np.sin((2 * k - 1) * x) / (2 * k - 1) for k in range(1, n + 1)) * 4 / np.pi
        ax.plot(x, y, color=INK, ls=ls, lw=1, label='%d sine wave%s' % (n, '' if n == 1 else 's'))
    ax.legend(frameon=False, fontsize=8, loc='lower left')
    ax.set_xticks([]); ax.set_yticks([-1, 0, 1])
    ax.set_xlabel('one period')
    save(fig, 'square_wave')


def rc_charge():
    t = np.linspace(0, 5, 400)
    fig, ax = plt.subplots(figsize=(5.0, 3.0))
    ax.plot(t, 1 - np.exp(-t), color=INK)
    for k in (1, 2, 3, 5):
        v = 1 - np.exp(-k)
        ax.plot([k], [v], 'o', color=INK, ms=4)
        ax.text(k + 0.06, v - 0.09, '%d%%' % round(100 * v) if k < 5 else '99%', fontsize=8)
    ax.set_xlabel('time, in units of R times C')
    ax.set_ylabel('capacitor voltage\n(share of the supply)')
    ax.set_ylim(0, 1.08)
    save(fig, 'rc_charge')


def phasor():
    a = np.deg2rad(50)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.0, 2.6), gridspec_kw={'width_ratios': [1, 2]})
    th = np.linspace(0, 2 * np.pi, 300)
    a1.plot(np.cos(th), np.sin(th), color=LIGHT)
    a1.annotate('', xy=(np.cos(a), np.sin(a)), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=INK, lw=1.4))
    a1.plot([np.cos(a), 1.6], [np.sin(a), np.sin(a)], color=MID, ls=':')
    a1.set_aspect('equal'); a1.axis('off')
    a1.set_title('a rotating arrow', fontsize=9)
    t = np.linspace(0, 2 * np.pi, 300)
    a2.plot(t, np.sin(t + a), color=INK)
    a2.plot([0], [np.sin(a)], 'o', color=INK)
    a2.axhline(0, color=LIGHT, lw=0.8)
    a2.set_title('its shadow: the sinusoid', fontsize=9)
    a2.set_xticks([]); a2.set_yticks([])
    fig.tight_layout()
    save(fig, 'phasor')


def human_timeline():
    events = [(7e6, 'human and\nchimp lines split'), (3.3e6, 'stone tools'),
              (1e6, 'kept fire'), (3e5, 'Homo sapiens'), (6.5e4, 'Australia'),
              (1.2e4, 'farming'), (5.2e3, 'writing'), (265, 'steam'), (57, 'the Moon')]
    fig, ax = plt.subplots(figsize=(6.2, 2.4))
    ax.set_xscale('log')
    ax.axhline(0, color=INK, lw=1)
    for i, (t, label) in enumerate(events):
        ax.plot([t], [0], 'o', color=INK, ms=4.5)
        y = 0.22 if i % 2 == 0 else -0.22
        ax.text(t, y, label, ha='center', va='bottom' if y > 0 else 'top', fontsize=7.5)
    ax.set_xlim(2e7, 20)
    ax.set_ylim(-1.0, 1.0); ax.set_yticks([]); ax.spines['left'].set_visible(False)
    ax.set_xlabel('years ago (logarithmic)')
    save(fig, 'human_timeline')


if __name__ == '__main__':
    for f in (light_cone, simultaneity, entropy_coins, hubble, cosmic_timeline, double_slit,
              fourier_budget, stern_gerlach, bell_ceiling, decoherence, zeno, hawking, bands,
              feynman, drift_selection, codons, unit_circle, tangent, area, square_wave,
              rc_charge, phasor, human_timeline):
        f()
