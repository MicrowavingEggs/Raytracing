from Sphere import Sphere
from Light import Light
class Scene():

    def __init__(self,objects=[Sphere()],light=Light()):
        self.objects = objects
        self.light = light