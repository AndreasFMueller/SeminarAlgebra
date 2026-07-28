# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:00:29 2026

@author: noelk
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_transformed_grid(f, x_range=(-1, 1), y_range=(0, 2*np.pi), n_lines=15, res=500):
    """
    Zeichnet ausschließlich das transformierte Gitter einer komplexen Funktion f.
    """
    # 1. Gitter-Werte festlegen
    x_lines = np.linspace(x_range[0], x_range[1], n_lines)
    y_lines = np.linspace(y_range[0], y_range[1], n_lines)
    
    # 2. Auflösung der einzelnen Linien (für glatte Kurven)
    t_x = np.linspace(y_range[0], y_range[1], res)
    t_y = np.linspace(x_range[0], x_range[1], res)

    plt.figure(figsize=(10, 10))

    # 3. Vertikale Linien (x = const) transformieren und plotten
    # Bei exp(z) werden das die KREISE
    for x in x_lines:
        z = x + 1j * t_x
        w = f(z)
        plt.plot(w.real, w.imag, color='blue', lw=1, alpha=0.8)

    # 4. Horizontale Linien (y = const) transformieren und plotten
    # Bei exp(z) werden das die STRAHLEN
    for y in y_lines:
        z = t_y + 1j * y
        w = f(z)
        plt.plot(w.real, w.imag, color='red', lw=1, alpha=0.8)

    # Styling
    plt.title("Transformiertes Koordinatengitter (W-Ebene)")
    plt.xlabel("Re(w)")
    plt.ylabel("Im(w)")
    plt.gca().set_aspect('equal') # Wichtig für Winkeltreue
    plt.grid(True, linestyle=':', alpha=0.4)
    
    # Achsen-Limits automatisch sinnvoll setzen
    plt.show()

# --- Beispiele zum Ausprobieren ---

# Für exp(z): Ergibt Kreise (blau) und Strahlen (rot)
plot_transformed_grid(lambda z: 1/((z+1)*(z+2)), x_range=(-5, 5), y_range=(-5, 5), n_lines=400, res=10000)

# Für z^2: Ergibt orthogonale Hyperbeln
# plot_transformed_grid(lambda z: z**2, x_range=(-2, 2), y_range=(-2, 2))

# Für 1/z: Ergibt Kreise, die durch den Ursprung gehen
# plot_transformed_grid(lambda z: 1/z, x_range=(0.5, 2), y_range=(0.5, 2))