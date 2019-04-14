
# coding: utf-8

# In[ ]:


import ee
import numpy as np
import matplotlib

ee.Initialize()


# In[ ]:


# Parse places
p_df = pd.read_csv('../data/targets.csv')
places = {}

WIDTH = 10 / 111

for index, row in p_df.iterrows():
    places[row['name']] = np.array([row['lat'] - WIDTH, row['lon'] - WIDTH, row['lat'] + WIDTH, row['lon'] + WIDTH])
    
print(places)


# In[ ]:


for place in places:
    rgb_ds = gdal.Open(f'./data/rgb_{place}.tif')
    ir_ds = gdal.Open(f'./data/ir_{place}.tif')
    
    r = rgb_ds.GetRasterBand(1).ReadAsArray()
    g = rgb_ds.GetRasterBand(2).ReadAsArray()
    b = rgb_ds.GetRasterBand(3).ReadAsArray()
    rgb = np.array([r, g, b])
    
    ir1 = ir_ds.GetRasterBand(1).ReadAsArray()
    ir2 = ir_ds.GetRasterBand(2).ReadAsArray()
    therm = ir_ds.GetRasterBand(3).ReadAsArray()
    ir = np.array([ir1, ir2, therm])
    
    for i in range(3):
        # Strip NaNs (I think these appear where data is redacted)
        rgb[i][np.isnan(rgb[i])]=np.median(rgb[i][np.isfinite(rgb[i])])-np.std(rgb[i][np.isfinite(rgb[i])])
        ir[i][np.isnan(ir[i])]=np.median(ir[i][np.isfinite(ir[i])])-np.std(ir[i][np.isfinite(ir[i])])
        
        # Scale to [0, 255]
        rgb[i] = rgb[i] - np.min(rgb[i])
        rgb[i] = rgb[i] / np.max(rgb[i]) * 255
        ir[i] = ir[i] - np.min(ir[i])
        ir[i] = ir[i] / np.max(ir[i]) * 255
        
    # Plot
    matplotlib.image.imsave(f'rgb_{place}.png', rgb)
    matplotlib.image.imsave(f'ir_{place}.png', ir)

