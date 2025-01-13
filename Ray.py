from numpy import dot,sqrt
import numpy as np
from numba import jit, njit


class Ray():

    def __init__(self,s,d,color=np.zeros(3,dtype=int),remainingReflection=5):
        self.s = s
        self.d = d
        self.color = color
        self.remainingReflection = remainingReflection

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
        if self.remainingReflection >= 0:
            objT = [(obj,t) for (obj,t) in [obj.findMint(self) for obj in Scene.objects] if t>=0]
        #print(objT)
        if len(objT) == 0:
            self.color = (Scene.light.color*max(0,dot(self.d,-Scene.light.d))**shininess).astype(int)#self.color = np.zeros(3)
            
        else:
            obj,t = min(objT,key = lambda x:x[1])
            if abs(t) <= 0.01:
                self.color = (Scene.light.color*max(0,dot(self.d,-Scene.light.d))**shininess).astype(int)#self.color = np.zeros(3)
            else:
                y = self.s + 0.99*t*self.d
                n = obj.normal(y)#return the normalVect at y on the surface of the obj
                r = self.d - 2*dot(n,self.d)*n
                r = r/np.linalg.norm(r)
                nextRay = Ray(y,r,remainingReflection = self.remainingReflection-1)
                if self.remainingReflection == 0:
                    self.color =  np.round((1-obj.reflectionFactor)*obj.color*max(0,dot(r,-Scene.light.d)) + obj.reflectionFactor*Scene.light.color*max(0,dot(r,-Scene.light.d))**shininess).astype(int)
                else:
                    nextRay.castOnScene(Scene)
                    self.color = np.round((1-obj.reflectionFactor)*obj.color*max(0,dot(r,-Scene.light.d)) + obj.reflectionFactor*nextRay.color).astype(int) #Replace max(0,dot(r,-Scene.light.d) by 0 if r intersects item before light... (shadows...)