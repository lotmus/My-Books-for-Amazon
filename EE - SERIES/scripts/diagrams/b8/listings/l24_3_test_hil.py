"""Hardware-in-the-loop tests with pytest: the real board on a serial port, checked from the PC.

Run: pytest l24_3_test_hil.py --port COM5      (needs conftest.py with the --port option)
"""
import time

import pytest
import serial

@pytest.fixture(scope="module")
def board(request):
    port = request.config.getoption("--port")
    with serial.Serial(port, 115200, timeout=2) as s:
        s.dtr = False                         # pulse reset on boards that wire DTR/RTS to EN
        s.rts = True
        time.sleep(0.1)
        s.rts = False
        time.sleep(2.0)                       # boot time
        s.reset_input_buffer()
        yield s

def read_reading(board):
    line = board.readline().decode("ascii", errors="replace").strip()
    t, h, p = (float(x) for x in line.split(","))
    return t, h, p

def test_sends_plausible_readings(board):
    for _ in range(3):
        t, h, p = read_reading(board)
        assert 10.0 < t < 40.0, f"temperature {t} not room temperature"
        assert 0.0 <= h <= 100.0
        assert 900.0 < p < 1100.0

def test_reading_interval(board):
    board.reset_input_buffer()
    board.readline()                          # synchronize to a line boundary
    t0 = time.monotonic()
    for _ in range(5):
        board.readline()
    interval = (time.monotonic() - t0) / 5
    assert interval == pytest.approx(1.0, abs=0.05)

def test_version_command(board):
    board.write(b"version\n")
    deadline = time.monotonic() + 2.0
    while time.monotonic() < deadline:
        line = board.readline().decode("ascii", errors="replace")
        if line.startswith("fw "):
            assert line.split()[1].count(".") == 2      # semantic version x.y.z
            return
    pytest.fail("no version reply within 2 s")
