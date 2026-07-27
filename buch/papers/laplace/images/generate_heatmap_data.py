import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('Latex/images', exist_ok=True)

# 1. Generate Heatmap Image
x = np.linspace(-15, 5, 800)
y = np.linspace(-12, 12, 800)
X, Y = np.meshgrid(x, y)
S = X + 1j * Y

# F(s) = 1/s, t=1
with np.errstate(divide='ignore', invalid='ignore'):
    Z = np.log10(np.abs(np.exp(S) / S))
Z = np.nan_to_num(Z, nan=2) # at s=0
Z = np.clip(Z, -8, 2)

fig = plt.figure(figsize=(10, 12), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

# Use viridis with explicit vmin/vmax
cax = ax.imshow(Z, extent=[-15, 5, -12, 12], origin='lower', cmap='viridis', vmin=-8, vmax=2, aspect='auto')

# Add contour lines
levels = np.arange(-8, 3, 1)
ax.contour(X, Y, Z, levels=levels, colors='white', linewidths=0.5, alpha=0.5)

# Save the raw image
fig.savefig('Latex/images/heatmap_bg.png', dpi=300, bbox_inches='tight', pad_inches=0, transparent=True)
plt.close(fig)

# 2. Generate Talbot Contour CSV
# sigma=0, lambda=2, beta=1
# s(theta) = 2*(theta * cot(theta) + i * theta)
theta = np.linspace(-np.pi + 0.01, np.pi - 0.01, 1000)
cot = 1.0 / np.tan(theta)
s_tal = 2 * (theta * cot + 1j * theta)
# Manually add the limit at theta=0 which is s=2
s_tal[np.abs(theta) < 0.015] = 2.0

with open('Latex/images/talbot_contour_heatmap.csv', 'w') as f:
    f.write("re,im\n")
    for r, i in zip(np.real(s_tal), np.imag(s_tal)):
        if r >= -15 and r <= 5 and i >= -12 and i <= 12:
            f.write(f"{r:.6f},{i:.6f}\n")

print("Heatmap and contour data generated.")
