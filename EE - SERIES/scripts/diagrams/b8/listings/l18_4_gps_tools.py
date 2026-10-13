"""GPS helpers for the PC or the Pi: distance between fixes, and an RMC speed parser."""
import math

R_EARTH = 6_371_000.0   # mean Earth radius, m

def haversine_m(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi, dlmb = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlmb / 2) ** 2
    return 2 * R_EARTH * math.asin(math.sqrt(a))

def nmea_checksum_ok(sentence):
    body, _, given = sentence.strip().lstrip("$").partition("*")
    calc = 0
    for ch in body:
        calc ^= ord(ch)
    return given != "" and calc == int(given[:2], 16)

def rmc_speed_kmh(sentence):
    """Speed over ground from $GPRMC or $GNRMC, in km/h; None without a valid fix."""
    if not nmea_checksum_ok(sentence):
        return None
    f = sentence.split("*")[0].split(",")
    if not f[0].endswith("RMC") or f[2] != "A" or f[7] == "":
        return None
    return float(f[7]) * 1.852          # knots to km/h

if __name__ == "__main__":
    d = haversine_m(48.1173, 11.5167, 48.1374, 11.5755)
    print("GGA fix to Marienplatz: %.0f m" % d)
    print("1e-5 deg of latitude: %.2f m" % haversine_m(48.0, 11.0, 48.00001, 11.0))
    s = "$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A"
    print("RMC checksum ok:", nmea_checksum_ok(s), " speed %.1f km/h" % rmc_speed_kmh(s))
