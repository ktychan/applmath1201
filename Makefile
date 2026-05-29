# vim:number
include ./guidednotes/Makefile
COURSE="ApplMath_1201B_$(shell git rev-parse --abbrev-ref HEAD)"

.PHONY: all clean 

.DEFAULT_GOAL := all
all: build.pdf slides.pdf polls.pdf
	cp build.pdf ${COURSE}_main.pdf
	cp slides.pdf ${COURSE}_slides.pdf
	cp polls.pdf ${COURSE}_polls.pdf

clean:
	rm -f {*,**/*}.pdf
	rm -f {*,**/*}.synctex.gz
	rm -rf **/.aux build
