#!/usr/bin/env python3
"""
md2tex.py -- convert the MyST-markdown chapters in book/*.md to LaTeX.

Usage (from the repository root or from book/):

    python book/tools/md2tex.py            # writes book/chapters/*.tex

Design goals
------------
* Faithful: the prose is carried over verbatim; only markup is translated.
  Known *syntactic* defects in the markdown that would break LaTeX are
  repaired by a small, explicit patch table (SOURCE_PATCHES) and every
  patch is echoed as a `% CONVERSION NOTE` comment in the output.
* Every equation, example, exercise, definition and figure receives a
  \\label{...}: the markdown label when one exists, otherwise an
  automatically generated one (eq:<chapter-slug>-<n>, eg:..., ex:..., ...).
* Cross references `[](#label)` become \\cref{...} (or \\eqref{...} for
  equations).  Dangling references are left dangling and reported.

Markup handled
--------------
  headings            #, ##, ###
  roles               {math}`...`  (also the mangled {math}`...\\) closer)
  directives          ```{math} / :::{math}      -> equation (+label)
                      :::{prf:example}            -> example
                      :::{prf:definition}         -> definition
                      :::{exercise}               -> exercise
                      :::{solution .dropdown}     -> solution
                      :::{figure} [path]          -> figure (placeholder if missing)
                      :::{attention}/{danger}     -> admonition boxes
                      ```{code}/{code-cell}/python-> minted (or raw LaTeX passthrough)
                      ```{csv-table}              -> table
  lists               -, *, 1.   (nested by indentation)
  pipe tables         | a | b |
  footnotes           [^id] ... [^id]: text
  links               [text](url), [Chapter 2](./ch2)
  emphasis            *em*, **bold**, `code`
  raw LaTeX blocks    \\begin{...} ... \\end{...} are passed through
"""
from __future__ import annotations

import os
import re
import shutil
import sys
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(HERE)
SRC = BOOK
OUT = os.path.join(BOOK, "chapters")
STANDALONES = os.path.join(BOOK, "standalones")
PARENT_STANDALONES = os.path.join(os.path.dirname(BOOK), "standalones")

# order of files in the book, with a short slug used for auto labels
FILES = [
    # (markdown file, slug, numbered?)
    ("index.md", "welcome", False),
    ("ch1.md", "models", True),
    ("ch2.md", "de", True),
    ("ch3.md", "inexact", True),
    ("ch4.md", "prob", True),
    ("ch5.md", "rv", True),
    ("ch6.md", "vec", True),
    ("ch7.md", "eig", True),
    ("ch8.md", "sys", True),
    ("biology.md", "bio", True),
]
CHAPTER_LABEL = {f"ch{i}": slug for i, (fn, slug, _) in enumerate(FILES[1:9], start=1)}

# ---------------------------------------------------------------------------
# Source patches: minimal *syntactic* repairs so the LaTeX compiles.  Nothing
# here changes wording.  Each entry: (file, old, new, note).
# ---------------------------------------------------------------------------
SOURCE_PATCHES = [
    (
        "ch8.md",
        "trim={1in, 4.5in, 2in, 0.75in}, clip",
        "trim={1in 4.5in 2in 0.75in}, clip",
        "graphicx's trim= option takes four space-separated lengths; the markdown had commas, which LaTeX rejects.",
    ),
    (
        "ch2.md",
        "Consequently, {math}`u(t) = 0` is the solution for all {math}`t`, we can obtain \n```{math}",
        "Consequently, {math}`u(t) = 0` is the solution for all {math}`t`.}, we can obtain \n```{math}",
        "the \\footnote{...} opened at `Provided u(t) is not zero` was never closed in the markdown; "
        "closed it after `for all t` so the footnote ends before the display equation.",
    ),
]

# A global, mechanical repair: somewhere upstream every `\\[` inside LaTeX
# became the literal text ``\\```{math}``.  Restore it.
MANGLED_LINEBREAK = "\\```{math}"


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
FENCE_RE = re.compile(r"^(\s*)(`{3,}|:{3,})\s*(?:\{([A-Za-z:_.-]+)(?:\s+([^}]*))?\}|([A-Za-z][\w+-]*))?\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")
OPTION_RE = re.compile(r"^:([A-Za-z][\w-]*):\s*(.*)$")
FOOTDEF_RE = re.compile(r"^\[\^([^\]]+)\]:\s*(.*)$")
BEGIN_RE = re.compile(r"^\s*\\begin\{([A-Za-z*]+)\}")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")

VERBATIM_DIRECTIVES = {"math", "code", "code-cell", "csv-table", "python"}
THEOREM_DIRECTIVES = {
    "prf:example": ("example", "eg"),
    "prf:definition": ("definition", "def"),
    "prf:theorem": ("thm", "thm"),
    "exercise": ("exercise", "ex"),
}
ADMONITIONS = {"attention", "danger", "warning", "note", "tip", "important", "caution", "hint", "seealso"}


def dedent(lines: list[str]) -> list[str]:
    indents = [len(l) - len(l.lstrip()) for l in lines if l.strip()]
    if not indents:
        return [l.strip() for l in lines]
    k = min(indents)
    return [l[k:] if len(l) >= k else l.lstrip() for l in lines]


def find_fence_close(lines: list[str], start: int, fence: str) -> int:
    """Index of the line closing `fence` (same char, length >= len(fence)), or len(lines)."""
    ch = fence[0]
    n = len(fence)
    for j in range(start, len(lines)):
        s = lines[j].strip()
        if s and set(s) == {ch} and len(s) >= n:
            return j
    return len(lines)


def find_env_close(lines: list[str], start: int, env: str) -> int:
    depth = 0
    b = re.compile(r"\\begin\{" + re.escape(env) + r"\}")
    e = re.compile(r"\\end\{" + re.escape(env) + r"\}")
    for j in range(start, len(lines)):
        depth += len(b.findall(lines[j]))
        depth -= len(e.findall(lines[j]))
        if depth <= 0:
            return j
    return len(lines) - 1


def matching_brace(s: str, i: int) -> int:
    """s[i] == '{'; return index of the matching '}'."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return -1


def convert_brack(s: str) -> str:
    r"""{a \brack b} -> \begin{bmatrix} a \\ b \end{bmatrix} (plain-TeX \brack is
    discouraged under amsmath).  {2 \quad 4 \brack 1 \quad 2} -> 2x2 matrix."""
    while True:
        k = s.find("\\brack")
        if k < 0:
            return s
        # find the innermost '{' before k whose matching '}' is after k
        i = k
        opener = -1
        while i >= 0:
            if s[i] == "{" and (i == 0 or s[i - 1] != "\\"):
                j = matching_brace(s, i)
                if j > k:
                    opener = i
                    break
            i -= 1
        if opener < 0:
            # give up: leave as is
            return s
        closer = matching_brace(s, opener)
        inner = s[opener + 1 : closer]
        top, bottom = inner.split("\\brack", 1)
        def row(x: str) -> str:
            return " & ".join(p.strip() for p in re.split(r"\\quad", x)) if "\\quad" in x else x.strip()
        rep = r"\begin{bmatrix} " + row(top) + r" \\ " + row(bottom) + r" \end{bmatrix}"
        s = s[:opener] + rep + s[closer + 1 :]


def tex_escape_code(s: str) -> str:
    out = []
    for c in s:
        if c == "\\":
            out.append(r"\textbackslash{}")
        elif c in "{}":
            out.append("\\" + c)
        elif c in "#$%&_":
            out.append("\\" + c)
        elif c == "^":
            out.append(r"\^{}")
        elif c == "~":
            out.append(r"\textasciitilde{}")
        else:
            out.append(c)
    return "".join(out)


# ---------------------------------------------------------------------------
# converter
# ---------------------------------------------------------------------------
@dataclass
class Ctx:
    slug: str
    numbered: bool = True
    in_caption: bool = False
    in_math: bool = False
    box_depth: int = 0
    counters: dict = field(default_factory=dict)
    footnotes: dict = field(default_factory=dict)
    notes: list = field(default_factory=list)
    labels: dict = field(default_factory=dict)  # label -> kind (eq, fig, eg, ...)
    refs: list = field(default_factory=list)
    missing: list = field(default_factory=list)

    def auto_label(self, kind: str) -> str:
        n = self.counters.get(kind, 0) + 1
        self.counters[kind] = n
        return f"{kind}:{self.slug}-{n}"

    def register(self, label: str, kind: str):
        if label:
            self.labels[label] = kind


class Converter:
    def __init__(self, ctx: Ctx, label_kinds: dict):
        self.ctx = ctx
        self.label_kinds = label_kinds  # global map from first pass

    # ----- inline -----------------------------------------------------------
    def roles(self, s: str) -> str:
        """{math}`...`  or  {math}`...\\)  ->  \\(...\\)"""
        s = re.sub(r"\{math\}`(.*?)(?:`|\\\))", lambda m: r"\(" + m.group(1) + r"\)", s)
        return s

    def refs(self, s: str) -> str:
        def rep(m):
            label = m.group(1)
            if label.startswith("./ch") or label.startswith("ch"):
                return m.group(0)
            self.ctx.refs.append(label)
            kind = self.label_kinds.get(label) or self.ctx.labels.get(label)
            prefix = s[max(0, m.start() - 12) : m.start()]
            if kind == "eq":
                return r"\eqref{" + label + "}"
            if re.search(r"(Figure|Figures|Example|Examples|Table|Tables|Equation|Section|Chapter)s?\s+$", prefix):
                return r"\ref{" + label + "}"
            if re.search(r"\\ref\{[^}]*\}[a-z]?\s*(and|,|&)\s*$", prefix):
                return r"\ref{" + label + "}"
            return r"\cref{" + label + "}"

        return re.sub(r"\[\]\(#?([^)\s]+)\)", rep, s)

    def links(self, s: str) -> str:
        def rep(m):
            text, url = m.group(1), m.group(2)
            mm = re.match(r"^\./(ch\d)$", url)
            if mm:
                return r"\hyperref[ch:" + CHAPTER_LABEL[mm.group(1)] + "]{" + text + "}"
            return r"\href{" + url + "}{" + text + "}"

        return re.sub(r"(?<!\!)\[([^\]]+)\]\(([^)\s]+)\)", rep, s)

    def inline_image(self, path: str) -> str:
        p, ok = self.resolve_image(path)
        if ok:
            return "\\begin{center}\\includegraphics[width=0.8\\linewidth]{" + p + "}\\end{center}"
        return "\\begin{center}\\missingfigure{" + path + "}\\end{center}"

    def inline(self, s: str, raw: bool = False) -> str:
        """Convert inline markup of a prose string (may span lines)."""
        s = s.replace(MANGLED_LINEBREAK, "\\\\[")
        store: list[str] = []

        def stash(text: str) -> str:
            store.append(text)
            return f"\x00{len(store) - 1}\x00"

        # 1. protect math roles, inline code, and LaTeX reference commands
        s = re.sub(r"\{math\}`(.*?)(?:`|\\\))", lambda m: stash(r"\(" + convert_brack(m.group(1)) + r"\)"), s)
        s = re.sub(r"\\\((.*?)\\\)", lambda m: stash(r"\(" + m.group(1) + r"\)"), s)
        if not raw:
            s = re.sub(r"`([^`\n]+)`", lambda m: stash(r"\code{" + tex_escape_code(m.group(1)) + "}"), s)
        s = re.sub(r"\\(eqref|ref|cref|Cref|label|cite|hyperref|href|includegraphics)(\[[^\]]*\])?\{[^}]*\}",
                   lambda m: stash(m.group(0)), s)
        # 2. images, references and links
        s = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", lambda m: stash(self.inline_image(m.group(2))), s)
        s = self.refs(s)
        s = self.links(s)
        s = re.sub(r"<span class=\"(\w+)\">(.*?)</span>", r"\\\1{\2}", s)
        # 3. footnote references
        def fn(m):
            key = m.group(1)
            body = self.ctx.footnotes.get(key)
            if body is None:
                return m.group(0)
            return stash(r"\footnote{" + self.inline(body) + "}")

        s = re.sub(r"\[\^([^\]]+)\]", fn, s)
        if not raw:
            # 4. emphasis
            s = re.sub(r"\*\*(?!\s)(.+?)(?<!\s)\*\*", r"\\textbf{\1}", s)
            s = re.sub(r"(?<![\w\\*])\*(?![\s*])(.+?)(?<![\s\\])\*(?![\w*])", r"\\emph{\1}", s)
            # 5. straight double quotes -> LaTeX quotes
            s = re.sub(r'"([^"\n]+?)"', r"``\1''", s)
            # 6. escape special characters that are special only to LaTeX
            s = re.sub(r"(?<!\\)&", r"\\&", s)
            s = re.sub(r"(?<!\\)#", r"\\#", s)
            s = re.sub(r"(?<![\\\w])_(?=\w)|(?<=\w)_(?![\w{])", r"\\_", s)
        s = convert_brack(s)
        # restore
        s = re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], s)
        return s

    # ----- blocks -----------------------------------------------------------
    def convert(self, lines: list[str]) -> str:
        out: list[str] = []
        i, n = 0, len(lines)
        while i < n:
            line = lines[i]
            s = line.strip()
            if not s:
                out.append("")
                i += 1
                continue
            # fenced directive / code
            m = FENCE_RE.match(line)
            if m and (m.group(3) or m.group(5)):
                fence = m.group(2)
                name = m.group(3) or m.group(5)
                extra = (m.group(4) or "").strip()  # e.g. ".dropdown"
                arg = m.group(6).strip()
                j = find_fence_close(lines, i + 1, fence)
                body = dedent(lines[i + 1 : j])
                if j >= n:
                    self.ctx.notes.append(f"unterminated fence {name} near: {line.strip()[:60]}")
                out.append(self.directive(name, extra, arg, body))
                i = j + 1
                continue
            # raw LaTeX environment
            mb = BEGIN_RE.match(line)
            if mb:
                env = mb.group(1)
                j = find_env_close(lines, i, env)
                out.append(self.raw_block(lines[i : j + 1]))
                i = j + 1
                continue
            # heading
            mh = HEADING_RE.match(line)
            if mh:
                out.append(self.heading(len(mh.group(1)), mh.group(2)))
                i += 1
                continue
            # footnote definition (already collected) -> skip
            if FOOTDEF_RE.match(line):
                i += 1
                continue
            # list
            ml = LIST_RE.match(line)
            if ml:
                j, text = self.parse_list(lines, i)
                out.append(text)
                i = j
                continue
            # pipe table
            if s.startswith("|") and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]):
                j = i
                while j < n and lines[j].strip().startswith("|"):
                    j += 1
                out.append(self.pipe_table(lines[i:j]))
                i = j
                continue
            # LaTeX comment line
            if s.startswith("%"):
                out.append(line.rstrip())
                i += 1
                continue
            # paragraph
            j = i
            para: list[str] = []
            while j < n:
                l = lines[j]
                t = l.strip()
                if not t:
                    break
                mf = FENCE_RE.match(l)
                if (mf and (mf.group(3) or mf.group(5))) or HEADING_RE.match(l) or BEGIN_RE.match(l) \
                        or FOOTDEF_RE.match(l) or (LIST_RE.match(l) and j > i) or t.startswith("%") \
                        or (t.startswith("|") and j + 1 < n and TABLE_SEP_RE.match(lines[j + 1])):
                    break
                para.append(l.rstrip())
                j += 1
            if not para:  # safety
                para = [line.rstrip()]
                j = i + 1
            out.append(self.inline("\n".join(para)))
            i = j
        text = "\n".join(out)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text

    def heading(self, level: int, title: str) -> str:
        title = self.inline(title)
        star = "" if self.ctx.numbered else "*"
        if level == 1:
            lab = f"ch:{self.ctx.slug}"
            self.ctx.register(lab, "ch")
            extra = ""
            if not self.ctx.numbered:
                extra = f"\n\\addcontentsline{{toc}}{{chapter}}{{{title}}}"
            return f"\\chapter{star}{{{title}}}\\label{{{lab}}}{extra}"
        if level == 2:
            return f"\\section{star}{{{title}}}"
        if level == 3:
            return f"\\subsection{star}{{{title}}}"
        return f"\\subsubsection{star}{{{title}}}"

    # ----- directives -------------------------------------------------------
    @staticmethod
    def split_options(body: list[str]) -> tuple[dict, list[str]]:
        opts: dict = {}
        k = 0
        while k < len(body):
            mo = OPTION_RE.match(body[k])
            if mo:
                opts[mo.group(1)] = mo.group(2).strip()
                k += 1
            elif not body[k].strip() and k == 0:
                k += 1
            else:
                break
        rest = body[k:]
        while rest and not rest[0].strip():
            rest = rest[1:]
        while rest and not rest[-1].strip():
            rest = rest[:-1]
        return opts, rest

    def math_block(self, body: list[str], label: str | None) -> str:
        content = "\n".join(body)
        content = content.replace(MANGLED_LINEBREAK, "\\\\[")
        content = self.roles(content)
        content = convert_brack(content)
        content = re.sub(r"\[\]\(#?([^)\s]+)\)", lambda m: r"\ref{" + m.group(1) + "}", content)
        if self.ctx.in_caption:
            # a caption is measured inside a box, where display math is illegal
            return "\\(" + " ".join(content.split()) + "\\)"
        if not label:
            label = self.ctx.auto_label("eq")
        self.ctx.register(label, "eq")
        if "\\\\" in content and "\\begin{" not in content:
            content = "\\begin{gathered}\n" + content + "\n\\end{gathered}"
        return f"\\begin{{equation}}\\label{{{label}}}\n{content}\n\\end{{equation}}"

    def directive(self, name: str, extra: str, arg: str, body: list[str]) -> str:
        opts, rest = self.split_options(body) if name not in {"python"} else ({}, body)
        label = opts.get("label", "").strip() or None
        if label and re.fullmatch(r"\w+:", label):
            label = None  # a bare prefix such as `ex:` is not a usable label
        if name == "math":
            return self.math_block(rest, label)

        if name in THEOREM_DIRECTIVES:
            env, kind = THEOREM_DIRECTIVES[name]
            title = arg
            ml = re.search(r"\\label\{([^}]*)\}", title)
            if ml:
                label = label or ml.group(1).strip() or None
                title = (title[: ml.start()] + title[ml.end():]).strip()
            if not label:
                label = self.ctx.auto_label(kind)
            self.ctx.register(label, kind)
            head = f"\\begin{{{env}}}"
            if title:
                head += f"[{self.inline(title)}]"
            head += f" \\label{{{label}}}"
            self.ctx.box_depth += 1
            inner = self.convert(rest)
            self.ctx.box_depth -= 1
            return head + "\n" + inner + f"\n\\end{{{env}}}"

        if name == "solution":
            ref = arg.strip()
            comment = f" % solution to {ref}" if ref and ref != "eg:" else ""
            self.ctx.box_depth += 1
            inner = self.convert(rest)
            self.ctx.box_depth -= 1
            return f"\\begin{{solution}}{comment}\n" + inner + "\n\\end{solution}"

        if name in ADMONITIONS:
            title = self.inline(arg) if arg else ""
            head = f"\\begin{{{name}box}}"
            if title:
                head += f"[{title}]"
            if label:
                self.ctx.register(label, "box")
                head += f"\\label{{{label}}}"
            self.ctx.box_depth += 1
            inner = self.convert(rest)
            self.ctx.box_depth -= 1
            return head + "\n" + inner + f"\n\\end{{{name}box}}"

        if name == "figure":
            return self.figure(arg, label, rest)

        if name in {"code", "code-cell", "python"}:
            text = "\n".join(rest)
            if re.search(r"^\s*\\begin\{(figure|center|tikzpicture)\}", text, re.M):
                # the markdown abused a code fence to embed raw LaTeX
                return self.raw_block(rest)
            lang = "python"
            if arg and arg.split()[0].isalpha():
                lang = arg.split()[0]
            return f"\\begin{{minted}}{{{lang}}}\n{text}\n\\end{{minted}}"

        if name == "csv-table":
            return self.csv_table(arg, opts, rest)

        self.ctx.notes.append(f"unknown directive {name}; emitted as plain text")
        return self.convert(rest)

    # ----- figures ----------------------------------------------------------
    def resolve_image(self, path: str) -> tuple[str, bool]:
        """Return (path for \\includegraphics relative to book/, exists?)."""
        base = os.path.basename(path.strip().rstrip("}"))
        for cand in (os.path.join(STANDALONES, base), os.path.join(STANDALONES, base + ".pdf")):
            if os.path.exists(cand):
                return "standalones/" + os.path.basename(cand), True
        for cand in (os.path.join(PARENT_STANDALONES, base), os.path.join(PARENT_STANDALONES, base + ".pdf")):
            if os.path.exists(cand):
                # copy into book/standalones so the book is self-contained
                os.makedirs(STANDALONES, exist_ok=True)
                dst = os.path.join(STANDALONES, os.path.basename(cand))
                if not os.path.exists(dst):
                    shutil.copy2(cand, dst)
                    self.ctx.notes.append(f"copied {cand} -> book/standalones/")
                return "standalones/" + os.path.basename(cand), True
        self.ctx.missing.append(path)
        return path, False

    def figure(self, arg: str, label: str | None, body: list[str]) -> str:
        text = "\n".join(body)
        boxed = self.ctx.box_depth > 0  # floats are illegal inside tcolorbox-style environments
        out = ["\\begin{center}"] if boxed else ["\\begin{figure}[htbp]", "  \\centering"]
        if arg:
            path, ok = self.resolve_image(arg)
            if ok:
                out.append(f"  \\includegraphics[width=0.8\\linewidth]{{{path}}}")
            else:
                out.append(f"  \\missingfigure{{{path}}}")
        has_raw_caption = "\\caption" in text
        if re.search(r"\\begin\{tikzpicture\}|\\includegraphics|\\caption", text):
            out.append(self.raw_block(body, indent="  "))
            caption_text = None
        else:
            caption_text = text.strip()
        if caption_text:
            self.ctx.in_caption = True
            cap = self.convert(body).strip()
            self.ctx.in_caption = False
            cap = re.sub(r"\n\s*\n", "\n", cap)
            out.append(f"  \\captionof{{figure}}{{{cap}}}" if boxed else f"  \\caption{{{cap}}}")
        if not has_raw_caption:
            if not label:
                label = self.ctx.auto_label("fig")
            self.ctx.register(label, "fig")
            out.append(f"  \\label{{{label}}}")
        elif label:
            self.ctx.register(label, "fig")
            out.append(f"  \\label{{{label}}}")
        out.append("\\end{center}" if boxed else "\\end{figure}")
        return "\n".join(out)

    def raw_block(self, lines: list[str], indent: str = "") -> str:
        text = "\n".join(lines)
        if self.ctx.box_depth > 0 and "\\begin{figure}" in text:
            # floats are illegal inside boxes: keep the content in place instead
            text = re.sub(r"\\begin\{figure\}(\[[^\]]*\])?", r"\\begin{center}", text)
            text = text.replace("\\end{figure}", "\\end{center}")
            text = text.replace("\\caption{", "\\captionof{figure}{")
        text = text.replace(MANGLED_LINEBREAK, "\\\\[")
        text = text.replace("{{math}`", "{\x01")  # protect `{{math}` so the role regex sees it
        text = text.replace("\x01", "{math}`")
        text = self.roles(text)
        text = convert_brack(text)
        # cross references inside captions
        text = re.sub(r"\[\]\(#?([^)\s]+)\)", lambda m: self.refs(m.group(0)), text)
        # register labels defined in the raw block, guessing their kind from the
        # enclosing environment
        for m in re.finditer(r"\\label\{([^}]*)\}", text):
            before = text[: m.start()]
            kind = "eq"
            if before.rfind("\\begin{figure}") > before.rfind("\\end{figure}"):
                kind = "fig"
            self.ctx.register(m.group(1), kind)
        # every equation gets a label; unnumbered multline* becomes numbered
        def add_label(m):
            env = m.group(1)
            rest = m.group(2)
            if "\\label" in rest:
                return m.group(0)
            lab = self.ctx.auto_label("eq")
            self.ctx.register(lab, "eq")
            return f"\\begin{{{env}}}\\label{{{lab}}}{rest}"

        text = re.sub(r"\\begin\{(equation|multline|align|gather)\*\}", r"\\begin{\1}", text)
        text = re.sub(r"\\end\{(equation|multline|align|gather)\*\}", r"\\end{\1}", text)
        text = re.sub(r"\\begin\{(equation|multline|align|gather)\}([^\n]*)", add_label, text)
        # figure paths
        def fix_path(m):
            path, ok = self.resolve_image(m.group(2))
            return f"\\includegraphics{m.group(1)}{{{path}}}" if ok else f"\\missingfigure{{{m.group(2)}}}"

        text = re.sub(r"\\includegraphics(\[[^\]]*\])?\{([^}]*)\}", fix_path, text)
        if indent:
            text = "\n".join(indent + l for l in text.split("\n"))
        return text

    # ----- tables -----------------------------------------------------------
    def csv_table(self, caption: str, opts: dict, rows: list[str]) -> str:
        delim = opts.get("delim", ",")
        header = opts.get("header")
        label = opts.get("label") or self.ctx.auto_label("tab")
        self.ctx.register(label, "tab")
        data = [r for r in rows if r.strip()]
        ncol = max(len(r.split(delim)) for r in data)
        out = ["\\begin{table}[htbp]", "  \\centering", "  \\small",
               "  \\begin{tabular}{" + "l" + "r" * (ncol - 1) + "}", "    \\toprule"]
        if header:
            out.append("    " + " & ".join(self.inline(c.strip()) for c in header.split(delim)) + " \\\\")
            out.append("    \\midrule")
        for r in data:
            out.append("    " + " & ".join(self.inline(c.strip()) for c in r.split(delim)) + " \\\\")
        out += ["    \\bottomrule", "  \\end{tabular}",
                f"  \\caption{{{self.inline(caption)}}}", f"  \\label{{{label}}}", "\\end{table}"]
        return "\n".join(out)

    def pipe_table(self, lines: list[str]) -> str:
        def cells(l: str) -> list[str]:
            l = l.strip()
            if l.startswith("|"):
                l = l[1:]
            if l.endswith("|"):
                l = l[:-1]
            return [self.inline(c.strip()) for c in l.split("|")]

        header = cells(lines[0])
        body = [cells(l) for l in lines[2:]]
        ncol = len(header)
        out = ["\\begin{center}", "  \\begin{tabular}{" + "c" * ncol + "}", "    \\toprule",
               "    " + " & ".join(header) + " \\\\", "    \\midrule"]
        for r in body:
            out.append("    " + " & ".join(r) + " \\\\")
        out += ["    \\bottomrule", "  \\end{tabular}", "\\end{center}"]
        return "\n".join(out)

    # ----- lists ------------------------------------------------------------
    def parse_list(self, lines: list[str], i: int) -> tuple[int, str]:
        first = LIST_RE.match(lines[i])
        base = len(first.group(1))
        ordered = first.group(2)[0].isdigit()
        items: list[list[str]] = []
        n = len(lines)
        j = i
        while j < n:
            l = lines[j]
            if not l.strip():
                # blank line: list continues only if the next non-blank line is indented or a marker at base
                k = j + 1
                while k < n and not lines[k].strip():
                    k += 1
                if k >= n:
                    break
                nxt = lines[k]
                ind = len(nxt) - len(nxt.lstrip())
                mk = LIST_RE.match(nxt)
                if (mk and len(mk.group(1)) == base) or ind > base:
                    items[-1].append("")
                    j += 1
                    continue
                break
            ind = len(l) - len(l.lstrip())
            m = LIST_RE.match(l)
            if m and ind == base and (m.group(2)[0].isdigit() == ordered):
                items.append([m.group(3)])
                j += 1
                continue
            if ind > base and items:
                items[-1].append(l)
                j += 1
                continue
            break
        env = "enumerate" if ordered else "itemize"
        out = [f"\\begin{{{env}}}"]
        for it in items:
            head, rest = it[0], it[1:]
            rest = dedent(rest)
            content = self.convert([head] + rest).strip()
            content = content.replace("\n", "\n  ")
            out.append("  \\item " + content)
        out.append(f"\\end{{{env}}}")
        return j, "\n".join(out)


# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------
def preprocess(fname: str, text: str) -> tuple[str, list[str]]:
    notes = []
    for f, old, new, note in SOURCE_PATCHES:
        if f == fname:
            if old in text:
                text = text.replace(old, new, 1)
                notes.append(note)
            else:
                notes.append(f"PATCH NOT APPLIED (text not found): {note}")
    # strip YAML front matter
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    if MANGLED_LINEBREAK in text:
        notes.append("restored every mangled `\\```{math}` back to `\\\\[` (a line break with vertical space)")
    text = text.replace(MANGLED_LINEBREAK, "\\\\[")
    return text, notes


def collect_footnotes(lines: list[str]) -> dict:
    fns = {}
    for l in lines:
        m = FOOTDEF_RE.match(l)
        if m:
            fns[m.group(1)] = m.group(2).strip()
    return fns


def convert_file(fname: str, slug: str, numbered: bool, label_kinds: dict) -> tuple[str, Ctx]:
    with open(os.path.join(SRC, fname), encoding="utf-8") as fh:
        text = fh.read()
    text, notes = preprocess(fname, text)
    lines = text.split("\n")
    ctx = Ctx(slug=slug, numbered=numbered)
    ctx.notes.extend(notes)
    ctx.footnotes = collect_footnotes(lines)
    conv = Converter(ctx, label_kinds)
    body = conv.convert(lines).strip() + "\n"
    header = [
        "%! TeX program = lualatex",
        f"% Converted from book/{fname} by book/tools/md2tex.py (initial conversion).",
        "% This .tex file is the maintained source from now on; the converter is kept for provenance only.",
    ]
    for note in ctx.notes:
        header.append(f"% CONVERSION NOTE: {note}")
    header.append("\\documentclass[../book.tex]{subfiles}")
    header.append("\\begin{document}")
    tex = "\n".join(header) + "\n\n" + body + "\n\\end{document}\n"
    return tex, ctx


def main():
    os.makedirs(OUT, exist_ok=True)
    # pass 1: collect labels and their kinds across the whole book
    label_kinds: dict = {}
    for fname, slug, numbered in FILES:
        _, ctx = convert_file(fname, slug, numbered, {})
        label_kinds.update(ctx.labels)
    # pass 2: emit
    all_refs = set()
    report = []
    for fname, slug, numbered in FILES:
        tex, ctx = convert_file(fname, slug, numbered, label_kinds)
        outname = os.path.splitext(fname)[0] + ".tex"
        with open(os.path.join(OUT, outname), "w", encoding="utf-8") as fh:
            fh.write(tex)
        all_refs.update(ctx.refs)
        report.append((fname, ctx))
        print(f"wrote chapters/{outname}")
    dangling = sorted(r for r in all_refs if r not in label_kinds)
    print("\nDangling references (left as-is):", ", ".join(dangling) or "none")
    for fname, ctx in report:
        if ctx.missing:
            print(f"Missing figures in {fname}: " + ", ".join(sorted(set(ctx.missing))))
        for note in ctx.notes:
            print(f"Note [{fname}]: {note}")


if __name__ == "__main__":
    main()
