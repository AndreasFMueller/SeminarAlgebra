import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'text.latex.preamble': r'\usepackage{mathptmx}',
})

def get_colormap(length):
    cmap = plt.get_cmap('tab10')
    col_val = np.linspace(0, 1, length)
    return cmap, col_val

# Funktion
def f(z):
    if abs(z) < 1e-12:
        return np.nan + 1j*np.nan
    return 1 / np.conj(z)

# --- Complex Points ---
path_z = []
path_w = []

z = 1.6 + 0j
w = f(z)

# --- Grid ---
grid_max = 20
grid_max_plot = 2
steps = 4

cmap, col_val = get_colormap(steps)

t = np.linspace(-grid_max, grid_max, 1500)
x_vals = np.linspace(-grid_max_plot, grid_max_plot, steps)
y_vals = np.linspace(-grid_max_plot, grid_max_plot, steps)

# --- Plot Initialisation ---
fig, ax = plt.subplots(1, 2, figsize=(10, 6))

ax[0].axhline(0, color='black', linewidth=1.5)
ax[0].axvline(0, color='black', linewidth=1.5)
ax[1].axhline(0, color='black', linewidth=1.5)
ax[1].axvline(0, color='black', linewidth=1.5)

# --- Plot Grid ---
for x, y, col in zip(x_vals, y_vals, col_val):

    # vertical lines
    z_line1 = t + 1j * y
    w_line1 = np.array([f(z) for z in z_line1])

    ax[0].plot(w_line1.real, w_line1.imag, color=cmap(col), linewidth=1)
    ax[1].plot(z_line1.real, z_line1.imag, color=cmap(col), linewidth=1)

    # horizontal lines
    z_line2 = x + 1j * t
    w_line2 = np.array([f(z) for z in z_line2])

    ax[0].plot(w_line2.real, w_line2.imag, linestyle=(0, (6, 3)), color=cmap(col), linewidth=1)
    ax[1].plot(z_line2.real, z_line2.imag, linestyle=(0, (6, 3)), color=cmap(col), linewidth=1)

# --- Plot Settings ---
ax[0].set_xlabel(r'$\mathrm{Re}(z)$')
ax[0].set_ylabel(r'$\mathrm{Im}(z)$')
ax[0].set_xlim(-1.5, 1.5)
ax[0].set_ylim(-1.5, 1.5)

ax[1].set_xlabel(r'$\mathrm{Re}(z)$')
# ax[1].set_ylabel(r'$\mathrm{Im}(z)$')
ax[1].set_xlim(-3, 3)
ax[1].set_ylim(-3, 3)


ax[0].set_aspect('equal')
ax[1].set_aspect('equal')

plt.savefig("moebius_transform_plot.pdf", bbox_inches="tight")
plt.show()