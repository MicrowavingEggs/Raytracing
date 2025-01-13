from Object import Object
import numpy as np
from numpy import dot,sqrt


class Sphere(Object):

    def __init__(self,c=np.array([5,-2,0]),r=2,color=np.array([219,122,147])):
        super().__init__()
        self.c = c
        self.r = r
        self.color = color
    
    def normal(self,y):
        n1 = y-self.c
        return n1/np.linalg.norm(n1)

    def findMint(self,ray):
        v = ray.s - self.c
        tempC = dot(v,v) - self.r*self.r
        tempA = (dot(v,ray.d))
        positiveT = [x for x in [-tempA + sqrt(tempA**2-tempC),-tempA - sqrt(tempA**2-tempC)] if x >=0]
        if len(positiveT)>0:
            t = min(positiveT)
        else:
            t = -1
        return (self,t)