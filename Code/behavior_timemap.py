from posdata import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d


environment_size = int(input("Enter the size of the environment in centimeter: "))
sampling_freq = int(input("Enter the sampling frequency of the camera: "))
smooth_factor = int(input("Enter the smoothing factor for ratemap: "))


# Calculate time of the session
time_session = posts[-1]/1000

# Extract distance between each position samples
raw_dist = []
for i in range(len(posx)-1):
    dist = ((posx[i+1]-posx[i])**2)+((posy[i+1]-posy[i])**2)
    raw_dist.append(np.sqrt(dist))

# Calculate size of the position see by the camera
size_map_arena = abs(np.diff([np.max(posx), np.min(posx)]))
# calculate real distance for each sample position
real_dist = np.array(raw_dist)*environment_size/size_map_arena

distance = real_dist
 
# Calculate instantaneous speed
instantaneous_posts = np.diff(posts)/1000
nonzero_indices = np.nonzero(instantaneous_posts)[0]
distance = distance[nonzero_indices]
instantaneous_posts = instantaneous_posts[nonzero_indices]
instantaneous_speed = distance/instantaneous_posts

# This function allows to build a timemap from the coordinate position of each spike
bins = len(mapAxis) # extract bins from MapAxis
time_map = np.zeros((bins, bins)) # create matrix of zeros

# Calculate time in each cell of the matrix
N = len(posts)
for i in range(N):
    ind_x = np.where(mapAxis <= posx[i])[0]
    ind_y = np.where(mapAxis <= posy[i])[0]
    if len(ind_x) > 0 and len(ind_y) > 0:
        ind_x = np.max(ind_x)
        ind_y = np.max(ind_y)
        time_map[ind_x, ind_y] += 1

# Calculate the time in seconds in each cell of the matrix
time_map = time_map * sampling_freq / 1000

# Smooth the timemap using a 5x5 filter
HH = np.array([[0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0]]) / 13

time_map = convolve2d(time_map, HH, mode='same', boundary='symm')

# Remove cell/bin that animal has not visited
time_map[visited == 0] = np.nan

# Calculate total distance covered by the animal during the session
total_distance = np.sum(real_dist)

# Calculate total time of the session
total_time = posts[-1] / 1000

# Calculate mean speed of the animal during the session
mean_speed = total_distance / total_time

# Calculate mean instantaneous speed of the animal during the session
mean_instantaneous_speed = np.mean(instantaneous_speed)

# Calculate maximum value in the time map
maxtimemap = np.nanmax(time_map)

# Create a figure to display the time map
mytimefig = plt.pcolor(time_map, cmap='jet')
plt.colorbar()
mytimefig.set_edgecolor('none')
plt.gca().set_aspect('equal', 'box')
plt.axis('off')
plt.title('Time map, max=%.2f sec' % maxtimemap, fontsize=12)



