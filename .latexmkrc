# Note for vscode: Don't set $jobname in .latexmkrc and in vscode because the jobname in LaTeX-workshop must be a fixed string. If jobname is set, then the preview feature in LaTeX-workshop doesn't work. Use a Makefile to compile pdfs for students.
# $jobname = "MATH_1229_F24_%A";

set_tex_cmds( '--shell-escape %O %S' );
$pdf_mode = 4;  # 4 is lualatex, 5 is xelatex
$dvi_mode = 0;
$postscript_mode = 0;
$do_cd = 1;

$pdf_previewer = "open -a Skim";

$out_dir = "build";
$aux_dir = "build/aux";
