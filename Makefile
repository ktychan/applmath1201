LATEXMK=latexmk -lualatex -halt-on-error -interaction=nonstopmode
COURSE=ApplMath_1201B_W26

.PHONY: all clean standalones main publish 

all: publish

clean: 
	rm -rf _build
	rm -rf _minted-main
	rm -rf standalones/build
	rm -rf publish/*.tex publish/build

standalones:
	${LATEXMK} standalones/*.tex

main: standalones
	mkdir -p publish
	${LATEXMK} polls.tex main.tex
	cp build/main.pdf ${COURSE}_main.pdf

slides: 
	${LATEXMK} -jobname="${COURSE}_%A" slides.tex polls.tex
	cp build/polls.pdf ${COURSE}_polls.pdf
	cp build/slides.pdf ${COURSE}_slides.pdf

publish: main slides
	${LATEXMK} -jobname="${COURSE}_%A" publish/*.tex
