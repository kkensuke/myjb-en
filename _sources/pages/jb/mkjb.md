# Let's make a Jupyter book
> last update: {sub-ref}`today`

> [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) is a tool for building publication-quality books and documents from computational materials. Jupyter Book extends the capabilities of Sphinx (a tool for building documentation) and MyST Markdown (a flavor of Markdown designed for technical content). It can generate different (HTML, PDF, eBook, etc.) versions of your content, and is used widely across the Jupyter ecosystem for publishing documentation, research, and educational material.

We are going to make a Jupyter book from scratch.

## Make a jupyter book

### Make directories
At first, we make the structure and activate the venv(virtual environment).

```bash
./jupyter-book
	└── test-book
	    ├── venv
```

```bash
$ mkdir -p ./jupyter-book/test-book
$ cd ./jupyter-book/test-book

$ python3 -m venv venv
$ source venv/bin/activate
```

see which python is working:
```bash
(venv)$ which python
```
You can see that you are using python in the venv.

````{note}
Sometimes, you need to update pip. In that case, you can use the command below. (Replace `<Username>` with your username.)\
Update pip:
```bash
(venv)$ /Users/<Username>/jupyter-book/test-book/venv/bin/python3 -m pip install --upgrade pip
```
````

### Install jupyter-book package
```bash
(venv)$ pip install -U jupyter-book
```

### Create a new jupyter-book.
```bash
./jupyter-book
	└── test-book
	    ├── venv
	    └── test-book
                ├── _condig.yml
                ├── _toc.yml
                ├── ...
```

```bash
(venv)$ jb create test-book
(venv)$ cd test-book
(venv)$ jb build .
(venv)$ open /Applications/Safari.app _build/html/index.html
```

```{note}
jb short for jupyter-book
```

When the build is completed, you will see the following HTML file URL: `file:///Users/<Username>/path/to/jupyterbook/test-book/test-book/_build/html/index.html` in the terminal. Paste it into your browser to check it out.

## Publish
First, we make a repository named `test-book` on GitHub website without initializing.
Second, we execute the commands below in the test-book directory on your local computer.
```bash
(venv)$ echo "# test-book" >> README.md
(venv)$ git init
(venv)$ git add .
(venv)$ git commit -m "first commit"
(venv)$ git branch -M main
(venv)$ git remote add origin https://github.com/<Username>/test-book.git
(venv)$ git push -u origin main
```

```bash
(venv)$ pip install ghp-import
(venv)$ ghp-import -n -p -f _build/html
```

You can see the published website at `https://<Username>.github.io/test-book/intro.html`. It may take a few minutes to be published.


## Update
After you modified the source code, you can update the website by the commands below.

```bash
(venv)$ cd test-book
(venv)$ jb build --all .

(venv)$ git add .
(venv)$ git commit -m "comment"
(venv)$ git push origin main

(venv)$ ghp-import -n -p -f _build/html
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
