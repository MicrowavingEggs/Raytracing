from Object import Object
import numpy as np
from numpy import dot,sqrt


class Polygon(Object):

    def __init__(self,x1=np.array([-1,-4,0]),x2=np.array([-3,3,4]),x3=np.array([7,5,-4]),color=np.array([255,255,255])):
        super().__init__()
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.color = color
    
    def normal(self,y=np.array([0,0,0])):
        n1 = np.cross(self.x2 - self.x1, self.x3 - self.x1)
        return n1/np.linalg.norm(n1)
    
    def findMint(self,ray):
        Otr = self.x1 - ray.s
        n = np.cross(self.x2 - self.x1, self.x3 - self.x1)
        invnormalisor = 1/np.dot(n,ray.d)
        t = -np.dot(n,Otr)*invnormalisor
        Iu = np.dot(np.cross(Otr,(self.x3-self.x1)),ray.d)*invnormalisor
        Iv = np.dot(np.cross((self.x2-self.x1),Otr),ray.d)*invnormalisor
        #print(Iu,Iv,t)
        if ((Iu >=0) and (Iu <= 1) and (Iv >=0) and (Iv <= 1) and (t >= 0) and ((Iu + Iv) <=1)):
            #print("collision with polygon")
            return (self,t)            
        else:
            return (self,-1)