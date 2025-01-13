import numpy as np

class Light():

    def __init__(self,p=np.array([0,0,1]),d=np.array([3/np.sqrt(19),-1/np.sqrt(19),-3/np.sqrt(19)]),color = np.array([255,255,255])):
        self.p = p
        self.d = d
        self.color = color