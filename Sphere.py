from Object import Object
import numpy as np


class Sphere(Object):

    def __init__(self,c=np.array([5,0,0]),r=2,color=np.array([219,122,147])):
        super().__init__()
        self.c = c
        self.r = r
        self.color = color
    
    def normal(self,y):
        n1 = y-self.c
        return n1/np.linalg.norm(n1)