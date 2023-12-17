from Ray import Ray
from Scene import Scene
from Camera import Camera
from numpy import pi,cos,sin
import numpy as np
from matplotlib import pyplot as plt

w=1920
h=1080

def main():
    scene = Scene()
    camera = Camera()
    aspectRatio = w/h
    FOV = camera.FOV
    thetaFOV = FOV / aspectRatio
    theta0 = camera.theta0
    phi0 = camera.phi0
    WIN = np.zeros([h,w,3],dtype = int)
    s = camera.s
    for i in range(w):
        phi = 0.5*(FOV*(1 - 2*i/(w-1))) + phi0
        for j in range(h):
            #print(i,j)
            theta = 0.5*(thetaFOV*(1 - 2*j/(h-1))) + theta0
            d = np.array([sin(theta)*cos(phi),sin(theta)*sin(phi),cos(theta)])
            #print(d)
            ray = Ray(s,d)
            ray.castOnScene(scene)
            WIN[-j][-i] = ray.color
    plt.imshow(WIN)
    plt.show()

if __name__ == '__main__':
    main()