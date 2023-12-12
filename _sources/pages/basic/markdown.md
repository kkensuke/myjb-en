# Markdown
> last update: {sub-ref}`today`
<div style="width: 790px;"></div>


Here, you can learn the basic usage of Markdown. Markdown is **a simple, lightweight markup language for creating formatted, structured text**.
This whole Jupyter Book source code are also written in Markdown (especiallly MyST). You can use Markdown to make websites, documents, notes, book, presentations, email messages. MyST is one of markedown derivatives which have features for **scientific and technical documentation**.

In the following, you see how to write Markdown and how it looks like.

>```md
># Heading 1
>## Heading 2
>### Heading 3
>```
>
>># Heading 1
>>## Heading 2
>>### Heading 3
---


## list
:::{example}
- list item 1
- list item 2
- list item 3
    - list item 3-1
    - list item 3-2
        - list item 3-2-1
        * list item 3-2-2
        + list item 3-2-3

1. list item 1
2. list item 2
3. list item 3
    1. list item 3-1
    2. list item 3-2
:::


## Color
You can use HTML in Markdown.
:::{example}
<font color="red">赤い文字</font>
:::

## Code
::::{example}
```python
import streamlit as st
import numpy as np
import pandas as pd
```
::::


## Link
:::{example}
[Wikipedia](https://ja.wikipedia.org/wiki/Markdown)
:::


## Checkbox
:::{example}
- [ ] task 1
- [x] task 2
:::


## raw text, code, bold, italic, strikethrough
::::{example}
```
asdf
```

`asdf`

*asdf*
_adsf_

**asdf**
__adsf__

***asdf***
___adsf___
*__adsf__*
~~asdf~~
::::


## Latex
:::{example}
$\LaTeX$

$$
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq
\left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$$
:::


## Quote
:::{example}
> This is a quote.
:::


## Table
:::{example}
| Header 1 | Header 2 | Header 3 |
| :-------- | :--------: | --------: |
| align=left | align=center | align=right |
| cell 1   | cell 2   | cell 3   |
| cell 4   | cell 5   | cell 6   |
| caption |
:::


## In-page link
>```md
>[link to list](#list)
>```
>>[link to list](#list)



## Reference
- [Markdown Guide](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiW8bKRiv33AhXFC94KHb5XAYgQFnoECAwQAQ&url=https%3A%2F%2Fwww.markdownguide.org%2F&usg=AOvVaw1fohdJEEbL6kohiJ-Pimbe)
