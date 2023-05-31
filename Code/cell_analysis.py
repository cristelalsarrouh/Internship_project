from posdata import *
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

# Define global variables
tetrode = None
cell = None
binWidth = None
smooth_factor = None
TimeWindow = None
Tbin = None
threshold = None
binSizeDir = None
correction = None

# Load the data
mat = loadmat('C:/Users/cristel_alsarrouh/Documents/recordings.mat/Zmoth_03032020_S1-01.mat')

def parameters():
    # prompt the user for input
    global tetrode, cell, binWidth, smooth_factor, TimeWindow, Tbin, threshold, binSizeDir, correction
    
    tetrode = input("Enter the tetrode number (leave blank for all cells): ")
    cell = input("Enter the cell number (leave blank if tetrode is not specified or for all cells): ")
    if tetrode == "":
       tetrode = None
    else:
       tetrode = int(tetrode)
    if cell == "":
       cell = None
    else:
       cell = int(cell)
    binWidth = int(input("Enter the bin width for ratemaps: "))
    smooth_factor = int(input("Enter the smoothing factor for ratemap: "))
    TimeWindow = int(input("Enter the length of time autocorrelogram (in msec): "))
    Tbin = int(input("Enter the bin size of autocorrelogram (in msec): "))
    threshold = int(input("Enter the threshold for path correction: "))
    binSizeDir = int(input("Enter the binning size for polar plot (choose 5, 6, or 10): "))
    correction = int(input("Enter the angle shift of LEDs position on the animal head: "))

   # print out the input parameters
    params = {
        "tetrode": tetrode,
        "cell": cell,
        "binWidth": binWidth,
        "smooth_factor": smooth_factor,
        "TimeWindow": TimeWindow,
        "Tbin": Tbin,
        "threshold": threshold,
        "binSizeDir": binSizeDir,
        "correction": correction
    }
    for key, value in params.items():
        print(f"{key}: {value}")
        
    return params

# Call the parameters function to set the global variables
params = parameters()

# Load the data
mat = loadmat('C:/Users/cristel_alsarrouh/Documents/recordings.mat/Zmoth_03032020_S1-01.mat')
# Extract the relevant positions from PosMtx and remove any rows with zero values
TTMtx = mat['TTMtx']
# print(TTMtx)

if tetrode:  # check if tetrode is not None or empty
    TTMtx2 = TTMtx[TTMtx[:, 1] == tetrode, :]  # extract rows where the 2nd column matches tetrode
    p = tetrode  # set p to the value of tetrode
    
    # call the posdata function with four arguments and unpack the result into variables
    # posx, posy, posts, posgx, posgy, posrx, posry, mapAxis, visited = posdata(PosMtx, threshold, shape, binWidth)
    
    cells = cell  # set cells to the value of cell
    
    # extract the first column of TTMtx2 where the third column matches cells
    ts = TTMtx2[TTMtx2[:, 3] == cells, 0]
    
    # extract columns 4 through 131 of TTMtx2 where the third column matches cells
    waveforms = TTMtx2[TTMtx2[:, 3] == cells, 4:131]
    
    i = cells  # set i to the value of cells

print (ts)
#     # Create a new figure and hide it
#     zztop = plt.figure(figsize=(10,10))
#     zztop.set_visible(False)

#     # Call the celldata2 function and assign the returned values to variables
#     freq_peak_distr, ret, beta, f0, Grid_score, peak, Vector_length, peak_HD, dirrate, deg_theta, posdirts, ratemap = celldata2(waveforms, ts, posx, posy, posts, visited, smooth_factor, binWidth, mapAxis, PosMtx, posgx, posgy, posrx, posry, threshold, correction, binSizeDir, TimeWindow, Tbin)

#     # Set the figure size to the size of the screen
#     zztopManager = plt.get_current_fig_manager()
#     zztopManager.window.showMaximized()

#     # Save the figure if save_figure is True
#     if save_figure == 1:
#         complete_name = pathfigure + inputfile[:-4] + '_t' + str(p) + '_c' + str(i) + '.png'
#         plt.savefig(complete_name, dpi=600)

#     # Close the figure if close_figure is True
#     if close_figure == 1:
#         plt.close(zztop)

# else:
#     # define a list of unique tetrodes from the TTMtx matrix
#     tetrodes = np.unique(TTMtx[:,1])

#     # loop through each tetrode in the list
#     for p in range(len(tetrodes)):
    
#         # extract rows from TTMtx that correspond to the current tetrode
#         TTMtx2 = TTMtx[TTMtx[:,2] == tetrodes[p],:]
    
#         # remove any rows with a zero value in the third column
#         TTMtx2[TTMtx2[:,2] == 0,:] = []
    
#         # call the posdata function to get positional data
#         posx,posy,posts,posgx,posgy,posrx,posry,mapAxis,visited = posdata(PosMtx, threshold, shape, binWidth)
    
#         # define a list of unique cells in the current tetrode
#         cells = unique(TTMtx2[:,3])
    
#         # if there are cells in the list
#         if not cells:
#             # loop through each cell in the list
#             for i in range(len(cells)):
            
#                 # extract spike times and waveforms for the current cell
#                 ts = TTMtx2[TTMtx2[:,3] == cells[i],1]
#                 waveforms = TTMtx2[TTMtx2[:,3] == cells[i],4:131]
            
#                 # call the celldata2 function to get cell data and plot results
#                 celldata2(waveforms,ts,posx,posy,posts,visited,smooth_factor,binWidth,mapAxis,PosMtx,threshold,TimeWindow,Tbin,shape)
            
#                 # create a figure and save it if desired
#                 zztop = figure('visible', 'off')
#                 if save_figure == 1:
#                     complete_name = pathfigure + inputfile[:-4] + '_t' + str(tetrodes[p]) + '_c' + str(cells[i])
#                     print('-dpng',complete_name,'-r200')
            
#                 # close the figure if desired
#                 if close_figure == 1:
#                     close(zztop)
