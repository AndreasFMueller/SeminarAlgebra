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
# Kapitel  9
chapter=9
4
6
#
# Kapitel 10
chapter=10
2
3
7
#
# Kapitel 11
chapter=11
2
5
15
16
#
# Kapitel 12
chapter=12
2
9
12
22
25
41
#
# Kapitel 13
chapter=13
2
4
6
7
13
15
19
20
21
25
32
33
#
# Kapitel 14 geoalgebra
chapter=geoalgebra
4
5
7
8
13
14
15
#
# Kapitel 15 nerven
chapter=nerven
2
3
4
5
6
12
13
14
#
# Kapitel 16 poinbendix
chapter=poinbendix
4
6
7
8
10
#
# Kapitel 17 elastomechanik
chapter=elastomechanik
#
# Kapitel 18 maxwell
chapter=maxwell
#
# Kapitel 19 diffortho
chapter=diffortho
2
5
#
# Kapitel 20 helmholtz
chapter=helmholtz
2
3
4
15
16
#
# Kapitel 21 reaktdiff
chapter=reaktdiff
5
10
11
12
14
15
#
# Kapitel 22 mongeampere
chapter=mongeampere
4
5
#
# Kapitel 23 mongekant
chapter=mongekant
2
6
10
12
13
14
#
# Kapitel 24 neuronal
chapter=neuronal
3
6
9
10
11
12
13
14
15
#
# Kapitel 25 parallelisierung
chapter=parallelisierung
9
10
11
12
14
15
19
20
21
22
24
#
# Kapitel 26 openfoam
chapter=openfoam
10
11
13
15
18
#
# Kapitel 27 reynolds
chapter=reynolds
7
9
#
# Kapitel 28 ueberschall
chapter=ueberschall
5
6
7
9
11
13
14
#
# Kapitel 29 schall
chapter=schall
8
12
13
#
# Kapitel 30 wirbelringe
chapter=wirbelringe
2
4
5
8
12
16
#
# Kapitel 31 geostrophisch
chapter=geostrophisch
4
5
8
9
12
13
14
15
#
# Kapitel 32 rossby
chapter=rossby
3
4
5
7
8
9
13
14
#
# Kapitel 33 fourier
chapter=fourier
3
6
7
8
9
#
# Kapitel 34 particles
chapter=particles
2
3
8
9
10
11
12
EOF
