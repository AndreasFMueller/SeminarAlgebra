#!/usr/bin/env bash
#
# farbseiten.sh -- Formattierung der Farbseiteninfo für die Druckerei
#
# (c) 2020 Prof Dr Andreas Müller, OST Ostschweizer Fachhochschule
#
./chapters --auxfile=../build/buch.aux <<EOF
#
# Kapitel  1
chapter=1
2
6
#
# Kapitel  2
chapter=2
#
15
27
32
33
34
43
55
# Kapitel  3
chapter=3
8
13
16
17
25
32
#
# Kapitel  4
chapter=4
3
7
10
11
13
14
16
18
19
26
28
29
34
35
37
38
39
40
45
46
47
48
53
#
# Kapitel  5
chapter=5
6
8
10
15
16
22
23
39
#
# Kapitel  6
chapter=6
6
7
#
# Kapitel  7
chapter=7
15
19
#
# Kapitel  8
chapter=8
8
16
17
43
57
61
72
84
#
# Kapitel 9 konstruktion
chapter=konstruktion
7
9
13
#
# Kapitel 10 moebius
chapter=moebius
2
3
6
8
11
14
16
#
# Kapitel 11 geradlinig
chapter=geradlinig
#
# Kapitel 12 julia
chapter=julia
9
11
12
15
16
17
18
19
20
21
22
23
#
# Kapitel 13 jordan
chapter=jordan
#
# Kapitel 14 qa
chapter=qa
#
# Kapitel 15 elektro
chapter=elektro
#
# Kapitel 16 joukowski
chapter=joukowski
#
# Kapitel 17 aircraft
chapter=aircraft
#
# Kapitel 18 fresnel
chapter=fresnel
#
# Kapitel 19 pade
chapter=pade
#
# Kapitel 20 step
chapter=step
#
# Kapitel 21 hauptwert
chapter=hauptwert
#
# Kapitel 22 kepler
chapter=kepler
3
8
#
# Kapitel 23 laplace
chapter=laplace
4
5
6
9
11
13
14
16
#
# Kapitel 24 weyl
chapter=weyl
2
5
7
12
#
# Kapitel 25 produkt
chapter=produkt
#
# Kapitel 26 basel
chapter=basel
3
5
7
8
10
13
14
#
# Kapitel 27 gamma
chapter=gamma
5
6
#
# Kapitel 28 bessel
chapter=bessel
#
# Kapitel 29 hankel
chapter=hankel
#
# Kapitel 30 zeta
chapter=zeta
3
4
#
# Kapitel 31 buchberger
chapter=buchberger
6
7
11
#
# Kapitel 32 resultante
chapter=resultante
4
6

#
# Kapitel 33 elliptisch
chapter=elliptisch
2
4
7
11
13
EOF
