import numpy as np

def colormapc(*varargin):
    nargin = len(varargin)
    if nargin == 0:
        T = 1
        N = 256
    elif nargin == 1:
        T = varargin[0]
        N = 256
    elif nargin == 2:
        T = varargin[0]
        N = varargin[1]
    else:
        raise ValueError('Too many parameters.')
    
    Y = np.zeros((N, 3))
    
    def cmapc(N, *colors):
        if len(colors) < 2:
            raise ValueError('Too few inputs.')
        C = np.vstack((colors, colors[0]))

        Y = np.zeros((N, 3))
        ls = 0
        r = N / (C.shape[0] - 1) # Length of each color transition.
        for i in range(C.shape[0] - 1):
            li = ls
            ls = round((i + 1) * r)
            d = ls - li + 1
            Y[li:ls, :] = np.transpose([np.linspace(C[i,0], C[i+1,0], d),
                                         np.linspace(C[i,1], C[i+1,1], d),
                                         np.linspace(C[i,2], C[i+1,2], d)])
        return Y

    if T == 1:
        Y = cmapc(N, [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0])
    elif T == 2:
        Y = cmapc(N, [0, 1, 1], [0, 0, 1], [1, 0, 1])
    elif T == 3:
        Y = cmapc(N, [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0])
    elif T == 4:
        Y = cmapc(N, [0, 0, 0], [1, 0, 0], [1, 1, 0])
    elif T == 5:
        Y = cmapc(N, [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0])
    elif T == 6:
        Y = cmapc(N, [0, 0, 1], [1, 0, 0])
    elif T == 7:
        Y = cmapc(N, [0, 0, 0], [0, 0, 0])
    else:
        raise ValueError('Unknown colormap type.')

    return Y
