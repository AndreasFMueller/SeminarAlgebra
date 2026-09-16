#!/usr/bin/env python3
#
# troposkein-werte.py -- Profil y(x) = a*sn(x/c, k) des rotierenden
# Springseils zwischen den Punkten A=(-L,0) und B=(L,0).
#
# sn, cn, dn werden durch RK4-Integration des Systems
#   sn' = cn*dn,  cn' = -sn*dn,  dn' = -k^2*sn*cn
# mit sn(0)=0, cn(0)=1, dn(0)=1 berechnet (reines Standard-Python,
# keine Abhaengigkeiten). K(k) ueber das arithmetisch-geometrische
# Mittel, wie in ke-werte.py.
#
import math

k = 0.55
L = 2.30       # halbe Spannweite A-B
a = 1.05       # Amplitude der Woelbung


def kk(k):
    x = 1.0
    y = math.sqrt(1.0 - k * k)
    while abs(x - y) > 1e-15:
        x, y = 0.5 * (x + y), math.sqrt(x * y)
    return math.pi / (2.0 * x)


def sn_step(state, u_dummy, h):
    def deriv(s):
        sn, cn, dn = s
        return (cn * dn, -sn * dn, -k * k * sn * cn)

    s = state
    d1 = deriv(s)
    s2 = tuple(s[i] + 0.5 * h * d1[i] for i in range(3))
    d2 = deriv(s2)
    s3 = tuple(s[i] + 0.5 * h * d2[i] for i in range(3))
    d3 = deriv(s3)
    s4 = tuple(s[i] + h * d3[i] for i in range(3))
    d4 = deriv(s4)
    return tuple(
        s[i] + h / 6.0 * (d1[i] + 2 * d2[i] + 2 * d3[i] + d4[i])
        for i in range(3)
    )


def main():
    K = kk(k)
    u_max = 2.0 * K
    n_steps = 4000
    h = u_max / n_steps
    state = (0.0, 1.0, 1.0)
    samples = [(0.0, state[0])]
    for i in range(n_steps):
        state = sn_step(state, i * h, h)
        samples.append(((i + 1) * h, state[0]))

    n_out = 121
    with open("troposkein-werte.dat", "w") as f:
        for j in range(n_out):
            t = j / (n_out - 1)
            idx = round(t * n_steps)
            u, sn = samples[idx]
            x = -L + 2.0 * L * t
            y = a * sn
            f.write(f"{x:.6f} {y:.6f}\n")


if __name__ == "__main__":
    main()
