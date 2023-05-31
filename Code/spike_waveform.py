import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

# # Define global variables
# tetrode = None
# cell = None
# binWidth = None
# smooth_factor = None
# sampling_freq = None
# TimeWindow = None
# Tbin = None
# theta_freq = None
# delta_freq = None
# spikeDuration = None

# # Load the data
# mat = loadmat('C:/Users/cristel_alsarrouh/Documents/recordings.mat/Zmoth_03032020_S1-01.mat')

# def parameters():
#     # prompt the user for input
#     global tetrode, cell, binWidth, smooth_factor, sampling_freq, TimeWindow, Tbin, theta_freq, delta_freq, spikeDuration
    
#     tetrode = input("Enter the tetrode number (leave blank for all cells): ")
#     cell = input("Enter the cell number (leave blank if tetrode is not specified or for all cells): ")
#     if tetrode == "":
#        tetrode = None
#     else:
#        tetrode = int(tetrode)
#     if cell == "":
#        cell = None
#     else:
#        cell = int(cell)
#     binWidth = int(input("Enter the bin width for ratemaps: "))
#     smooth_factor = int(input("Enter the smoothing factor for ratemap: "))
#     sampling_freq = int(input("Enter the sampling frequency of the recordings: "))
#     TimeWindow = int(input("Enter the length of time autocorrelogram (in msec): "))
#     Tbin = int(input("Enter the bin size of autocorrelogram (in msec): "))
#     theta_freq = list(map(int, input("Enter the limits of theta band frequencies for FFT (e.g. '4 12'): ").split()))
#     delta_freq = list(map(int, input("Enter the limits of delta band frequencies for FFT (e.g. '2 4'): ").split()))
#     spikeDuration = int(input("Enter the spike duration on your recordings: "))
        
#     return params

# # Call the parameters function to set the global variables
# params = parameters()

##############################################################################

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

# Define empty arrays to store waveforms for each electrode
waveform_el_1 = []
waveform_el_2 = []
waveform_el_3 = []
waveform_el_4 = []

# Iterate over each waveform in the input data
for ii in range(waveforms.shape[0]):
    waveform_el_1.append(waveforms[ii, 0:125:4])
    waveform_el_2.append(waveforms[ii, 1:126:4])
    waveform_el_3.append(waveforms[ii, 2:127:4])
    waveform_el_4.append(waveforms[ii, 3:128:4])

# Calculate the mean waveform for each electrode 
average_waveform_el_1 = np.mean(waveform_el_1, axis=0)
average_waveform_el_2 = np.mean(waveform_el_2, axis=0)
average_waveform_el_3 = np.mean(waveform_el_3, axis=0)
average_waveform_el_4 = np.mean(waveform_el_4, axis=0)
# Combine the average waveforms for all four electrodes
average_all = np.vstack((average_waveform_el_1, average_waveform_el_2, average_waveform_el_3, average_waveform_el_4))


# Calculate the peak-to-peak values along the rows of the "average_all" array
y = np.ptp(average_all, axis=1)
# Find the index of the maximum peak-to-peak value
idx = np.argmax(y)
# Convert the flat index to row and column indices corresponding to the original shape of "average_all"
row, col = np.unravel_index(idx, average_all.shape)

# select samples corresponding to the chosen electrode
selected_el = []
for ii in range(waveforms.shape[0]): 
    selected_el.append(waveforms[ii, col:col+125:4]) 

# Compute mean and standard deviation of selected samples
average_selected_el = np.mean(selected_el, axis=0)  
std_selected_el = np.std(selected_el, axis=0) 
# compute values above and below the mean
std_plus_selected_el = average_selected_el + std_selected_el  
std_minus_selected_el = average_selected_el - std_selected_el  

 # convert to numpy array
selected_el = np.array(selected_el) 
# compute the derivative
derive_selected_el = np.zeros((selected_el.shape[0], 30))  
for iii in range(selected_el.shape[0]):  
    for iiii in range(30):  
        derive_selected_el[iii, iiii] = (selected_el[iii, iiii+1] - selected_el[iii, iiii]) / (1/32000)  

# compute mean and standard deviation of the derivative
average_derive_selected_el = np.mean(derive_selected_el, axis=0)  
std__derive_selected_el = np.std(derive_selected_el, axis=0)  
# compute values below and above the derivative mean
std_plus_derive_selected_el = average_derive_selected_el + std__derive_selected_el
std_minus_derive_selected_el = average_derive_selected_el - std__derive_selected_el 



# plot figure of the mean waveform
fig = plt.figure(dpi=300)  # create a new figure object
ax1 = fig.add_subplot(2, 2, 1)  # add a subplot to the figure in the upper-left position
ax1.set_title('Mean waveform')  # set the title of the subplot
ax1.plot(average_selected_el, linewidth=2, color='k')  # plot the average selected element
ax1.plot(std_plus_selected_el, '--', linewidth=2, color='k')  # plot the upper standard deviation
ax1.plot(std_minus_selected_el, '--', linewidth=2, color='k')  # plot the lower standard deviation
ax1.set_xticklabels(['0', '1'])  # set the x-tick labels
ax1.set_xlabel('msec')  # set the x-axis label
ax1.set_ylabel('µvolt')  # set the y-axis label
ax1.tick_params(direction='out', length=4, width=2)  # customize tick parameters
ax1.spines['top'].set_visible(False)  # remove the top spine
ax1.spines['right'].set_visible(False)  # remove the right spine
ax1.xaxis.set_ticks_position('bottom')  # set the x-axis ticks to the bottom
ax1.yaxis.set_ticks_position('left')  # set the y-axis ticks to the left
plt.show()  # show the figure

# plot figure of the mean derived waveform
fig = plt.figure(dpi=300)
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title('Mean derived waveform', fontsize=10)
ax2.plot(average_derive_selected_el, linewidth=2, color='k')
ax2.plot(std_plus_derive_selected_el, '--', linewidth=2, color='k')
ax2.plot(std_minus_derive_selected_el, '--', linewidth=2, color='k')
ax2.set_xticklabels([])
ax2.set_yticklabels([])
ax2.set_xticks([])
ax2.set_yticks([])
ax2.tick_params(direction='out', length=4, width=2)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
plt.xlim([0, recordingsamplingfrequency])
plt.show()

# # create the subplot
# ax3 = fig.add_subplot(2, 2, 3)

# # set the title and font size
# ax3.set_title('Phase plot', fontsize=12)

# # plot the horizontal line
# ax3.plot([0, 0], [-max(average_derive_selected_el), max(average_derive_selected_el)], linewidth=1, color='k')

# # plot the vertical line
# ax3.plot([-max(average_selected_el), max(average_selected_el)], [0, 0], linewidth=1, color='k')

# # plot the waveform data
# ax3.plot(average_selected_el[:3], average_derive_selected_el, linewidth=3, color='k')

# # set the aspect ratio to be square
# ax3.set_box_aspect(1)

# # normalize the data
# average_selected_el_v2 = average_selected_el / max(average_selected_el)
# average_derive_selected_el_v2 = average_derive_selected_el / max(average_derive_selected_el)

# # customize tick parameters
# ax3.tick_params(direction='out', length=4, width=2)
# ax3.set_xlabel('amplitudeXtime')
# ax3.set_ylabel('derived amplitudeXtime')

# # set the font size and line width
# ax3.tick_params(labelsize=18, width=4)

# # customize tick parameters
# ax3.tick_params(direction='out', length=4, width=2)
# ax3.spines['top'].set_visible(False)
# ax3.spines['right'].set_visible(False)
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(2, 2, 3)
# ax.set_title('Phase plot', fontsize=12)
# ax.plot([0, 0], [-(np.max(average_derive_selected_el)), np.max(average_derive_selected_el)], linewidth=1, color='k')
# ax.plot([-(np.max(average_selected_el)), np.max(average_selected_el)], [0, 0], linewidth=1, color='k')
# ax.plot(average_selected_el[:29], average_derive_selected_el[:29], linewidth=3, color='k')
# ax.axis('square')
# ax.set_xlabel('amplitudeXtime')
# ax.set_ylabel('derived amplitudeXtime')
# ax.tick_params(direction='out')
# h = plt.gca()
# h.tick_params(axis='both', which='both', direction='out', top=False, right=False, width=4, length=6)
# h.spines['top'].set_visible(False)
# h.spines['right'].set_visible(False)
# h.spines['bottom'].set_linewidth(4)
# h.spines['left'].set_linewidth(4)
# plt.show()


# Outputs

# waveform characteristics
mean_height_spike = np.max(average_selected_el) # maximum voltage of the spike
mean_amplitude_spike = abs(np.max(average_selected_el) - np.min(average_selected_el)) # amplitude (max-min) of the spike
# time of the spike between the peak and the trough
time_max = np.argmax(average_selected_el)
time_min = np.argmin(average_selected_el)
time_spike = [time_max, time_min]
mean_ptt = np.diff(time_spike) / recordingsamplingfrequency * 1000
CoefficientVariation = np.max(std_selected_el) / np.max(average_selected_el)
