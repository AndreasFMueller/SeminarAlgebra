#
# kepler.py -- erzeugt die Datentabelle fuer die Abbildung mit E-M als
#              Funktion von M fuer drei Exzentrizitaeten sowie die
#              Bessel-Reihe mit einem und mit drei Gliedern fuer epsilon=0.8
#
# Aufruf: python3 kepler.py > kepler.dat
#
# (c) 2026 Gian Cavegn, OST Ostschweizer Fachhochschule
#
import numpy as np
from scipy.special import jv

def kepler(M, e):
    # Newton-Iteration fuer E - e sin E = M
    E = M + e * np.sin(M)
    for _ in range(50):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return E

def reihe(M, e, N):
    return sum(2 * jv(n, n * e) / n * np.sin(n * M) for n in range(1, N + 1))

M = np.arange(0.0, 2 * np.pi + 1e-9, 0.01)
print("M d02 d05 d08 s1 s3")
for m in M:
    print("%.4f %.6f %.6f %.6f %.6f %.6f" % (
        m,
        kepler(m, 0.2) - m,
        kepler(m, 0.5) - m,
        kepler(m, 0.8) - m,
        reihe(m, 0.8, 1),
        reihe(m, 0.8, 3)))
