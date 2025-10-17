#
# This Makefile can also construct the short tests
#
tests:  test1.pdf test2.pdf test3.pdf

test1.pdf:	test/test-common.tex test/test1.tex test/aufgaben1.tex $(TEXFILES)
	$(pdflatex) test/test1.tex
	cp build/test1.pdf .

test2.pdf:	test/test-common.tex test/test1.tex test/aufgaben2.tex
	$(pdflatex) test/test2.tex
	cp build/test2.pdf .

test3.pdf:	test/test-common.tex test/test3.tex test/aufgaben3.tex 
	$(pdflatex) test/test3.tex
	cp build/test3.pdf .

