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
    "pgf.rcfonts": False,
})

v = np.arange(-4.5, 4.5, 0.01)
S, C = sc.fresnel(v)
xaxis = [-4, -3, -2, -1, 1, 2, 3, 4]
yaxis = [-0.75, -0.5, -0.25, 0.25, 0.5, 0.75]

fig, ax = plt.subplots()

plt.plot(v, C, color='blue', label='$C(v)$')
plt.plot(v, S, color='red', label='$S(v)$')
plt.xticks(xaxis)
plt.yticks(yaxis, yaxis)
plt.xlim(-4.2, 4.2)
plt.ylim(-0.79, 0.79)
plt.grid(True, which='major', axis='y',color='0.8', linestyle='dotted')

# Achsen ins Zentrum
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.text(4.5,0,'$v$')
ax.text(0, 0.81, '$C(v), S(v)$', horizontalalignment='center')

# Legende
plt.legend(loc='upper left', frameon=False)

# plt.show()
plt.savefig('./tikz/fresnel-c-s.pgf')