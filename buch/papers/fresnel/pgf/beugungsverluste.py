import numpy as np
import scipy.special as sc
import matplotlib
import matplotlib.pyplot as plt

# Configure matplotlib to use PGF backend for LaTeX integration
# https://blog.timodenk.com/exporting-matplotlib-plots-to-latex/
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    #"font.family": "serif",
    "font.size": 10,
    "text.usetex": True,
    "text.latex.preamble": plt.rcParams["pgf.preamble"],    # For \text{}-command
    'pgf.preamble': r'\usepackage{amsmath}',                # For \text{}-command
    "pgf.rcfonts": False,
})
# For \text{}-command, see also
# https://stackoverflow.com/questions/23824687/text-does-not-work-in-a-matplotlib-label

v = np.arange(-4.5, 4.5, 0.01)
v_pos = np.arange(0, 4.5, 0.01)
v_neg = np.arange(-4.5, 0, 0.01)

S, C = sc.fresnel(v)
S_pos, C_pos = sc.fresnel(v_pos)
S_neg, C_neg = sc.fresnel(v_neg)

L = 2/(abs(0.5 -C)**2 + abs(0.5 - S)**2)
L_pos = 2/(abs(0.5 -C_pos)**2 + abs(0.5 - S_pos)**2)
L_neg = 2/(abs(0.5 -C_neg)**2 + abs(0.5 - S_neg)**2)

L_db = 10 * np.log10(L)
L_db_pos = 10 * np.log10(L_pos)
L_db_neg = 10 * np.log10(L_neg)

fig, ax = plt.subplots()

plt.plot(v_neg, L_db_neg, color='blue')
plt.plot(v_pos, L_db_pos, color='red')
plt.xlim(-4.2, 4.2)
plt.ylim(-6, 30)

ax.annotate(r"Verluste", horizontalalignment='center',color='black',
            xy=(3.8, 4), xycoords='data',
            xytext=(3.8, 20), textcoords='data',
            arrowprops=dict(arrowstyle="wedge,tail_width=1.2", 
                            color="black", connectionstyle="arc3"))

# Achsen ins Zentrum
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# Bereichbeschriftung
ax.text(-2.5, -5, 
        r'Line-of-Sight (LOS)'
        '\n'
        r'(Sonnenseite)',
        color='blue', fontweight='bold', horizontalalignment='center')
ax.text(2.5, -5, 
        r'Non-Line-of-Sight (NLOS)'
        '\n'
        r'(Schattenseite)', 
        color='red', fontweight='bold', horizontalalignment='center')

# Fresnel-Parameter
# ax.text(-2.5, 15, r'$v = h_{edge} \sqrt{2 \frac{d_1 + d_2}{\lambda d_1d_2} }$', horizontalalignment='center')

# Achsenbeschriftung
ax.text(4.5,0,'$v$')
ax.text(0, 32, r"$L_{\text{dB}}$", horizontalalignment='center')

# plt.show()
plt.savefig('./buch/papers/fresnel/pgf/beugungsverluste.pgf')