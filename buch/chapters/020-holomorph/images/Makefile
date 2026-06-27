#
# Makefile
#
# (c) 2026 Prof Dr Andreas Müller
#
all:	imaginaerteil.pdf polynome.pdf rekursion.pdf konform.pdf

imaginaerteil.pdf:	imaginaerteil.tex
	pdflatex imaginaerteil.tex

polynome.pdf:	polynome.tex
	pdflatex polynome.tex

rekursion.pdf:	rekursion.tex
	pdflatex rekursion.tex

konform.pdf:	konform.tex konformcurves.tex
	pdflatex konform.tex

konformcurves.tex:	konform.m
	octave konform.m

