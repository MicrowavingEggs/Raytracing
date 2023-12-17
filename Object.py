import numpy as np

class Object():

    def __init__(self,p=np.zeros(0),reflectionFactor=0.3):
        self.p = p
        self.reflectionFactor = reflectionFactor