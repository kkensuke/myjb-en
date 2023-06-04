# Commit Masssages with emoji

When you commit files in github, you add some commit-messages. In the code of comduct of some project, it is recommended to use `emoji` to easily represent what the commit is all about. Here, we introduce a setting for that with aliases.


Put code below in `.zshrc`.
```zsh
## Using EMOJI-LOG (https://github.com/ahmadawais/Emoji-Log) ##
# Git Commit, Add all and Push — in one step.
gacp() { git add . && git commit -m "$*" && git push origin main }

gini() { gacp "🎉 Initial commit"}
gnew() { gacp "✨ NEW: $@" }
gimp() { gacp "👌 IMPROVE: $@" }
gprg() { gacp "🚧 PROGRESS: $@" }

gmtn() { gacp "🔧 MAINTAIN: $@" }
gfix() { gacp "🐛 FIX: $@" }
ghot() { gacp "🚑 HOTFIX: $@" }
gbrk() { gacp "‼️ BREAKING: $@" }
grem() { gacp "🗑️ REMOVE: $@" }

gmrg() { gacp "🔀 MERGE: $@" }
gref() { gacp "♻️ REFACTOR: $@" }
gtst() { gacp "🧪 TEST: $@" }
gdoc() { gacp "📚 DOC: $@" }
grls() { gacp "🚀 RELEASE: $@" }
gsec() { gacp "👮 SECURITY: $@" }

# See more in .gitmessage

# Show commit type
gtyp() {
NORMAL='\033[0;39m'
GREEN='\033[0;32m'
echo "$GREEN gini$NORMAL — 🎉 Initial commit
$GREEN gnew$NORMAL — ✨ NEW
$GREEN gimp$NORMAL — 👌 IMPROVE
$GREEN gprg$NORMAL — 🚧 PROGRESS
$GREEN gmtn$NORMAL — 🔧 MAINTAIN
$GREEN gfix$NORMAL — 🐛 FIX
$GREEN ghot$NORMAL — 🚑 HOTFIX
$GREEN gbrk$NORMAL — ‼️  BREAKING
$GREEN grem$NORMAL — 🗑️  REMOVE
$GREEN gmrg$NORMAL — 🔀 MERGE
$GREEN gref$NORMAL — ♻️  REFACTOR
$GREEN gtst$NORMAL — 🧪 TEST
$GREEN gdoc$NORMAL — 📚 DOC
$GREEN grls$NORMAL — 🚀 RELEASE
$GREEN gsec$NORMAL — 👮 SECURITY"
}

```


## Reference

- [jupyterbook Development Conventions](https://github.com/executablebooks/.github/blob/master/CONTRIBUTING.md#commit-messages)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [Emoji-Log](https://github.com/ahmadawais/Emoji-Log)
- [gitmoji-cli](https://github.com/carloscuesta/gitmoji-cli)
- [emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)
- [Complete list of github markdown emoji markup ](https://gist.github.com/rxaviers/7360908)
- [Commit message examples](https://gist.github.com/mono0926/e6ffd032c384ee4c1cef5a2aa4f778d7)
