# Preamble

In $\Latex$ preamble, we can load packages, define commands, and set some options for the document.

Sometimes, you can't use some packages due to the conflict between packages and document class. Thus you need change settings in the preamble according to the document class.

You also have to care about the conflict between packages because you can't use some packages together, or you need to load them in a specific order.

We are going to see some examples of the preamble for some document classes.


## article
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

The contents of `main.tex` is as follows:
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



## revtex4-2
```latex
\usepackage[top=15truemm,bottom=15truemm,left=15truemm,right=15truemm]{geometry}
\usepackage[dvipdfmx]{graphicx,hyperref,xcolor}
\usepackage{amsmath,amsthm,amssymb,bm,mathtools,amsfonts,mathrsfs}
\usepackage{ascmac}% to use itembox
\usepackage{algorithm,algorithmic}
\usepackage{physics}
\usepackage{tikz}
\usepackage{quantikz}
\usepackage{comment}
\usepackage{here}
\usepackage{dcolumn}% Align table columns on decimal point


% style setting
% ---------------------------------------------------------------------------- %
\allowdisplaybreaks[1]
\renewcommand{\baselinestretch}{1}
\renewcommand{\abstractname}{\vspace{-\baselineskip}}
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



The contents of `main.tex` is as follows:
```latex
\documentclass[dvipdfmx,twocolumn,preprintnumbers,superscriptaddress,nofootinbib]{revtex4-2}
% landscape
% footinbib for PRL

\input{preamble}
\allowdisplaybreaks[1]

\begin{document}


\title{Asdf of asdf for asdf}

\author{Qwerty Qwerty}
    \email[]{qwerty(at)asdf.asdf.ac.jp}
    \affiliation{
    Dept.\ of Physics, The University of Qwerty, address
    }

    \author{Asdf Asdf}
    \email[]{asdf(at)asdf.asdf.ac.jp}
    \affiliation{
    Dept.\ of Physics, The University of Asdf, address
    }

\date{\today}

\begin{abstract}
    abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract abstract.
\end{abstract}

\maketitle


\section{Introduction}
asdf asdf asdf asdf asdf asdf

\end{document}
```



## Beamer
```latex
\usepackage{bm,mathtools,mathrsfs}
\usepackage{algorithm,algorithmic}
\usepackage{physics}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage{comment}
\usepackage{here}
\usepackage{caption}
\captionsetup[figure]{labelformat=empty}

% font family
\usepackage{helvet}
\renewcommand{\kanjifamilydefault}{\gtdefault} % for japanese

% define colors
% ---------------------------------------------------------------------------- %
\definecolor{red}{rgb}{0.9,0.30,0.30}
\definecolor{blue}{rgb}{0.32,0.66,0.82}
\definecolor{darkblue}{rgb}{0.2,0.4,0.6}
\definecolor{green}{rgb}{0.47,0.72,0.29}
\definecolor{darkgreen}{rgb}{0.25,0.42,0.21}
\definecolor{yellow}{rgb}{0.95,0.85,0.25}
\definecolor{darkyellow}{rgb}{0.75,0.65,0.05}
\definecolor{orange}{rgb}{0.95,0.55,0.25}
\definecolor{darkorange}{rgb}{0.75,0.35,0.05}
\definecolor{purple}{rgb}{0.75,0.55,0.85}
\definecolor{darkpurple}{rgb}{0.55,0.35,0.65}
\definecolor{brown}{rgb}{0.75,0.55,0.25}
\definecolor{darkbrown}{rgb}{0.55,0.35,0.05}
\definecolor{pink}{rgb}{0.95,0.55,0.75}
\definecolor{darkpink}{rgb}{0.75,0.35,0.55}
\definecolor{grey}{rgb}{0.55,0.55,0.55}
\definecolor{darkgrey}{rgb}{0.35,0.35,0.35}
% ---------------------------------------------------------------------------- %

% set colors
% ---------------------------------------------------------------------------- %
\setbeamercolor{structure}{fg=blue}
\setbeamertemplate{blocks}[rounded][shadow=false]
\setbeamercolor{block title alerted}{bg=red, fg=white}
\setbeamercolor{block title example}{bg=green, fg=white}


% define blocks
% ---------------------------------------------------------------------------- %
\addtobeamertemplate{theorem begin}{
    \setbeamercolor{block title}{bg=darkblue, fg=white}
}{}
\addtobeamertemplate{proof begin}{
    \setbeamercolor{block title}{bg=grey, fg=white}
}{}

\newenvironment<>{note}[1]{
    \setbeamercolor{block title}{bg=blue, fg=white}
    \begin{block}{Note}#1}{\end{block}}
\newenvironment<>{warning}[1]{
    \setbeamercolor{block title}{bg=red}
    \begin{block}{Warning}#1}{\end{block}}
\newenvironment<>{important}[1]{
    \setbeamercolor{block title}{bg=orange}
    \begin{block}{Important}#1}{\end{block}}

\newenvironment<>{definition}[1]{
    \setbeamercolor{block title}{bg=grey}
    \begin{block}{Definition}#1}{\end{block}}
\newenvironment<>{proposition}[1]{
    \setbeamercolor{block title}{bg=darkblue}
    \begin{block}{Proposition}#1}{\end{block}}
\newenvironment<>{lemma}[1]{
    \setbeamercolor{block title}{bg=darkblue}
    \begin{block}{Lemma}#1}{\end{block}}
\newenvironment<>{corollary}[1]{
    \setbeamercolor{block title}{bg=darkblue}
    \begin{block}{Corollary}#1}{\end{block}}
\newenvironment<>{remark}[1]{
    \setbeamercolor{block title}{bg=blue}
    \begin{block}{Remark}#1}{\end{block}}
% ---------------------------------------------------------------------------- %
```




The contents of `main.tex` is as follows:
```latex
\documentclass[10pt,aspectratio=169]{beamer}

\input{beamer-preamble.tex}
\input{preamble.tex}


\title{Title}
%\subtitle{Subtitle}

\author{Qwerty Qwerty\inst{1} \and Asdf Asdf\inst{2}}
\institute{\inst{1} Dept.\ of Physics, The University of Qwerty \quad \inst{2} Dept.\ of Physics, The University of Asdf}

\date{\today}
%\logo{\includegraphics[width=2cm]{logo.png}}

\begin{document}

\frame{\titlepage}


\begin{frame}{Table of Contents}
    \tableofcontents
\end{frame}




\section{abcd}

\begin{frame}{Motivation}
    \begin{itemize}
        \item a
        \item b
    \end{itemize}
\end{frame}




\begin{frame}
    \begin{columns}
        \column{0.5\textwidth}
            This is a first column. This is a first column. This is a first column. This is a first column. This is a first column. This is a first column. This is a first column.
        \column{0.5\textwidth}
            This is a second column. This is a second column. This is a second column. This is a second column. This is a second column. This is a second column.
    \end{columns}
\end{frame}





\section{efgh}

\begin{frame}
    \begin{theorem}
        $$ a^2 + b^2 = c^2 $$
    \end{theorem}

    \begin{proof}<2>
        asdf asdf asdf.
    \end{proof}

\end{frame}





\begin{frame}
    \begin{warning}
        asdf asdf asdf.
    \end{warning}

    \begin{example}
        asdf asdf asdf.
    \end{example}

    \begin{important}
        asdf asdf asdf.
    \end{important}

    \begin{remark}
        asdf asdf asdf.
    \end{remark}
\end{frame}





\section{ijkl}

\begin{frame}{Table}
    \begin{table}[]
        \begin{tabular}{|l|c|c|}
        \hline
        a & b & c \\ \hline
        d & e & f \\ \hline
        \end{tabular}
    \end{table}
\end{frame}




\begin{frame}{Reference}
    \scriptsize
    \beamertemplatetextbibitems
    \bibliographystyle{abbrv}
    \bibliography{ref}
\end{frame}

\end{document}
```



## newcommands regardless of document class
```latex
%% Latin abbreviations
% ---------------------------------------------------------------------------- %
\newcommand{\etal}{\textit{et al. }}
\newcommand{\eg}{\textit{e.g. }}
\newcommand{\cf}{\textit{c.f. }}
\newcommand{\ie}{\textit{i.e. }}
\newcommand{\etc}{\textit{etc. }}
% ---------------------------------------------------------------------------- %

%% math
% ---------------------------------------------------------------------------- %
% mathbb
\newcommand{\bbA}{\mathbb{A}}
\newcommand{\bbB}{\mathbb{B}}
\newcommand{\bbC}{\mathbb{C}}
\newcommand{\bbD}{\mathbb{D}}
\newcommand{\bbE}{\mathbb{E}}
\newcommand{\bbF}{\mathbb{F}}
\newcommand{\bbG}{\mathbb{G}}
\newcommand{\bbH}{\mathbb{H}}
\newcommand{\bbI}{\mathbb{I}}
\newcommand{\bbJ}{\mathbb{J}}
\newcommand{\bbK}{\mathbb{K}}
\newcommand{\bbL}{\mathbb{L}}
\newcommand{\bbM}{\mathbb{M}}
\newcommand{\bbN}{\mathbb{N}}
\newcommand{\bbO}{\mathbb{O}}
\newcommand{\bbP}{\mathbb{P}}
\newcommand{\bbQ}{\mathbb{Q}}
\newcommand{\bbR}{\mathbb{R}}
\newcommand{\bbS}{\mathbb{S}}
\newcommand{\bbT}{\mathbb{T}}
\newcommand{\bbU}{\mathbb{U}}
\newcommand{\bbV}{\mathbb{V}}
\newcommand{\bbW}{\mathbb{W}}
\newcommand{\bbX}{\mathbb{X}}
\newcommand{\bbY}{\mathbb{Y}}
\newcommand{\bbZ}{\mathbb{Z}}

% \mathcal
\newcommand{\calA}{\mathcal{A}}
\newcommand{\calB}{\mathcal{B}}
\newcommand{\calC}{\mathcal{C}}
\newcommand{\calD}{\mathcal{D}}
\newcommand{\calE}{\mathcal{E}}
\newcommand{\calF}{\mathcal{F}}
\newcommand{\calG}{\mathcal{G}}
\newcommand{\calH}{\mathcal{H}}
\newcommand{\calI}{\mathcal{I}}
\newcommand{\calJ}{\mathcal{J}}
\newcommand{\calK}{\mathcal{K}}
\newcommand{\calL}{\mathcal{L}}
\newcommand{\calM}{\mathcal{M}}
\newcommand{\calN}{\mathcal{N}}
\newcommand{\calO}{\mathcal{O}}
\newcommand{\calP}{\mathcal{P}}
\newcommand{\calQ}{\mathcal{Q}}
\newcommand{\calR}{\mathcal{R}}
\newcommand{\calS}{\mathcal{S}}
\newcommand{\calT}{\mathcal{T}}
\newcommand{\calU}{\mathcal{U}}
\newcommand{\calV}{\mathcal{V}}
\newcommand{\calW}{\mathcal{W}}
\newcommand{\calX}{\mathcal{X}}
\newcommand{\calY}{\mathcal{Y}}
\newcommand{\calZ}{\mathcal{Z}}

% multiplicative group
\newcommand{\Zx}{\Z^\times}
\newcommand{\Qx}{\Q^\times}
\newcommand{\Rx}{\R^\times}
\newcommand{\Cx}{\C^\times}

% non-negative
\newcommand{\Znn}{\Z_{\ge0}}
\newcommand{\Qnn}{\Q_{\ge0}}
\newcommand{\Rnn}{\R_{\ge0}}

% positive
\newcommand{\Zpo}{\Z_{>0}}
\newcommand{\Qpo}{\Q_{>0}}
\newcommand{\Rpo}{\R_{>0}}

% MathOperator
\DeclareMathOperator{\sgn}{sgn}
\DeclareMathOperator{\sign}{sign}
\DeclareMathOperator{\Supp}{Supp}
\DeclareMathOperator{\diag}{diag}
\DeclareMathOperator{\E}{E}
\DeclareMathOperator{\Var}{Var}
\DeclareMathOperator{\Cov}{Cov}
\DeclareMathOperator{\poly}{poly}
\DeclareMathOperator{\SWAP}{SWAP}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Aut}{Aut}
\DeclareMathOperator{\End}{End}
% limit type
\DeclareMathOperator*{\argmin}{arg~min}
\DeclareMathOperator*{\argmax}{arg~max}

% others
\renewcommand{\bar}[1]{\overline{#1}}
\newcommand{\combi}[2]{{}_{#1}\text{C}_{#2}}
\newcommand{\dg}{^\dagger}
\newcommand{\fa}{{}^\forall}
\newcommand{\ex}{{}^\exists}
\newcommand{\pd}{\partial}
\newcommand{\then}{\;\Longrightarrow\;}
% ---------------------------------------------------------------------------- %
```