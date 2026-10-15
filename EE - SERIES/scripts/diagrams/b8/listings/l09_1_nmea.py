"""NMEA 0183 checksum and GGA parsing for the reader lab's GPS (runs on the PC or a Pi)."""

def nmea_checksum_ok(sentence: str) -> bool:
    """XOR of every character between '$' and '*' must equal the two hex digits after '*'."""
    if not sentence.startswith("$") or "*" not in sentence:
        return False
    body, _, given = sentence[1:].partition("*")
    calc = 0
    for ch in body:
        calc ^= ord(ch)
    return given[:2].upper() == "%02X" % calc

def parse_gga(sentence: str):
    """Return (lat_deg, lon_deg, fix_quality, satellites, altitude_m) or None."""
    if not nmea_checksum_ok(sentence):
        return None
    f = sentence.split("*")[0].split(",")
    if not f[0].endswith("GGA") or f[6] == "0":
        return None                                   # wrong type or no fix
    lat = int(f[2][:2]) + float(f[2][2:]) / 60        # ddmm.mmmm
    lon = int(f[4][:3]) + float(f[4][3:]) / 60        # dddmm.mmmm
    if f[3] == "S":
        lat = -lat
    if f[5] == "W":
        lon = -lon
    return lat, lon, int(f[6]), int(f[7]), float(f[9])

if __name__ == "__main__":
    s = "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
    print(nmea_checksum_ok(s), parse_gga(s))
    print(nmea_checksum_ok(s.replace("4807", "4808")))   # one corrupted digit -> False
