#
# Makefile
#
# (c) 2026 Prof Dr Andreas Müller
#
all:	gausszahlen.pdf gaussebene.pdf kehrwert.pdf hyperbeln.pdf farben.pdf

gausszahlen.pdf:	gausszahlen.tex
	pdflatex gausszahlen.tex

gaussebene.pdf:	gaussebene.tex
	pdflatex gaussebene.tex

kehrwert.pdf:	kehrwert.tex
	pdflatex kehrwert.tex

hyperbeln.pdf:	hyperbeln.tex
	pdflatex hyperbeln.tex

farbdreiecke.inc:	farben.m
	octave farben.m

farben.png:	farben.pov farbdreiecke.inc
	povray +A0.1 -W1920 -H1080 -Ofarben.png farben.pov

farben.jpg:	farben.png Makefile
	magick farben.png farben.jpg

farben.pdf:	farben.tex farben.jpg
	pdflatex farben.tex
