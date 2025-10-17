#
# Makefile -- build stuff used in subdirectories
#
# (c) 2022 Prof Dr Andreas Müller, Hochschule Rapperswil
# 
CHAPTERS =								\

images:
	@for d in ${CHAPTERS};						\
	do								\
		(							\
			if [ -f $${d}/Makefile ];			\
			then						\
				echo "make images in $${d}";		\
				cd $${d};				\
				make images;				\
			fi;						\
		);							\
	done
