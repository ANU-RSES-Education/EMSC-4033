---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"deletable": true, "editable": true}

# ipython 

[ipython](https://ipython.org) is an _interactive_ version of the python interpreter. It provides a number of extras which are helpful when writing code. `ipython` code is almost always `python` code, and the differences are generally only important when editing a code in a live (interactive) environment. 

The `jupyter` notebook is a fine example of an interactive environment - you are changing the code as it runs and checking answers as you go. Because you may have a lot of half-completed results in an interactive script, you probably want to make as few mistakes as you can. This is the purpose of `ipython`.

`ipython` provides access to the help / documentation system, provides tab completion of variable and function names, allows you see see what methods live inside a module ... 

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: true
---
## Try the autocomplete ... it works on functions that are in scope

#print

# it also works on variables

long_but_helpful_variable_name = 1

long_but_helpful_variable_name
```

+++ {"deletable": true, "editable": true}

---

It works on modules to list the available methods and variables. Take the `math` module, for example:

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: false
tags: []
---
import math

math.isinf  # Try completion on this

help(math.isnan)

# try math.isinf() and hit shift-tab while the cursor is between the parentheses 
# you should see the same help pop up.

# math.isinf()
```

+++ {"deletable": true, "editable": true}

---

It works on functions that take special arguments and tells you what you need to supply.

Try this and try tabbing in the parenthesis when you use this function yourself:

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: false
tags: [raises-exception]
---
import string
string.capwords("the quality of mercy is not strained")

string.capwords()
```

+++ {"deletable": true, "editable": true}

It also provides special operations that allow you to drill down into the underlying shell / filesystem (but these are not standard python code any more). 

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: false
---
# execute simple unix shell commands 

!ls

!echo ""

!pwd
```

+++ {"deletable": true, "editable": true}

---

Another way to do this is to use the __cell magic__ functionality to direct the notebook to change the cell to something different (here everything in the cell is interpreted as a unix shell ) 

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: false
---
%%sh 

ls -l

echo ""

pwd
```

+++ {"deletable": true, "editable": true}

---

I don't advise using this too often as the code becomes more difficult to convert to python. 

  - A `%` is a one-line magic function that can go anywhere in the cell. 
  - A `%%` is a cell-wide function 



```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: true
---
%magic  # to see EVERYTHING in the magic system !
```

+++ {"deletable": true, "editable": true}


Useful magic functions:

   - `%matplotlib inline` makes plots appear in the notebook and not an external window
   - `%run FILE` runs the contents of the file in place of the given cell 
   - `%%timeit` times how long the cell takes to run
   
---

+++ {"deletable": true, "editable": true}

You can also run ipython in the terminal / shell on this machine. You will see that some of the interactivity still works in a text environment but not all of the pop up help is as helpful as in the notebooks.

<a href="/terminals/1"> Terminal </a>
