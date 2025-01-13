from Sphere import Sphere
from Polygon import Polygon
from Light import Light
import numpy as np
class Scene():

    def __init__(self,objects=[
    Sphere(),
    Sphere(c=np.array([5, 3, 2]), r=2, color=np.array([0, 128, 255])),
    Sphere(c=np.array([7, 5, -2]), r=1, color=np.array([255, 255, 255])),
    Sphere(c=np.array([8, 0, 0]), r=2, color=np.array([0, 255, 0])),
    Sphere(c=np.array([7.55457654, 7.08104308, -1.19281201]), r=1.171805924426327, color=np.array([35, 139, 54])),
    Sphere(c=np.array([9.65685299, 7.51508785, 3.26232795]), r=1.755150547057609, color=np.array([28, 246, 47])),
    Sphere(c=np.array([9.83105223, 2.20616802, 3.79248051]), r=1.6151119839515407, color=np.array([159, 211, 195])),
    Sphere(c=np.array([7.47992893, 1.8257776, -2.85305855]), r=1.3097642505405878, color=np.array([166, 87, 109])),
    Sphere(c=np.array([7.90955786, 9.91461659, -1.23915584]), r=0.5670396018341637, color=np.array([24, 145, 97])),
    Sphere(c=np.array([8.29448998, 3.05350395, -0.09953937]), r=0.9315007207064034, color=np.array([33, 30, 232])),
    Sphere(c=np.array([7.02145206, 0.6990432, 3.59612266]), r=1.0889575796907573, color=np.array([181, 20, 127])),
    Sphere(c=np.array([6.08869314, 7.5358072, -3.47348471]), r=1.5621337278498775, color=np.array([135, 157, 120])),
    Sphere(c=np.array([5.69094411, 8.46937182, 3.16704599]), r=1.9413221130754557, color=np.array([64, 160, 117])),
    Sphere(c=np.array([5.75521049, 3.64522134, -3.10945815]), r=1.0107992909329568, color=np.array([227, 131, 3])),
    Sphere(c=np.array([9.25583776, 9.82285154, -2.1359573]), r=0.8825851095809457, color=np.array([30, 19, 17])),
    Sphere(c=np.array([8.74071539, 6.82132293, -3.62958628]), r=0.8462676063470801, color=np.array([156, 233, 230])),
    Sphere(c=np.array([6.64016753, 5.95369452, 0.30159025]), r=0.6331138198373455, color=np.array([17, 125, 198])),
    Sphere(c=np.array([8.18419778, 3.81227721, 2.41537845]), r=0.5456753966995124, color=np.array([146, 123, 231])),
    Sphere(c=np.array([9.70804726, 4.75005779, 1.08006504]), r=0.9730658047948653, color=np.array([219, 103, 55])),
    Sphere(c=np.array([9.85360545, 2.21542649, -0.89015952]), r=0.7557651871870379, color=np.array([236, 39, 51])),
    Sphere(c=np.array([6.26538782, 5.35302613, 3.52353165]), r=0.6303031798860937, color=np.array([206, 136, 87])),
    Sphere(c=np.array([7.38730011, 6.16026157, 3.02787253]), r=0.5053940692060378, color=np.array([201, 81, 237])),
    Sphere(c=np.array([8.68093373, 9.54944372, 0.36108259]), r=0.8784350944774415, color=np.array([56, 34, 12])),
    Sphere(c=np.array([9.90827393, 4.94853094, -1.80999628]), r=0.6839935279304445, color=np.array([12, 207, 114])),
    Sphere(c=np.array([5.17819548, 0.23325768, 0.26416572]), r=0.5713117112385555, color=np.array([43, 216, 12])),
    Sphere(c=np.array([6.22984107, 3.74005658, -1.04247887]), r=0.6813107152246105, color=np.array([39, 103, 120])),
    Sphere(c=np.array([9.84399491, 5.09223856, -3.94081497]), r=0.6017404623949096, color=np.array([175, 176, 70])),
    Sphere(c=np.array([5.45813008, 0.49479058, -3.96324996]), r=0.5341136844546084, color=np.array([221, 103, 154])),
    Sphere(c=np.array([6.31170642, 9.67805568, 0.20814029]), r=0.504091078216011, color=np.array([124, 152, 42])),
    Sphere(c=np.array([8.2545984, 5.46098298, 0.14135786]), r=0.597000126941479, color=np.array([97, 210, 103])),
    Sphere(c=np.array([8.96009941, 8.41531961, -1.17762897]), r=0.7112494353457695, color=np.array([111, 157, 223])),
    Sphere(c=np.array([5.58719827, 7.0573376, 0.45526242]), r=0.6464772878282374, color=np.array([29, 171, 108])),
    Sphere(c=np.array([7.10168196, 4.54734395, 0.27019968]), r=0.5216670178831908, color=np.array([158, 30, 117])),
    Sphere(c=np.array([9.72353128, 1.71752023, -3.13669246]), r=0.566810115453227, color=np.array([76, 152, 115])),
    Sphere(c=np.array([9.21605615, 7.05565563, 0.25451076]), r=0.5142380882668306, color=np.array([51, 167, 201])),
    Sphere(c=np.array([8.08183501, 6.31450529, 1.52431085]), r=0.8433519572525714, color=np.array([100, 91, 11])),
    Sphere(c=np.array([7.46072774, 3.94720815, -3.32007123]), r=0.6486471834948206, color=np.array([90, 137, 82])),
    Sphere(c=np.array([8.35913687, 9.48472424, -3.83557372]), r=0.6481772342272569, color=np.array([15, 154, 188])),
    Sphere(c=np.array([9.66114804, 4.56894346, 3.81108707]), r=0.7439170139607552, color=np.array([40, 19, 136])),
    Sphere(c=np.array([9.52950746, 3.27441408, -2.56569972]), r=0.768495437053564, color=np.array([152, 247, 62])),
    Sphere(c=np.array([6.98325143, 8.48013987, 0.47616399]), r=0.7711373018171122, color=np.array([249, 210, 91])),
    Sphere(c=np.array([6.25695339, 9.93002913, 1.28154123]), r=0.5081714286643966, color=np.array([240, 87, 199])),
    Sphere(c=np.array([5.53543905, 2.85435171, -1.2447306]), r=0.503888820303257, color=np.array([225, 78, 57])),
    Sphere(c=np.array([7.65951025, 1.53580385, -2.72198295]), r=0.6214789030038505, color=np.array([155, 176, 139])),
    Sphere(c=np.array([8.00247496, 4.11201391, -1.26149189]), r=0.7208305408496457, color=np.array([127, 185, 229])),
    Sphere(c=np.array([8.91433235, 8.31955485, -1.6160527]), r=0.797299673197578, color=np.array([11, 133, 51])),
    Sphere(c=np.array([9.02483639, 3.07512341, 0.94292417]), r=0.7048566617920492, color=np.array([76, 97, 88])),
    Sphere(c=np.array([5.69092915, 7.54867356, -3.87895827]), r=0.8069536681294878, color=np.array([170, 80, 136])),
    Sphere(c=np.array([9.35519991, 7.47319966, 1.12806561]), r=0.9329227927930188, color=np.array([187, 214, 187])),
    Sphere(c=np.array([6.98819126, 7.41539013, -3.65988907]), r=0.7511036312981873, color=np.array([14, 89, 104])),
    Polygon(x1=np.array([0,-2,1]),x2=np.array([2,3,2]),x3=np.array([2,0,1.5])),
    Polygon(x1=np.array([5,-2,0]),x2=np.array([-3,3,2]),x3=np.array([7,0,-2])),
    Polygon(x1=np.array([1,1,1]),x2=np.array([1,2,1]),x3=np.array([2,2,1])),
    Polygon(x1=np.array([1,1,1]),x2=np.array([1,2,2]),x3=np.array([2,2,1]))]
    #Polygon(x1=np.array([0,0,-2]),x2=np.array([10,10,-2]),x3=np.array([0,10,-2])),
    #Polygon(x1=np.array([10,-4,-2]),x2=np.array([10,8,-2]),x3=np.array([10,8,4])),
    ,light=Light()):
        self.objects = objects
        self.light = light


#[Sphere(),Sphere(c=np.array([5,3,2]),r=2,color=np.array([0,128,255])),Sphere(c=np.array([7,5,-2]),r=1,color=np.array([255,255,255])),Sphere(c=np.array([8,0,0]),r=2,color=np.array([0,255,0]))]