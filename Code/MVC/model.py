from scipy.io import loadmat


class Model():

    def read_file(self, filename):
        # Load the data

        # mat = loadmat('C:/Users/cristel_alsarrouh/Documents/recordings.mat/Zmoth_03032020_S1-01.mat')

        mat = loadmat(filename)