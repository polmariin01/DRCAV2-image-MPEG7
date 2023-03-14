# Distance measure: D = Sum_i(local)|ha(i) - hb(i)| + 5*Sum_i(global)|ha(i) - hb(i)| + Sum_i(semi_global)|ha(i) - hb(i)|
# 80 local bins, 5 global bins, 65 semi global bins
# L1 distance

import os
from matching import *
import numpy as np
from numpy import loadtxt

print(os.getcwd())

ehd_txt_path = "./db/UkentuckyDatabaseEHD.txt"
max_col = 81
k = 10 #Number of images to compute points

ehd = loadtxt(ehd_txt_path, delimiter=" ",usecols=np.arange(1,max_col), unpack=False)
num_rows, num_cols = ehd.shape
print('Number of images: ' + str(num_rows) +'\nNumber of EHD bins: ' + str(num_cols))

ehd_query = ehd[::4] # One image for every group
ehd_database = np.delete(ehd,np.s_[::4],0) # The rest of the images from the group, each group is made of 4
                                           # Every 3 consecutive rows are from similar images
print('Number of queries: '+ str(ehd_query.shape[0]))
print('Maximum value of EHD: ' + str(np.max(ehd)))

distance_ehd = np.full((ehd_query.shape[0], ehd_database.shape[0]), np.nan)

for i in range(ehd_query.shape[0]):
    for j in range(ehd_database.shape[0]):
        distance_ehd[i,j] = distances(ehd_query[i,:],ehd_database[j,:])

print(distance_ehd)
print('Maximum value of distance: ' + str(np.max(distance_ehd)))
print('Minimum value of distance: ' + str(np.min(distance_ehd)))

idx_lowestdistance = np.argsort(distance_ehd, axis=1)[:,:10]

lowest_dist = np.take_along_axis(distance_ehd, idx_lowestdistance, axis=1)

print(lowest_dist)


