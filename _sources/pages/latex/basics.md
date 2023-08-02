Latex Basics
===

# How to write equations

## Inline equations

You can write inline equations by using `$`.

>```latex
>The equation $E=mc^2$ is the most famous equation in physics.
>```
>
>The equation $E=mc^2$ is the most famous equation in physics.

## Display equations

You can write display equations by using `$$` or `\[ \]`.

>```latex
>Schrodinger equation is
>$$
>    i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle
>    =
>    H |\psi(t)\rangle
>$$
>```
>Schrodinger equation is
>$$ i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle = H |\psi(t)\rangle $$

```{tip}
You can use shorter commands with `physics` package.

>```latex
>\begin{equation}
>    \pdv{t} \ket{\psi(t)} = H \ket{\psi(t)}
>\end{equation}
>```
>$$\begin{equation}
    \pdv{t} \ket{\psi(t)} = H \ket{\psi(t)}
\end{equation}$$
```

## Basic Symbols

### Greek letters
| Symbol | Command |
| --- | --- |
| $\alpha$ | `\alpha` |
| $\beta$ | `\beta` |
| $\gamma$ | `\gamma` |
| $\delta$ | `\delta` |
| $\epsilon$ | `\epsilon` |
| $\zeta$ | `\zeta` |
| $\eta$ | `\eta` |
| $\theta$ | `\theta` |
| $\iota$ | `\iota` |
| $\kappa$ | `\kappa` |
| $\lambda$ | `\lambda` |
| $\mu$ | `\mu` |
| $\nu$ | `\nu` |
| $\xi$ | `\xi` |
| $\pi$ | `\pi` |
| $\rho$ | `\rho` |
| $\sigma$ | `\sigma` |
| $\tau$ | `\tau` |
| $\upsilon$ | `\upsilon` |
| $\phi$ | `\phi` |
| $\chi$ | `\chi` |
| $\psi$ | `\psi` |
| $\omega$ | `\omega` |
| $\Gamma$ | `\Gamma` |
| $\Delta$ | `\Delta` |
| $\Theta$ | `\Theta` |
| $\Lambda$ | `\Lambda` |
| $\Xi$ | `\Xi` |
| $\Pi$ | `\Pi` |
| $\Sigma$ | `\Sigma` |
| $\Upsilon$ | `\Upsilon` |
| $\Phi$ | `\Phi` |
| $\Psi$ | `\Psi` |
| $\Omega$ | `\Omega` |

### Operators

| Symbol | Command |
| --- | --- |
| $\pm$ | `\pm` |
| $\times$ | `\times` |
| $\div$ | `\div` |
| $\cdot$ | `\cdot` |
| $\neq$ | `\neq` |
| $\approx$ | `\approx` |
| $\equiv$ | `\equiv` |
| $\leq$ | `\leq` |
| $\geq$ | `\geq` |
| $\in$ | `\in` |
| $\notin$ | `\notin` |
| $\subset$ | `\subset` |
| $\supset$ | `\supset` |
| $\subseteq$ | `\subseteq` |
| $\supseteq$ | `\supseteq` |
| $\forall$ | `\forall` |
| $\exists$ | `\exists` |
| $\infty$ | `\infty` |
| $\nabla$ | `\nabla` |
| $\partial$ | `\partial` |
| $\int$ | `\int` |
| $\oint$ | `\oint` |
| $\sum$ | `\sum` |
| $\prod$ | `\prod` |
| $\lim$ | `\lim` |
| $\log$ | `\log` |
| $\ln$ | `\ln` |
| $\exp$ | `\exp` |
| $\sin$ | `\sin` |
| $\cos$ | `\cos` |
| $\tan$ | `\tan` |
| $\arcsin$ | `\arcsin` |
| $\arccos$ | `\arccos` |
| $\arctan$ | `\arctan` |
| $\sinh$ | `\sinh` |
| $\cosh$ | `\cosh` |
| $\sqrt{x}$ | `\sqrt{x}` |
| $\frac{a}{b}$ | `\frac{a}{b}` |
| $\binom{n}{k}$ | `\binom{n}{k}` |


### Matrices
| Symbol | Command |
|:------:|:-------:|
| $\begin{pmatrix} a \\ b \end{pmatrix}$ | `\begin{pmatrix} a \\ b \end{pmatrix}` |
| $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ | `\begin{pmatrix} a & b \\ c & d \end{pmatrix}` |
| $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ | `\begin{bmatrix} a & b \\ c & d \end{bmatrix}` |
| $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ | `\begin{vmatrix} a & b \\ c & d \end{vmatrix}` |
| $\begin{Vmatrix} a & b \\ c & d \end{Vmatrix}$ | `\begin{Vmatrix} a & b \\ c & d \end{Vmatrix}` |



## `amsmath` package

You can use `amsmath` package to use more commands, such as `cases` and `align`.

### `cases`

You can use `cases` environment to write piecewise functions.

>```latex
>\begin{equation}
>    f(x) = \begin{cases}
>        0 & (x < 0) \\
>        1 & (x \geq 0)
>    \end{cases}
>\end{equation}
>```
>$$\begin{equation}
    f(x) = \begin{cases}
        0 & (x < 0) \\
        1 & (x \geq 0)
    \end{cases}
\end{equation}$$

### `align`

You can align equations by using `align` environment. You can align equations by `&`.

>```latex
>\begin{align}
>    f(x) &= \int_{0}^{x} \left( \frac{1}{2}t^3 - 3t^2 + 4t + 7 \right) dt \\
>    &= \left[ \frac{1}{8}t^4 - t^3 + 2t^2 + 7t \right]_{0}^{x} \\
>    &= \frac{1}{8}x^4 - x^3 + 2x^2 + 7x
>\end{align}
>```
>$$\begin{align}
    f(x)
    &= \int_{0}^{x} \left( \frac{1}{2}t^3 - 3t^2 + 4t + 7 \right) dt \\
    &= \left[ \frac{1}{8}t^4 - t^3 + 2t^2 + 7t \right]_{0}^{x} \\
    &= \frac{1}{8}x^4 - x^3 + 2x^2 + 7x
\end{align}$$


## `physics` package

You can use `physics` package to use more commands, such as `\qty`, `\dv`, `pdv`, `\eval`, `\order`, `\abs`, `\norm`, `\commutator` [or `comm`], `\anticommutator` [or `acomm`]

### `\qty`

You can use `\qty` command to write adaptive parentheses instead of `\left` and `\right`.

>```latex
>\begin{equation}
>    \qty( \frac{1}{2} ) \\
>    \qty[ \frac{1}{2} ] \\
>    \qty{ \frac{1}{2} } \\
>\end{equation}
>```
>$$\begin{equation}
    \qty( \frac{1}{2} ) \\
    \qty[ \frac{1}{2} ] \\
    \qty{ \frac{1}{2} } \\
\end{equation}$$


### `dv`

You can use `dv` command to write derivatives.

>```latex
>\begin{equation}
>    \dv{x} \sin{x} = \cos{x}
>\end{equation}
>```
>$$\begin{equation}
    \dv{x} \sin{x} = \cos{x}
\end{equation}$$


### `pdv`

You can use `pdv` command to write partial derivatives.

>```latex
>\begin{equation}
>    \pdv{x} f(x, y), \pdv{f}{x}, \pdv{f}{x}{y}, \pdv[2]{f}{x}
>\end{equation}
>```
>$$\begin{equation}
    \pdv{x} f(x, y), \pdv{f}{x}, \pdv{f}{x}{y}, \pdv[2]{f}{x}
\end{equation}$$


### `\eval`

You can use `\eval` command to write evaluation.

>```latex
>\begin{equation}
>    \eval{x^2}_{x=1} \\
>    \eval{x^{-2}}_{1}^{\infty} \\
>\end{equation}
>```
>$$\begin{equation}
    \eval{x^2}_{x=1} \\
    \eval{x^{-2}}_{1}^{\infty} \\
\end{equation}$$


### `\order`

You can use `\order` command to write order.

>```latex
>\begin{equation}
>    \order{x^2}, \order{\frac{1}{x^2}}
>\end{equation}
>```
>$$\begin{equation}
    \order{x^2}, \order{\frac{1}{x^2}}
\end{equation}$$


### `\abs`

You can use `\abs` command to write absolute value.

>```latex
>\begin{equation}
>    \abs{x}, \abs{\frac{1}{x}}
>\end{equation}
>```
>$$\begin{equation}
    \abs{x}, \abs{\frac{1}{x}}
\end{equation}$$


### `\norm`

You can use `\norm` command to write norm.

>```latex
>\begin{equation}
>    \norm{x}, \norm{\frac{1}{x}}
>\end{equation}
>```
>$$\begin{equation}
    \norm{x}, \norm{\frac{1}{x}}
\end{equation}$$


### `\commutator` [or `comm`]

You can use `\commutator` command to write commutator.

>```latex
>\begin{equation}
>    \commutator{A}{B}\\
>    \comm{A}{B}
>\end{equation}
>```
>$$\begin{equation}
    \commutator{A}{B}\\
    \comm{A}{B}
\end{equation}$$


### `\anticommutator` [or `acomm`]

You can use `\anticommutator` command to write anticommutator.

>```latex
>\begin{equation}
>    \anticommutator{A}{B}\\
>    \acomm{A}{B}
>\end{equation}
>```
>$$\begin{equation}
    \anticommutator{A}{B}\\
    \acomm{A}{B}
\end{equation}$$


### Dirac bra-ket notation

| Command | Output |
|:-------:|:------:|
| `\bra{a}` | $\bra{a}$ |
| `\ket{a}` | $\ket{a}$ |
| `\braket{a}` | $\braket{a}$ |
| `\braket{a}{b}` | $\braket{a}{b}$ |
| `dyad{a}` | $\dyad{a}$ |
| `dyad{a}{b}` | $\dyad{a}{b}$ |
| `expval{A}` | $\expval{A}$ |
| `ev{A}` | $\ev{A}$ |
| `expval{A}{a}` | $\expval{A}{a}$ |
| `ev{A}{a}` | $\ev{A}{a}$ |
| `\mel{a}{A}{b}` | $\mel{a}{A}{b}$ |

### Matrices

| Command | Output |
|:-------:|:------:|
| `\mqty(a & b \\ c & d)` | $\mqty(a & b \\ c & d)$ |
| `\mqty[ a & b \\ c & d ]` | $\mqty[ a & b \\ c & d ]$ |
| `\mqty| a & b \\ c & d |` | $\mqty| a & b \\ c & d |$ |
| `\imat{n}` | $\imat{n}$ |
| `\pmat{0}` | $\pmat{0}$ |
| `\pmat{1}` | $\pmat{1}$ |
| `\pmat{2}` | $\pmat{2}$ |
| `\pmat{3}` | $\pmat{3}$ |
| `\mqty(\dmat{1,2,3})` | $\mqty(\dmat{1,2,3})$ |
| `\mqty(\admat{1,2,3})` | $\mqty(\admat{1,2,3})$ |





