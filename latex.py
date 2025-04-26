latex = r"""\documentclass{article}
\usepackage[T1]{fontenc}

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
"""

introfp = open("intro.txt", "r")
intro = introfp.read()
introfp.close()
latex += intro

dialogfp = open("excerpts.txt", "r")
dialog = dialogfp.read()
dialog = dialog.replace("\\", "$\\backslash$")
dialogfp.close()
lines = dialog.splitlines()


nested_lines = []
for line in lines:
  if line=='':
    continue

  if not(line.startswith(" ")):
    if nested_lines:
      latex += r"\begin{quote}"
      for nested in nested_lines:
        latex += f"{nested}\\\\\n"
      nested_lines = []
      latex += r"\end{quote}"

    latex += "\n\\noindent " + line + "\n"
  else:
    nested_lines.append(line)


outrofp = open("outro.txt", "r")
outro = outrofp.read()
outro = outro.replace("|","$|$")
outrofp.close()

latex += outro

latex += r"""\end{document}
"""

latex = latex.replace('"', r'{\textquotedbl}')
latex = latex.replace("'", r'{\textquotesingle}')
latex = latex.replace("_", r"\_")
latex = latex.replace('#', r"\#")

outfp=open("meno2.tex", "w")
outfp.write(latex)
outfp.close()