#
# Makefile -- build the book cover
#
# (c) 2018 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	buchcover.jpg backcover.jpg front.jpg back.pdf

buchcover.pdf:	buchcover.tex teilnehmer.tex
	pdflatex buchcover.tex

buchcover.png:	buchcover.pdf  Makefile
	magick -density 300 -extract 2054x2900+2630+190 buchcover.pdf \
		buchcover.png
buchcover.jpg:	buchcover.png
	magick buchcover.png buchcover.jpg
buchcover-small.jpg:	buchcover.jpg
	magick buchcover.jpg -scale 50% buchcover-small.jpg
backcover.png:	buchcover.pdf Makefile
	magick -density 300 -extract 2054x2900+192+190 buchcover.pdf \
		backcover.png
backcover.jpg:	backcover.png
	magick backcover.png backcover.jpg

front.pdf:	front.tex buchcover.pdf
	pdflatex front.tex
front.jpg:	front.pdf
	magick -density 150 front.pdf front.jpg

back.pdf:	back.tex buchcover.pdf
	pdflatex back.tex

