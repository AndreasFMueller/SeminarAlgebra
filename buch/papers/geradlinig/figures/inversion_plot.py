import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'text.latex.preamble': r'\usepackage{mathptmx}',
})

radius = 1

def get_colormap(length):
    cmap = plt.get_cmap('tab10')
    col_val = np.linspace(0, 1, length)
    return cmap, col_val

# Funktion
def f(z):
    if abs(z) < 1e-12:
        return np.nan + 1j*np.nan
    return radius**2 / np.conj(z)


# --- Complex Points ---
path_z = []
path_w = []

z = 1.6 + 0j
w = f(z)

# --- Grid ---
grid_max = 20
steps = 1

cmap, col_val = get_colormap(1)


# --- Plot Initialisation ---
fig, ax = plt.subplots(1, 1, figsize=(6,6))
ax.axhline(0, color='black', linewidth=1.5)
ax.axvline(0, color='black', linewidth=1.5)

t = np.linspace(-grid_max, grid_max, 1500)

# --- Inner Circles and Lines ---
x = 1.4
z_line1 = x+ 1j * t
w_line1 = np.array([f(z) for z in z_line1])

ax.plot(w_line1.real, w_line1.imag, color='red', linewidth=1)
ax.plot(z_line1.real, z_line1.imag, color='blue', linewidth=1)

x = 1.2
z_line2 = x+ 1j * t
w_line2 = np.array([f(z) for z in z_line2])

ax.plot(w_line2.real, w_line2.imag, linestyle=(0, (8, 4)), color='red', linewidth=1)
ax.plot(z_line2.real, z_line2.imag, linestyle=(0, (8, 4)), color='blue', linewidth=1)

x = 1
z_line2 = x+ 1j * t
w_line2 = np.array([f(z) for z in z_line2])

ax.plot(w_line2.real, w_line2.imag, linestyle=(0, (12, 6, 2, 6)), color='red', linewidth=1)
ax.plot(z_line2.real, z_line2.imag, linestyle=(0, (12, 6, 2, 6)), color='blue', linewidth=1)

# --- Inversion Circle ---
theta = np.linspace(0, 2 * np.pi, 400)
z_circle = radius * np.exp(1j * theta)  # radius 1 around origin
ax.plot(z_circle.real, z_circle.imag, color='green', linewidth=1.5, label='Unit circle')

z_circle = 0.15 * np.exp(1j * theta) - 0.7  # radius 1 around origin
w_line2 = np.array([f(z) for z in z_circle])
ax.plot(w_line2.real, w_line2.imag, color='blue', linewidth=1, linestyle='dotted')
ax.plot(z_circle.real, z_circle.imag, color='red', linewidth=1, linestyle='dotted')

# --- Plot Settings ---
ax.set_xlabel(r'$\mathrm{Re}(z)$')
ax.set_ylabel(r'$\mathrm{Im}(z)$')
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 1.5)


ax.set_aspect('equal')

plt.savefig("inversion_plot.pdf", bbox_inches="tight")
plt.show()