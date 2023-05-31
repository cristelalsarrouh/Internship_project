from posdata import *
import numpy as np

tetrode = 5
cell = 3  
# binWidth = 3   
# smooth_factor = 2
recordingsamplingfrequency = 32
TimeWindow = 1000  
Tbin = 10 
theta_freq = [4, 12]  
delta_freq = [2, 4]  
spikeDuration = 1  

# Load the data
mat = loadmat('C:/Users/cristel_alsarrouh/Documents/recordings.mat/Zmoth_03032020_S1-01.mat')

# Extract the relevant positions from PosMtx and remove any rows with zero values
TTMtx = mat['TTMtx']

# Extract signal from specific tetrode
TTMtx2 = TTMtx[TTMtx[:, 1] == tetrode, :] 

# Extract time of spike from specific cell
ts = TTMtx2[TTMtx2[:, 2] == cell, 0]  


def get_pos_spikes(ts, posx, posy, posts):
    # get the position of the spikes
    N = len(ts)
    spkx = np.zeros(N)
    spky = np.zeros(N)
    for i in range(N):
        # Find the index of the position data that is closest to the current spike timestamp
        ind = np.argmin(np.abs(posts - ts[i]))
        # Store the x- and y-coordinates of the spike at the corresponding index in the output arrays
        spkx[i] = posx[ind]
        spky[i] = posy[ind]
    return spkx, spky

spkx, spky = get_pos_spikes(ts, posx, posy, posts)


import matplotlib.pyplot as plt

# plot the gray line
plt.plot(posx, posy, color=[.7, .7, .7], linewidth=2)
# plot the red dots and set their zorder to a larger number to bring them to the front
plt.scatter(spkx, spky, s=20, color='red', zorder=10)

# Create a figure to display the spike map
plt.title('Path spikes')
plt.gca().set_aspect('equal', adjustable='box')
plt.gca().set_axis_off()
plt.show()

# Rate map

binWidth = 3.5
smooth_factor = 2


h = smooth_factor * binWidth

def ratemap_gaussian(h, spkx, spky, posx, posy, posts, binWidth, mapAxis):
    invh = 1 / h
    ratemap = np.zeros((len(mapAxis), len(mapAxis)))
    yy = 0
    for y in mapAxis:
        yy += 1
        xx = 0
        for x in mapAxis:
            xx += 1
            def rate_estimator(spkx, spky, x, y, invh, posx, posy, posts):
                def gaussian_kernel(x, y):
                    return 0.15915494309190 * np.exp(-0.5 * (x * x + y * y))
                conv_sum = np.sum(gaussian_kernel((spkx - x) * invh, (spky - y) * invh))
                edge_corrector = np.trapz(gaussian_kernel((posx - x) * invh, (posy - y) * invh), x=posts)
                r = (conv_sum / (edge_corrector + 0.0001)) + 0.0001
                return r

            ratemap[yy-1, xx-1] = rate_estimator(spkx, spky, x, y, invh, posx, posy, posts)

    return ratemap

ratemap = ratemap_gaussian(h, spkx, spky, posx, posy, posts, binWidth, mapAxis)

# remove unvisited bins from the rate map
ratemap[visited==0] = np.nan


# Create a figure to display the rate map
mytimefig = plt.pcolor(ratemap, cmap='jet')
mytimefig.set_edgecolor('none')
plt.gca().set_aspect('equal', 'box')
plt.axis('off')
plt.title('Rate map',fontsize=12)


