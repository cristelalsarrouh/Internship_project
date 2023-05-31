from scipy.io import loadmat
import numpy as np


# Load the data
# mat = loadmat('C:/Users/cristel_alsarrouh/Documents/recordings.mat/Zmoth_03032020_S1-01.mat')
mat = loadmat('C:/Users/cristel_alsarrouh/Desktop/Un_20092022_S1_bis_r1_r2-01')

# Extract the relevant positions from PosMtx and remove any rows with zero values
PosMtx = mat['PosMtx']
PosMtx = PosMtx[PosMtx[:, 1] != 0, :] 
PosMtx = PosMtx[PosMtx[:, 2] != 0, :] 

# Define a function to extract the x, y, and timestamps from PosMtx
def extract_position(PosMtx):
    posx = PosMtx[:, 1]
    posy = PosMtx[:, 2]
    posts = PosMtx[:, 0]  # timestamps are in the first column of every other row
    
    return posx, posy, posts

# Define a function to get the positions of the green, red, and IR LEDs
def get_led_positions(PosMtx):
    posx = PosMtx[:, 1]
    posy = PosMtx[:, 2]
    posgx = PosMtx[:, 1]  # green LED x positions
    posgy = PosMtx[:, 2]  # green LED y positions
    posrx = PosMtx[:, 3]  # red LED x positions
    posry = PosMtx[:, 4]  # red LED y positions
    
    # Check if the first value of posrx is 0 and update posrx and posry
    if posrx[0] == 0:
        posrx = np.roll(posgx, -1, axis=0)
        posry = np.roll(posgy, -1, axis=0)
    
    return posx, posy, posgx, posgy, posrx, posry

def smooth_path(posx, posy):
    posx = posx.tolist()  # Convert input array to list
    posy = posy.tolist()  # Convert input array to list
    span = 14
    
    for cc in range(int(span/2+1), len(posx)-int(span/2)):
        posx[cc] = np.mean(posx[cc-int(span/2):cc+int(span/2)])
        posy[cc] = np.mean(posy[cc-int(span/2):cc+int(span/2)])
        
    return posx, posy

def center_path(posx, posy):
    # Define the corners of the reference box
    maxX = max(posx)
    minX = min(posx)
    maxY = max(posy)
    minY = min(posy)
    NE = [maxX, maxY]
    NW = [minX, maxY]
    SW = [minX, minY]
    SE = [maxX, minY]

    # Find the center of the path
    a = (NE[1] - SW[1]) / (NE[0] - SW[0])  # Slope for the NE-SW diagonal
    b = (SE[1] - NW[1]) / (SE[0] - NW[0])  # Slope for the SE-NW diagonal
    c = SW[1]
    d = NW[1]
    x = (d - c + a * SW[0] - b * NW[0]) / (a - b)  # X-coord of center
    y = a * (x - SW[0]) + c  # Y-coord of center
    center = [x, y]

    # Set all coordinates relative to the center
    posx = posx - center[0]
    posy = posy - center[1]

    return center, posx, posy

binWidth = 3.5

# Define mapaxis function
def mapaxis(posx, posy, binWidth):
    # get the length of the recorded map (the real length is 150cm).
    obsSLength = max(max(posx)-min(posx), max(posy)-min(posy))
    # gets the N bins in x y axis of the map
    bins = np.ceil(obsSLength / binWidth)
    # calculate the corrected length
    sLength = binWidth * bins
    # set map axis
    mapAxis = np.arange(-sLength/2-binWidth/2, sLength/2+binWidth/2, binWidth)
    
    return mapAxis

# This function calculates what area of the map has been visited by the rat
def visited_bins(posx, posy, mapAxis):

    # Number of bins in each direction of the map
    N = len(mapAxis)
    visited = np.zeros((N, N))

    for ii in range(N):
        for jj in range(N):
            px = mapAxis[ii]
            py = mapAxis[jj]
            distance = np.sqrt((px - posx)**2 + (py - posy)**2)

            if np.min(distance) <= 3:
                visited[jj, ii] = 1

    return visited


# Call the functions to extract the positions of interest
posx, posy, posts = extract_position(PosMtx)
posx, posy, posgx, posgy, posrx, posry = get_led_positions(PosMtx)
posx, posy = smooth_path(posx, posy)
center, posx, posy = center_path(posx, posy)
mapAxis = mapaxis(posx, posy, binWidth)
visited = visited_bins(posx, posy, mapAxis)

