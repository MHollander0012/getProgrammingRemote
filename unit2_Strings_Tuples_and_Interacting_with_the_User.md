---
header-includes:
  - \definecolor{mSoftHeaderOne}{RGB}{22,87,136}
  - \usepackage{sectsty}
  - \sectionfont{\centering}
  - \subsectionfont{\centering\color{mSoftHeaderOne}}
  - \subsubsectionfont{\color{mSoftHeaderOne}}
  - \paragraphfont{\color{mSoftHeaderOne}}
  - \subparagraphfont{\color{mSoftHeaderOne}}
title: Strings, Tuples, and Interacting with the User
#author: Document Author
geometry:
- top=15mm
- left=20mm
- right=20mm
- bottom=20mm
mainfont: Source Sans Pro
fontsize: 12pt
#output: word_document
output: 
  pdf_document:
    latex_engine: xelatex
toc: true
# When running from vscodes 'makrdown enhanced', simply right click and click on pandoc.
# When running from cmd, use pandoc -f markdown input.md -o output.pdf --pdf-engine xelatex
---
\clearpage

# Lesson 7 - Introducing String Objects: Sequences of Characters

## 7.1 Strings as Sequences of Characters

Remember, a string is a sequence of characters. They are denoted within quotes. The sequence of characters can contain numbers, uppercase and lowercase letters, spaces, special characters representing a new line, and symbols in any order.