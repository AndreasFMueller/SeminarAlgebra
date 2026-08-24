#
# Makefile -- Bilder fuer das Paper elliptisch
#
# (c) 2026 Baris Catan, OST Ostschweizer Fachhochschule
#

all:	gradskala.pdf ellipse.pdf koerperturm.pdf ke-plot.pdf sn-konstruktion.pdf lemniskate.pdf troposkein.pdf

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

sn-konstruktion.pdf:	sn-konstruktion.tex
	pdflatex sn-konstruktion.tex

lemniskate.pdf:	lemniskate.tex
	pdflatex lemniskate.tex

troposkein-werte.dat:	troposkein-werte.py
	python3 troposkein-werte.py

troposkein.pdf:	troposkein.tex troposkein-werte.dat
	pdflatex troposkein.tex

clean:
	rm -f *.aux *.log *.pdf ke-werte.dat troposkein-werte.dat
