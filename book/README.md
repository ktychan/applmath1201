# Course textbook (LaTeX)

LaTeX (lualatex) edition of the course textbook, converted from the MyST
markdown sources in this folder (`index.md`, `ch1.md` … `ch8.md`).

## Build

```sh
cd book
latexmk book.tex            # instructor edition: solutions shown  -> book.pdf
latexmk book-student.tex    # student edition: solutions removed   -> book-student.pdf
```

`./.latexmkrc` selects lualatex with `--shell-escape` (needed by `minted`,
which calls `pygmentize`) and puts auxiliary files in `./.aux`.

A single chapter can be compiled on its own thanks to `subfiles`:

```sh
cd book/chapters && lualatex --shell-escape ch3.tex
```

## Layout

| Path | Purpose |
| --- | --- |
| `book.tex` | main file, instructor edition |
| `book-student.tex` | defines `\hidesolutions` and inputs `book.tex`; every `solution` environment is dropped |
| `preamble.tex` | packages, fonts (TeX Gyre Pagella, STIX Two Math, Iosevka Term), colours, boxes, theorem environments, cross-referencing |
| `chapters/index.tex` | the "Welcome" page (front matter, unnumbered) |
| `chapters/ch1.tex` … `ch8.tex` | the eight chapters |
| `chapters/biology.tex` | conversion of the orphan `biology.md` (not in the MyST table of contents; not included in `book.tex`) |
| `standalones/` | figures. `diagram-venn-2sets.pdf` and `image-total-probability.png` were copied here from `../standalones/` so the book is self-contained |
| `tools/md2tex.py` | the converter that produced the first version of `chapters/*.tex` |

## Conventions used in the LaTeX

* `{math}` roles → `\( … \)`; ```` ```{math} ```` blocks → `equation` environments.
* `{prf:example}`, `{prf:definition}`, `{exercise}` → `example`, `definition`,
  `exercise` (amsthm, one shared counter per chapter, as in the guided notes).
* `{solution}` → `solution` (handled by the `comment` package so the student
  edition can drop it; `\begin{solution}` / `\end{solution}` must stand alone on
  their own lines).
* `{attention}`, `{danger}`, … → `attentionbox`, `dangerbox`, … (tcolorbox).
  The `box` suffix avoids a clash with the pre-existing `\danger` symbol.
* Every equation, example, exercise and definition has a `\label`. Labels from
  the markdown were kept; the others were generated as
  `eq:<chapter>-<n>`, `eg:<chapter>-<n>`, `ex:<chapter>-<n>`, `def:<chapter>-<n>`,
  `fig:<chapter>-<n>` with chapter slugs `models, de, inexact, prob, rv, vec, eig, sys`.
* `[](#label)` → `\cref{label}` (cleveref, capitalised, no abbreviation), or
  `\eqref` when the target is an equation, or plain `\ref` when the markdown
  already spelled out "Figure"/"Example"/… before the reference.
* Inline code → `\code{…}` (monospace); code blocks → `minted`.
* Figures whose image file does not exist are rendered as a red
  `\missingfigure{path}` placeholder so the gap is visible in the PDF.
* Figures that sit inside an example/solution box are not floats (floats are
  illegal there); they are `center` blocks with `\captionof{figure}`.
* The three theorem environments share one counter; inside each environment the
  counter is aliased to the environment's type so `\cref` says "Example 2.3",
  not "Statement 2.3".
* Lines that started with `%` in the markdown (LaTeX-style remarks by the
  author) are kept as LaTeX comments.

## Conversion policy

The conversion changes markup only; the wording and the mathematics are
exactly those of the markdown, including its mistakes (to be edited later).
The only edits to the source text were syntactic repairs without which LaTeX
cannot compile; each is recorded as a `% CONVERSION NOTE` at the top of the
chapter file:

* `ch2`: a `\footnote{…}` opened at "Provided u(t) is not zero" was never
  closed in the markdown; it is closed after "the solution for all t".
* `ch8`: every `\\[` in the markdown had been mangled into the literal text
  ``\```{math}``; restored to `\\[…]` line breaks.
* `ch8`: a `trim={1in, 4.5in, 2in, 0.75in}` option used commas, which
  `graphicx` rejects; changed to space-separated lengths.
* plain-TeX `{a \brack b}` column vectors → `bmatrix` (amsmath discourages `\brack`).
* `multline*` → numbered `multline` so that every equation has a label.

Page counts: instructor edition 95 pages, student edition 74 pages.
See `CONVERSION-NOTES.md` for everything noticed during the conversion check
(dangling references, missing figures, mathematical slips, typos) that was
deliberately left for the editing phase.

## Known issues inherited from the markdown (left as they are)

* Dangling references: `tab:birds` (the table is labelled `table:birds`),
  `eg.age` (typo for `eg:age`), `fig:excel`, `fig:pmf` (that figure has no
  label in the source), `tab:PF`; `\cite{zar}` has no bibliography. In ch8,
  `eg:linear1` points to the Chapter 2 example of that name.
* Missing figure files (placeholders in the PDF): `../standalones/build/*`
  was never built: plot-cdf, plot-pmf, plot-pdf, plot-monte-carlo (ch5);
  plot-vector_rep, plot-vector-addition, plot-cosine-law,
  plot-dotprod-triangle, plot-cross-product-exercise,
  plot-linear-transformation, plot-vector-field-geoff, plot-dt_motion,
  plot-adult-juveniles-transition-diagram, plot-invertible-vf (ch6);
  plot-triangle, plot-antisymmetric-matrix, plot-perron,
  plot-age-structure-primitive (ch7); plot-predprey1, plot-timeseries1 (ch8).
* `standalones/image-birds.pdf` is 150 MB and accounts for almost all of the
  size of `book.pdf` (about 160 MB). Downsampling it is an asset decision,
  not a conversion one, so it was left untouched.
