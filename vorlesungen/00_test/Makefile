#
# Makefile -- test
#
# (c) 2017 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	test-handout.pdf MathSem-00-test.pdf

include ../slides/Makefile.inc

SOURCES = common.tex slides.tex $(slides)

MathSem-00-test.pdf:	MathSem-00-test.tex $(SOURCES)
	pdflatex MathSem-00-test.tex

test-handout.pdf:	test-handout.tex $(SOURCES)
	pdflatex test-handout.tex

thumbnail:	thumbnail.jpg # fix1.jpg

thumbnail.pdf:	MathSem-00-test.pdf
	pdfjam --outfile thumbnail.pdf --papersize '{16cm,9cm}' \
		MathSem-00-test.pdf 1
thumbnail.jpg:	thumbnail.pdf
	convert -density 300 thumbnail.pdf \
                -resize 1920x1080 -units PixelsPerInch thumbnail.jpg

fix1.pdf:	MathSem-00-test.pdf
	pdfjam --outfile fix1.pdf --papersize '{16cm,9cm}' \
		MathSem-00-test.pdf 1
fix1.jpg:	fix1.pdf
	convert -density 300 fix1.pdf \
                -resize 1920x1080 -units PixelsPerInch fix1.jpg

