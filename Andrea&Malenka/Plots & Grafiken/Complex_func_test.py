import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)

Z = X + 1j*Y

F = 2*np.log(Z + 2) - np.log(Z - 2)

u = np.real(F)   # Potential
v = np.imag(F)   # Feldlinienfunktion

K = np.log(Z)  # Beispiel: Logarithmus einer komplexen Zahl

# 3. Visualisierung des Betrags (Absolutwert)
plt.figure(figsize=(8, 6))
plt.contour(X, Y, u, cmap='viridis', levels=35)
plt.contour(X, Y, v, colors='green', linestyles='dashed', levels=35)
plt.colorbar(label='Betrag $|f(z)|$')
plt.title('Darstellung von $f(z) = z^2$')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()