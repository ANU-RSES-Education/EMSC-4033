---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 2
  language: python
  name: python2
---

# The game of life 

The universe of the Game of Life ([John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway)) is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

* Any live cell with fewer than two live neighbours dies, as if by needs caused by underpopulation.
* Any live cell with more than three live neighbours dies, as if by overcrowding.
* Any live cell with two or three live neighbours lives, unchanged, to the next generation.
* Any dead cell with exactly three live neighbours becomes a live cell.

See [this page](http://web.stanford.edu/~cdebs/GameOfLife/) for some more information. And, note, thanks to Dan Sandiford for setting up this example. 

```{code-cell} ipython2
%pylab inline
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython2
start = np.array([[1,0,0,0,0,0],
                  [0,0,0,1,0,0],
                  [0,1,0,1,0,0],
                  [0,0,1,1,0,0],
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,1]])
```

We will talk more about plotting later, but for now we can use this without digging deeper:

```{code-cell} ipython2
plt.imshow(start, interpolation='nearest', cmap="gray") 
```

```{code-cell} ipython2
print start[4:8,4:8]  # neighbours of start[5,5]
print start[1:4,1:4]  # neighbours of start[2,2]
#print start[?:?]  # neighbours of start[1,1]
#print start[?:?] # neighbours of start[0,0]
```

```{code-cell} ipython2
live_neighbours = np.empty(start.shape)
for index, value in np.ndenumerate(start):
    #Need to add 2, becase the slicing works like 'up to but not including'
    x0 = max(0,(index[0]-1))
    x1 = max(0,(index[0]+2))
    y0 = max(0,(index[1]-1))
    y1 = max(0,(index[1]+2))
    subarray = start[x0:x1, y0:y1]
    live_neighbours[index] = subarray.sum() - value # need to subtract actual value at that cell...
```

```{code-cell} ipython2
live_neighbours
```

---

__Exercise:__   Your task is to write a function that "runs" the game of life. This should be possible by filling out the two function templates below. 

  - conditions: boundaries are always dead

```{code-cell} ipython2
def get_neighbours(start):
"""
This function gets the number of live neighbours in the binary array start
start : np.ndarray
""" 
```

```{code-cell} ipython2
def game_of_life(start, n):
    """
    this function runs the game of life for n steps...
    start : np.ndarray (0s and 1s)
    n: int number of steps 
    """
    assert (1>= start.min() >= 0) and (1>= start.max() >= 0), "array must be ones and zeros"
    
    current = np.copy(start)
    
    while n:
        neighbours = get_neighbours(current)
        
        for index, value in np.ndenumerate(current):
            print(index, value)
            # Apply the rules to current
            if ...
            
            else ...
            
        n -= 1 
            
            
    return current
```
