'''Import packages.'''
#----------------------------------------------------------------------------
import flopy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
import pyproj
import pandas as pd
#----------------------------------------------------------------------------



'''Create a MODFLOW model object and run with MODFLOW 2005.'''
#----------------------------------------------------------------------------
modelname = "my_model"
m = flopy.modflow.Modflow(modelname, exe_name = 'mf2005')
#----------------------------------------------------------------------------



'''Experiment with the Discretization package'''
#----------------------------------------------------------------------------
# Define model domain in lat/long coordinates
sw_lat = 39.9727 #southwest latitude
sw_long = -90.537 #southwest longitude
ne_lat = 40.6657 #northeast latitude
ne_long = -89.1371 #northeast longitude

# In Illinois, the Illimap projection is used to minimize distortion
# See https://www.spatialreference.org/ref/sr-org/7772/ for details
# Also see http://library.isgs.illinois.edu/Pubs/pdfs/circulars/c451.pdf
# Values originate from here (https://www.spatialreference.org/ref/sr-org/7772/html/)
D = {'proj': 'lcc', # define projection as Lambert Conformal Conic
        'ellps': 'clrk66', # Use the Clarke 1866 ellipsoid
        'lon_0': -89.5, #Central Meridian
        'lat_0': 33, #Latitude of Origin
        'lat_1': 33, #Standard Parallel 1
        'lat_2': 45, #Standard Parallel 2
        'x_0': 2999994*0.3048006096012192, # starting x coordinate is in feet, Python expects meters
        'y_0': 0} # starting y coordinate}

# illimap projection
illimap = pyproj.Proj(D) # Create a projection object that will be used to convert lat/long to illimap

# wgs84 projection
wgs84 = pyproj.Proj('esg:4326')

nex, ney = pyproj.transform(wgs84,illimap,ne_lat,ne_long)
print(nex*3.28,ney*3.28)
# swx, swy = pyproj.transform(wgs84,illimap,sw_lat,sw_long)
#Define the northeastern coordintes, round to nearest 10,000
# nex, ney = illimap(ne_long, ne_lat) # this will return meters
# nex, ney = round(nex/0.3048006096012192,-4), round(ney/0.3048006096012192,-4) # convert to feet

newlat, newlong = pyproj.transform(illimap,wgs84,nex,ney)
print(newlat,newlong)