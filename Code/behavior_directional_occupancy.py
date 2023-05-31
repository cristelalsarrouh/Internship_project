from posdata import *
import numpy as np
from scipy.signal import savgol_filter
from colormapc import *

binSizeDir = 6
correction = 0
samplerate_camera = 25

posts = PosMtx[:, 0]

# Smoothing path 
posgx_smoothed, posgy_smoothed = smooth_path(posgx, posgy)
posrx_smoothed, posry_smoothed = smooth_path(posrx, posry)

posgx_smoothed = np.array(posgx_smoothed)
posgy_smoothed = np.array(posgy_smoothed)
posrx_smoothed = np.array(posrx_smoothed)
posry_smoothed = np.array(posry_smoothed)

thetacartesian = np.mod((180/np.pi)*np.arctan2(-posry_smoothed + posgy_smoothed, posrx_smoothed - posgx_smoothed), 360)
deg_theta = np.round(thetacartesian)

# Defining the bin edges
degbin = np.arange(0, 361, binSizeDir)

# Initializing the dirmap array with zeros
dirmap = np.zeros((degbin.size - 1, 2))

# Looping through each bin and counting the number of angles falling in it
for b in range(degbin.size - 1):
    dirmap[b, 0] = np.sum((deg_theta > degbin[b]) & (deg_theta <= degbin[b+1]))
    
# Computing the time taken to cover each direction
dirtime = dirmap[:, 0] / samplerate_camera

# Replacing NaN values with zero
dirtime[np.isnan(dirtime)] = 0

# Smoothing the dirtime using the Savitzky-Golay filter
dirtime = savgol_filter(dirtime, window_length=3, polyorder=1)

def colormapc(num_colors, nbins):
    import matplotlib.pyplot as plt
    import numpy as np

    # Creating the colormap
    cmap = plt.get_cmap('hsv', num_colors)

    # Creating the color array
    col = np.zeros((nbins, 3))
    for i in range(num_colors):
        col[i:num_colors:nbins, :] = cmap(i)[:3]

    return col

# import numpy as np
# import matplotlib.pyplot as plt

# # Create the angles and time arrays
# Angles = np.arange(0, 360, binSizeDir)
# nbins = len(Angles)
# Time = dirtime
# x = np.cos(np.radians(Angles)) * Time
# y = np.sin(np.radians(Angles)) * Time

# # Create the color map
# cc = colormapc(7, nbins)
# col = np.squeeze(cc)

# # Create the polygon vertices
# v = np.column_stack((x, y))
# f = np.arange(len(dirtime))

# # Create the figure and plot the polygon
# fig, ax = plt.subplots()
# ax.add_patch(plt.Polygon(v, facecolor=col, edgecolor='k', linewidth=3))

# # Add lines to the plot
# ax.axhline(0, color='k', linewidth=2)
# ax.axvline(0, color='k', linewidth=2)

# # Set the axis limits and turn off the axis labels
# ax.set_xlim(-np.max(Time), np.max(Time))
# ax.set_ylim(-np.max(Time), np.max(Time))
# ax.axis('off')
# plt.show()
