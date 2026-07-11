#
# Makefile -- build algebra.tex poster
#
# (c) 2015 Prof Dr Andreas Mueller, Hochschule Rapperswil
#
seminar = algebra

$(seminar).pdf:	$(seminar).tex ../cover/buchcover.png qrcode.pdf
	pdflatex $(seminar).tex

qrcode.pdf:     qrcode.tex ../cover/mathman.png
	pdflatex qrcode.tex

