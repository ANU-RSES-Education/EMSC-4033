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

# Using `sympy` for ODEs

We can use the capacity in `sympy` to differentiate symbolic expressions for simple verification of solutions of an ODE or PDE.
For ODEs, there is an extensive set of documentation that deals with finding sets of solutions: 
https://docs.sympy.org/latest/modules/solvers/ode.html#ode-docs.

Often, however, we are verifying a solution we know or suspect to have a certain form and we simply
need `sympy` to make sure there are no mistakes. 

Let's begin with a simple harmonic oscillator:

$$
    \frac{d^2 \theta}{d t^2} = -k \theta 
$$

which we expect to have solutions like 

$$ \theta = A \cos(\omega t + \phi) $$

Can we verify these solutions using symbolic manipulation ?

```{code-cell} ipython3
import sympy
import math
import numpy as np
```

## Symbolic approach

```{code-cell} ipython3
from sympy.core.symbol import Symbol

t = Symbol('t')
A = Symbol('A')

omega = Symbol('omega', positive=True)
phi = Symbol('phi')
```

```{code-cell} ipython3
theta = A * sympy.cos(omega * t + phi)
```

Let's now check to see whether this form of theta is an eigenfunction of the ODE

```{code-cell} ipython3
theta.diff(t,2) / theta
```

So, yes, this satisfies the equation subject to additional information needed to determine
$\phi$. The value of $\omega$ is $\sqrt{k}$.

# Use of the `sympy` equation module (`Eq`)

If we tell sympy that we have an equation, there are tools we can use to solve it

```{code-cell} ipython3
Theta = sympy.Function("Theta")

eq=sympy.Eq(Theta(t).diff(t,2) + omega**2 * Theta(t), 0)
eq
```

```{code-cell} ipython3
sol=sympy.dsolve(eq,Theta(t)).rhs
display(sol)
display(sol.free_symbols)
c1,c2 = list(sol.free_symbols)[0], list(sol.free_symbols)[1]
display(c1, c2)
```

```{code-cell} ipython3
myform = A * sympy.cos(omega * t + phi)
myform
```

```{code-cell} ipython3
sympy.expand_trig(myform)
```

```{code-cell} ipython3
their_form = sol.subs([(c1, -A * sympy.sin(phi)), (c2, A * sympy.cos(phi))])
their_form
```

```{code-cell} ipython3
(myform - their_form).simplify()
```

```{code-cell} ipython3
# Check to see if they are (exactly) equivalent

myform.equals(their_form)
```
