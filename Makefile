include ./guidednotes/Makefile
COURSE="ApplMath_1201B_W26"

appendix:
	${LATEXMK} appendix/*.tex

slides:
	${LATEXMK} -jobname="${COURSE}_%A" slides.tex polls.tex

exercises:
	${LATEXMK} -jobname="${COURSE}_exercises_%A" exercises/week*.tex

