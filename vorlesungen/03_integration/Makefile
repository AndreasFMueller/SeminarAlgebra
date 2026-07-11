#
# Makefile -- integration
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	integration-handout.pdf MathSem-03-integration.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

MathSem-03-integration.pdf:	MathSem-03-integration.tex $(SOURCES)
	pdflatex MathSem-03-integration.tex

integration-handout.pdf:	integration-handout.tex $(SOURCES)
	pdflatex integration-handout.tex

thumbnail:	thumbnail.jpg # fix1.jpg

thumbnail.pdf:	MathSem-03-integration.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		MathSem-03-integration.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

fix1.pdf:	MathSem-03-integration.pdf
	pdfjam --outfile fix1.pdf --papersize '{16cm,9cm}' \
		MathSem-03-integration.pdf 1
fix1.jpg:	fix1.pdf
	convert -density 300 fix1.pdf \
                -resize 1920x1080 -units PixelsPerInch fix1.jpg

