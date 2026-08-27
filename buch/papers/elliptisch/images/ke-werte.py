#!/usr/bin/env python3
#
# ke-werte.py -- Wertetabelle fuer K(k) und E(k), k in [0, 0.99]
#
# Berechnung ueber das arithmetisch-geometrische Mittel:
#   a_0 = 1, b_0 = sqrt(1 - k^2), a_{n+1} = (a_n + b_n)/2,
#   b_{n+1} = sqrt(a_n b_n)
#   K(k) = pi / (2 a_inf)
#   E(k) = K(k) * (1 - sum_{n>=0} 2^{n-1} (a_n^2 - b_n^2))
# Reines Standard-Python, keine Abhaengigkeiten (scipy nimmt m = k^2,
# darum wird hier direkt mit k gerechnet).
#
import math


def ellip_ke(k):
    a = 1.0
    b = math.sqrt(1.0 - k * k)
    s = 0.5 * (a * a - b * b)
    n = 1
    while n <= 50:
        a, b = 0.5 * (a + b), math.sqrt(a * b)
        d = a * a - b * b
        if d < 1e-15 * a * a:
            # d ist am Rundungsfehler-Floor angelangt, Beitrag vernachlaessigbar
            break
        s += 2.0 ** (n - 1) * d
        n += 1
    K = math.pi / (2.0 * a)
    E = K * (1.0 - s)
    return K, E


def main():
    ks = [i / 1000.0 for i in range(0, 991, 5)]
    with open("ke-werte.dat", "w") as f:
        f.write("k K E\n")
        for k in ks:
            K, E = ellip_ke(k)
            f.write(f"{k:.3f} {K:.6f} {E:.6f}\n")


if __name__ == "__main__":
    main()
