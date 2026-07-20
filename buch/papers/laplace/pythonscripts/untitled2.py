# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:05:17 2026

@author: noelk
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_complex_contours(f, x_range=(-2, 2), y_range=(-2, 2), res=100, n_levels=20):
    # 1. Gitter in der Z-Ebene erstellen
    x = np.linspace(x_range[0], x_range[1], res)
    y = np.linspace(y_range[0], y_range[1], res)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # 2. Funktion anwenden
    W = f(Z)
    U = W.real
    V = W.imag

    # 3. Plotten
    plt.figure(figsize=(8, 8))
    
    # Linien für konstanten Realteil (entspricht vertikalen Linien in der W-Ebene)
    cp1 = plt.contour(X, Y, U, levels=n_levels, colors='blue', linewidths=1, alpha=0.7)
    # Linien für konstanten Imaginärteil (entspricht horizontalen Linien in der W-Ebene)
    cp2 = plt.contour(X, Y, V, levels=n_levels, colors='red', linewidths=1, alpha=0.7)

    plt.title(f"Isolinien von Re(f) und Im(f) in der Z-Ebene")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.gca().set_aspect('equal')
    plt.grid(True, linestyle=':', alpha=0.5)
    
    # Optionale Farblegende
    plt.clabel(cp1, inline=True, fontsize=8, fmt='%1.1f')
    
    plt.show()

# Beispiel: f(z) = z^2
plot_complex_contours(lambda z: np.log(z), res = 100, n_levels=90)


