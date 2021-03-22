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

# Using `sympy` for a PDE

If we already know the form of the solution to a PDE, then there is no difference from
the approach we just demonstrated with the simple harmonic oscillator. 

However, PDEs are more diverse and difficult to solve in general and it is 
very unlikely that you will be able to treat `sympy` as a black box for this.
The documentation for the PDE solvers is here: https://docs.sympy.org/latest/modules/solvers/pde.html

$$
    \frac{\partial^2 u}{\partial t^2} = c^2  \frac{\partial^2 u}{\partial x^2}
$$

Let's just check to see that we can write this in the appropriate symbolic form that
we can form the relevant derivatives

```{code-cell} ipython3
import sympy
import math
import numpy as np
```

## Symbolic approach

```{code-cell} ipython3
from sympy.core.symbol import Symbol
from sympy.core.function import Function

t     = Symbol('t')
x     = Symbol('x')
c     = Symbol('c', positive=True)
omega = Symbol('omega', positive=True)
k     = Symbol('k', positive=True)
U     = Function('U')

# Potential solution
X = sympy.exp(-sympy.I * omega * t -sympy.I * k * x)
X
```

```{code-cell} ipython3
F = U(t,x).diff(t,2) -  c**2 * U(t,x).diff(x,2)
eq=sympy.Eq(F, 0)
eq
```

```{code-cell} ipython3
eq=sympy.Eq(F, 0)
eq
```

```{code-cell} ipython3
eq2 = eq.replace(U(t,x), X).simplify()
eq2
```

```{code-cell} ipython3
sympy.solve(eq2, k)
```

```{code-cell} ipython3
eq2.subs(k, omega/c )
```
