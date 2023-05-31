from posdata import *
import numpy as np
from scipy.io import loadmat
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

###################################################################################

# Burst analysis 

# Calculate the inter-spike intervals (ISIs) by taking the difference between consecutive spike times
IsI = np.diff(ts)
# Calculate the mean ISI
mean_IsI = np.mean(IsI)
# Filter out ISIs shorter than mean_isi
Ln = IsI.copy()
Ln[Ln > mean_IsI] = 0

# Mean of selected ISIs
ML = np.mean(Ln[Ln > 0])


# Find bursts
isi_burst = np.zeros_like(IsI)
k = len(Ln) - 1
q = 1
p = 1

while p <= k and p+q < len(Ln):
    # Check if the mean of current segment is less than or equal to ML and current value is greater than 0
    if np.mean(Ln[p:p+q]) <= ML and Ln[p] > 0:
        # Assign the current segment to isi_burst array
        isi_burst[p:p+q] = Ln[p:p+q]
        # Increment q
        q = q + 1
    else:
        # Move to the next segment and reset q to 1
        p = p+q
        q = 1

isi_on = (isi_burst > 0).astype(int)
diff_isi = np.diff(isi_on)
start = np.where(diff_isi == 1)[0] + 1
stop = np.where(diff_isi == -1)[0]

# Note: The `+1` in the `start` index calculation is because `np.diff()` returns an array that is one element shorter
# than the original array, so we need to shift the indices by one to align them with the original array.


# If the first stop time is less than the first start time, add a start time of 1 at the beginning
if stop[0] < start[0]:
    start = np.concatenate(([1], start))
    
# If there are more start times than stop times, add a stop time at the end of the isi_burst array
if len(start) > len(stop):
    stop = np.append(stop, len(isi_burst))



burst = {}   # Initialize an empty dictionary to store burst information
m = 1   # Initialize burst number
c = len(start)   # Get the number of bursts found

for j in range(c):   # Loop through each burst
    burstnumber = 'burstnumber' + str(m)   # Define burst number as a string
    burst[burstnumber] = isi_burst[start[j]:stop[j]]   # Assign burst data to dictionary
    m += 1   # Increment burst number

burst_isi = []
for jk in range(c):
    # create a matrix of burst inter-spike intervals
    burst_isi.append(isi_burst[start[jk]:stop[jk]+1])
    
# convert the matrix into a list and remove zeros
burst_isi = [x for sublist in burst_isi for x in sublist if x != 0]

# compute the mean of inter-spike intervals in bursts
mean_burst_isi = np.mean(burst_isi)

# initialize variables
t = len(burst.keys())
numberofspike = []
burst_duration = []
number_of_burst = t
ratio = []

for j in range(1, t+1):
    nameburst = 'burstnumber' + str(j)
    values = burst[nameburst]
    # compute the number of spikes in the burst
    numberofspike.append(len(values) + 1)
    # compute the duration of the burst
    burst_duration.append(np.sum(values))
    
# convert the lists into arrays
numberofspike = np.array(numberofspike)
burst_duration = np.array(burst_duration)

# compute the burst ratio
ratio = numberofspike / np.sum(numberofspike)
ratio = ratio.reshape(-1, 1) # reshape to (n, 1) array


# Figure 1: Scatter plot of IsI
fig1, ax1 = plt.subplots(figsize=(10, 8))
a = 50
ax1.scatter(IsI[:-1], IsI[1:], a, facecolors=[.7, .7, .7], edgecolors='k', linewidths=1)
ax1.set_xscale('log')
ax1.set_yscale('log')
newLim = [min(ax1.get_xlim()[0], ax1.get_ylim()[0]), max(ax1.get_xlim()[1], ax1.get_ylim()[1])]
ax1.axhline(ML, color='r', linestyle='--', linewidth=3)
ax1.axvline(ML, color='r', linestyle='--', linewidth=3)
ax1.axis('square')
ax1.set_title('Burst Analysis')
ax1.set_xlabel('Interspike Interval (ms)')
ax1.set_ylabel('Interspike Interval (ms)')
ax1.set_xlim(newLim)
ax1.set_ylim(newLim)
ax1.tick_params(direction='out', length=4, width=2, labelsize=18)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.set_xlim(0.1)
ax1.set_ylim(0.1)


# Figure 2: Histogram of IsI
fig2, ax2 = plt.subplots()
bin_edges = range(0, 100, 1)
ISItot = np.diff(ts)
ISItot = ISItot[ISItot > 3]
ax2.hist(ISItot, bins=bin_edges, color=[.6, .6, .6], edgecolor='k', linewidth=3)
ax2.set_title('Interspike Intervals')
ax2.set_xlabel('Interspike Interval (ms)')
ax2.set_ylabel('Spikes')
ax2.axis('square')
ax2.tick_params(direction='out', length=4, width=2, labelsize=18)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.set_xlim(0, 100)
ax2.set_xticks([0, 50, 100])
ax2.set_ylim(0, 15) 
ax2.set_yticks([0,5,10])

plt.show()

# burst characteristics

mean_numb_spike_burst = np.mean(numberofspike)
std_numb_spike_burst = np.std(numberofspike)
mean_burst_duration = np.mean(burst_duration)
std_burst_duration = np.std(burst_duration)
number_burst = t
number_spikes = sum(numberofspike)
mean_ISI = ML
mean_ratio = np.mean(ratio)
