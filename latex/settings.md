# How to use latex in VScode

## Install TexLive

Download `install-tl-unx.tar.gz`
```zsh
$ curl -OL http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
```

Open `install-tl-unx.tar.gz`
```zsh
$ tar xvf install-tl-unx.tar.gz
```

Change directory to the installer:
```zsh
$ cd install-tl-2*
```

Install TexLive
```zsh
$ sudo ./install-tl -no-gui -repository http://mirror.ctan.org/systems/texlive/tlnet/
```

To start installation, type `I` and enter.
```zsh
Actions:
 <I> start installation to hard disk
 <H> help
 <Q> quit
Enter command: I
```

Add a symbolic link to `/usr/local/bin`
```zsh
$ sudo /usr/local/texlive/????/bin/*/tlmgr path add
```

## Setting for Japanese in VScode

1. Install [`LaTeX Workshop`](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension.

2. Open `settings.json` in VScode.
```zsh
$ code ~/Library/Application\ Support/Code/User/settings.json
```

Add the following lines to `settings.json`.
You have two recipes, `ptex2pdf*3` and `ptex2pdf -> pbibtex -> ptex2pdf*2`. The former is compile `.tex` files without `.bib`, and the latter is for `.tex` files with `.bib`. (This setting also works for English.)
```json
{
    // latex
    "latex-workshop.latex.tools": [
        {
            "name":"ptex2pdf",
            "command": "ptex2pdf",
            "args": [
                "-l",
                "-ot",
                "-interaction=nonstopmode",
                "-kanji=utf8 -synctex=1",
                "%DOC%"
            ]
        },
        {
            "name": "pbibtex",
            "command": "pbibtex",
            "args": [
                "-kanji=utf8",
                "%DOCFILE%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "ptex2pdf*3",
            "tools":[
                "ptex2pdf",
                "ptex2pdf",
                "ptex2pdf",
            ]
        },
        {
            "name": "ptex2pdf -> pbibtex -> ptex2pdf*3",
            "tools":[
                "ptex2pdf",
                "pbibtex",
                "ptex2pdf",
                "ptex2pdf",
            ]
        },
    ],
    "latex-workshop.latex.clean.fileTypes":
    [
        "*.bbl", "*.blg", "*.idx", "*.ind", "*.lof", "*.lot", "*.out", "*.toc", "*.acn", "*.acr", "*.alg",
        "*.glg", "*.glo", "*.gls", "*.ist", "*.fls", "*.log", "*.fdb_latexmk", "*.synctex.gz",
        "_minted*", "*.nav", "*.snm", "*.vrb",
    ],
    "latex-workshop.latex.autoClean.run": "onBuilt",
    "latex-workshop.latex.autoBuild.run": "onFileChange",
    "latex-workshop.synctex.afterBuild.enabled": true,
    "latex-workshop.view.pdf.viewer": "tab",
}
```

