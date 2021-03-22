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

# scipy 


`scipy` is a collection of tools that are commonly encountered in scientific environments. The implementations are generally robust and reliable. The documentation varies in quality but is generally helpful. 

It is impossible to cover all the aspects of the entire package because it includes modules to cover an enormous range of functionality:

  - `cluster`: clustering algorithms (data analysis)
  - `constants`: physical / mathematical constants
  - `fftpack`: fourier transforms
  - `integrate`: numerical integration routines
  - `interpolate`: various data interpolation routines
  - `linalg`: linear algebra routines (matrices etc)
  - `ndimage`: N dimensional image manipulation and resizing (also array manipulations)
  - `odr`: Orthogonal distance regression
  - `optimize`: Optimization / root finding
  - `signal`: Signal processing
  - `sparse`: Sparse matrix packages
  - `spatial`: Spatial data / triangulation / Voronoi diagrams 
  - `special`: Special (mathematical) functions 
  - `stats`: Statistics routines
  
  
Here we will just skim some of the available sub-modules and go through some of the examples provided. 

```{code-cell} ipython3
## importing scipy does very little (mostly the numpy namespace)
import numpy as np
import scipy

## to use the modules import each one separately
from scipy import constants as constants

print (constants.electron_mass)
print ()
print (constants.find("electron mass"))
print ()
print (constants.value("electron mass")," ", constants.unit("electron mass"))
```

```{code-cell} ipython3
## Note, this is actually the numpy array as well

help(scipy.ndarray)
```

```{code-cell} ipython3

```
