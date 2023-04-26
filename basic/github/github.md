---
title: GitHub
summary:
description: Usage of GitHub
author: kkensuke
date: 2022-07-06
some_url:
tags:
  -
  -
---
# GitHub

```{image} ./img/GitHub-flow.png
:name: flow
:width: 600px
:align: center
```

## Git (version control system, VSC)
Git is a popular version control system used by developers to manage source code changes and collaborate on software development projects. It allows multiple people to work on the same codebase simultaneously and track changes made over time.

A local repository in Git is a copy of the codebase that is stored on a developer's computer. When changes are made to the codebase, they are tracked locally using Git, and the developer can commit those changes to their local repository. This allows developers to experiment with new code changes and make revisions without affecting the codebase that other developers are working on.

A remote repository, on the other hand, is a copy of the codebase that is stored on a remote server. Developers can push their local changes to the remote repository to share them with others on the team. This allows everyone on the team to see the latest changes made to the codebase and collaborate more effectively.

The key difference between local and remote repositories is that local repositories are stored on a developer's computer, while remote repositories are stored on a server that can be accessed by multiple developers. Both local and remote repositories are essential to a Git workflow, as they allow developers to work on code changes independently while still keeping everyone on the team up to date with the latest changes.

Here are some key terms and concepts related to Git:

- Repository: A repository is a collection of files and folders that are tracked by Git. It is usually located on a server and can be accessed by multiple developers.
- Clone: To clone a repository means to create a local copy of the repository on your own computer.
- Add: When you add a file to a Git repository, you are telling Git to start tracking changes to that file.
- Commit: A commit is a snapshot of the changes you have made to the files in your repository. When you commit changes, you are creating a permanent record of those changes.
- Push: Pushing changes means sending your committed changes to the remote repository (i.e., the server where the repository is stored). This makes your changes visible to other team members who are also working on the same repository.
- Pull: Pulling changes means retrieving changes from the remote repository and updating your local repository with those changes. This is typically done before making changes to ensure that your local repository is up-to-date with the latest changes made by other team members.
- Branch: A branch is a separate line of development that allows you to work on changes independently of the main codebase. This can be useful when you want to experiment with new features without affecting the main codebase.
- Merge: Merging is the process of combining changes from one branch into another. This is typically done when a feature is complete and ready to be integrated into the main codebase.

These are just a few of the most common terms and concepts used in Git. Learning Git can take some time, but it's an important skill for any developer working on a team.


## Basic commands
### Create a new repository
First, make a repository on the [GitHub website](https://github.com/) without initializing.
Second, execute the commands below on the local computer

```
[mkdir project_name]
[cd project_name]
echo "# test" >> README.md

# initialize the repository
git init

# add all files in the current directory to working tree
git add .

# commit the changes to the local repository
git commit -m "first commit"

git branch -M main
git remote add origin https://github.com/<Username>/<repository>.git

# push the changes to the remote repository
git push -u origin main
```

`git init` makes repository, or `.git`, in the current directory.

`git init project_name` makes a directory named project_name and `.git` in it.


### push an existing repository from the command line
If you have already made (or initialized) a local repository, you just need to use the following commands after making a remote repository.
```
git remote add origin https://github.com/<Username>/<repository>.git
git branch -M main
git push -u origin main
```

### Clone
In an arbitrary directory,
```
$ git clone [branch, or you can omit here for main] https://github.com/<Username>/<repository>.git
$ cd <repository>
```

After you add or modify files:
```
$ git add <file>
($ git add .  # add current directory)
($ git status)
$ git commit -m "<comment>"
$ git push origin main
($ git status)
```

<!--
### Defference between fork and clone
#### clone
リモートリポジトリをローカルリポジトリに複製すること
#### fork
他人のリポジトリを自分のアカウントのリモートリポジトリにコピーすること
* オリジナルのリポジトリへの貢献が前提
* forkした場合そのリポジトリを所有する開発者に通知される

1. リポジトリAをfork2. forkしたリポジトリBをローカルにclone3. cloneしたリポジトリCで開発し、リポジトリBに反映4. リポジトリAの管理者にPull Requestを送信
-->

### take new changes of the remote repository into the local repository
```
$ git pull origin main
```

````{tip}
This is equivalent to
```
$ git fetch
$ git merge origin main
```
````

### make a branch and change branches at local

When you make a repository, the only main branch exists at first.
So, you are in the main branch by default.

You can check the current branch by
```
$ git branch
```

You can see all branches including the remote branches by
```
$ git checkout -a
```

1, Making new branch at local (branch not in remote)

Let's make a new branch!
```
# make a branch
$ git branch <branch>
# switch to <branch> from main
$ git checkout <branch>
```

````{tip}
These two lines are equivalent to
```
$ git checkout -b <branch>
```
````

Then reflect the new branch to the remote repository.
```
$ git push origin <branch>
```

2, when remote/branch already exists
```
# create a new local branch pointing to the remote branch
$ git branch <branch> origin/<branch>
# check out that branch
$ git checkout <branch>
```

````{tip}
These two lines are equivalent to
```
$ git checkout -b <branch> origin/<branch>
```
````




### .gitignore

You can configure Git to ignore files you don't want to check in to GitHub.
All you have to do is write down filenames in `.gitignore` in the same directory as `.git`.

However, making `.gitignore` and writing filenames in each directory in the control of Git is troublesome. You can make `.gitignore` easily with [gitignore.io website](https://www.toptal.com/developers/gitignore) or [gitignore.io CLI](https://docs.gitignore.io)

As to some files, you will append their filenames in every `.gitignore`.
To avoid it, making `~/.gitignore_global` is a solution. `~/` represents the home directory.

```{note}
First, make `~/.gitignore_global` if you haven't made it yet
```
install .gitignore.io from https://docs.gitignore.io/install/command-line

for macOS :

- one time
```
$ git config --global core.excludesfile ~/.gitignore_global
$ echo "function gi() { curl -sLw "\n" https://www.toptal.com/developers/gitignore/api/\$@ ;}" >> \
~/.rc && source ~/.rc
```

- make `.gitignore`
```
$ gi macos,python,visualstudiocode >> ~/.gitignore_global
```
Refer to https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files for details.


### When you want to rename a repository
First, rename it on GitHub website.
Second, open the corresponding [.git->config], and [url = https://~.<rename_here>.git]


### quit Git administration

All you have to do is remove the `.git` directory.


### remove files
1, remove files from the repository and local directory

2, remove files from the repository

```
$ git rm FILENAME #1
$ git rm --cached FILENAME #2
$ git commit -m "delete"; git push origin main
```


### Invite people to my Private repository





## GitHub CLI
### install
```
$ brew install gh
```
### make a new repository based on the current directory
```
$ git init; git add .
$ git commit -m "Initial commit"
$ gh repo create --private --source=. --push'
```
### make an alias to delete remote repository
#### register
```
$ gh alias set repo-delete 'api -X DELETE repos/$1'
$ gh auth refresh -h github.com -s delete_repo
```
#### usage (WARNING: no confirmation!)
```
$ gh repo-delete user/myrepo
```

#### comfirm
```
$ gh alias list
```


## Reference
[What is Git?](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)

[Bitbucket](https://www.atlassian.com/git/tutorials).
