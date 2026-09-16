#
# besselj.py -- erzeugt die Datentabelle fuer die Abbildung mit
#               J_0, J_1 und J_2 auf dem Intervall [0,20]
#
# Aufruf: python3 besselj.py > besselj.dat
#
# (c) 2026 Gian Cavegn, OST Ostschweizer Fachhochschule
#
import numpy as np
from scipy.special import jv

x = np.arange(0.0, 20.0001, 0.05)
print("x J0 J1 J2")
for xi in x:
    print("%.4f %.6f %.6f %.6f" % (xi, jv(0, xi), jv(1, xi), jv(2, xi)))
