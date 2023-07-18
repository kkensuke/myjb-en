# Let's make a Jupyter book

We are going to make a Jupyter book from scratch.
```zsh
~/jupyter-book
	└── test-book
	    ├── venv
	    └── test-book
```

## Make a jupyter book

### Make directories
At first, we make the structure and activate the venv(virtual environment).
```zsh
$ mkdir -p ~/jupyter-book/test-book
$ cd ~/jupyter-book/test-book

$ python3 -m venv venv
$ source venv/bin/activate
```

see which python is working:
```zsh
$ which python
```
You can see that you are using python in the venv.

Sometimes, you need to update pip. In that case, you can use the command below. (Replace `<Username>` with your username.)
Update pip:
```zsh
$ /Users/<Username>/jupyter-book/test-book/venv/bin/python3 -m pip install --upgrade pip
```

### Install jupyter-book package
```zsh
(venv)$ pip install -U jupyter-book
```

### Create a new jupyter-book.
```zsh
$ jb create test-book
$ cd test-book
$ jb build .
$ open /Applications/Safari.app _build/html/index.html
```
(jb short for jupyter-book)


## Publish
First, we make a repository named `test-book` on GitHub website without initializing.
Second, we execute the commands below in the test-book directory on your local computer.
```zsh
echo "# test-book" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<Username>/test-book.git
git push -u origin main
```

```zsh
$ pip install ghp-import
$ ghp-import -n -p -f _build/html
```

You can see the published website at `https://\<Username\>.github.io/test-book/intro.html` .


## Update
After you modified the source code, you can update the website by the commands below.

```zsh
$ cd test-book
$ jb build --all .
$ git add .
$ git commit -m "comment"
$ git push origin main
```

Update GitHub Pages
```zsh
$ ghp-import -n -p -f _build/html
```


## Other ways to create jb
### Create a more complete book from interactive prompts.

Jupyter Book also provides a Jupyter Book cookiecutter that can be used to interactively create a book directory structure.
```
jupyter-book create mynewbook/ --cookiecutter
```
https://github.com/executablebooks/cookiecutter-jupyter-book

### Create book files from a Table of Contents
It is possible to use a _toc.yml file in order to create the skeleton of a book automatically. This is useful if you wish to quickly generate empty files from a single structure, and then populate them with content yourselves.
```
jupyter-book toc to-project path/to/_toc.yml
```