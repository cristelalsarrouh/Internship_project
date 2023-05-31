from posdata import *
import numpy as np
from scipy.io import loadmat
from calcXCH_TimeWindow import *
import matplotlib.pyplot as plt


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

# Extract waveform characteristics of the spikes
waveforms = TTMtx2[TTMtx2[:, 2] == cell, 3:132]  

IsI = np.diff(ts)

# Plot figure of ISI
plt.figure()
plt.title('Interspike Intervals')
plt.xlabel('msec')
plt.ylabel('spikes')
plt.hist(IsI, bins=np.arange(0, 10.5, 0.5), color=[0.6, 0.6, 0.6], edgecolor=[0, 0, 0])
plt.xticks(np.arange(0, 11, 2))
plt.axis('square')
plt.tick_params(direction='out', length=4, width=2)
plt.grid(False)
plt.show()


