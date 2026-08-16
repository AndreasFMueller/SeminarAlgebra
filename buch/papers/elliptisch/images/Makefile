#
# Makefile -- Bilder fuer das Paper elliptisch
#
# (c) 2026 Baris Catan, OST Ostschweizer Fachhochschule
#

all:	gradskala.pdf ellipse.pdf koerperturm.pdf ke-plot.pdf

ke-werte.dat:	ke-werte.py
	python3 ke-werte.py

gradskala.pdf:	gradskala.tex
	pdflatex gradskala.tex

ellipse.pdf:	ellipse.tex
	pdflatex ellipse.tex

koerperturm.pdf:	koerperturm.tex
	pdflatex koerperturm.tex

ke-plot.pdf:	ke-plot.tex ke-werte.dat
	pdflatex ke-plot.tex

clean:
	rm -f *.aux *.log *.pdf ke-werte.dat
