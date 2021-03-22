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

# Numpy data structures

When we looked at python data structures, it was obvious that the only way to deal with arrays of values (matrices / vectors etc) would be via lists and lists of lists.

This is slow and inefficient in both execution and writing code. 

`Numpy` attempts to fix this. 

```{code-cell} ipython3
import numpy as np

## This is a list of everything in the module
np.__all__
```

```{code-cell} ipython3
an_array = np.array([0,1,2,3,4,5,6], dtype=np.float)

print (an_array)
print( type(an_array))
help(an_array)
```

```{code-cell} ipython3
print(an_array.dtype)
print(an_array.shape)
```

```{code-cell} ipython3
A = np.zeros((4,4))
print (A)

print (A.shape)
print (A.diagonal())

A[0,0] = 2.0
print (A)

np.fill_diagonal(A, 1.0)
print (A)

B = A.diagonal()
B[0] = 2.0
```

```{code-cell} ipython3
for i in range(0,A.shape[0]):
    A[i,i] = 1.0
print (A)
print()

A[:,2] = 2.0
print (A)
print()

A[2,:] = 4.0
print (A)
print()

print (A.T)
print()

A[...] = 0.0
print (A)
print()

for i in range(0,A.shape[0]):
    A[i,:] = float(i)
    
print (A)
print()

for i in range(0,A.shape[0]):
    A[i,:] = i
    
print (A)
print()

print (A[::2,::2] )


print (A[::-1,::-1])
```

## Speed

```{code-cell} ipython3
%%timeit

B = np.zeros((1000,1000))
for i in range(0,1000):
    for j in range(0,1000):
        B[i,j] = 2.0
        
        
```

```{code-cell} ipython3
%%timeit

B = np.zeros((1000,1000))
B[:,:] = 2.0
```

```{code-cell} ipython3
%%timeit

B = np.zeros((1000,1000))
B[...] = 2.0
```

## Views of the data (are free)

It costs very little to look at data in a different way (e.g. to view a 2D array as a 1D vector).

Making a copy is a different story

```{code-cell} ipython3
print( A.reshape((2,8)))
print()

print( A.reshape((-1)))
print( A.ravel())
print()

print( A.reshape((1,-1)))
print()
```

```{code-cell} ipython3
%%timeit 

A.reshape((1,-1))
```

```{code-cell} ipython3
%%timeit

elements = A.shape[0]*A.shape[1]
B = np.empty(elements)
B[...] = A[:,:].reshape(elements)
```

```{code-cell} ipython3
%%timeit

elements = A.shape[0]*A.shape[1]
B = np.empty(elements)

for i in range(0,A.shape[0]):
    for j in range(0,A.shape[1]):
        B[i+j*A.shape[1]] = A[i,j]
```

__Exercise:__ Try this again for a 10000x10000 array

+++

## Indexing / broadcasting

In numpy, we can index an array by explicitly specifying elements, by specifying slices, by supplying lists of indices (or arrays), we can also supply a boolean array of the same shape as the original array which will select / return an array of all those entries where `True` applies.

Although some of these might seem difficult to use, they are often the result of other numpy operations. For example `np.where` converts a truth array to a list of indices.

```{code-cell} ipython3
AA = np.zeros((100,100))

AA[10,11] = 1.0
AA[99,1]  = 2.0

cond = np.where(AA >= 1.0)
print (cond)
print (AA[cond])
print (AA[ AA >= 1])
print(AA>=1.0)
```

---

Broadcasting is a way of looping on arrays which have "compatible" but unequal sizes.

For example, the element-wise multiplication of 2 arrays

```python
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0]) 
print a * b
```
has an equivalent:

```python
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0]) 
print a * b
```

or 

```python
a = np.array([1.0, 2.0, 3.0])
b = 2.0 
print a * b
```

in which the "appropriate" interpretation of `b` is made in each case to achieve the result. 

```{code-cell} ipython3
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0]) 

print( a * b)

b = np.array([2.0]) 

print (a * b)
print (a * 2.0)
```

Arrays are compatible as long as each of their dimensions (shape) is either equal to the other or 1. 

Thus, above, the multplication works when `a.shape` is `(1,3)` and `b.shape` is either `(1,3)` or `(1,1)`

(Actually, these are `(3,)` and `(1,)` in the examples above ... 

```{code-cell} ipython3
print (a.shape)
print (b.shape)
print ((a*b).shape)
print ((a+b).shape)


aa = a.reshape(1,3)
bb = b.reshape(1,1)

print (aa.shape)
print (bb.shape)
print ((aa*bb).shape)
print ((aa+bb).shape)
```

In multiple dimensions, the rule applies but, perhaps, is less immediately intuitive:

```{code-cell} ipython3
a = np.array([[ 0.0, 0.0, 0.0],
              [10.0,10.0,10.0],
              [20.0,20.0,20.0],
              [30.0,30.0,30.0]])
b = np.array([[1.0,2.0,3.0]])
print (a + b)
print ()
print (a.shape)
print (b.shape)
print ((a+b).shape)
```

Note that this also works for 

```{code-cell} ipython3
a = np.array([[ 0.0, 0.0, 0.0],
              [10.0,10.0,10.0],
              [20.0,20.0,20.0],
              [30.0,30.0,30.0]])

b = np.array([1.0,2.0,3.0])
print (a + b)
print ()
print (a.shape)
print (b.shape)
print ((a+b).shape)
```

But not for 

```{code-cell} ipython3
a = np.array([[ 0.0, 0.0, 0.0],
              [10.0,10.0,10.0],
              [20.0,20.0,20.0],
              [30.0,30.0,30.0]])

b = np.array([[1.0],[2.0],[3.0]])

print (a.shape)
print (b.shape)
print ((a+b).shape)
```

## Vector Operations

```{code-cell} ipython3
X = np.arange(0.0, 2.0*np.pi, 0.0001)
```

```{code-cell} ipython3
print (X)
```

```{code-cell} ipython3
import math

math.sin(X)
```

```{code-cell} ipython3
np.sin(X)
```

```{code-cell} ipython3
S = np.sin(X)
C = np.cos(X)
```

```{code-cell} ipython3
S2 =  S**2 + C**2
print (S2)
```

```{code-cell} ipython3
print (S2 - 1.0)
```

```{code-cell} ipython3
test = np.isclose(S2,1.0)
print (test)
```

```{code-cell} ipython3
print (np.where(test == False))
print (np.where(S2 == 0.0))
```

---

__Exercise__: find out how long it takes to compute the sin, sqrt, power of a 1000000 length vector (array). How does this speed compare to using the normal `math` functions element by element in the array ? What happens if X is actually a complex array ?

__Hints:__ you might find it useful to know about:
  - `np.linspace` v `np.arange`
  - `np.empty_like` or `np.zeros_like`
  - the python `enumerate` function
  - how to write a table in markdown
  
| description     | time   | notes |
|-----------------|--------|-------|
| `np.sin`        | ?      |       |
| `math.sin`      | ?      |       |
|                 | ?      |  -    |

```{code-cell} ipython3
:solution: hidden
:solution_first: true

X = np.linspace(0.0, 2.0*np.pi, 10000000)
print (X.shape)

# ... 
```

```{code-cell} ipython3
:solution: hidden

%%timeit
S = np.sin(X)
```

```{code-cell} ipython3
:solution: hidden

%%timeit

S = np.empty_like(X)
for i, x in enumerate(X):
    S[i] = math.sin(x)
    
```

```{code-cell} ipython3
XX = np.ones((100,100,100))
XX.shape
```

```{code-cell} ipython3
%%timeit
np.sin(XX)
```

```{code-cell} ipython3
%%timeit

for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            math.sin(XX[i,j,k])
                    
```

```{code-cell} ipython3
:solution: hidden

X = np.linspace(0.0, 2.0*np.pi, 10000000)
Xj = X + 1.0j
print (Xj.shape, Xj.dtype)
```

```{code-cell} ipython3
:solution: hidden

%%timeit

Sj = np.sin(Xj)
```

```{code-cell} ipython3
:solution: hidden

import cmath
```

```{code-cell} ipython3
:solution: hidden

%%timeit

Sj = np.empty_like(Xj)
for i, x in enumerate(Xj):
    Sj[i] = cmath.sin(x)
    
```

+++ {"solution": "hidden", "solution_first": true}

__Exercise__: look through the functions below from numpy, choose 3 of them and work out how to use them on arrays of data. Write a few lines to explain what you find. 

  - `np.max` v. `np.argmax`
  - `np.where`
  - `np.logical_and`
  - `np.fill_diagonal`
  - `np.count_nonzero`
  - `np.isinf` and `np.isnan`
  
  
Here is an example: 

`np.concatenate` takes a number of arrays and glues them together. For 1D arrays this is simple:

```python

A = np.array([1.0,1.0,1.0,1.0])
B = np.array([2.0,2.0,2.0,2.0])
C = np.array([3.0,3.0,3.0,3.0])

R = np.concatenate((A,B,C))

# array([ 1.,  1.,  1.,  1.,  2.,  2.,  2.,  2.,  3.,  3.,  3.,  3.])
```

an equivalent statement is `np.hstack((A,B,C))` but note the difference with `np.vstack((A,B,C))`

With higher dimensional arrays, the gluing takes place along one `axis`:

```python
A = np.array(([1.0,1.0,1.0,1.0],[2.0,2.0,2.0,2.0]))
B = np.array(([3.0,3.0,3.0,3.0],[4.0,4.0,4.0,4.0]))
C = np.array(([5.0,5.0,5.0,5.0],[6.0,6.0,6.0,6.0]))

R = np.concatenate((A,B,C))
print R
print
R = np.concatenate((A,B,C), axis=1)
print R

```

```{code-cell} ipython3
:solution: hidden

# Test the results here 

A = np.array(([1.0,1.0,1.0,1.0],[2.0,2.0,2.0,2.0]))
B = np.array(([3.0,3.0,3.0,3.0],[4.0,4.0,4.0,4.0]))
C = np.array(([5.0,5.0,5.0,5.0],[6.0,6.0,6.0,6.0]))

R = np.concatenate((A,B,C))
print R
print
R = np.concatenate((A,B,C), axis=1)
print R
```
