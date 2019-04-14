
# coding: utf-8

# In[1]:


import ee
import numpy as np
import matplotlib.pyplot as plt

ee.Initialize()
sentinel1 = ee.ImageCollection('COPERNICUS/S1_GRD')


# In[3]:


# Define date range
start_date = ee.Date('2018-01-01')
end_date = start_date.advance(180, 'day')    # 180 days later
sentinel1 = sentinel1.filterDate(start_date, end_date)

# Grab the VH and VV polarized parts in interferometric
# wide swath mode
vh = sentinel1.filter(
    ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')).filter(
    ee.Filter.listContains('transmitterReceiverPolarisation', 'VH')).filter(
    ee.Filter.eq('instrumentMode', 'IW'))

# Separate data collected when the sat was ascending and descending
ascending = vh.filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'));
descending = vh.filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'));

# Create a composite from means at different polarizations
# and look angles *for visualization*
composite_max = ee.Image.cat([
    ascending.select('VH').max(),
    descending.select('VH').max(), 
    ee.ImageCollection(ascending.select('VV').merge(
        descending.select('VV'))).max()]).focal_median();

composite_min = ee.Image.cat([
    ascending.select('VH').min(),
    descending.select('VH').min(), 
    ee.ImageCollection(ascending.select('VV').merge(
        descending.select('VV'))).min()]).focal_median();


# In[6]:


# type(ascending)
help(ee.Image.cat)


# In[4]:


places = {'Middle East': [41.137081, 28.780227, 28.934843, 48.239208]}
#           'Europe': [59.084463, 4.23123, 52.82251, 20.086696],
#           'Asia': [36.594309, 70.724632, 31.724374, 77.000019],
#           'North America': [30.322289, -84.243317, 21.169193, -75.04117]}

for place in places:
    rep = places[place]
    
    llx = rep[2]
    lly = rep[1]
    urx = rep[0]
    ury = rep[3]
    geometry = [[llx,lly], [llx,ury], [urx,ury], [urx,lly]]
    
    task_config = {
    'scale': 500,
    'region': geometry
    }

    task = ee.batch.Export.image(composite_max, place, task_config)
    task.start()

