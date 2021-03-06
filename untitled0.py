#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:41:40 2018

@author: qimindeng
"""

from mpl_toolkits.basemap import Basemap, cm
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

data1 = sio.loadmat('/Users/qimindeng/research/Germany/thres56.mat');
ge5 = data1['ge5']
ge6 = data1['ge6']
gs5 = data1['gs5']
gs6 = data1['gs6']
gl5 = data1['gl5']
gl6 = data1['gl6']
pgs5 = data1['pgs5']
pgs6 = data1['pgs6']
gl_e = data1['gl_e']
pgl = data1['pgl']
pgl_b = data1['pgl_b']
pgl_e = data1['pgl_e']


# plot 

with np.load('/Users/qimindeng/research/Germany/GermanyT.npz') as data:#open the dataset
#initialize
    lat=data['lat']
    lon=data['lon']
    
data=np.transpose(pgs5)
lon_0 = (lon[0]+lon[-1])/2
lat_0 = (lat[0]+lat[-1])/2

# create figure and axes instances
fig = plt.figure(figsize=(8,8))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
# create polar stereographic Basemap instance.
m = Basemap(projection='lcc',lon_0=lon_0,lat_0=lat_0,\
            llcrnrlat=lat[0],urcrnrlat=lat[-1],\
            llcrnrlon=lon[0],urcrnrlon=lon[-1],\
            resolution='i')
# draw coastlines, state and country boundaries, edge of map.
m.drawcoastlines()
m.drawstates()
m.drawcountries()
# draw parallels.
parallels = np.arange(0.,90,2.5)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridians
meridians = np.arange(0.,180.,2.5)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
ny = data.shape[0]; nx = data.shape[1]
lons, lats = m.makegrid(nx, ny) # get lat/lons of ny by nx evenly space grid.
x, y = m(lons, lats) # compute map proj coordinates.
# draw filled contours.
clevs=np.linspace(30,100,71)
#clevs=np.linspace(np.nanmin(data),np.nanmax(data),20)
#clevs = [6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12]
cs = m.contourf(x,y,data,clevs,cmap='PiYG')
# add colorbar.
cbar = m.colorbar(cs,location='bottom',pad="5%")
#cbar.set_label('days')
# add title
plt.title('root mean square error')
filename = "pgs5.png"
plt.savefig(filename)
plt.show()
 
