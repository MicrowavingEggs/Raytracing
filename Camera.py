from numpy import pi
import numpy as np

class Camera():

    def __init__(self,s=np.array([-0.5,0,1]),FOV=2*pi/3,phi0=0,theta0=pi/2):
        self.s = s
        self.FOV = FOV
        self.phi0 = phi0
        self.theta0 = theta0