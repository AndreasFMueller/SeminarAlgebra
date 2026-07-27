import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.integrate import trapezoid

# 1. Laplace-Funktion und analytische Lösung
def F(s):
    return 1 / (s + 1)

def f_analytical(t):
    return np.exp(-t)

# 2. Feste Talbot-Kontur (Geometrie bleibt immer gleich)
def talbot_fixed(theta, sigma=0.0, mu=3.5, nu=1.0):
    theta = np.where(theta == 0, 1e-10, theta)
    cot = 1.0 / np.tan(theta)
    s = sigma + mu * theta * (cot + 1j * nu)
    csc2 = 1.0 / (np.sin(theta)**2)
    ds_dtheta = mu * (cot - theta * csc2 + 1j * nu)
    return s, ds_dtheta

# 3. Parameter für die Animation
t_val = 1.5
# Verfeinerte Schritte für N für ein langsameres, flüssigeres GIF
n_range = np.arange(4, 101, 1) 

# Speicher für die Fehlerhistorie (für den Linienplot)
n_history = []
err_talbot_history = []
err_bromwich_history = []

# Setup der Figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

def update(n_val):
    # Daten berechnen
    n_history.append(n_val)
    
    # --- Talbot Berechnung ---
    theta_N = np.linspace(-np.pi + 0.01, np.pi - 0.01, n_val)
    s_t, ds_t = talbot_fixed(theta_N)
    res_t = (1 / (2j * np.pi)) * trapezoid(F(s_t) * np.exp(s_t * t_val) * ds_t, theta_N)
    
    # --- Bromwich Berechnung (feste Gerade) ---
    L = 20
    omega = np.linspace(-L, L, n_val)
    s_b = 0.5 + 1j * omega
    res_b = (1 / (2j * np.pi)) * trapezoid(F(s_b) * np.exp(s_b * t_val) * 1j, omega)
    
    f_true = f_analytical(t_val)
    err_talbot_history.append(abs(res_t.real - f_true))
    err_bromwich_history.append(abs(res_b.real - f_true))
    
    # --- PLOT 1: S-Ebene ---
    ax1.clear()
    ax1.axvline(0, color='black', lw=0.5)
    ax1.axhline(0, color='black', lw=0.5)
    ax1.scatter(-1, 0, color='red', marker='x', s=100, label='Pol (s=-1)', zorder=5)
    
    # Zeichne die feste Kurve im Hintergrund
    theta_fine = np.linspace(-np.pi + 0.01, np.pi - 0.01, 200)
    sf, _ = talbot_fixed(theta_fine)
    ax1.plot(sf.real, sf.imag, 'b-', alpha=0.1)
    ax1.plot([0.5, 0.5], [-20, 20], 'r-', alpha=0.1)
    
    # Aktuelle Punkte
    ax1.scatter(s_t.real, s_t.imag, color='blue', s=15, alpha=0.6, label=f'Talbot Punkte (N={n_val})')
    ax1.scatter(s_b.real, s_b.imag, color='red', s=15, alpha=0.6, label=f'Gerade Punkte (N={n_val})')
    
    ax1.set_xlim(-15, 5)
    ax1.set_ylim(-18, 18)
    ax1.set_title("Integrationspfade in der s-Ebene")
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.2)

    # --- PLOT 2: Logarithmischer Fehler ---
    ax2.clear()
    ax2.plot(n_history, err_bromwich_history, color='red', lw=2, label='Fehler Gerade (Bromwich)')
    ax2.plot(n_history, err_talbot_history, color='blue', lw=2, label='Fehler Talbot-Kontur')
    
    ax2.set_yscale('log')
    ax2.set_xlim(4, 100)
    ax2.set_ylim(1e-16, 10) # Von Maschinengenauigkeit bis 1
    ax2.set_xlabel("Anzahl der Punkte (N)")
    ax2.set_ylabel("Absoluter Fehler |f_num - f_exakt|")
    ax2.set_title(f"Konvergenzgeschwindigkeit bei t={t_val}")
    ax2.legend(loc='upper right')
    ax2.grid(True, which="both", ls="-", alpha=0.2)

    plt.tight_layout()

# Animation erstellen
# frames=n_range sorgt für viele Bilder, fps=8 macht es ruhig und langsam
ani = FuncAnimation(fig, update, frames=n_range, repeat=False)

print("Erstelle flüssiges GIF (100 Frames)... Bitte warten.")
writer = PillowWriter(fps=8)
ani.save("laplace_konvergenz_log.gif", writer=writer)
print("Datei 'laplace_konvergenz_log.gif' wurde erfolgreich erstellt.")

plt.show()