# Zsh

```{admonition} Zsh
Z shell (Zsh) is one of the Unix command shells. It can be used as an interactive login command shell and as a powerful shell script command interpreter. Zsh can also be viewed as an extended version of Bourne Shell with many improvements. Not only that, but some useful features of bash, ksh, and tcsh are also incorporated. [- wikipedia](https://en.wikipedia.org/wiki/Z_Shell)
```

## Manage `.zsh*` files in `zsh/` directory
```{image} img/zsh.png
:width: 600px
:align: center
```

`.zsh*` files are easy to get messy in the home directory. By setting `$ZDOTDIR`, most files can be moved from the home directory. In the following, `.zsh*` is managed in a directory named `zsh/`.

```bash
- zsh/
  |-- aliases/
	|-- git.sh
	|-- ...
	|-- python.sh
  |-- settings/
	|-- prompt.sh
	|-- zsh-extensions.sh
  |-- .zprofile
  |-- .zshrc
  |-- .zshenv
  |-- ...
  |-- .git
  |-- .gitignore
```

Set `zsh/` as `ZDOTDIR` so that `.zsh*` in it is read.

```bash
# In .zshenv
# Set zsh/ to ZDOTDIR
export ...
export ZDOTDIR="$HOME/path/to/zsh"
```

```bash
# Put the alias of .zshenv in the home directory
.zshenv -> '/Users/$HOME/path/to/zsh/.zshenv'
```

## `.zshrc`

Contents in`.zshrc` are also easy to get messy, so divide them into files and import them in `.zshrc`. Here, we have prepared directories called `aliases` and `settings` in the same hierarchy as `.zshrc`, and put the files to be read in them.

```bash
[[ -f $ZDOTDIR/settings/prompt.sh ]]  && . $ZDOTDIR/settings/prompt.sh
...
[[ -f $ZDOTDIR/aliases/git.sh ]]      && . $ZDOTDIR/aliases/git.sh
[[ -f $ZDOTDIR/aliases/python.sh ]]   && . $ZDOTDIR/aliases/python.sh
...
```

```{hint}
👉 Other dotfiles in the home directory can also be managed in the same way.
```

[zsh/](https://github.com/kkensuke/setting/tree/main/zsh)