"""Small model helper used by the PC simulator in Listing 38.1.

Keep this function identical to the ``bjt_ic`` synthetic-device model in
Chapter 7, Listing 7.1. Copy this file beside ``l38_1_mini_tracer.py`` when
running that listing on a PC; a physical board uses the hardware backend.
"""

from __future__ import annotations

import math


def bjt_ic(vce: float, ib: float, beta: float = 200.0,
           va: float = 75.0, vsat: float = 0.08) -> float:
    """Return collector current from the Chapter 7 synthetic BJT model (A)."""
    return beta * ib * (1.0 + vce / va) * (1.0 - math.exp(-vce / vsat))
