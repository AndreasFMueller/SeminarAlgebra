#
# Makefile -- planung
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	planung-handout.pdf MathSem-04-planung.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

MathSem-04-planung.pdf:	MathSem-04-planung.tex $(SOURCES)
	pdflatex MathSem-04-planung.tex

planung-handout.pdf:	planung-handout.tex $(SOURCES)
	pdflatex planung-handout.tex

thumbnail:	thumbnail.jpg # fix1.jpg

thumbnail.pdf:	MathSem-04-planung.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		MathSem-04-planung.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

fix1.pdf:	MathSem-04-planung.pdf
	pdfjam --outfile fix1.pdf --papersize '{16cm,9cm}' \
		MathSem-04-planung.pdf 1
fix1.jpg:	fix1.pdf
	convert -density 300 fix1.pdf \
                -resize 1920x1080 -units PixelsPerInch fix1.jpg

