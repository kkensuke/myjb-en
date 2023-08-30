# $\LaTeX$
> last modified: {sub-ref}`today`

:::{admonition} $\LaTeX$
:class: important

$\LaTeX$ is a typesetting system that is widely used in academia. It is especially useful for writing mathematical equations.
:::

We are going to see some basic settings and usage for LaTeX in VS Code.

- [$\LaTeX$ settings in VS Code](./settings.md)
- [LaTeX Basics](./basics.md)

---
:::{admonition} Preamble
:class: note

Preamble is the part in which you can set the document class, load packages, define commands, and set some options for the document. It is placed between `\documentclass` and `\begin{document}`. You can also put it in a separate file and load it with `\input{preamble.tex}`.
:::

Sometimes, you can't use some packages due to the conflicts between packages and document classes. So, you need to change the settings in the preamble according to the document class.

You also have to care about the conflicts between packages themselves because you can't use some packages together, or you need to load them in a specific order.

We are going to see some examples of the preamble for some document classes.

- [article](./article.md)
- [revtex4-2](./revtex4-2.md)
- [beamer](./beamer.md)
- [\newcommands](./newcommands.md)

You can download all the files related to these sections [here](https://github.com/kkensuke/latex-template/tree/main).