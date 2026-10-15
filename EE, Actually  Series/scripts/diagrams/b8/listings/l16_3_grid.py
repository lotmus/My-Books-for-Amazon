"""Occupancy grid from range readings: the mapping half of SLAM, with known robot poses."""
import math

CELL = 0.05                    # 5 cm cells
SIZE = 40                      # 2 m x 2 m map
L_HIT = math.log(0.7 / 0.3)    # +0.847: evidence that a cell is occupied
L_MISS = math.log(0.4 / 0.6)   # -0.405: evidence that a cell is free
grid = [[0.0] * SIZE for _ in range(SIZE)]   # log-odds, 0 = unknown (p = 0.5)

def update(x, y, heading_deg, rng):
    """Walk the beam from the robot at (x, y) meters; mark free cells and the hit cell."""
    h = math.radians(heading_deg)
    steps = int(rng / CELL)
    for s in range(steps + 1):
        cx = int((x + s * CELL * math.cos(h)) / CELL)
        cy = int((y + s * CELL * math.sin(h)) / CELL)
        if not (0 <= cx < SIZE and 0 <= cy < SIZE):
            return
        grid[cy][cx] += L_HIT if s == steps else L_MISS

def prob(l):
    return 1.0 - 1.0 / (1.0 + math.exp(l))

# Three readings from a ToF sensor, robot at (0.5 m, 1.0 m) facing a wall at x = 1.5 m.
for _ in range(3):
    update(0.5, 1.0, 0.0, 1.0)
print("wall cell p = %.3f, free cell p = %.3f" % (prob(grid[20][30]), prob(grid[20][20])))
