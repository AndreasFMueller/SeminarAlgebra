import numpy as np
import os

t = 1.0
gamma = 1.0
omega = np.linspace(-40, 40, 1000)

s_brom = gamma + 1j * omega
integrand_brom = np.real(np.exp(s_brom * t) / s_brom)

theta = np.linspace(-np.pi + 1e-5, np.pi - 1e-5, 1000)
cot = 1.0 / np.tan(theta)
csc2 = 1.0 / np.sin(theta)**2
s_tal = 2 * (theta * cot + 1j * theta)
s_prime = 2 * (cot - theta * csc2 + 1j)

integrand_tal = np.real(np.exp(s_tal * t) * (1.0 / s_tal) * s_prime / (2j * np.pi))

N = 12
theta_pts = -np.pi + (np.arange(1, N + 1) - 0.5) * (2 * np.pi / N)
cot_pts = 1.0 / np.tan(theta_pts)
csc2_pts = 1.0 / np.sin(theta_pts)**2
s_tal_pts = 2 * (theta_pts * cot_pts + 1j * theta_pts)
s_prime_pts = 2 * (cot_pts - theta_pts * csc2_pts + 1j)
integrand_tal_pts = np.real(np.exp(s_tal_pts * t) * (1.0 / s_tal_pts) * s_prime_pts / (2j * np.pi))

os.makedirs('Latex/images', exist_ok=True)
with open('Latex/images/data_integrand_bromwich.csv', 'w') as f:
    f.write("omega,integrand\n")
    for w, i_b in zip(omega, integrand_brom):
        f.write(f"{w:.6e},{i_b:.6e}\n")

with open('Latex/images/data_integrand_talbot.csv', 'w') as f:
    f.write("theta,integrand\n")
    for th, i_t in zip(theta, integrand_tal):
        f.write(f"{th:.6e},{i_t:.6e}\n")

with open('Latex/images/data_integrand_talbot_pts.csv', 'w') as f:
    f.write("theta,integrand\n")
    for th, i_t in zip(theta_pts, integrand_tal_pts):
        f.write(f"{th:.6e},{i_t:.6e}\n")

print("Data generated successfully.")
