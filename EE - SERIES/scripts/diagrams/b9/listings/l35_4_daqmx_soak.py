"""Wait for the device under test to soak at its set temperature: read a type-K thermocouple
with NI-DAQmx at 10 S/s and return when the last 120 one-second means all lie within
±0.2 °C of the target. The same task in LabVIEW is DAQmx Create Channel, DAQmx Timing,
DAQmx Start Task, DAQmx Read in a While Loop, and DAQmx Clear Task."""
import collections
import time

import nidaqmx
from nidaqmx.constants import AcquisitionType, CJCSource, TemperatureUnits, ThermocoupleType


def wait_for_soak(channel, target_c, band_c=0.2, window_s=120, timeout_s=3600.0):
    recent = collections.deque(maxlen=window_s)          # one mean per second
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_thrmcpl_chan(
            channel, min_val=0.0, max_val=200.0, units=TemperatureUnits.DEG_C,
            thermocouple_type=ThermocoupleType.K, cjc_source=CJCSource.BUILT_IN)
        task.timing.cfg_samp_clk_timing(10.0, sample_mode=AcquisitionType.CONTINUOUS,
                                        samps_per_chan=1000)
        task.start()
        t0 = time.monotonic()
        while time.monotonic() - t0 < timeout_s:
            block = task.read(number_of_samples_per_channel=10)     # one second of data
            recent.append(sum(block) / len(block))
            if len(recent) == window_s and max(abs(t - target_c) for t in recent) <= band_c:
                return recent[-1], time.monotonic() - t0
    raise TimeoutError(f"no soak at {target_c} °C within {timeout_s:.0f} s")


if __name__ == "__main__":
    temp, waited = wait_for_soak("cDAQ1Mod1/ai0", 75.0)
    print(f"soaked at {temp:.2f} °C after {waited / 60:.1f} min")
