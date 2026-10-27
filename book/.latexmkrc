# latexmk configuration for the textbook (run latexmk from inside book/)
set_tex_cmds( '--shell-escape -interaction=nonstopmode %O %S' );
$pdf_mode = 4;      # lualatex
$dvi_mode = 0;
$postscript_mode = 0;
$aux_dir = ".aux";
$out_dir = ".";
