#
# Makefile.inc -- Makefile Targets und Variablen für Papers
#
# Achtung: dieses File wird erzeugt vom Skript scripts/mkmakefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
PAPERFILES = \
	papers/part2.tex \
	papers/uebersicht.tex \
	papers/beispiel/main.tex \
	
$(workdir)/buch1-blx.bbl:	$(workdir)/buch1-blx.aux
	cd $(workdir); bibtex buch1-blx

$(workdir)/$(seminar)1-blx.bbl:	$(workdir)/$(seminar)1-blx.aux
	cd $(workdir); bibtex $(seminar)1-blx

$(workdir)/buch2-blx.bbl:	$(workdir)/buch2-blx.aux
	cd $(workdir) bibtex buch2-blx

$(workdir)/$(seminar)2-blx.bbl:	$(workdir)/$(seminar)2-blx.aux
	cd $(workdir) bibtex $(seminar)2-blx

BLXFILES = $(workdir)/buch.bbl \
	$(workdir)/buch1-blx.bbl \
	$(workdir)/buch2-blx.bbl \


SBLXFILES = $(workdir)/$(seminar).bbl\
	$(workdir)/$(seminar)1-blx.bbl \
	$(workdir)/$(seminar)2-blx.bbl \


PAPER_DIRECTORIES = \
	beispiel \
	
PAPER_MAKEFILEINC = \
	papers/beispiel/Makefile.inc \
	
