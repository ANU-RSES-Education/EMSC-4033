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

#  Data storage

Python provides file read write and object serialisation / reconstruction (python pickle module). `numpy` provides methods for storing and retrieving structured arrays quickly and efficiently (including data compression). `scipy` provides some helper functions for common file formats such as `netcdf` and `matlab` etc etc.

Sometimes data are hard won - and reformatting them into easily retrieved files can be a lifesaver.

```{code-cell} ipython3
:deletable: true
:editable: true

import numpy as np
from scipy.io import netcdf
```

+++ {"deletable": true, "editable": true}

## text-based data files

Completely portable and human readable, text-based formats are common outputs from simple scripted programs, web searches, program logs etc. Reading and writing them is trivial, and it is easy to append information to a file. The only problem is that the conversion can be extremely slow. 

This example is taken from our mapping exercise and shows the benefit of converting data to binary formats.

---

```python

# Seafloor age data and global image - data from Earthbyters

# The data come as ascii lon / lat / age tuples with NaN for no data. 
# This can be loaded with ...

age = np.loadtxt("global_age_data.3.6.xyz")
age_data = age.reshape(1801,3601,3)  # I looked at the data and figured out what numbers to use
age_img  = age_data[:,:,2]

# But this is super slow, so I have just stored the Age data on the grid (1801 x 3601) which we can reconstruct easily

datasize = (1801, 3601, 3)
age_data = np.empty(datasize)

ages = np.load("global_age_data.3.6.z.npz")["ageData"]

lats = np.linspace(90, -90, datasize[0])
lons = np.linspace(-180.0,180.0, datasize[1])

arrlons,arrlats = np.meshgrid(lons, lats)

age_data[...,0] = arrlons[...]
age_data[...,1] = arrlats[...]
age_data[...,2] = ages[...]
```


---

The timing comparison is astonishing

On my laptop the numpy binary file is about a million times faster to read. I cut out the lat/lon values from this file to save some space, but this would add, at most, a factor of 3 to the npz timing. 

```{code-cell} ipython3
:deletable: true
:editable: true

%%timeit

gadtxt = np.loadtxt("../../Data/Resources/global_age_data.3.6.xyz")
```

```{code-cell} ipython3
:deletable: true
:editable: true

%%timeit

gadnpy = np.load("../../Data/Resources/global_age_data.3.6.z.npz")
```

+++ {"deletable": true, "editable": true}

## netcdf

Many earth-science datasets are stored in the `netcdf` format. `scipy` provides a reader for this format

```{code-cell} ipython3
:deletable: true
:editable: true

nf = netcdf.netcdf_file(filename="../../Data/Resources/velocity_AU.nc")

from pprint import pprint # pretty printer for python objects

pprint( nf.dimensions )
pprint( nf.variables )

print (nf.variables["lat"].data.shape)
print (nf.variables["lon"].data.shape)
print (nf.variables['ve'].data.shape)
print (nf.variables['vn'].data.shape)
```
