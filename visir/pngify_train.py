import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

import gdal

gdal.AllRegister()

# Parse places
p_df = pd.read_csv('../data/target.csv')
places = {}

WIDTH = 10 / 111

for index, row in p_df.iterrows():
    places[row['name']] = np.array([row['lat'] - WIDTH, row['lon'] - WIDTH, row['lat'] + WIDTH, row['lon'] + WIDTH])

for place in places:
    if place[0] != 'n':
        continue

    rgb_ds = gdal.Open(f'../data/tif/rgb_{place}.tif')
#    ir_ds = gdal.Open(f'../data/tif/ir_{place}.tif')

    rgb_l = []
    for k in range(1, 4):
        rep = rgb_ds.GetRasterBand(k).ReadAsArray() # TODO handle fully NaN cases?
        rep[np.isnan(rep)]=np.median(rep[np.isfinite(rep)])-np.std(rep[np.isfinite(rep)])
        rep = rep - np.min(rep)
        rep = rep / np.max(rep) * 255
        rgb_l.append(rep)
    img = cv2.merge((rgb_l[2], rgb_l[1], rgb_l[0]))
    cv2.imwrite(f'../data/rgb_{place}.png', img)

#    ir_l = []
#    for k in range(1, 4):
#        rep = ir_ds.GetRasterBand(k).ReadAsArray() # TODO handle fully NaN cases?
#        rep[np.isnan(rep)]=np.median(rep[np.isfinite(rep)])-np.std(rep[np.isfinite(rep)])
#        rep = rep - np.min(rep)
#        rep = rep / np.max(rep) * 255
#        ir_l.append(rep)
#    img = cv2.merge((ir_l[2], ir_l[1], ir_l[0]))
#    cv2.imwrite(f'../data/ir_{place}.png', img)
