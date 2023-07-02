# Alias

If you are using command line, there must be commands you use frequently.
Some commands are long and you might think that copying them every time is a waste of time. In such case, you can use `alias` for a command. If you want to use `h` as an alias for `cd ~`, you define `alias h='cd ~'` in `~/.zshrc` (or `~/.bashrc`). If you can't find such files in your home directory, you need to make it with `touch ~/.zshrc`.

If you find some useful aliases below, write them in `~/.zshrc`.

## Basic

### Customize and colorize PROMPT
```bash
PS1="%F{082}%n%f %F{051}%~%f %# "
RPROMPT='%T'
```
`%n` means username, `%~` means current directory, `%#` shows `#` if you are root, `%` if not. `RPROMPT` is the right prompt. `%T` shows the current time in 24-hour format (`%t` for 12-hour format). Read more about Prompt Expansion in this [link](https://zsh.sourceforge.io/Doc/Release/Prompt-Expansion.html).

By using `%F{color number}` and `%f`, you can colorize the prompt. You can find color numbers [here](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit).


### Put a blank line before every prompt except the first one.
```bash
precmd() { precmd() { echo } }
```

### change directory

```bash
cs() { cd $@ && la }
alias cd='cs'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias cb='cd -'
alias d='cd ~/Desktop'
alias dl="cd ~/Downloads"
alias h='cd ~'
alias /='cd /'

# Change working directory to the top-most Finder window location.
cdf() { cd "$(osascript -e 'tell app "Finder" to POSIX path of (insertion location as alias)')" }
```

### show files
```bash
#alias ls='ls -F'
alias ls='gls --color --group-directories-first -F'
alias l='ls'
alias la='ls -A'
alias ll='ls -AhlS'
alias ds='du -d 1 -h 2>/dev/null | sort -h'
alias pwd='sed "s/ /\\\ /g" <<< ${PWD/#$HOME/"~"}'
alias p='pwd'
alias path='echo -e ${PATH//:/\\n}'
```
- `ls`: To use `gls`, you need to install `coreutils` with `brew install coreutils`. You can use the same colorization as `tree` command.
	- `--color` option colorize the output of `gls` command.
	- `--group-directories-first` option puts directories first.
	- `-F` option adds a trailing `/` to directory names, `@` to symbolic links, and so on. 

- `la`, `ll`: `ls` is defined as `gls --color --group-directories-first -F` before `la='ls -A'`. This means `la='gls --color --group-directories-first -F -A'` and the same for `ll`.
	- `-A` option shows all files and directories except `.` and `..`.
	- `-h` option shows the size in human readable format.
	- `-l` option shows the file size, owner, group, and permissions.
	- `-S` option sorts by file size.

- `ds`: `du -d 1` shows the size of files and directories in the current directory.
	- `-h` option shows the size in human readable format.
	- `2>/dev/null` hides error messages.
	- `sort -h` sorts by file size using [pipe](./linux.md#pipeline-and-redirect).

- `pwd` :`sed "s/ /\\\ /g"` puts `\` before every space. `<<<` is a "here string". `${PWD/#$HOME/"~"}` replaces `$HOME` with `~` in the current directory path.

```{hint}
When you specify options, you can use `ls -AhlS` instead of `ls -A -h -l -S`.
```


### edit files
```bash
alias v='vi'
alias cp='cp -iv'
alias mv='mv -iv'
alias rm='rm -iv'
alias rf='rm -rf'
```
- `-i` option asks you before overwriting a file.
- `-v` option shows the name of the file being copied, moved, or removed.


### search
```bash
fb() { find . -size +$2M -type f -name $1 -exec ls -lhS "{}" \; | awk '{print $5,$9}' }
fd() { find . -name "*.$1" -type f -delete }
rn() { for filename in *.$1; do mv -f "$filename" $(echo "$filename" | sed -e "s/$2//g"); done }
dif(){ diff --color -u $1 $2 }
alias imgopt='open -a ImageOptim .'
alias grep='grep --color'
```
```{note}
You can make an alias with arguments, which is called a function. Functions are defined as `function_name() { commands }`. For example, `fb` takes two arguments, `$1` and `$2`. `$1` is the first argument and `$2` is the second argument. Use like `fb pdf 10` to find files with the name `pdf` larger than 10 MB.

In addition to `$1` and `$2`, there are other special variables: `$0` is the function name. `$@` is all arguments. `$#` is the number of arguments. `$?` is the exit status of the last command. `$$` is the process ID of the current shell. `$!` is the process ID of the last command run in the background.
```

- `fb` finds files larger than `$2` MB with the name `$1` in the current directory.
	- `-size +$2M` option finds files larger than `$2` MB.
	- `-type f` option finds only files (`-type d` finds only directories).
	- `-name $1` option finds files with the name `$1`.
	- `-exec ls -lhS "{}" \;` option executes `ls -lhS` command for each file found.
	- `awk '{print $5,$9}'` option prints the size and name of the file. `$5` means the 5th column and `$9` means the 9th column of the output of `ls -lhS` command.
- `find . -name "*.$1" -type f -delete` finds files with the extension `$1` and deletes them.
- `rn` renames files with the extension `$1` by removing `$2` from the file name. For example, `rn txt asdf` renames `aaasdfff.txt` to `aaff.txt`.

```{note}
`-exec <command> {} \;` is a common syntax. `{}` is replaced by the file name found. `\;` means the end of the command.
```

### open apps
```bash
alias hr='open .'
alias c='open /Applications/CotEditor.app'
alias vs='code'
alias firefox='open /Applications/Firefox.app'
alias chrome='open /Applications/Google\ Chrome.app'
alias safari='open /Applications/Safari.app'
```

### others
```bash
alias his='history'
alias rl='exec ${SHELL} -l' #reload
alias ne='2>|/dev/null'
alias no='&>|/dev/null'
alias eo='>|/dev/null'
```


### zip encryption
```
zipen(){
	zip -er enc.zip "$@"
}
```

## Mac OS settings
### Show/hide hidden files in Finder
```bash
alias show="defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder"
alias hide="defaults write com.apple.finder AppleShowAllFiles -bool false && killall Finder"
```
```{note}
You can use `Command + Shift + .` to show/hide hidden files in Finder.
```

### Hide/show all desktop icons
```bash
alias dhide="defaults write com.apple.finder CreateDesktop -bool false && killall Finder"
alias dshow="defaults write com.apple.finder CreateDesktop -bool true && killall Finder"
```

### Screenshot settings
```bash
alias dwl='defaults write com.apple.screencapture location'
alias ddl='defaults delete com.apple.screencapture location'
alias drl='defaults read com.apple.screencapture location'
```
You can change the location of screenshots by `dwl ~/path/to/dir`.


### sleep setting
```bash
alias sleepon='sudo pmset -a disablesleep 0'
alias sleepoff='sudo pmset -a disablesleep 1'
```


## GitHub
```bash
alias g='git'
alias ga='git add'
alias gb='git branch'
alias gc='git commit'
alias gch='git checkout'
alias gcl='git clone'
alias gd='git diff'
alias gf='git fetch'
alias gi='git init'
alias gm='git merge'
alias gps='git push'
alias gpl='git pull'
alias gpom='git push origin main'
alias gs='git status'
```

### Define an alias of several commands with arguments (function)
```bash
gacpm() { git add -A && git commit -m "$1" && git push origin main }
```

For example, you can define an alias to make a new repository with just one command.
```bash
# $1 = private or public
ginit() {
	git init
	git add .
	git commit -m "🎉  Initial commit"
	gh repo create --"$1" --source=. --push
}
```
You need to install [GitHub CLI](https://cli.github.com/) to use `gh` command.


### gitignore.io
gitignore.io enable us to make .gitignore file easily
```bash
function gi() { curl -sLw n https://www.toptal.com/developers/gitignore/api/$@ ;}
```

## Python
```bash
alias python='python3'
alias wpy='which python'

alias pip='pip3'
alias pin='pip install'
alias puin='pip uninstall'
alias pup='pip install --upgrade pip'
alias pinreq='pip install -r requirements.txt'
alias pf='pip list --format=freeze'
alias pfr='pip list --format=freeze > requirements.txt'
```

### Make, activate, deactivate venv
```bash
alias mkv='python3 -m venv venv; acv; pip install --upgrade pip'
alias acv='source venv/bin/activate'
alias deac='deactivate'
```

## Latex
### Copy latex-template directory to somewhere;
If you write a lot of latex documents, you should make a template directory. You can copy the template directory to somewhere with this function.
```bash
mklt(){
	cp -r ~/latex-template ./"$1"
}

mkbt(){
	cp -r ~/beamer-template ./"$1"
}
```