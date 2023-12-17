from numpy import dot,sqrt
import numpy as np


class Ray():

    def __init__(self,s,d,color=np.zeros(3,dtype=int)):
        self.s = s
        self.d = d
        self.color = color

    def findMint(self,obj):
        v = self.s - obj.c
        tempC = dot(v,v) - obj.r*obj.r
        tempA = (dot(v,self.d))
        positiveT = [x for x in [-tempA + sqrt(tempA**2-tempC),-tempA - sqrt(tempA**2-tempC)] if x >=0]
        if len(positiveT)>0:
            t = min(positiveT)
        else:
            t = -1
        return (obj,t)

    def castOnScene(self,Scene):
        shininess = 16
        #while self.remainingReflection > 0:
        objT = [(obj,t) for (obj,t) in [self.findMint(obj) for obj in Scene.objects] if t>=0]
        #print(objT)
        if len(objT) == 0:
            self.color = np.zeros(3)
        else:
            obj,t = min(objT,key = lambda x:x[1])
            if t < 0:
                self.color = np.zeros(3)
            else:
                y = self.s + t*self.d
                n = obj.normal(y)#return the normalVect at y on the surface of the obj
                r = self.d - 2*dot(n,self.d)*n
                self.color = np.round((1-obj.reflectionFactor)*obj.color*max(0,dot(n,-Scene.light.d)) + obj.reflectionFactor*Scene.light.color*max(0,dot(r,self.d))**shininess).astype(int)