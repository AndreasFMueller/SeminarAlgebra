#!/usr/bin/env python3
#
# pendel-werte.py -- relative Abweichung der exakten Schwingungsdauer
# von der Kleinwinkelnaeherung, in Prozent, ueber der Amplitude.
#
#   T(theta0) / T_0 = (2/pi) K(sin(theta0/2)),  T_0 = 2 pi sqrt(l/g)
#
# K ueber das arithmetisch-geometrische Mittel wie in ke-werte.py.
#
import math


def ellip_k(k):
    a = 1.0
    b = math.sqrt(1.0 - k * k)
    for _ in range(60):
        a, b = 0.5 * (a + b), math.sqrt(a * b)
    return math.pi / (2.0 * a)


def main():
    with open("pendel-werte.dat", "w") as f:
        f.write("theta abw\n")
        for i in range(0, 341):
            th = i * 0.5
            k = math.sin(math.radians(th) / 2.0)
            abw = 100.0 * (2.0 / math.pi * ellip_k(k) - 1.0)
            f.write(f"{th:.1f} {abw:.5f}\n")


if __name__ == "__main__":
    main()
