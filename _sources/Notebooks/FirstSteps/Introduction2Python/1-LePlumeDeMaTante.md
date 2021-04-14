---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Python Phrase Book

The first thing we should do is become familiar with the shape and feel of python code because we can't really discuss the features of python without a few examples. So here is a little phrase book ...

```{admonition} Aside
The Python name derives from *Monty Python's Flying Circus* which means you should be alarmed at the mention of a [Phrase Book](https://www.youtube.com/watch?v=C1Sw0PDgHU4)
```

## Obligatory Hello world program

```python
# Print out the "Hello World" message
print("Hello World")
```
---
```
>>> 
Hello World
```

There is no set up needed to run this simple example because the `print` command is built into python. 
It is actually implemented as a *function* that displays its argument to the screen, so now you know what python functions look like ! You can also see how to write a comment.

Here are a couple of other ways to do the same thing

```python

hello_world_string = "Hello World"
print(hello_world_string)

# Formatting output is also possible (cf c `printf` formats)
print("-- {:s} --".format(hello_world_string))
```
---
```
>>>
Hello World
Hello World
```

We can assign the message to a variable and print that directly. The `print` function does not need to be told that `hello_world_string` is a string (and the fact that the name has the word *string* in it is neither here nor there). Variable names are allowed to have underscore characters in them, letters and numbers (other than the first character, that can't be a number). underscores at the beginning of a variable are conventionally *"hidden"* which actually just means they are a bit harder to find in an interactive environment.

```{note}
In fact, the string is a python object that understands that it may need to be printed and will respond appropriately to the print function's call. The `format` function is also part of the repertoire of the string object and we will see this `object.function` way of accessing the "methods" of an object very, very often.
```

+++

## Indentation and block structure

`python` uses indentation to define code blocks and will complain when the indentation is broken. This is important for defining functions, conditional statements, loops and so on:

### Loops and if statements

```python

for i in range(0,5):
    print("The value of i is {} ".format(i), end=" ")
    if i%2:
        print("which is an odd number")
    else:
        print("which is an even number")        
```

This has the layout of a typical python code - the blocks that make up a loop or the branches of conditions are defined by the indentation. Easy if the code is short, much harder to follow if you cram too much into a block. 


## Functions

```python

def my_first_function(argument1, argument2):
    """This is the "help" for a function a.k.a. docstring. This particular function returns 
       its first argument"""
    
    # indent the function definition
    
    return(argument1)

print(my_first_function(1,2))
print(my_first_function("Hello world", 0))
help(my_first_function)
    
```
---

```
>>>
1
Hello world

Help on function my_first_function in module __main__:

my_first_function(argument1, argument2)
    This is the "help" for a function a.k.a. docstring. This particular function returns 
    its first argument
```
---

```python
def my_second_function(argument1, argument2):
    """Function returns both arguments"""
    
    # indent the function definition
    
    return(argument1, argument2)

print(my_second_function(1,2))
print(my_second_function("Hello world", 0))
help(my_second_function)

a,b = my_second_function(1,2)
print(a)
print(b)

```
---
```
>>>
(1, 2)
('Hello world', 0)
Help on function my_second_function in module __main__:

my_second_function(argument1, argument2)
    Function returns both arguments
    
1
2
```

Functions can return many arguments and they come back as a tuple. It is straightforward to *unpack* the values that are returned (the last example above). 

```{note}
Since `python` is an interpreted language, you must define functions before they are encountered in the code. That inverts the way many people write their code with the *subroutines* defined after the logic of the code is laid out. Instead, `python` uses *modules* to organise collections of code that are defined outside the main flow of the code. 
```


+++

## Modules

The power of `python` is probably in the way it encourages sharing and builds a community of users. Before we can do much with `python`, we generally need to `import` the *modules* with the extra functionality we need. The `print` function is unusual in not needing to be imported, nearly everything else we want to do needs an `import` first

For example, the standard python library comes with modules for basic file system operations, string manipulation, mathematical functions, spawning processes ... and so on. The full list is in the [python documentation](https://docs.python.org/3/py-modindex.html). These capabilities are provided (if you have downloaded python, you have these modules) but are not automatically activated. 

Here are a couple of examples:

```python
import math

print(math.sin(math.pi/2))
print(math.cos(math.pi/2))

```
---
```
>>>
1.0
6.123233995736766e-17
```
---

See how the `module.function` works.
Sometimes, you just want to import a few bits and pieces and you can save some
typing by importing those functions at the base level - they can then be used without referencing the module name (if the names do not clash, of course, and provided you remember to import everything you need !)

```python

from math import sin, pi

print(sin(pi/2))
print(cos(pi/2))
```
---
```
>>>
1.0
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-2b3c4d0b7471> in <module>
      4 
      5 #
----> 6 print(cos(pi/2))

NameError: name 'cos' is not defined
```

You can change the names when you import to avoid clashes. Here is an example using `cmath` which is the complex math library complementary to the standard (real numbers) math library.

```python
from math import sin, pi
from cmath import sin as csin 

print(sin(pi/2))
print(csin(pi/2))
```
---
```
>>>
1.0
(1+0j)
```
---

If it makes sense to you, import modules under a different name too

```python
import math as real_math
import cmath as complex_math

print(real_math.sin(real_math.pi))
```

+++

## Parlez-vous Python / Beszélsz pythonban ?

Not yet !

But now you should have some sense of what a python code looks like and why it will break if you type the wrong number of spaces and how dots are used to denote a hierarchy. Next we can take a look at the different types of data in python and then go on to explore how data and functions are bundled together in python objects. All the while, it is fine to dip in to the step-by-step examples.

But it would be useful for us to be able to try out examples and for that, we will want to use live documents and jupyter notebooks.  

```{code-cell} ipython3

```
