#! /bin/bash
#
# teilnehmer.sh -- Formattierung der Teilnehmerliste aller Seminare
#
# (c) 2026 Prof Dr Andreas Müller
#
(
sed -e '/^#/d' <<EOF
# 2013 Optimierung
Dorian Amiet
Hannes Badertscher
Gregor Dengler
Roman Gassmann
Lukas Loser
Selina Malacarne
Tabea Méndez
Raphael Nestler
Philip Riedel
Christian Schmid
Armin Stocklin
Dario Wickart
# 2014 HPC
Dorian Amiet
Hannes Badertscher
Danilo Bargen
Marco Bassotti
Reto Christen
Gregor Dengler
Felix Hofer
Fabian Klein
Flavio La Morea
Andreas Linggi
Tabea Méndez
Daniel Monti
Lukas Murer
Nicol\'as Rom\'an Lüthold
Christian Schmid
Philipp Solenthaler
Pascal Stump
Stefan Steiner
Dario Trütsch
Thomas Ziegler
# 2015 QM
Dorian Amiet
Hannes Badertscher
Roger Billeter
Joel Brunner
Christian Cavegn
Michael Cerny
Reto Christen
Hannes Diethelm
Benny Gächter
Daniel Gubser
Thomas Gujer
Stefan Hedinger
Marc Juchli
Simon Kuster
Andreas Linggi
Gabriel Looser
Daniel Monti
Max Obrist
Nicola Ochsenbein
Kirusanth Poopalasingam
Nicol\'as Rom\'an Lüthold
Stefan Schindler
Christoph Schmitz-Dräger
Arwed Schudel
Tobias Stauber
Stefan Steiner
Claudio Stucki
Pascal Stump
Martin Stypinski
# 2016 DGL
Reto Christen
Kevin Cina
Andri Hartmann
Pascal Horat
Matthias Knöpfel
Stefan Kull
Daniela Meier
Max Obrist
Hansruedi Patzen
Benjamin Räber
Simon Schäfer
Tibor Schneider
Tobias Schuler
Roy Seitz
Martin Stypinski
# 2017 Kosmologie
Jonas Gründler
Sascha Jecklin
Peter Nötzli
Hansruedi Patzen
Nadja Rutz
Fabian Schmid
Kevin Schmidiger
Matthias Schneider
Melina Staub
Pascal Stump
Ambroise Suter
Nico Vinzens
# 2018 Klimawandel
Matthias Baumann
Oliver Dias
Jonas Gründler 
Sebastian Lenhard
Silvio Marti
Michael Müller
Hansruedi Patzen
Melina Staub
Martin Stypinski
Nicolas Tobler
Raphael Unterer
# 2019 Wavelets
Julian Bärtschi
Jonas Gründler
Dominic Hüppi
Raphael Nestler
Hansruedi Patzen
Cédric Renda
Michael Schmid
Roy Seitz
Manuel Tischhauser
Nicolas Tobler
Raphael Unterer
Kris Wyss
# 2020 Numerik
Benjamin Bouhafs-Keller
Daniel Bucher
Manuel Cattaneo
Patrick Elsener
Reto Fritsche
Niccolò Galliani
Tobias Grab
Thomas Kistler
Fabio Marti
Joël Rechsteiner
Cédric Renda
Michael Schmid
Mike Schmid
Michael Schneeberger
Martin Stypinski
Manuel Tischhauser
Nicolas Tobler
Raphael Unterer
Severin Weiss
# 2021 Matrizen
Joshua Bär
Marius Baumann
Reto Fritsche
Alain Keller
Marc Kühne
Robine Luchsinger
Naoki Pross
Thomas Reichlin
Michael Schmid
Pascal Andreas Schmid
Adrian Schuler
Thierry Schwaller
Michael Steiner
Tim Tönz
Fabio Viecelli
Lukas Zogg
# 2022 Spezielle Funktionen
Joshua Bär
Marc Benz
Manuel Cattaneo
Fabian Dünki
Enez Erdem
Réda Haddouche
David Hugentobler
Alain Keller
Yanik Kuster
Marc Kühne
Erik Löffler
Andrea Mozzini Vellen
Patrik Müller
Samuel Niederer
Naoki Pross
Thierry Schwaller
Nicolas Tobler
Tim Tönz
Raphael Unterer
# 2023 Harmonische Analysis
David Bättig
Florian Baumgartner
Jakob Gierer
Dimitry Grigoriev
Dominik Gschwind
Vincent Haufe
Nathan Hoffman
Alain Keller
Jan Langenegger
Marco Niederberger
Lukas Reitemeier
Stefan Richle
Yanick Schoch
# 2024 Variationsprinzipien
Sofia Aaltonen
Ronja Allenfort
Selvin Blöchlinger
Flurin Brechbühler
Baris Catan
Gabriela Rodrigues
Maurin Doswald
Jakob Gierer
Jannis Gull
Andrin Kälin
Shaarujan Kamalanathan
Kevin Kempf
Tobias Locher
Matthias Meyer
Ana Milivojevic
Patrik Müller
Stephan Oseghale
David Peter
Anna Pietak
Marco Rouge
Sven Schlömmer
Lukas Schöpf
Joel Stohler
Nico Tuscano
# 2025 Felder
Sofia Aaltonen
Emir Arslan
Jero Barahona
Rafael Monteiro
Damian Birchler
Flurin Brechbühler
Nino Briker
Philip Brun
Roman Cvijanovic
Nicola Dall'Acqua
Yanick Diggelmann
Robin Eberle
Sebastian Eggli
Damien Flury
Laurin Heitzer
Andrin Kälin
Shaarujan Kamalanathan
Alain Keller
Martina Knobel
Gian Kraus
Patrik Müller
Mike Peng
Dino Ramcilovic
Joël Rechsteiner
Andrin Rütsche
Michael Schmid
Lukas Schöpf
Fabian Steiner
Loris Trüb
Raphael Unterer
Pascal Widmer
Tobias Zuber
# 2026 Algebra und Analysis
Lukas Buchli
Dominik Castelberg
Baris Catan
Gian Cavegn
Tom Dawson
Nicola Dall'Acqua
Jack Dumovich
Kai Erdin
Nathanael Fässler
Damien Flury
Jan Gachnang
Jakob Gierer
Timon Gnehm
Jannis Gull
Melissa Haumüller
Pascal Hirzel
Malenka Hossli
Shaarujan Kamalanathan
Noel Karlsson
Jan Klarer
Simon Köpfli
Lukas Krüdewagen
Manuel Kuhn
Selina Malacarne
Stephanie Märklin
Roman Meyer
Etienne Schafflützel
José Schmid
Andri Sprecher
Andrea Studer
Fabian Suter
Florian von Wyl
Roman Weber
Simon Widmer
EOF
) | awk '{
	key = $NF
	printf("%s", key)
	for (i = 1; i < NF; i++) {
		printf(" %s", $i)
	}
	printf("\n")
}' | sort | uniq -c | awk 'BEGIN {
	linenumber = 0;
	printf("%%\n")
	printf("%% teilnehmer.tex -- Alle Seminarteilnehmer\n")
	printf("%% do not edit, created by teilnehmer.sh\n")
	printf("%%\n")
	printf("%% (c) 2026 Prof Dr Andreas Müller\n")
	printf("%%\n")
	printf("\\def\\teilnehmerallerseminare{")
	counter = 0
}
{
	counter = counter + 1
	linenumber = linenumber + 1
	if (linenumber > 1) {
		printf(", ")
	}
	count=$1
	lastname=$2
	for (i = 3; i <= NF; i++) {
		printf("%s ", $i)
	}
	if (count > 1) {
		printf("%s (%d)", lastname, count)
	} else {
		printf("%s", lastname, count)
	}
}
END {
	printf("}\n")
	printf("\\def\\anzahlteilnehmer{%d}\n", counter)
}'
