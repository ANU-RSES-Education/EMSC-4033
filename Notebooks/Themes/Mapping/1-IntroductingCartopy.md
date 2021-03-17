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

#  Cartopy

Is a mapping and imaging package originating from the Met. Office in the UK. The home page for the package is http://scitools.org.uk/cartopy/. Like many python packages, the [documentation](http://scitools.org.uk/cartopy/docs/latest/index.html) is patchy and the best way to learn is to try to do things and ask other people who have figured out this and that. 

We are going to work through a number of the examples and try to extend them to do the kinds of things you might find interesting and useful in the future. The examples are in the form of a [gallery](http://scitools.org.uk/cartopy/docs/latest/gallery.html)

You might also want to look at the [list of map projections](http://scitools.org.uk/cartopy/docs/latest/crs/projections.html) from time to time. Not all maps can be plotted in every projection (sometimes because of bugs and sometimes because they are not supposed to work for the data you have) but you can try them and see what happens.

Cartopy is built on top of a lot of the matplotlib graphing tools. It works by introducing a series of projections associated with the axes of a graph. On top of that there is a big toolkit for reading in images, finding data from standard web feeds, and manipulating geographical objects. Many, many libraries are involved and sometimes things break. Luckily the installation that is built for this course is about as reliable as we can ever get. I'm just warning you, though, that it can be quite tough if you want to put this on your laptop from scratch.

+++

## Let's get started

We have a number of imports that we will need almost every time. 

If we are going to plot anything then we need to include **matplotlib**.

```{code-cell} ipython3
:hide_input: false

%pylab inline

import matplotlib.pyplot as plt

import cartopy
import cartopy.crs as ccrs
```

```{code-cell} ipython3
:hide_input: true

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()
```

The simplest plot: global map using the default image built into the package and adding coastlines

```{code-cell} ipython3
fig = plt.figure(figsize=(12, 12), facecolor="none")
ax  = plt.axes(projection=ccrs.Mercator())

    # make the map global rather than have it zoom in to
    # the extents of any plotted data
    
ax.set_global()
ax.coastlines()  
ax.stock_img()
```

Try changing the projection - either look at the list in the link I gave you above or use the tab-completion feature of iPython to see what ``ccrs`` has available ( not everything will be a projection, but you can see what works and what breaks ).

Here is how you can plot a region instead of the globe:

```{code-cell} ipython3
fig = plt.figure(figsize=(12, 12), facecolor="none")
ax  = plt.axes(projection=ccrs.Robinson())    
ax.set_extent([0, 40, 28, 48])

ax.coastlines(resolution='50m')  
ax.stock_img()
```

```{code-cell} ipython3
help(ax.stock_img)
```

```{code-cell} ipython3

```
