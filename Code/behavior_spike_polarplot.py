from scipy.io import loadmat
from posdata import *
import numpy as np
from colormapc import *

# Load the data
mat = loadmat('C:/Users/cristel_alsarrouh/Desktop/Un_20092022_S1_bis_r1_r2-01')


cell = 1
tetrode = 2

TTMtx = mat['TTMtx']
TTMtx2 = TTMtx[TTMtx[:, 1] == tetrode, :] 
ts = TTMtx2[TTMtx2[:, 2] == cell, 0]  

binSizeDir = 6    # bining for polar plouot (choose 5,6 or 10)
correction = 0     # angles shift of LEDs position on the animal head
samplerate_camera = 25

# Extracting the first column of PosMtx and storing it in posts
posts = PosMtx[:, 0]

# Smoothing the path defined by posgx and posgy
posgx, posgy = smooth_path(posgx, posgy)

# Smoothing the path defined by posrx and posry
posrx, posry = smooth_path(posrx, posry)

# Converting posrx and posry to numpy arrays
posrx = np.array(posrx)
posry = np.array(posry)
# Calculating the angle in degrees between the line joining the points (posgx, posgy) and (posrx, posry) and the positive x-axis
thetacartesian = np.mod((180/np.pi)*(np.arctan2(-posry+posgy, posrx-posgx)), 360)

# Rounding the angle to the nearest integer
deg_theta = np.round(thetacartesian)

# Creating a numpy array of zeros with the same length as posts
posdirts = np.zeros(len(posts))

# Calculating the number of samples between each consecutive pair of timestamps in posts
posdirts[0] = np.sum((ts > 0) & (ts <= posts[0]))
for l in range(1, len(posdirts)):
    posdirts[l] = np.sum((ts > posts[l-1]) & (ts <= posts[l]))


degbin = np.arange(0, 361, binSizeDir)

dirmap = np.zeros((degbin.size - 1, 2))

for b in range(degbin.size - 1):
    dirmap[b, 0] = np.sum((deg_theta > degbin[b]) & (deg_theta <= degbin[b+1]))
    dirmap[b,1] = np.sum(posdirts[(deg_theta > degbin[b]) & (deg_theta <= degbin[b+1]), 0])



# dirrate = dirmap[:, 1] / (dirmap[:, 0] / samplerate_camera)
# dirrate[np.isnan(dirrate)] = 0

# dirrate = np.roll(dirrate, -int(correction/binSizeDir))

# Angles = np.arange(0, 360, binSizeDir)
# nbins = len(Angles)
# Rate = dirrate
# x = np.cos(np.deg2rad(Angles)) * Rate
# y = np.sin(np.deg2rad(Angles)) * Rate

# MaxBinRate = np.where(Rate == np.max(Rate))[0]
