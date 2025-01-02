LATEXMK=latexmk -lualatex -halt-on-error -interaction=nonstopmode
COURSE=ApplMath_1201B_W25

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
	${LATEXMK} polls.tex main.tex
	cp build/main.pdf ${COURSE}_main.pdf
	cp build/polls.pdf ${COURSE}_polls.pdf

publish: main
	${LATEXMK} -jobname="${COURSE}_%A" publish/*.tex
