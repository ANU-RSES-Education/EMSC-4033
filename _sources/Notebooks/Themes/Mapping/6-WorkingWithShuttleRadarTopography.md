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

# Cartopy and the Shuttle Radar Topography Map data

The SRTM project provides a global land elevation model at a resolution of (roughly) 30m. That's a useful thing to be able to access - either as raw data or simply for plotting into maps. Here are some examples of methods to access, process and display this data using the cartopy interfaces.

For more information on the project: http://www2.jpl.nasa.gov/srtm/

```{code-cell} ipython3
%pylab inline

from osgeo import gdal
from osgeo import gdal_array

import cartopy.crs as ccrs
from cartopy.io import srtm
import matplotlib.pyplot as plt

from cartopy.io import PostprocessedRasterSource, RasterSourceContainer, LocatedImage
from cartopy.io.srtm import SRTM3Source

import cartopy.feature as cfeature
```

```{code-cell} ipython3
from cloudstor import cloudstor
teaching_data = cloudstor(url="L93TxcmtLQzcfbk", password='')
teaching_data.download_file_if_distinct("color_etopo1_ice_low.tif", "Resources/color_etopo1_ice_low.tif")
```

```{code-cell} ipython3
from http.cookiejar import CookieJar
# from urllib import urlencode
import urllib.request


# The user credentials that will be used to authenticate access to the data

username = "lmoresi"
password = "hpX-AnW-xrT-5D6"


# The url of the file we wish to retrieve

url = "http://e4ftl01.cr.usgs.gov/MOLA/MYD17A3H.006/2009.01.01/MYD17A3H.A2009001.h12v05.006.2015198130546.hdf.xml"


# Create a password manager to deal with the 401 reponse that is returned from
# Earthdata Login

password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, "https://urs.earthdata.nasa.gov", username, password)


# Create a cookie jar for storing cookies. This is used to store and return
# the session cookie given to use by the data server (otherwise it will just
# keep sending us back to Earthdata Login to authenticate).  Ideally, we
# should use a file based cookie jar to preserve cookies between runs. This
# will make it much more efficient.

cookie_jar = CookieJar()


# Install all the handlers.

opener = urllib.request.build_opener(
    urllib.request.HTTPBasicAuthHandler(password_manager),
    #urllib2.HTTPHandler(debuglevel=1),    # Uncomment these two lines to see
    #urllib2.HTTPSHandler(debuglevel=1),   # details of the requests/responses
    urllib.request.HTTPCookieProcessor(cookie_jar))
urllib.request.install_opener(opener)
```

```{code-cell} ipython3
# Region of interest

map_extent = [ -120, -117, 33, 36]

lon0 = map_extent[0]
lat0 = map_extent[2]

# High res coastline

coastline = cfeature.NaturalEarthFeature('physical', 'coastline', '10m',
                           edgecolor=(1.0,0.8,0.0),
                           facecolor="none")

ocean = cfeature.NaturalEarthFeature('physical', 'ocean', '50m',
                           edgecolor="green",
                           facecolor="blue")
```

```{code-cell} ipython3
# SRTM - how to grab the data and plot it as an image (in the usual way)

# There may be some "download" warnings but this is simply a result of the way that the SRTM 
# module caches data the first time that it needs a tile. Replotting will be a lot quicker.
 
elev, crs, extent = SRTM3Source().combined(lon0, lat0, 3, 3)

# Take out low points 
#elev = np.ma.masked_less_equal(elev, -100, copy=False)

print (elev.min(), elev.max(), elev.mean())
```

```{code-cell} ipython3
plt.figure(figsize=(15, 10))
ax = plt.subplot(111, projection=ccrs.PlateCarree())
ax.add_feature(coastline, edgecolor="black", linewidth=1, zorder=3)

plt.imshow(elev, extent=extent, transform=crs,
           cmap='terrain', origin='lower', vmin=-400., vmax=2000.)

cb = plt.colorbar(orientation='vertical')
cb.set_label('Altitude')
plt.title("SRTM Map")
gl = ax.gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_left = False
```

Patching data

```{code-cell} ipython3
# Patching holes in the data by a smoothing / interpolation routine from gdal

elev, crs, extent = SRTM3Source().combined(lon0, lat0, 3, 3)

old_elev = elev.copy()

src_ds = gdal_array.OpenArray(elev)

srcband = src_ds.GetRasterBand(1)
dstband = srcband
maskband = srcband 

smoothing_iterations = 0   # iterations applied after patching
options = []
max_distance = 15           # distance in pixels used to find data to patch
result = gdal.FillNodata(dstband, maskband,
                         max_distance, smoothing_iterations, options,
                         callback=None)

elev2 = dstband.ReadAsArray()

# It's probably worth looking at these figures to see what is going on 

print ("Number of points previously out of range ", np.count_nonzero( old_elev < -12000))
print ("Number of points currently out of range ", np.count_nonzero( elev < -12000))
print ("Number of points changed: ", np.count_nonzero(elev-old_elev))
print ("Range of changed points: ",  elev[elev != old_elev].min(), " ", elev[elev != old_elev].max())
```

```{code-cell} ipython3
# And plotting

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, projection=ccrs.PlateCarree())

plt.imshow(elev-elev2, extent=extent, transform=crs, cmap='terrain', origin='lower')
ax.add_feature(coastline, edgecolor="black", linewidth=1, zorder=3)

cb = plt.colorbar(orientation='vertical')
cb.set_label('Altitude')
plt.title("SRTM Map")
gl = ax.gridlines(draw_labels=True,)
gl.xlabels_top = False
gl.ylabels_left = False
```

```{code-cell} ipython3
plt.figure(figsize=(15, 10))
ax = plt.subplot(111, projection=ccrs.PlateCarree())

plt.imshow(elev, extent=extent, transform=crs,
           cmap='terrain', origin='lower', vmin=-200.0, vmax=3000)

ax.add_feature(coastline, edgecolor="black", linewidth=1, zorder=3)

cb = plt.colorbar(orientation='vertical')
cb.set_label('Altitude')
plt.title("SRTM Map")
gl = ax.gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_left = False
```

```{code-cell} ipython3
# Here is a completely different way to do this !! 

# Rather than downloading data, we can make use of on-demand downloading
# through interfaces provided by cartopy. This might save us managing a
# huge amount of data but the manipulations we used routinely above now
# have to be handled by helper functions handed into the cartopy classes.


# The "container" is like a placeholder for what will need to be called 
# when the plotting routines need to grab data

srtm = RasterSourceContainer(SRTM3Source())

plt.figure(figsize=(15, 10))
ax = plt.subplot(111, projection=ccrs.PlateCarree())
ax.set_extent(map_extent)

data_norm = matplotlib.colors.Normalize(vmin=-300, vmax=2000)
ax.add_raster(srtm, cmap='terrain', norm=data_norm)
ax.add_feature(coastline)
```

```{code-cell} ipython3
# Shuttle radar shaded relief map 

from cartopy.io import srtm as csrtm

globaletopo       = gdal.Open("Resources/color_etopo1_ice_low.tif")
globaletopo_img   = globaletopo.ReadAsArray().transpose(1,2,0)

def shade(located_elevations):
    """
    Given an array of elevations in a LocatedImage, fill any holes in
    the data and add a relief (shadows) to give a realistic 3d appearance.

    """

    new_img = csrtm.add_shading(located_elevations.image, azimuth=135, altitude=33)
    return LocatedImage(new_img, located_elevations.extent)


# Define a raster source which uses the SRTM3 data and applies the
# fill_and_shade function when the data is retrieved.

shaded_srtm = PostprocessedRasterSource(SRTM3Source(), shade)

fig = plt.figure(figsize=(10, 10))
ax  = plt.subplot(111, projection=ccrs.PlateCarree())
ax.set_extent(map_extent)

# Add the shaded SRTM source to our map with a grayscale colormap.

ax.add_raster(shaded_srtm, cmap='Greys', zorder=1)

plt.imshow(globaletopo_img, zorder=2, transform=ccrs.PlateCarree(), 
            extent = [-180.0, 180.0, -90.0, 90.0], interpolation='bicubic', alpha=0.333)

ax.add_feature(coastline, edgecolor="black", linewidth=1, zorder=3)
ax.add_feature(ocean,  zorder=4, alpha = 0.5)

# This data is high resolution, so pick a small area which has some
# interesting orography.

plt.title("SRTM Shaded Relief Map")

gl = ax.gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_left = False

fig.savefig("LA_Region_ShadedRelief", dpi=600)
```

```{code-cell} ipython3
# Shuttle radar shaded relief map 

from cartopy.io import srtm as csrtm

# globaletopo       = gdal.Open("../../Data/Resources/color_etopo1_ice_low.tif")
# globaletopo_img   = globaletopo.ReadAsArray().transpose(1,2,0)

map_extent = [ -118.5, -117.6, 33.5, 34.5]


def shade(located_elevations):
    """
    Given an array of elevations in a LocatedImage, fill any holes in
    the data and add a relief (shadows) to give a realistic 3d appearance.

    """
    new_img = csrtm.add_shading(located_elevations.image, azimuth=135, altitude=33)
    return LocatedImage(new_img, located_elevations.extent)


# Define a raster source which uses the SRTM3 data and applies the
# fill_and_shade function when the data is retrieved.

shaded_srtm = PostprocessedRasterSource(SRTM3Source(), shade)

fig = plt.figure(figsize=(10, 10))
ax  = plt.subplot(111, projection=ccrs.PlateCarree())
ax.set_extent(map_extent)

# Add the shaded SRTM source to our map with a grayscale colormap.

ax.add_raster(shaded_srtm, cmap='Greys', zorder=1)

plt.imshow(globaletopo_img, zorder=2, transform=ccrs.PlateCarree(), 
           extent = [-180.0, 180.0, -90.0, 90.0], interpolation='bicubic', alpha=0.333)

ax.add_feature(coastline, edgecolor="black", linewidth=1, zorder=3)
ax.add_feature(ocean,  zorder=4, alpha = 0.25)


# This data is high resolution, so pick a small area which has some
# interesting orography.


plt.title("SRTM Shaded Relief Map")

gl = ax.gridlines(draw_labels=True)
gl.xlabels_top = False
gl.ylabels_left = False

fig.savefig("LA_Basin_ShadedRelief", dpi=600)
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
