# Markdown

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


## horizontal rule
```md
---
```
---


## list
>```md
>- list item 1
>- list item 2
>- list item 3
>    - list item 3-1
>    - list item 3-2
>        - list item 3-2-1
>        * list item 3-2-2
>        + list item 3-2-3
>
>1. list item 1
>2. list item 2
>3. list item 3
>    1. list item 3-1
>    2. list item 3-2
>```
>
>>- list item 1
>>- list item 2
>>- list item 3
>>    - list item 3-1
>>    - list item 3-2
>>        - list item 3-2-1
>>        * list item 3-2-2
>>        + list item 3-2-3
>>
>>
>>1. list item 1
>>2. list item 2
>>3. list item 3
>>    1. list item 3-1
>>    2. list item 3-2
---

## Color
You can use HTML in Markdown.
>```md
><font color="red">Red string</font>
>```
>><font color="red">Red string </font>
---

## Code
>````md
>```python
>import streamlit as st
>import numpy as np
>import pandas as pd
>```
>````
>>```python
>>import streamlit as st
>>import numpy as np
>>import pandas as pd
>>```
---

## Links
>```md
>[Wikipedia](https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework)
>```
>>リンク
[Wikipedia](https://en.wikipedia.org/wiki/)

---

## Checkbox
>```md
>- [ ] タスク1
>- [x] タスク2
>```
>>- [ ] タスク1
>>- [x] タスク2
---


## raw text, code, bold, italic, strikethrough
>````md
>```
>asdf
>```
>
>`asdf`
>
>*asdf*
>_adsf_
>
>**asdf**
>__adsf__
>
>***asdf***
>___adsf___
>*__adsf__*
>~~asdf~~
>````
>>```
>>asdf
>>```
>>
>>`asdf`
>>
>>*asdf*
>>_adsf_
>>
>>**asdf**
>>__adsf__
>>
>>***asdf***
>>___adsf___
>>*__adsf__*
>>
>>~~asdf~~
---

## Latex
>```md
>>$\LaTeX$
>$$
>\left( \sum_{k=1}^n a_k b_k \right)^2 \leq
>\left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 >\right)
>$$
>```
>>$\LaTeX$
>>
>>$$
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq
\left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$$

## Quote
>```md
>> This is a quote.
>```
>> This is a quote.
---

## Table
>```md
>| Header 1 | Header 2 | Header 3 |
>| :-------- | :--------: | --------: |
>| align=left | align=center | align=right |
>| cell 1   | cell 2   | cell 3   |
>| cell 4   | cell 5   | cell 6   |
>| caption |
>```
>>| Header 1 | Header 2 | Header 3 |
>>| :-------- | :--------: | --------: |
>>| align=left | align=center | align=right |
>>| cell 1   | cell 2   | cell 3   |
>>| cell 4   | cell 5   | cell 6   |
>>| caption |
---


## In-page link
>```md
>[link to list](#list)
>```
>>[link to list](#list)



## Reference
[Markdown Guide](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiW8bKRiv33AhXFC94KHb5XAYgQFnoECAwQAQ&url=https%3A%2F%2Fwww.markdownguide.org%2F&usg=AOvVaw1fohdJEEbL6kohiJ-Pimbe)
