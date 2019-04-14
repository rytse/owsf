
# coding: utf-8

# In[1]:


import ee
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ee.Initialize()


# In[2]:


rgb_col = ee.ImageCollection('COPERNICUS/S2').filterDate('2018-01-01', '2018-06-30').filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
ir_col = ee.ImageCollection('LANDSAT/LC08/C01/T1').filterDate('2017-01-01', '2017-12-31')

rgb_data = ee.Image.cat([rgb_col.select('B6').mean(), rgb_col.select('B7').mean(), rgb_col.select('B10').mean()])
ir_data = ee.Image.cat([ir_col.select('B4').mean(), ir_col.select('B3').mean(), ir_col.select('B2').mean()])


# In[5]:


# Parse places
p_df = pd.read_csv('../data/target.csv')
places = {}

WIDTH = 10 / 111

for index, row in p_df.iterrows():
    places[row['name']] = np.array([row['lat'] - WIDTH, row['lon'] - WIDTH, row['lat'] + WIDTH, row['lon'] + WIDTH])


# In[6]:


for place in places:
    print(place)
    rep = places[place]
    
    llx = rep[0]
    lly = rep[1]
    urx = rep[2]
    ury = rep[3]
    geometry = [[llx,lly], [llx,ury], [urx,ury], [urx,lly]]
    
    rgb_task = ee.batch.Export.image.toDrive(rgb_data, description=f'rgb_{place}', scale=500, region=geometry)
    rgb_task.start()
    
    ir_task = ee.batch.Export.image.toDrive(ir_data, description=f'ir_{place}', scale=500, region=geometry)
    ir_task.start()

print('Done')

