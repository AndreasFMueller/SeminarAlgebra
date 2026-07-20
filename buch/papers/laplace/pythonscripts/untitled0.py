import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb

# 1. Parameter für den Bereich
x_min, x_max = -8, 6
y_min, y_max = -8, 8
res = 800

sigma = np.linspace(x_min, x_max, res)
omega = np.linspace(y_min, y_max, res)
Sigma, Omega = np.meshgrid(sigma, omega)
S = Sigma + 1j * Omega

# 2. Funktion mit 3 Polen definieren
p1 = 1 + 0j
p2 = -2 + 3j
p3 = -2 - 3j
F_s = 10 / ((S - p1) * (S - p2) * (S - p3))

# 3. Domain Coloring (Phase als Hintergrund)
H = (np.angle(F_s) + np.pi) / (2 * np.pi)
S_val = np.ones_like(H) * 0.4  # Dezentere Farben
V_val = np.ones_like(H) * 0.95 
img = hsv_to_rgb(np.stack((H, S_val, V_val), axis=-1))

# 4. Plot erstellen
fig, ax = plt.subplots(figsize=(12, 10))

# Hintergrund: Phasen-Information
ax.imshow(img, extent=[x_min, x_max, y_min, y_max], origin='lower', alpha=0.4)

# 5. Transformiertes Koordinatengitter
# Da die Werte nahe der Pole explodieren, nutzen wir eine nicht-lineare 
# Skalierung für die Gitterlinien (Isolinien von Re und Im)
grid_levels = np.linspace(-1.5, 1.5, 31)

# Realteil-Gitter (Blau)
ax.contour(Sigma, Omega, F_s.real, levels=grid_levels, colors='blue', 
           linewidths=0.6, alpha=0.7)
# Imaginärteil-Gitter (Rot)
ax.contour(Sigma, Omega, F_s.imag, levels=grid_levels, colors='red', 
           linewidths=0.6, alpha=0.7)

# 6. Bromwich-Integrationsweg (D-Kontur)
gamma = 2.5  # Rechts von allen Polen
R = 7.0      # Radius des Bogens

# Vertikale Linie
w_max = np.sqrt(R**2 - (gamma+1)**2) # Leicht angepasst für die Optik
w_vals = np.linspace(-w_max, w_max, 100)
line_x = np.ones_like(w_vals) * gamma

# Großer Bogen (links herum geschlossen)
phi = np.linspace(np.pi/2 + 0.3, 3*np.pi/2 - 0.3, 150)
arc_x = R * np.cos(phi) + (gamma - 1)
arc_y = R * np.sin(phi)

# Pfad zeichnen (Weiß mit schwarzem Rand)
def plot_styled_path(x, y, **kwargs):
    ax.plot(x, y, color='black', lw=3.5, zorder=10)
    ax.plot(x, y, color='white', lw=1.5, zorder=11)

plot_styled_path(line_x, w_vals)
plot_styled_path(arc_x, arc_y)

# Verbindungslinien schließen
plot_styled_path([line_x[0], arc_x[-1]], [w_vals[0], arc_y[-1]])
plot_styled_path([line_x[-1], arc_x[0]], [w_vals[-1], arc_y[0]])

# Richtungspfeile
ax.annotate('', xy=(gamma, 1), xytext=(gamma, -1), 
            arrowprops=dict(arrowstyle='->', color='black', lw=2, zorder=12))

# 7. Pole markieren (Ti*k*Z-Stil)
poles = [p1, p2, p3]
for p in poles:
    ax.plot(p.real, p.imag, 'x', color='black', markersize=12, mew=3, zorder=20)
    ax.plot(p.real, p.imag, 'x', color='white', markersize=10, mew=1.5, zorder=21)

# Achsen und Beschriftung
ax.axhline(0, color='black', lw=1, alpha=0.2)
ax.axvline(0, color='black', lw=1, alpha=0.2)
ax.set_aspect('equal')
ax.set_xlabel(r'Re($s$)')
ax.set_ylabel(r'Im($s$)')
ax.set_title(r'Bromwich-Integrationsweg und Polstellen-Gitter von $F(s)$')

# Legende
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='blue', lw=1, label=r'Re($F(s)$)=const'),
    Line2D([0], [0], color='red', lw=1, label=r'Im($F(s)$)=const'),
    Line2D([0], [0], color='black', marker='x', markersize=10, lw=0, label='Pole'),
    Line2D([0], [0], color='white', lw=2, path_effects=[], label='Integrationsweg')
]
ax.legend(handles=legend_elements, loc='upper left', framealpha=0.9)

plt.savefig("bromwich_plot.svg", format='svg', bbox_inches='tight')

plt.tight_layout()
plt.show()