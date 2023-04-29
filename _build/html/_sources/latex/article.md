# article

## `preamble.tex`
```latex
\usepackage[top=15truemm,bottom=15truemm,left=15truemm,right=15truemm]{geometry}
\usepackage[dvipdfmx]{graphicx,hyperref,xcolor}
\usepackage{amsmath,amsthm,amssymb,bm,mathtools,amsfonts,mathrsfs}
\usepackage{ascmac}% to use itembox
\usepackage{algorithm,algorithmic}
\usepackage{physics}
\usepackage{tikz}
\usepackage{authblk}
\usepackage{comment}
\usepackage{here}


% style setting
% ---------------------------------------------------------------------------- %
\allowdisplaybreaks[1]
\renewcommand\Authfont{\fontsize{14}{14.4}\selectfont}
\renewcommand\Affilfont{\fontsize{10}{10.8}\itshape}
\renewcommand{\baselinestretch}{1.25}
% ---------------------------------------------------------------------------- %


% number figures, tables and equations within the sections
% ---------------------------------------------------------------------------- %
\numberwithin{equation}{section}
\numberwithin{figure}{section}
\numberwithin{table}{section}
% ---------------------------------------------------------------------------- %


% Logic and proofs
% ---------------------------------------------------------------------------- %
\newtheorem{theorem}{Theorem}[section]
\newtheorem{corollary}{Corollary}[theorem]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}

\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{example}{Example}[section]
\newtheorem{exercise}{Exercise}[section]

\theoremstyle{remark}
\newtheorem{remark}{Remark}[section]
% ---------------------------------------------------------------------------- %
```


## `main.tex`
```latex
\documentclass[12pt]{article}
\input{preamble}
\allowdisplaybreaks[1]

\title{Title}
\author{Author}
\affil{Dept.\ of Physics, The University of Asdf, address}
\date{\today}
\begin{document}
\maketitle
\tableofcontents

\section{Introduction}
asdf asdf asdf asdf asdf asdf

\end{document}
```