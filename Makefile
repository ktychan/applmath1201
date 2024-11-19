LATEXMK=latexmk -lualatex -halt-on-error -interaction=nonstopmode
COURSE=ApplMath_1201B_W24

.PHONY: all clean standalones main publish 

all: publish

clean: 
	rm -rf build
	rm -rf standalones/build
	rm -rf publish/*.tex publish/build

standalones:
	${LATEXMK} standalones/*.tex

main: standalones
	mkdir -p publish
	${LATEXMK} main.tex
	cp build/main.pdf ${COURSE}_main.pdf

publish: main
	${LATEXMK} -jobname="${COURSE}_%A" publish/*.tex
