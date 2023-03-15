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
k = 11 #Number of images to compute points + 1 (one extra because the query always retrives itself)

ehd = loadtxt(ehd_txt_path, delimiter=" ",usecols=np.arange(1,max_col), unpack=False)
num_rows, num_cols = ehd.shape
print('Number of images: ' + str(num_rows) +'\nNumber of EHD bins: ' + str(num_cols))

ehd_query = ehd[::4] # One image for every group
ehd_database = np.delete(ehd,np.s_[::4],0) # The rest of the images from the group, each group is made of 4
                                           # Every 3 consecutive rows are from similar images
num_queries = ehd_query.shape[0]
print('Number of queries: '+ str(ehd_query.shape[0]))
#print('Maximum value of EHD: ' + str(np.max(ehd)))

distance_ehd = np.full((ehd_query.shape[0], ehd.shape[0]), np.nan)

for i in range(ehd_query.shape[0]):
    for j in range(ehd.shape[0]):
        distance_ehd[i,j] = distances(ehd_query[i,:],ehd[j,:])

print(distance_ehd.shape)
#print('Maximum value of distance: ' + str(np.max(distance_ehd)))
#print('Minimum value of distance: ' + str(np.min(distance_ehd)))

idx_lowestdistance = np.argsort(distance_ehd, axis=1)[:,:k]

lowest_dist = np.take_along_axis(distance_ehd, idx_lowestdistance, axis=1)
idx_query_puntuable = np.array(range(num_rows)).reshape(num_queries,4) #Positions for each query that gives puntuation
points = np.zeros((num_queries,1))
detected_in_first_ten = np.zeros((num_queries,1))

#Max puntuation with ordered puntuation = 10+9+8=27
#Max puntuation if detected in first 5 images

#print(idx_lowestdistance[9:16,:])
#print(idx_query_puntuable[9:16,:])
#print(idx_lowestdistance.shape)

for i in range(1,k):
    
    idx_lowest_compare = idx_lowestdistance[:,i].reshape(num_queries,1,1)
    idx_query_compare = idx_query_puntuable.reshape(num_queries,1,idx_query_puntuable.shape[1])
    compare = (idx_lowest_compare == idx_query_compare).sum(-1).astype(bool).any(-1).reshape(num_queries,1)
    points[compare] = points[compare] + (11 - i)
    if i < 6:
        detected_in_first_ten[compare] = 1
    #print((idx_lowest_compare == idx_query_compare))
    #print(idx_lowest_compare)
    #print(idx_query_compare)
#print(points)
points = points / 27
total_points = np.sum(points)
total_detected = np.sum(detected_in_first_ten)
percentage_points = (total_points / num_queries)*100
percentage_detected = (total_detected / num_queries) * 100

#print('Positions with the maximum puntuation (1):' + str(np.flatnonzero(points == np.max(points))))
#print('Positions with the minimum puntuation (0):' + str(np.flatnonzero(points == np.min(points))))
print('Total points matching ' + str(num_queries) + ' queries with the dataset using EHD features and L1 distance: ' + str(np.format_float_positional(total_points,precision=2)))
print('Puntuation: ' + str(np.format_float_positional(percentage_points,precision=2)) +'%')
print('Total matched in first 5 images: ' + str(np.format_float_positional(total_detected,precision=2)))
print('Percentage: ' + str(np.format_float_positional(percentage_detected,precision=2)) +'%')
#print(np.min(points))







