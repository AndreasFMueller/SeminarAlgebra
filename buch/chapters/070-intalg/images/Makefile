#
# Makefile
#
# (c) 2026 Prof Dr Andreas Müller
#
all:	invcis.pdf							\
	invtan.pdf							\
	lf0.pdf								\
	lfN.pdf								\
	lf.pdf								\
	polylog.pdf							\
	li.pdf								\
	li2.pdf								\
	ei.pdf

invcis.pdf:	invcis.tex
	pdflatex invcis.tex

invtan.pdf:	invtan.tex
	pdflatex invtan.tex

lf0.pdf:	lf0.tex
	pdflatex lf0.tex

lfN.pdf:	lfN.tex
	pdflatex lfN.tex

lf.pdf:	lf.tex
	pdflatex lf.tex

polylog.pdf:	polylog.tex
	pdflatex polylog.tex

li.pdf:	li.tex lipaths.tex
	pdflatex li.tex
lipaths.tex:	li.m
	octave li.m

li2.pdf:	li2.tex li2paths.tex
	pdflatex li2.tex
li2paths.tex:	li2.m
	octave li2.m

ei.pdf:	ei.tex eipaths.tex
	pdflatex ei.tex
eipaths.tex:	ei.m
	octave ei.m
