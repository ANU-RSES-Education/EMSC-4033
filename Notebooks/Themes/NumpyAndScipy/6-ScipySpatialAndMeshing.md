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

# `scipy.spatial` 

scipy.spatial can compute triangulations, Voronoi diagrams, and convex hulls of a set of points, by leveraging the `Qhull` library.

Moreover, it contains `KDTree` implementations for nearest-neighbor point queries, and utilities for distance computations in various metrics.

## Triangulations (qhull)

```{code-cell} ipython3
%matplotlib inline

import numpy as np
from scipy.spatial import Delaunay, ConvexHull, Voronoi
import matplotlib.pyplot as plt


points = np.random.rand(30, 2)   # 30 random points in 2-D

tri = Delaunay(points)
hull = ConvexHull(points)
voronoi = Voronoi(points)
```

```{code-cell} ipython3
print ("Neighbour triangles\n",tri.neighbors[0:5])
print ("Simplices\n", tri.simplices[0:5])
print ("Points\n", points[tri.simplices[0:5]])
```

```{code-cell} ipython3
from scipy.spatial import delaunay_plot_2d
delaunay_plot_2d(tri)
pass
```

```{code-cell} ipython3
from scipy.spatial import convex_hull_plot_2d

convex_hull_plot_2d(hull)
pass
```

```{code-cell} ipython3
from scipy.spatial import voronoi_plot_2d

voronoi_plot_2d(voronoi)
pass
```

## KDtree

Allows very fast point to point searches.

```{code-cell} ipython3
from scipy.spatial import KDTree, cKDTree
```

```{code-cell} ipython3
tree = cKDTree(points)

print (tree.data)
```

```{code-cell} ipython3
%%timeit

tree.query((0.5,0.5))
```

```{code-cell} ipython3
test_points = np.random.rand(1000, 2)   # 1000 random points in 2-D
```

```{code-cell} ipython3
%%timeit

tree.query(test_points) 
```

```{code-cell} ipython3
more_points = np.random.rand(10000, 2)   # 1000 random points in 2-D

big_tree = KDTree(more_points)
```

```{code-cell} ipython3
%%timeit

KDTree(more_points)
```

```{code-cell} ipython3
%%timeit

big_tree.query(test_points) 
```

## Compare this to the brute-force version


At what point does it make sense to use kdTree and not brute-force distance tests ?

The brute force method takes a fixed time per sample point and a fixed cost associated with the N-neighbour distance computation (but this can be vectorised efficiently). 

```{code-cell} ipython3
# Brute force version

def brute_force_distance(pts, spt):

    d = pts - spt
    d2 = d**2
    distances2 = np.einsum('ij->i',d2)
    
    nearest = np.argsort(distances2)[0]
    
    return np.sqrt(distances2[nearest]), nearest

# print np.einsum('ij->i',distances2)
```

```{code-cell} ipython3
print (brute_force_distance(more_points, (0.0,0.0)))
print (big_tree.query((0.0,0.0)))
```

```{code-cell} ipython3
%%timeit

brute_force_distance(points, (0.5,0.5))
brute_force_distance(points, (0.0,0.0))
brute_force_distance(points, (0.25,0.25))
```

```{code-cell} ipython3
%%timeit

tree.query(np.array([(0.5,0.5), (0.0,0.0), (0.25,0.25)]))
```

```{code-cell} ipython3
%%timeit

brute_force_distance(more_points, (0.5,0.5))
# brute_force_distance(more_points, (0.0,0.0))
# brute_force_distance(more_points, (0.25,0.25))
```

```{code-cell} ipython3
%%timeit

big_tree.query(np.array([(0.5,0.5), (0.0,0.0), (0.25,0.25)]))
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
