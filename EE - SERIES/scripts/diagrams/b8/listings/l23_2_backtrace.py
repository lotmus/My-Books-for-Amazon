"""Turn an ESP32-S3 panic backtrace into file:line with addr2line.

idf.py monitor does this automatically; this script is for a backtrace that arrived by
e-mail, in a field log, or from a customer's screenshot.
"""
import re
import subprocess
import sys

ADDR2LINE = "xtensa-esp32s3-elf-addr2line"       # from the ESP-IDF toolchain

def pcs_from_backtrace(text):
    """'Backtrace: 0x4200a1b2:0x3fc9a0e0 0x4200b3c4:0x3fc9a100' -> ['0x4200a1b2', '0x4200b3c4']."""
    m = re.search(r"Backtrace:((?:\s+0x[0-9a-fA-F]{8}:0x[0-9a-fA-F]{8})+)", text)
    if not m:
        return []
    return [pair.split(":")[0] for pair in m.group(1).split()]

def resolve(elf, pcs):
    out = subprocess.run([ADDR2LINE, "-pfiaC", "-e", elf, *pcs],
                         capture_output=True, text=True, check=True)
    return out.stdout.strip().splitlines()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: l23_2_backtrace.py build/app.elf panic.txt")
    pcs = pcs_from_backtrace(open(sys.argv[2], encoding="utf-8", errors="replace").read())
    if not pcs:
        sys.exit("no backtrace found")
    for line in resolve(sys.argv[1], pcs):
        print(line)
