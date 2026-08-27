#
# Makefile
#
# (c) 2026 Prof Dr Andreas Müller
#
all:	fresnel-c-s.pdf							\
	fresnel-c-s-komplex.pdf						\
	beugungsverluste.pdf

cs.pdf:	cs.tex fresnel-c-s.pgf
	pdflatex cs.tex

fresnel-c-s.pdf:	fresnel-c-s.tex cs.pdf
	pdflatex fresnel-c-s.tex

cs-komplex.pdf:	cs-komplex.tex fresnel-c-s-komplex.pgf
	pdflatex cs-komplex.tex

fresnel-c-s-komplex.pdf:	fresnel-c-s-komplex.tex cs-komplex.pdf
	pdflatex fresnel-c-s-komplex.tex

verluste.pdf:	verluste.tex beugungsverluste.pgf
	pdflatex verluste.tex

beugungsverluste.pdf:	beugungsverluste.tex verluste.pdf
	pdflatex beugungsverluste.tex

