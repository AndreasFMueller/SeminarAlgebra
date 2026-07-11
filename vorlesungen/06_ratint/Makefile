#
# Makefile -- ratint
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	ratint-handout.pdf MathSem-06-ratint.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

MathSem-06-ratint.pdf:	MathSem-06-ratint.tex $(SOURCES)
	pdflatex MathSem-06-ratint.tex

ratint-handout.pdf:	ratint-handout.tex $(SOURCES)
	pdflatex ratint-handout.tex

thumbnail:	thumbnail.jpg # fix1.jpg

thumbnail.pdf:	MathSem-06-ratint.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		MathSem-06-ratint.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

fix1.pdf:	MathSem-06-ratint.pdf
	pdfjam --outfile fix1.pdf --papersize '{16cm,9cm}' \
		MathSem-06-ratint.pdf 1
fix1.jpg:	fix1.pdf
	convert -density 300 fix1.pdf \
                -resize 1920x1080 -units PixelsPerInch fix1.jpg

