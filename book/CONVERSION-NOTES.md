# Notes from the markdown → LaTeX conversion (2026-10-26)

Everything below was *noticed* while checking the converted chapters against
the markdown and deliberately **left unchanged**, because the conversion step
was markup-only. It is a to-do list for the editing phase. Line numbers refer
to `chapters/chN.tex` unless marked `md`.

## Dangling or odd cross-references

| Chapter | Reference | Note |
| --- | --- | --- |
| 1 | `tab:birds` (×4) | table is labelled `table:birds` |
| 1 | `[Chapter 2](./ch2)` | became `\hyperref[ch:de]{Chapter 2}`; fine in the full book |
| 2 | "see also Exercise 13" | hard-coded text, no label |
| 2 | "Figure 1.1" after "a value" | markdown had `[](fig:ch1_fig1)` with no parentheses; sentence reads oddly |
| 3 | "Example 1", "Chapter 2" (several) | hard-coded numbers; the example is 3.1 in the book |
| 3 | line 153 "(Figure fig:phase)" | probably meant panel (b) |
| 5 | `fig:pmf`, `fig:excel` | the pmf figure has no label in the source (auto label `fig:rv-1`); no spreadsheet figure exists |
| 5 | `fig:pdf` | figure has a label but no caption, so `\ref` resolves to the section number; the caption text follows as a paragraph |
| 5 | `\cite{zar}` | no bibliography |
| 6 | `eg.age` | typo for `eg:age` |
| 6 | md 216 second "(Figure fig:dotprod)" | probably meant `fig:xprod` |
| 6 | "Example 4", "Chapter 1" | hard-coded |
| 7 | `tab:PF` | no such table; the float is `fig:perron` |
| 7 | "as it was in Example `fig:vf_rot`" | a figure referred to as an Example |
| 8 | `eg:linear1` (caption of `fig:eg_illustrate`) | points at the Chapter 2 example; `eg:DE-linear1` meant |
| 8 | `eq:fieldplot` | a figure labelled with an `eq:` prefix (works) |

## Missing figure files (red placeholders in the PDF)

`../standalones/build/` does not exist in the repository.

* ch5: plot-cdf, plot-pmf, plot-pdf, plot-monte-carlo
* ch6: plot-vector_rep, plot-vector-addition, plot-cosine-law, plot-dotprod-triangle,
  plot-cross-product-exercise, plot-linear-transformation, plot-vector-field-geoff,
  plot-dt_motion, plot-adult-juveniles-transition-diagram, plot-invertible-vf;
  `fig:xprod` has no image at all, only a caption
* ch7: plot-triangle, plot-antisymmetric-matrix, plot-perron, plot-age-structure-primitive
* ch8: plot-predprey1, plot-timeseries1
* ch2: `fig:logistic` (inside the logistic solution) and `fig:ch1_fig4` both include
  `plot-logistic.pdf`; the first is described as a line of slope r/K, so it is
  probably the wrong file
* ch4: `diagram-venn-2sets.pdf` is a 3-page standalone; page 2 (both sets) is
  shown, which matches the caption "Inclusion-Exclusion Principle"
* Asset sizes: `standalones/image-birds.pdf` is 150 MB and
  `image-total-probability.png` 10 MB; they make `book.pdf` about 160 MB.

## Mathematical slips noticed

* ch1 `fig:bird_cubic` caption: solid line said to be \(k\ell^2\); text says \(k\ell^3\).
* ch1 code block: `lengths` has 22 entries, `mass` has 24.
* ch2 eq. (de-3): missing `+` before `\cdots`; the sentence after omits \(P_0\).
* ch2 eq. (de-28): integrand ends in `dt` instead of `ds`.
* ch2 eq. (de-34): "rate eliminated" drops the factor \(u(t)\).
* ch3 solution of `eg:equilibrium`: "g(4) = …" should be \(g'(4)\); equilibria called \(\bar u\) although the variable is \(N\).
* ch4 `eg:triple`: "6 000 − 431 = 5 539" (461 computed one sentence earlier).
* ch4 eq. (prob-24): first line should read \(1-\mathbb P(\text{homozygous offspring})\).
* ch4: numbers like `1 124` use a space as thousands separator inside math (renders as 1124).
* ch5 eq. (rv-1): `\text{``tails.}` lacks the closing quote; eq. (rv-10) lacks a comma before \(m\);
  eq. (rv-18) has `&,`; `eg:sample-stats`: \(-0.78/12 = -0.65\) (sum is −7.8), \(\bar X = 17.25\) grams and
  \(s^2 = 17.25/11\) do not match the data; "sample standard deviation is meant to estimate the variance".
* ch5 t-test solution: the numbered steps are 1, 2, 3 then 1, 2 (the markdown restarts the list after a
  display equation) while the text says "Repeat steps 1 to 4".
* ch6 eq. (vec-13): missing minus signs in the Law-of-Cosines rearrangement; eq. (vec-21): missing `+`
  between products; eq. (vec-24): \(f_2(x_2,x_2,\dots)\); eq. (vec-27): \(c_1\vec x_n\) should be \(c_n\);
  eq. (vec-36): \(x_1(1),x_2(1)\) repeated instead of \(x_1(2),x_2(2)\), period inside the matrix;
  "after t" vs underbrace "n times"; captions `\| y\|` and `F^{-1}(\vec x)` lack `\vec`.
* ch7: \(A\vec v-\lambda I\vec v = 0\) uses scalar 0; some displays end with "." before the sentence
  continues; `[[a,−b],[b,a]]` is called "antisymmetric".
* ch8: \(n_2 > \beta/\alpha\) (three times) where \(\alpha/\beta\) is meant; \(\alpha n_i(t)\) for \(n_1\);
  \(\frac{d\vec u}{dt} = A\vec x + \vec b(t)\); "distinct real eigenvectors \(\lambda_1,\lambda_2\) … \(\vec v_n\)";
  eq. (sys-29) sign vs the preceding multline; in `eg:ivp1` the constant vector and initial condition are
  written as row vectors and "multiple of this eigenvalue" (eigenvector); the final equation (sys-59)
  "… (2−5s) ds 5t −1." is garbled in the source.

## Typos and wording (as written in the markdown)

* ch1: "birds of a from an observation", "idea gas law", "exhibit isometry/allometry", "a constants",
  "a function function", "one from the method", "reproductive rated", "Which of the followings",
  "an negative index", "that are are far apart", "print `x = 5`".
* ch2: "natural phenomenons", "Differential equations appears", "is call solving an differential equation",
  "looking a family", "re-state this more using", "the the differential equation", "intraveneously",
  "more complicated that", "that involved in that problem"; caption "relation between r and k".
* ch3: "decrasing", "when when", "will tends away", "repells", "have be exact", "an approximate solutions".
* ch4: "heterzygous", "estriol the blood", "the of the 5 539", "formalize idea like this",
  "realization than another", "specificity of nasal-swab test", "the production a heterozygous".
* ch5: "one whose the range", "We generate pseudorandom to solve", "We have see that",
  "Data is typically store", "less that −0.519", "each these uniform variables",
  "Random number were normalized"; "the spreadsheet below" refers to an image that does not exist.
* ch6: "we we represent", "a point in two-dimensional can also", "always always", "an adults",
  "A few of remarks", "arrow's tail … the arrows tip", "We then take  follow".
* ch7: "Its solution is is", "the what is happening", "we to obtain", "while we it is true",
  "calculate greatest common divisor", "if a  A is positive", "the Perron's theorem"; caption says
  Perron-Frobenius while the text says Perron; the footnote never names Frobenius.
* ch8: "total rate birth rate", "postive", "straitforward", "equilbrium", "trace our straight lines",
  "part of a  the fundamental", "the \(w_1=2\)", "Homogenous" (subsection title), sentence without a
  final period at the end of the diagonal-system paragraph, "mg min\(^{-1}\)".
* index: "Lokta-Volterra", "matricies", unfinished bullet "Using", unfinished last sentence
  "Definitions and theorem are precise statements that describe".

## Source repairs made for compilation (recorded as `% CONVERSION NOTE` in the files)

* ch2: unclosed `\footnote{…}` at "Provided u(t) is not zero" closed after "for all t".
* ch8: `\\[` mangled into ``\```{math}`` restored; `trim={1in, 4.5in, …}` → space-separated.
* All chapters: `{a \brack b}` → `bmatrix`; `multline*` → labelled `multline`; display math inside the
  duck figure caption (ch1) set as inline math, because display math is illegal inside `\caption`.

## Markup fixes made by hand after the automatic conversion

* ch1: three-step list in the hymenopteran solution re-joined around its display equations.
* ch2: three tall portrait figures given `height=0.6\textheight, keepaspectratio`.
* ch3: `scale=3.25` tikz figure wrapped in `\resizebox`; duplicated `\centering` removed;
  `Figure \eqref{fig:…}` → `Figure \ref{fig:…}`.
* ch4: `page=2` on the Venn diagram.
* ch5: LaTeX quotes ``heads''/``tails'' that the converter had mistaken for inline code restored;
  `Example \ref{}` used in three places.
* ch6: `Figures \ref{} and \ref{}`; extra row spacing in the Law-of-Cosines `array`.
* ch8: `Figure \cref` / `Example \cref` in raw captions → `\ref`.
* preamble: theorem types aliased for cleveref (so `\cref` says "Example", not "Statement");
  parskip restored inside boxes; admonition environments renamed `…box`.
