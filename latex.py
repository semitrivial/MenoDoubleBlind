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

latex += "(Excerpt goes here)"

outrofp = open("outro.txt", "r")
outro = outrofp.read()
outro = outro.replace("|","$|$")
outrofp.close()

latex += outro

latex += r"""\end{document}
"""

latex = latex.replace('"', r'{\textquotedbl}')
latex = latex.replace("'", r'{\textquotesingle}')

outfp=open("meno2.tex", "w")
outfp.write(latex)
outfp.close()