# -*- coding: utf-8 -*-
"""Original figures for the four solvers Book 7 names.

These are drawings of the result each program is for. They are not screen
captures of ADS, HFSS, Momentum, or Sonnet, and they do not use those marks.
"""

import struct
import zlib
from pathlib import Path

OUT = Path(__file__).resolve().parent

# 5x7 uppercase glyphs, rows of 5 bits.
FONT = {
    " ": ["00000"] * 7,
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01110", "10001", "10000", "10111", "10001", "10001", "01110"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "J": ["00111", "00010", "00010", "00010", "00010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00100", "01100", "10100", "10100", "11111", "00100", "00100"],
    "5": ["11111", "10000", "10000", "11110", "00001", "00001", "11110"],
    "6": ["01110", "10000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00001", "01110"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    ":": ["00000", "01100", "01100", "00000", "01100", "01100", "00000"],
    "'": ["00100", "00100", "01000", "00000", "00000", "00000", "00000"],
}


class Canvas:
    def __init__(self, w, h, bg=(255, 255, 255)):
        self.w = w
        self.h = h
        self.buf = bytearray(bg * (w * h))
        self.bg = bg

    def put(self, x, y, rgb):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = (y * self.w + x) * 3
            self.buf[i : i + 3] = bytes(rgb)

    def rect(self, x, y, w, h, rgb):
        x0, y0 = int(x), int(y)
        for yy in range(y0, y0 + int(h)):
            for xx in range(x0, x0 + int(w)):
                self.put(xx, yy, rgb)

    def frame(self, x, y, w, h, rgb, t=2):
        self.rect(x, y, w, t, rgb)
        self.rect(x, y + h - t, w, t, rgb)
        self.rect(x, y, t, h, rgb)
        self.rect(x + w - t, y, t, h, rgb)

    def line(self, x0, y0, x1, y1, rgb, t=1):
        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
        dx, dy = abs(x1 - x0), abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        while True:
            for oy in range(-(t // 2), t // 2 + 1):
                for ox in range(-(t // 2), t // 2 + 1):
                    self.put(x0 + ox, y0 + oy, rgb)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def text(self, x, y, s, rgb, scale=3):
        cx = int(x)
        for ch in s.upper():
            glyph = FONT.get(ch, FONT[" "])
            for row, bits in enumerate(glyph):
                for col, bit in enumerate(bits):
                    if bit == "1":
                        self.rect(cx + col * scale, y + row * scale, scale, scale, rgb)
            cx += 6 * scale

    def png(self):
        raw = bytearray()
        row = self.w * 3
        for y in range(self.h):
            raw.append(0)
            start = y * row
            raw.extend(self.buf[start : start + row])

        def chunk(tag, data):
            return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

        ihdr = struct.pack(">IIBBBBB", self.w, self.h, 8, 2, 0, 0, 0)
        return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")


INK = (20, 24, 28)
BLUE = (0, 0, 180)
COPPER = (168, 96, 42)
GREEN = (214, 228, 206)
PAPER = (248, 248, 246)
MUTED = (80, 86, 94)
RED = (160, 40, 40)


def banner(c, title, subtitle):
    c.rect(0, 0, c.w, c.h, PAPER)
    c.rect(0, 0, c.w, 54, BLUE)
    c.text(16, 14, title, (255, 255, 255), 3)
    c.text(16, 68, subtitle, MUTED, 2)
    c.text(16, c.h - 28, "BOOK 7 DRAWING. NOT A CAPTURE OF THE PROGRAM.", MUTED, 2)


def fig_ads():
    c = Canvas(1100, 640, PAPER)
    banner(c, "ADS   HARMONIC BALANCE", "A PERIODIC SPECTRUM AT THE DRAIN. NOT A 3D MESH.")
    # schematic panel
    c.frame(24, 110, 500, 470, INK, 2)
    c.text(40, 124, "CIRCUIT", BLUE, 2)
    c.line(70, 300, 180, 300, INK, 3)
    c.rect(180, 270, 70, 60, (255, 255, 255))
    c.frame(180, 270, 70, 60, INK, 2)
    c.text(190, 290, "SRC", INK, 2)
    c.line(250, 300, 330, 300, INK, 3)
    # transistor
    c.line(330, 240, 330, 360, INK, 3)
    c.line(330, 270, 400, 240, INK, 3)
    c.line(330, 330, 400, 360, INK, 3)
    c.line(360, 250, 380, 230, INK, 2)
    c.text(410, 250, "DRAIN", BLUE, 2)
    c.line(400, 240, 460, 240, INK, 3)
    c.line(460, 210, 460, 390, INK, 3)
    c.text(400, 400, "LOAD", INK, 2)
    c.text(40, 500, "FUNDAMENTAL IN. LINES OUT.", MUTED, 2)
    # spectrum
    c.frame(560, 110, 516, 470, INK, 2)
    c.text(576, 124, "SPECTRUM AT THE DRAIN", BLUE, 2)
    base = 500
    c.line(600, base, 1020, base, INK, 2)
    bars = [(680, 280, "F0", "0 DB"), (800, 140, "2F0", "-15 DB"), (920, 70, "3F0", "")]
    for x, h, lab, db in bars:
        c.rect(x, base - h, 36, h, BLUE)
        c.text(x - 6, base + 16, lab, INK, 2)
        if db:
            c.text(x - 18, base - h - 28, db, RED, 2)
    c.text(600, 160, "15 DB IS THIS CHAPTER'S EXAMPLE.", MUTED, 2)
    return c.png()


def fig_hfss():
    c = Canvas(1100, 640, PAPER)
    banner(c, "HFSS   THREE-DIMENSIONAL METAL", "A CONNECTOR IN A CAGE. MESH THE GAP.")
    # isometric box, kept left so the checklist does not sit on the mesh
    ox, oy = 70, 170
    # front
    c.line(ox, oy + 80, ox + 360, oy + 80, INK, 3)
    c.line(ox, oy + 80, ox, oy + 320, INK, 3)
    c.line(ox + 360, oy + 80, ox + 360, oy + 320, INK, 3)
    c.line(ox, oy + 320, ox + 360, oy + 320, INK, 3)
    # top depth
    c.line(ox, oy + 80, ox + 120, oy, INK, 3)
    c.line(ox + 360, oy + 80, ox + 480, oy, INK, 3)
    c.line(ox + 120, oy, ox + 480, oy, INK, 3)
    c.line(ox + 480, oy, ox + 480, oy + 240, INK, 3)
    c.line(ox + 360, oy + 320, ox + 480, oy + 240, INK, 3)
    # mesh on front, tighter near a vertical gap
    for i in range(1, 8):
        x = ox + i * 45
        c.line(x, oy + 80, x, oy + 320, (170, 176, 186), 1)
    for j in range(1, 6):
        y = oy + 80 + j * 40
        c.line(ox, y, ox + 360, y, (170, 176, 186), 1)
    # dense mesh at gap
    gx = ox + 200
    for k in range(-4, 5):
        c.line(gx + k * 4, oy + 140, gx + k * 4, oy + 260, BLUE, 1)
    c.line(gx, oy + 150, gx + 70, oy + 130, RED, 3)
    c.text(gx - 20, oy + 96, "E AT THE GAP", RED, 2)
    # connector nub
    c.rect(ox + 150, oy + 300, 60, 28, COPPER)
    c.text(ox + 148, oy + 340, "PORT", INK, 2)
    c.text(680, 200, "ASK FOR:", BLUE, 3)
    c.text(680, 260, "MESH AT THE GAP", INK, 2)
    c.text(680, 300, "PORT MODE", INK, 2)
    c.text(680, 340, "CONVERGENCE", INK, 2)
    c.text(680, 420, "A COLOR PLOT ALONE", MUTED, 2)
    c.text(680, 450, "IS NOT THE RESULT.", MUTED, 2)
    return c.png()


def fig_momentum():
    c = Canvas(1100, 640, PAPER)
    banner(c, "MOMENTUM   CURRENTS ON LAYERS", "A TRACE OVER A PLANE. THE CAGE IS NOT IN THIS MODEL.")
    # stackup
    c.text(40, 120, "STACK", BLUE, 2)
    layers = [
        (160, 28, (230, 230, 220), "MASK"),
        (188, 18, COPPER, "TRACE"),
        (206, 70, GREEN, "DIELECTRIC"),
        (276, 16, COPPER, "GROUND"),
        (292, 70, GREEN, "CORE"),
    ]
    for y, h, col, name in layers:
        c.rect(40, y, 420, h, col)
        c.frame(40, y, 420, h, INK, 1)
        c.text(480, y + 2, name, INK, 2)
    # current arrows on a top view
    c.frame(40, 400, 620, 160, INK, 2)
    c.text(56, 412, "TOP VIEW", BLUE, 2)
    c.rect(120, 460, 400, 28, COPPER)
    for x in (180, 280, 380):
        c.line(x, 474, x + 40, 474, BLUE, 3)
        c.line(x + 40, 474, x + 28, 466, BLUE, 2)
        c.line(x + 40, 474, x + 28, 482, BLUE, 2)
    c.rect(90, 456, 24, 36, BLUE)
    c.rect(526, 456, 24, 36, BLUE)
    c.text(80, 500, "P1", INK, 2)
    c.text(530, 500, "P2", INK, 2)
    c.text(720, 200, "GOOD FOR", BLUE, 3)
    c.text(720, 260, "TRACE", INK, 2)
    c.text(720, 300, "PLANE", INK, 2)
    c.text(720, 340, "VIA FENCE", INK, 2)
    c.text(720, 410, "NOT A CONNECTOR", RED, 2)
    c.text(720, 444, "STANDING IN A CAGE", RED, 2)
    return c.png()


def fig_sonnet():
    c = Canvas(1100, 640, PAPER)
    banner(c, "SONNET   A STRIP IN A SHIELDED BOX", "THE BOX WALL IS PART OF THE MODEL.")
    # thick box
    c.rect(160, 150, 640, 360, (60, 64, 70))
    c.rect(190, 180, 580, 300, GREEN)
    c.rect(190, 300, 580, 22, COPPER)  # ground
    # strip
    c.rect(280, 250, 360, 22, COPPER)
    # ports as openings in the wall
    c.rect(150, 246, 50, 30, PAPER)
    c.rect(760, 246, 50, 30, PAPER)
    c.rect(168, 256, 140, 10, COPPER)
    c.rect(640, 256, 150, 10, COPPER)
    c.text(150, 120, "PORT 1", BLUE, 2)
    c.text(860, 210, "PORT 2", BLUE, 2)
    c.text(400, 210, "STRIP", INK, 2)
    c.text(400, 340, "SUBSTRATE INSIDE THE BOX", INK, 2)
    c.text(200, 530, "SIDEWALL PORTS. NOT AN OPEN SHEET OF AIR.", MUTED, 2)
    return c.png()


def main():
    figs = {
        "fig_ads.png": fig_ads,
        "fig_hfss.png": fig_hfss,
        "fig_momentum.png": fig_momentum,
        "fig_sonnet.png": fig_sonnet,
    }
    for name, fn in figs.items():
        path = OUT / name
        path.write_bytes(fn())
        print(path, path.stat().st_size)


if __name__ == "__main__":
    main()
