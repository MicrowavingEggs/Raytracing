from Sphere import Sphere
from Light import Light
import numpy as np
class Scene():

    def __init__(self,objects=[Sphere(),Sphere(c=np.array([5,0,3]),r=1.5,color=np.array([0,128,255]))],light=Light()):
        self.objects = objects
        self.light = light