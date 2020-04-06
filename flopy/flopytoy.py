#----------------------------------------------------------------------------
#
# Created on Sun Mar 29 15:06:36 2020
# @author: dbabrams
# FloPy Toy Model code, runs MODFLOW 2005
# Unless otherwise stated, all units are in feet and days.
#
#----------------------------------------------------------------------------



'''Import packages.'''
#----------------------------------------------------------------------------
import flopy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp
import pyproj
#----------------------------------------------------------------------------

#%%

'''Create a MODFLOW model object and run with MODFLOW 2005.'''
#----------------------------------------------------------------------------
modelname = "my_model"
m = flopy.modflow.Modflow(modelname, exe_name = 'mf2005')
#----------------------------------------------------------------------------

#%%

'''Create the Discretization package'''
#----------------------------------------------------------------------------
# define model domain in lat/long coordinates

sw_lat = 38.483
sw_long = -90.233
ne_lat = 38.917 
ne_long = -89.917

#define the projection
illimap = {'proj' : 'lcc',  #Lambert conformal conic
     'ellps' : 'clrk66',
     'lon_0' : -89.5,
     'lat_0' : 33, 
     'lat_1' : 33,
     'lat_2' : 45,
     'x_0' : 2999994*0.3048,
     'y_0' : 0}

# create the projection object
prj = pyproj.Proj(illimap)

# NE x and y most projection (NE corner of the area)
nex, ney = prj(ne_long, ne_lat)
# we need to get them back in feet
nex, ney = round(nex/0.3048, -4), round(ney/0.3048, -4)

# SW x and y most projection (SW corner of the area)
swx, swy = prj(sw_long, sw_lat)
swx, swy = round(swx/0.3048, -4), round(swy/0.3048, -4)
#print(nex, ney, swx, swy)

# Assign Discretization variables
Lx = nex - swx # Width of the model domain
Ly = ney - swy # Height of the model domain
ztop = 0. # Model top elevation
zbot = -50. # Model bottom elevation
nlay = 1 # Number of model layers
dx = 1000
dy = 1000
nrow = int(Ly/dy) # Number of rows
ncol = int(Lx/dx) # Number of columns
#print(nrow, ncol)
nper = 1 #specify number of stress periods
steady = [True] #specify if stress period is transient or steady-state

# create flopy discretization object
# length and time are feet (1) and days (4).
# See https://water.usgs.gov/ogw/modflow/MODFLOW-2005-Guide/index.html?dis.htm 
dis = flopy.modflow.ModflowDis(model=m, nlay=nlay, nrow=nrow, ncol=ncol, 
                               delr=dx, delc=dy, top=ztop, botm=zbot, 
                               itmuni = 4, lenuni = 1, 
                               nper=nper, steady=steady)

#%%

'''Expirement with the Discretization package'''
#----------------------------------------------------------------------------
# define model domain in lat/long coordinates
'''
sw_lat = 40.045872
sw_long = -90.397402
ne_lat = 40.575944 
ne_long = -89.587339

#define the projection
D = {'proj' : 'lcc',  #Lambert conformal conic
     'ellps' : 'clrk66',
     'lon_0' : -89.5,
     'lat_0' : 33, 
     'lat_1' : 33,
     'lat_2' : 45,
     'x_0' : 2999994*0.3048,
     'y_0' : 0}

# illimap projection
illimap = pyproj.Proj(D)

# wgs84 projection
wgs84 = pyproj.Proj('epsg:4326')

nex, ney = pyproj.transfrom(wgs84, illimap, ne_lat, ne_long) #1st proj, 2nd porj, 1st point, 2nd point
#print(nex*3.28, ney*3.28)
swx, swy = pyproj.transfrom(wgs84, illimap, sw_lat, sw_long) #1st proj, 2nd porj, 1st point, 2nd point

newlat, newlong = pyproj.transform(illimap, wgs84, nex, ney)
print(newlat, newlong)

# NE x and y most projection (NE corner of the area)
#nex, ney = prj(ne_long, ne_lat)
# we need to get them back in feet
nex, ney = round(nex/0.3048, -4), round(ney/0.3048, -4)

# SW x and y most projection (SW corner of the area)
#swx, swy = prj(sw_long, sw_lat)
swx, swy = round(swx/0.3048, -4), round(swy/0.3048, -4)
#print(nex, ney, swx, swy)

# Assign Discretization variables
Lx = nex - swx # Width of the model domain
Ly = ney - swy # Height of the model domain
ztop = 0. # Model top elevation
zbot = -50. # Model bottom elevation
nlay = 1 # Number of model layers
dx = 1000
dy = 1000
nrow = int(Ly/dy) # Number of rows
ncol = int(Lx/dx) # Number of columns
#print(nrow, ncol)
nper = 1 #specify number of stress periods
steady = [True] #specify if stress period is transient or steady-state

# create flopy discretization object
# length and time are feet (1) and days (4).
# See https://water.usgs.gov/ogw/modflow/MODFLOW-2005-Guide/index.html?dis.htm 
dis = flopy.modflow.ModflowDis(model=m, nlay=nlay, nrow=nrow, ncol=ncol, 
                               delr=dx, delc=dy, top=ztop, botm=zbot, 
                               itmuni = 4, lenuni = 1, 
                               nper=nper, steady=steady)
'''
#%%----------------------------------------------------------------------------



'''Create the Basic Package, which contains ibound and starting heads'''
#----------------------------------------------------------------------------
# Create ibound as array of ints (1), indicating all cells are active
ibound = np.ones((nlay, nrow, ncol), dtype=np.int32)
#ibound[:, :, 0] = -1 # Designate left boundary cells as constant head
#ibound[:, :, -1] = -1 # Designate right boundary cells as constant head

# Create starting head array, must be floats.
strt = 5*np.ones((nlay, nrow, ncol), dtype=np.float32) #set every cell to 5.0
strt[:, :, 0] = 10. #set left side head to 10 ft
strt[:, :, -1] = 0. #set right side head to 0 ft

#Create flopy bas object
bas = flopy.modflow.ModflowBas(m, ibound=ibound, strt=strt)
#----------------------------------------------------------------------------



'''Create the Layer Property Flow Package, which contains information about
hydruaulic conductivity and other information about how to calculate flow'''
#----------------------------------------------------------------------------
hk = np.ones((nlay,nrow,ncol), dtype=np.float32) #define horizontal hydraulic conductivity
vk = np.ones((nlay,nrow,ncol), dtype=np.float32) #define vertical hydraulic conductivity

#define layer type as convertible (1), must be an integer
#for more information, see https://water.usgs.gov/ogw/modflow/MODFLOW-2005-Guide/index.html?dis.htm
laytyp = np.ones((nlay,), dtype=np.int32)

# create the LPF object
lpf = flopy.modflow.ModflowLpf(model=m, hk=hk, vka=vk, laytyp=laytyp, ipakcb=1)
#%%----------------------------------------------------------------------------



'''Create a recharge package'''
#----------------------------------------------------------------------------
rch = flopy.modflow.mfrch.ModflowRch(model=m, rech=0.000001) # you might need to calibrate the recharge value
#%%----------------------------------------------------------------------------

''' create a recharge package '''
#import stage, lambert x, lambert y
dfriv = pd.read_csv('rivers_625.csv')
#print(dfriv)


#trim dataframe with river information to the model domain
dfriv = dfriv.loc[dfriv['lamx']<nex]
dfriv = dfriv.loc[dfriv['lamy']<ney]
dfriv = dfriv.loc[dfriv['lamx']>swx]
dfriv = dfriv.loc[dfriv['lamy']>swy]

# assign all rivers to the upper layer
dfriv['lay'] = 0
# convert lamx to column parameters
dfriv ['row'] = np.trunc((ney - dfriv['lamy'])/dy)
dfriv ['col'] = np.trunc((dfriv['lamx'] - swx)/dx)
# define the river stage
dfriv['stage'] = dfriv['rvr_stg']
# define the conductance (resistance to flow?)
dfriv['cond'] = 5000 # ft^2/day
# define the river bottom
dfriv['bot'] = dfriv['stage']-3 
# drop unneeded files
dfriv = dfriv.drop(['STR_ORD_MI', 'STR_ORD_MA', 'SUM_LENGTH', 'rvr_stg', 'lamx', 'lamy'], axis=1)

# put into a format that MODFLOW wants 
arriv = dfriv.values
riverdata = {0: arriv} # 0 means first stress period

flopy.modflow.mfriv.ModflowRiv(model=m, ipack=None, stress_period_data=riverdata)






#%%
'''Create the Output Control Package'''
#----------------------------------------------------------------------------
#create oc stress period data. 
spd = {(0, 0): ['print head', 'print budget', 'save head', 'save budget']}
#create output control object
oc = flopy.modflow.ModflowOc(model=m, stress_period_data=spd, compact=True)
#----------------------------------------------------------------------------



'''Create the PCG Solver Object'''
#----------------------------------------------------------------------------
# for the time being, we will use default settings with the solver
pcg = flopy.modflow.ModflowPcg(model=m)
#----------------------------------------------------------------------------



'''Write MODFLOW input files.'''
#----------------------------------------------------------------------------
m.write_input()
#----------------------------------------------------------------------------

#%%

'''Run the model'''
#----------------------------------------------------------------------------
# Executve the model run
success, mfoutput = m.run_model(pause=False, report=True)
# Report back if the model did not successfully complete
if not success:
    raise Exception('MODFLOW did not terminate normally.')
#----------------------------------------------------------------------------
    
#%%    
    
'''Extract binary data from head and flow files'''
#----------------------------------------------------------------------------
#extract binary data from head file as flopy head object
headobj = flopy.utils.binaryfile.HeadFile(modelname+'.hds')
#extract head data from head object
head = headobj.get_data(totim=1.0)

#extract binary data from budget file as flopy budget object
budgobj = flopy.utils.binaryfile.CellBudgetFile(modelname+'.cbc')
#extract flow data from budget object, define face over which flow is reported
frf = budgobj.get_data(text='flow right face', totim=1.0)
fff = budgobj.get_data(text='flow front face', totim=1.0)
#----------------------------------------------------------------------------

#%%

'''Plot grid and boundary conditions'''
#----------------------------------------------------------------------------
plt.figure(figsize=(10,10)) #create 10 x 10 figure
modelmap = flopy.plot.PlotMapView(model=m, layer=0)
grid = modelmap.plot_grid()
ib = modelmap.plot_ibound()
#to add the rivers
rvr = modelmap.plot_bc(ftype='RIV')
#add labels and legend
plt.xlabel('Lx (ft)',fontsize = 14)
plt.ylabel('Ly (ft)',fontsize = 14)
plt.title('Ibound', fontsize = 15, fontweight = 'bold')
plt.legend(handles=[mp.patches.Patch(color='blue',label='Const. Head',ec='black'),
                   mp.patches.Patch(color='white',label='Active Cell',ec='black'),
                   mp.patches.Patch(color='black',label='Inactive Cell',ec='black')],
                   bbox_to_anchor=(1.5,1.0))
#----------------------------------------------------------------------------

#%%

'''Plot results'''
#----------------------------------------------------------------------------
plt.figure(figsize=(10,10)) #create 10 x 10 figure
modelmap = flopy.plot.map.PlotMapView(model=m, layer=0) #use plotmapview to attach plot to model
grid = modelmap.plot_grid() #plot model grid
contour_levels = np.linspace(head[0].min(),head[0].max(),11) #set contour levels for contouring head
head_contours = modelmap.contour_array(head, levels=contour_levels) #create head contours
flows = modelmap.plot_discharge(frf[0], fff[0], head=head) #create discharge arrows
#to add the rivers
rvr = modelmap.plot_bc(ftype='RIV')
#display parameters
plt.xlabel('Lx (ft)',fontsize = 14)
plt.ylabel('Ly (ft)',fontsize = 14)
plt.title('Steady-State Model, Flow(ft^3/d) and Head(ft) Results', fontsize = 15, fontweight = 'bold')
plt.colorbar(head_contours,aspect=5)
plt.show(modelmap)
#----------------------------------------------------------------------------