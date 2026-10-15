"""Per-subcarrier EVM of an OFDM signal (64-QAM, 30 kHz spacing, 3276 used subcarriers as in a 100 MHz
5G NR carrier) with three classic impairments: noise added after a band-limiting filter (edge subcarriers
lose SNR), a spur on one subcarrier (-60 dBc of the whole carrier), and phase noise (common phase error removed by the pilots, the rest
spreads as inter-carrier interference).

On an analyzer, the EVM-vs-subcarrier trace comes from the standard's demodulation personality; this
listing reproduces the shape so you can read one. Run:  python l31_1_ofdm_evm.py
"""
import math
import numpy as np

NFFT, USED, SCS = 4096, 3276, 30e3

def qam64(n, rng):
    lev = np.arange(-7, 8, 2)
    return (rng.choice(lev, n) + 1j * rng.choice(lev, n)) / math.sqrt(42)

def run(nsym=60, snr_db=40.0, edge_db=6.0, spur_dbc=-60.0, spur_sc=900, pn_rms_deg=0.3, seed=31):
    rng = np.random.default_rng(seed)
    k = np.arange(-USED // 2, USED // 2)                                  # subcarrier index (DC included)
    x = k / (USED / 2)
    h = 10 ** (-edge_db * x ** 8 / 20)                                      # filter droop toward the band edges
    err = np.zeros(USED); ref_p = 0.0
    for _ in range(nsym):
        S = qam64(USED, rng)
        X = np.zeros(NFFT, complex); X[k % NFFT] = S * h
        t = np.fft.ifft(X) * math.sqrt(NFFT)
        pn = np.cumsum(rng.normal(0, 1, NFFT)); pn = pn - pn.mean()
        pn *= math.radians(pn_rms_deg) / pn.std()
        t = t * np.exp(1j * pn)
        n = (rng.normal(0, 1, NFFT) + 1j * rng.normal(0, 1, NFFT)) * 10 ** (-snr_db / 20) / math.sqrt(2)
        p_avg = USED / NFFT                                                     # average carrier power per sample
        spur = math.sqrt(p_avg * 10 ** (spur_dbc / 10)) * np.exp(2j * np.pi * (spur_sc % NFFT) * np.arange(NFFT) / NFFT)
        t = t + n + spur                                                    # spur_dbc relative to the whole carrier
        Y = np.fft.fft(t) / math.sqrt(NFFT)
        R = Y[k % NFFT] / h                                                 # equalizer: known channel
        cpe = np.angle(np.vdot(S, R)); R = R * np.exp(-1j * cpe)            # pilots remove the common phase
        err += np.abs(R - S) ** 2
    evm_sc = np.sqrt(err / nsym)                                            # reference power is 1
    total = math.sqrt(np.mean(err / nsym))
    return k, 100 * evm_sc, 100 * total

if __name__ == '__main__':
    k, e, tot = run()
    mid = np.abs(k) < 400
    print('composite EVM %.2f %% (%.1f dB)' % (tot, 20 * math.log10(tot / 100)))
    print('center EVM %.2f %%, band-edge EVM %.2f %%, spur subcarrier %.1f %%'
          % (np.sqrt(np.mean(e[mid] ** 2)), np.sqrt(np.mean(e[np.abs(k) > 1600] ** 2)), e[k == 900][0]))
    print('NR limits (3GPP TS 38.104): 64-QAM 8 %, 256-QAM 3.5 %')
