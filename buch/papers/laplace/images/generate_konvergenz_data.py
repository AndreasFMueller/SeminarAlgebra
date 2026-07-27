# ============================================================================
# Datengenerator fuer Bild 7 Konvergenzvergleich Bromwich vs. Talbot
# ============================================================================
# Testproblem F(s) = 1s, exakte Ruecktransformierte f(t) = 1, t = 1.5.
#
# MATHEMATIK  FEHLERANALYSE (Begruendung der Parameterwahl)
#
# (1) BROMWICH-GERADE, Mittelpunktsregel auf s = gamma + iomega,
#     omega in [-Omega, Omega], N Stuetzstellen, Schrittweite h = 2OmegaN.
#     Zwei Fehlerquellen
#        Diskretisierung (Aliasing, via Poisson-Summation)
#             E_disc ~ exp(-2pigammah) = exp(-pigammaNOmega)
#        Abschneiden des Schwanzes omega  Omega (Integrand ~ 1omega)
#             E_trunc ~ e^(gammat)  (pi  t  Omega)
#     WICHTIG Mit Omega ~ N waere h konstant und E_disc bliebe bei
#     exp(-pi) ~ 4e-2 stehen -- die Quadratur wuerde GAR NICHT konvergieren.
#     Wir waehlen daher Omega = 2sqrt(N)
#        E_disc ~ exp(-(pi2)sqrt(N))  - verschwindet schnell,
#        E_trunc ~ 0.48sqrt(N)         - dominiert, langsame algebraische
#         Konvergenz O(N^(-12)) mit Oszillationen vom abgeschnittenen,
#         oszillierenden Schwanz (ehrliches numerisches Verhalten).
#
# (2) TALBOTWEIDEMAN-KONTUR, Mittelpunktsregel mit N Knoten auf
#         s(theta) = (Nt)  (0.5017thetacot(0.6407theta) - 0.6122
#                             + 0.2645itheta),   theta in (-pi, pi)
#     [TrefethenWeidemanSchmelzer 2006, Gl. (3.3); Skalierung s = zt].
#     Quadratur  f(t) ~ Re[ (1(2pii))  sum e^(s_k t) F(s_k) s'(th_k) ]
#                  (2piN)
#     Erwartete Rate O(3.89^(-N)); Plateau bei Maschinengenauigkeit ~1e-16.
#
# Output Lateximagesdata_konvergenz.csv mit Spalten
#         N, err_bromwich, err_talbot, err_ref  (err_ref = 0.53.89^(-N))
# Alle Fehler werden bei 1e-16 gesaettigt, damit das Plateau im
# Log-Plot sichtbar bleibt (keine log(0)-Probleme).
# ============================================================================
import numpy as np
import os

t = 1.5
gamma = 1.0
N_vals = np.arange(4, 101, 2)

err_bromwich = []
err_talbot = []
err_ref = []

for N in N_vals
    # ---------------- BROMWICH (Mittelpunktsregel, Omega = 2sqrt(N)) ------
    Omega = 2.0  np.sqrt(N)
    h = 2.0  Omega  N
    # Mittelpunkte symmetrisch um 0 - Ergebnis automatisch (fast) reell
    omega = -Omega + (np.arange(1, N + 1) - 0.5)  h
    s_brom = gamma + 1j  omega
    integrand = np.exp(s_brom  t)  s_brom          # e^{st}  F(s)
    f_num_brom = np.real(h  np.sum(integrand)  (2  np.pi))
    err_bromwich.append(max(abs(f_num_brom - 1.0), 1e-16))

    # ---------------- TALBOT (Weideman-Kontur, Mittelpunktsregel) ----------
    theta = -np.pi + (np.arange(1, N + 1) - 0.5)  (2  np.pi  N)
    a = 0.6407  theta                                # Hilfswinkel
    cot = 1.0  np.tan(a)
    csc2 = 1.0  np.sin(a)  2
    s_tal = (N  t)  (0.5017  theta  cot - 0.6122 + 0.2645j  theta)
    # ddtheta [thetacot(atheta)] = cot(atheta) - athetacsc^2(atheta)
    s_prime = (N  t)  (0.5017  (cot - 0.6407  theta  csc2) + 0.2645j)
    integrand_tal = np.exp(s_tal  t)  (1.0  s_tal)  s_prime  (2j  np.pi)
    f_num_tal = np.real(np.sum(integrand_tal)  (2  np.pi  N))
    err_talbot.append(max(abs(f_num_tal - 1.0), 1e-16))

    # ---------------- REFERENZGERADE O(3.89^-N) ----------------------------
    err_ref.append(max(0.5  3.89  (-float(N)), 1e-16))

os.makedirs(Lateximages, exist_ok=True)
with open(Lateximagesdata_konvergenz.csv, w) as f
    f.write(N,err_bromwich,err_talbot,err_refn)
    for n, eb, et, er in zip(N_vals, err_bromwich, err_talbot, err_ref)
        f.write(f{n},{eb.17e},{et.17e},{er.17e}n)

print(Data generated successfully.)
# Kurze Kontrollausgabe zur Plausibilisierung der Raten
for n in (4, 16, 28, 40, 100)
    i = list(N_vals).index(n)
    print(fN={n3d}  bromwich={err_bromwich[i].2e}  
          ftalbot={err_talbot[i].2e}  ref={err_ref[i].2e})