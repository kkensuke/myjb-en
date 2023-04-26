# Alias

If you are using command line, there must be commands you repeatedly use.
Some commands are long and you would think that copying them every time is a waste of time. In such case, you can use `alias` for a command. If you want to use `h` as an alias for `cd ~`, you define `alias h='cd ~'` in `~/.zshrc` (or `~/.bashrc`). If you can't find such files in your home directory, you need to make it with `touch ~/.zshrc`.

If you find some useful aliases below, write them in `~/.zshrc`.

## Basic

### Customize and colorize PROMPT
```
PS1="%F{082}%n%f %F{051}%~%f %# "
RPROMPT='%t'
```

### Put a blank line before every prompt except the first one.
```
precmd() { precmd() { echo } }
```

### Frequently used commands

```
# change directory
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


# show files
#alias ls='ls -F'
alias ls='gls --color -F'
alias l='ls'
alias la='ls -A'
alias ll='ls -AhlS'
alias pwd='sed "s/ /\\\ /g" <<< ${PWD/#$HOME/"~"}'
alias p='pwd'
alias path='echo -e ${PATH//:/\\n}'


# edit files
alias v='vi'
alias cp='cp -iv'
alias mv='mv -iv'
alias rm='rm -iv'
alias rf='rm -rf'


# others
alias his='history'
alias grep='grep --color'
alias lns='ln -s'
alias rl='exec ${SHELL} -l' #reload


# open apps
alias here='open .'
alias c='open /Applications/CotEditor.app'
alias vs='code'
alias firefox='open /Applications/Firefox.app'
alias chrome='open /Applications/Google\ Chrome.app'
alias safari='open /Applications/Safari.app'


# zip encrypttion
zipen(){
	zip -er enc.zip "$@"
}
```

## Mac OS settings
### Show/hide hidden files in Finder
```
alias show="defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder"
alias hide="defaults write com.apple.finder AppleShowAllFiles -bool false && killall Finder"
```

### Hide/show all desktop icons
```
alias dhide="defaults write com.apple.finder CreateDesktop -bool false && killall Finder"
alias dshow="defaults write com.apple.finder CreateDesktop -bool true && killall Finder"
```

### Screenshot settings
```
alias dwl='defaults write com.apple.screencapture location'
alias ddl='defaults delete com.apple.screencapture location'
alias drl='defaults read com.apple.screencapture location'
```

### sleep setting
```
alias sleepon='sudo pmset -a disablesleep 0'
alias sleepoff='sudo pmset -a disablesleep 1'
```


## GitHub
```
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
alias gst='git status'
```

### Define an alias of several commands
```
gacpm() { git add -A && git commit -m "$1" && git push origin main }
```

For example, you can define an alias to make a new repository with just one command.
```
ginit() {
	git init
	git add .
	git commit -m "Initial commit"
	gh repo create --private --source=. --push'
}
```
You need to install [GitHub CLI](https://cli.github.com/) to use `gh` command.


### gitignore.io
gitignore.io enable us to make .gitignore file easily
```
function gi() { curl -sLw n https://www.toptal.com/developers/gitignore/api/$@ ;}
```

## Python
```
alias python='python3'
alias wpy='which python'

alias pip='pip3'
alias pin='pip install'
alias pup='pip install --upgrade pip'
alias pinreq='pip install -r requirements.txt'
alias pf='pip list --format=freeze'
alias pfr='pip list --format=freeze > requirements.txt'
```

### Make, activate, deactivate venv
```
alias mkv='python3 -m venv venv; acv; pip install --upgrade pip'
alias acv='source venv/bin/activate'
alias deac='deactivate'
```

## Latex
### Copy latex-template directory to somewhere;
```
mklt(){
	cp -r ~/.latex-template ./"$1"
}

mkbt(){
	cp -r ~/.beamer-template ./"$1"
}
```