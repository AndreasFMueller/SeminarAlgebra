#
# Makefile
#
# (c) 2026 Prof Dr Andreas Müller
#
all:	farben-transparent.png

farbdreiecke.inc:	farben.m
	octave farben.m

SIZE= -W1920 -H1080
SIZE= -W3840 -H2160

farben.png:	farben.pov farbdreiecke.inc
	povray +A0.1 $(SIZE) -Ofarben.png farben.pov

farben-transparent.png:	farben.png Makefile
	magick farben.png -transparent blue farben-transparent.png

