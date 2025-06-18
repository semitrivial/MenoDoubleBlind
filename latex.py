# File for creating latex for "Meno II".
# Change the line "full = False" to "full = True" for generating
# a version with the full dialogue, not just excerpts.

full = True

latex = r"""\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage{hyperref}

\title{Meno II: A self-referential Socratic dialogue about memory and computer programming}
\author{Anonymous}
\date{March 2025}

\begin{document}

\maketitle

\begin{abstract}"""

absfp = open("abstract.txt", "r")
abst = absfp.read()
absfp.close()
latex += abst

latex += r"""
\end{abstract}

\section{Introduction}
"""

introfp = open("intro.txt", "r")
intro = introfp.read()
introfp.close()

if full:
  indx = intro.index("Because of the venue")
  intro = intro[:indx]

latex += intro

if full:
  latex += "\n\\section{Dialogue}\n"
else:
  latex += "\n\\section{Excerpts of the Dialogue}\n"

if full:
  dialogfp = open("dialogue.txt", "r")
else:
  dialogfp = open("excerpts.txt", "r")

dialog = dialogfp.read()
dialog = dialog.replace("\\", "$\\backslash$")
dialogfp.close()

dialog = dialog.replace('"Meno:Goodmorning,Socrates."', '\\[\\mbox{"Meno:Goodmorning,Socrates."}\\]')
dialog = dialog.replace('"Nfop:Hppenpsojoh,Tpdsbufs."', '\\[\\mbox{"Nfop:Hppenpsojoh,Tpdsbufs."}\\]')

lines = dialog.splitlines()

nested_lines = []
for line in lines:
  if line=='':
    continue

  line = line.replace('"', r'{\textquotedbl}')
  line = line.replace("'", r'{\textquotesingle}')

  if not(line.startswith(" ")) or line.startswith("("):
    if nested_lines:
      latex += r"\begin{quote}\texttt{"
      for nested in nested_lines:
        if 'print("I think' in nested:
          latex += "\\noindent \\hphantom{1cm}" + f"{nested}\\\\\n"
        else:
          latex += "\\noindent" + f"{nested}\\\\\n"
      nested_lines = []
      latex += r"}\end{quote}"

    if line.startswith("Socrates:"):
      line = "\\textbf{Socrates:} " + line[len("Socrates: "):]
    elif line.startswith("Meno:"):
      line = "\\textbf{Meno:} " + line[len("Meno: "):]
    elif line.startswith("("):
      line = "\\emph{" + line + "}"

    latex += "\n\\noindent " + line + "\n"
  else:
    nested_lines.append(line)

latex += r"""
\section{Conclusion}
"""


outrofp = open("outro.txt", "r")
outro = outrofp.read()
outro = outro.replace("|","$|$")
outrofp.close()

latex += outro

latex += r"""\end{document}
"""

latex = latex.replace('"""n  r', '"""n {} r')
latex = latex.replace("%", "\\%")
latex = latex.replace('"', r'{\textquotedbl}')
latex = latex.replace("'", r'{\textquotesingle}')
latex = latex.replace("_", r"\_")
latex = latex.replace('#', r"\#")

outfp=open("meno2.tex", "w")
outfp.write(latex)
outfp.close()