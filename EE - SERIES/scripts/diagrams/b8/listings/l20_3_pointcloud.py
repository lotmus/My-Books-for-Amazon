"""Turn an 8 x 8 multizone ToF depth frame into a point cloud and fit the floor plane."""
import numpy as np

ZONES, FOV_DEG = 8, 45.0                     # VL53L5CX-class sensor: 8 x 8 zones, 45 x 45 deg

def zone_angles():
    step = np.radians(FOV_DEG) / ZONES
    a = (np.arange(ZONES) - (ZONES - 1) / 2) * step   # zone centers, radians
    return np.meshgrid(a, a)                           # azimuth (columns), elevation (rows)

def to_points(depth_mm):
    """Each zone reports range along its own ray; convert to x (right), y (up), z (forward), meters."""
    az, el = zone_angles()
    r = depth_mm / 1000.0
    x = r * np.cos(el) * np.sin(az)
    y = r * np.sin(el)
    z = r * np.cos(el) * np.cos(az)
    pts = np.stack([x, y, z], axis=-1).reshape(-1, 3)
    return pts[np.isfinite(pts).all(axis=1)]

def fit_plane(pts):
    """Least-squares plane through the points: returns unit normal and rms distance."""
    c = pts.mean(axis=0)
    _, _, vt = np.linalg.svd(pts - c)
    n = vt[-1]
    return n, float(np.sqrt(np.mean(((pts - c) @ n) ** 2)))

if __name__ == "__main__":
    # Synthetic frame: the sensor looks at a flat wall 1.000 m ahead, with 5 mm range noise.
    az, el = zone_angles()
    rng = np.random.default_rng(1)
    depth = 1000.0 / (np.cos(el) * np.cos(az)) + rng.normal(0, 5, (ZONES, ZONES))
    pts = to_points(depth)
    n, rms = fit_plane(pts)
    print("points:", len(pts), " corner zone range %.0f mm" % depth[0, 0])
    print("normal (%.3f, %.3f, %.3f), rms %.1f mm" % (*n, rms * 1000))
