"""Two-parameter calibration of a sensor against a reference: fit, residuals, and the correction."""
import numpy as np

# Paired readings: reference thermometer (degC) and the BME280 under test (degC).
ref = np.array([5.02, 10.11, 15.05, 20.00, 24.98, 30.04, 35.10])
dut = np.array([5.61, 10.69, 15.52, 20.49, 25.38, 30.44, 35.43])

gain, offset = np.polyfit(dut, ref, 1)          # ref = gain * dut + offset
corrected = gain * dut + offset
resid = corrected - ref
print("raw error: mean %+.3f, max %.3f degC" % (np.mean(dut - ref), np.max(np.abs(dut - ref))))
print("fit: ref = %.5f * dut %+.4f" % (gain, offset))
print("after correction: rms %.3f, max %.3f degC" % (np.sqrt(np.mean(resid ** 2)), np.max(np.abs(resid))))
