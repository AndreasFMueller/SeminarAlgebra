import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

def complex_to_rgb(z, alpha=1.0):
    """
    Mapping von komplexen Zahlen auf Farben:
    - Phase -> Farbe (Hue)
    - Amplitude -> Helligkeit (Value)
    """
    r = np.abs(z)
    arg = np.angle(z)
    
    # Hue: Map [-pi, pi] zu [0, 1]
    h = (arg + np.pi) / (2 * np.pi)
    
    # Saturation: Immer voll gesättigt für klare Farben
    s = np.ones_like(r)
    
    # Value (Helligkeit): Logarithmische Skalierung, damit Pole und Nullstellen sichtbar bleiben
    # v = 1 - 1/(1 + r) erzeugt einen schönen Verlauf
    v = 1 - 1 / (1 + r**0.5) 
    
    hsv = np.stack((h, s, v), axis=-1)
    return hsv_to_rgb(hsv)

# 1. Parameter für das Gitter (Bildbereich)
res = 800  # Auflösung
x_lim = [-2, 4]
y_lim = [-4, 4]

x = np.linspace(x_lim[0], x_lim[1], res)
y = np.linspace(y_lim[0], y_lim[1], res)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# 2. Definition einer Beispielfunktion F(s)
# Eine typische Funktion mit Polen, z.B. F(s) = 1 / ((s-1)*(s+1+2j)*(s+1-2j))
# Die Pole liegen bei s=1 und s=-1 +- 2j
F_z = 1 / ((Z - 1) * (Z + 1 + 2j) * (Z + 1 - 2j))

# 3. Bild erzeugen
img = complex_to_rgb(F_z)

fig, ax = plt.subplots(figsize=(8, 8), dpi=100)

# Hintergrund: Die komplexe Funktion
ax.imshow(img, extent=[x_lim[0], x_lim[1], y_lim[0], y_lim[1]], origin='lower', alpha=0.8)

# 4. Bromwich-Integrationsweg einzeichnen
gamma = 1.5  # Muss rechts von allen Polen liegen (hier Pole bei Re=-1 und Re=1)
ax.axvline(x=gamma, color='white', linestyle='--', linewidth=1, alpha=0.6)

# Den Weg mit Pfeilen markieren
arrow_y = [-3, 0, 3]
for ay in arrow_y:
    ax.annotate('', xy=(gamma, ay+0.5), xytext=(gamma, ay),
                arrowprops=dict(arrowstyle='->', color='yellow', lw=2))

# 5. Achsen und Beschriftung (TikZ-ähnlicher Stil)
ax.axhline(0, color='white', lw=0.5)
ax.axvline(0, color='white', lw=0.5)

ax.set_xlabel(r'Re($s$)')
ax.set_ylabel(r'Im($s$)')
ax.set_title(r'Domain Coloring von $F(s)$ mit Bromwich-Weg')

# Markierung der Pole (Singularitäten)
poles = [1, -1+2j, -1-2j]
ax.scatter([p.real for p in poles], [p.imag for p in poles], 
           marker='x', color='red', s=100, label='Pole')

# Beschriftung des Integrationswegs
ax.text(gamma + 0.1, 3.5, r'$s = \gamma + i\omega$', color='yellow', fontweight='bold')

plt.legend()
plt.tight_layout()
plt.show()