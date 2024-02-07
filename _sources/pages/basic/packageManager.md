# Homebrew and venv
> last update: {sub-ref}`today`
<div style="width: 790px;"></div>


What is a package manager?
> A package manager or package-management system is a collection of software tools that automates the process of installing, upgrading, configuring, and removing computer programs for a computer in a consistent manner. - wikipedia


There are various package managers.

For OS level,
- Windows: vcpkg
- Mac: Homebrew
- Ubuntu: apt

For application level,
- PHP: composer
- JavaScript(node): npm, Yarn
- Ruby: gem
- Java: Maven, Gradle
- Python: pip, conda
- R: conda, CRAN

In this page, we install homebrew and make a venv to manage python packages.

## [Homebrew](https://docs.brew.sh/Installation)
Homebrew is　a missing package manager for macOS (or Linux).
To install it, input next code in the Terminal (you should check the newest code [here](https://brew.sh/));
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

you will get next output:
```bash
==> Next steps:
- Run these two commands in your terminal to add Homebrew to your PATH:
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/kensuke/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
- Run brew help to get started
- Further documentation:
    https://docs.brew.sh
```

So input next to add Homebrew to your PATH (change Username below):
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/Username/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Let's check whether you succeeded!
```bash
brew --version
```
if you get: `Homebrew x.x.x`, you succeeded.

(venv)=
## [Venv](https://docs.python.org/3/library/venv.html)
To make a virtual environment for python, venv is the easiest tool! Although there are pyenv or anaconda for python, they are not necessary for beginners.
Let's make a venv.
Making and deleting a venv are really easy. Let's make a test venv in your home directory.

```bash
python3 -m venv ~/test
```
then activate the venv:
```bash
source test/bin/activate
```
or
```bash
. test/bin/activate
```

Now your venv is activated. You can see the name of venv on the left side of your user name in the terminal like `(test) Username@MacBook-Pro ~ %`.
Let's check the version of python:
```bash
python -V
```
and you get `Python 3.x.x`.

Now you made a new venv and activated it, but actually there is almost nothing in the venv.
`pip list --format=freeze` shows the packages in your venv and there is no output for now.
Before installing something, you might have to upgrade `pip`, which is a python package manager(change Username below):
```bash
/Users/Username/test/bin/python3 -m pip install --upgrade pip
```
then let's install a package (here numpy)!
```bash
pip install numpy
```
and let's check:
```bash
pip list --format=freeze
```
and you get `numpy==x.xx.x`.

If you want to use python as a beginner, you should install matplotlib, pandas, and jupyter-lab;
```bash
pip install matplotlib
pip install jupyterlab
```

Matplotlib is a library for visualization, pandas for data analysis and manipulation, and jupyter-lab for web-based user interface for running python code.
Scipy, which is for scientific computing, is also a useful package for some people.
Now you can see many packages in your test venv; try `pip list --format=freeze`, though you installed apparently just 4 or 5 packages. Actually, you installed many packages with jupyter-lab.
To deactivate the venv, just input: `deactivate` in the terminal. To activate again, input; `source test/bin/activate`.

````{warning}
If you want to delete the venv, remove it with:
```bash
rm -rf ~/test
```
in the terminal.
````

## Let's use jupyter-lab!
You installed jupyter-lab, so let's try to use it !!

```bash
jupyter-lab
```
Your default browser will show up and open jupyter-lab.

To deactivate juypter-lab (not venv) in the Terminal; `Control + C` and you will be asked whether to quit, then enter y[yes].
For more details, see [this](../python/basics.md) page.

```{note}
- Renaming venv
- Renaming the parent directories of venv
- Changing the location of venv  
are not recommended.
```


