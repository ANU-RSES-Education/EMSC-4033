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

# Getting started with `sympy`

The package `sympy` adds symbolic mathematical manipulation to the python ecosystem. Like other computational 
algebra packages, it allows you to write expressions, simplify them, differentiate them and make substitutions.
Sympy is relatively lightweight and is completely open source so it is quite an attractive starting point if you 
need to do some straightforward manipulations. 

It is possible to have `sympy` automatically generate code that you can include in other programs and, if you
are very ambitious, you can build in `sympy` as a library into your own code !

The documentation for `sympy` does assume some familiarity with computational algebra packages, you can
find it here [https://docs.sympy.org/latest/index.html](https://docs.sympy.org/latest/index.html). 

This is a quick summary of some things that a symbolic algebra module can give you

```{code-cell} ipython3
import sympy
import math
import numpy as np
```

## Symbols

Symbols are the building blocks of expressions and are defined like this

```{code-cell} ipython3
from sympy.core.symbol import Symbol

X = Symbol('x')
Y = Symbol('y')
psi = Symbol('\psi')

X + Y + psi
```

## Mathematical Functions

Symbols can be built into expressions using a collection of (the usual) mathematical functions and operators

```{code-cell} ipython3
S = sympy.sqrt(X)
S
```

```{code-cell} ipython3
phi = sympy.cos(X)**2 + sympy.sin(X)**2
phi
```

```{code-cell} ipython3
:tags: [raises-exception]

# But not ...

np.sin(S)
```

```{code-cell} ipython3
# and not ...

math.sin(S)
```

## Simplification and Subsitution

Since we are working with abstract symbols, we can simplify expressions but we cannot, in general, evaluate them 
unless we subsitute values for the symbols:

```{code-cell} ipython3
phi.simplify()
```

```{code-cell} ipython3
S.subs(X, 8)
```

```{code-cell} ipython3
S.subs(X, -8)
```

```{code-cell} ipython3
:tags: [raises-exception]

np.sqrt(-8)
```

## Differentiation / Integration

```{code-cell} ipython3
Ds = S.diff(X)
Ds
```

```{code-cell} ipython3
Ds.integrate(X)
```

```{code-cell} ipython3
Ds.integrate((X,2,3))
```

```{code-cell} ipython3

```
