#
# Makefile -- build images
#
# (c) 2026 Prof Dr Andreas Müller
#
all:	nichtanalytisch.pdf						\
	wurzel2.pdf							\
	wurzel.pdf							\
	ring.pdf

nichtanalytisch.pdf:	nichtanalytisch.tex
	pdflatex nichtanalytisch.tex

wurzel.png:	wurzel.pov
	povray +A0.1 -W3840 -H2160 -Owurzel.png wurzel.pov

wurzel.jpg:	wurzel.png Makefile
	magick -extract 2640x2160+584+0 wurzel.png wurzel.jpg

wurzel.pdf:	wurzel.tex wurzel.jpg
	pdflatex wurzel.tex

wurzel2.pdf:	wurzel2.tex
	pdflatex wurzel2.tex

ring.pdf:	ring.tex
	pdflatex ring.tex
