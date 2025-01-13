from numpy import pi
import numpy as np

class Camera():

    def __init__(self,s=np.array([0,0,0]),FOV=2*pi,phi0=pi,theta0=3*pi/2):
        self.s = s
        self.FOV = FOV
        self.phi0 = phi0
        self.theta0 = theta0