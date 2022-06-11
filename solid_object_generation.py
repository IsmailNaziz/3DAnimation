import math
import numpy as np
from geometry_utils import rotate

def torus_generation(radius, thickness, step=300):
    torus = []
    circle = circle_generation(radius, trans_x=thickness, trans_y=0, trans_z=0, step=100)

    # quarter of torus
    for theta in np.linspace(0, math.pi/4, num=step):
        for point in circle:
            torus.append(rotate(point, 'x', theta))

    # apply symmetry to avoid calculations






def circle_generation(radius, trans_x=0, trans_y=0, trans_z=0, step=100):
    '''
    equation of circle is:
    (x-a)²+(y-b)² = R > 0
    y = +- sqrt(R-(x-a)²)+b for x between -sqrt(R) + a and a-sqrt(R)
    Since I need 3D objects, I will add a third component set to 0
    :param radius:
    :param trans_x:
    :param trans_y:
    :param step:
    :return:
        set of numpy arrays
    '''
    assert radius > 0
    return [np.array((x, math.sqrt(radius - (x - trans_x) ** 2) + trans_y, trans_z))
            for x in np.linspace(trans_x - math.sqrt(radius), math.sqrt(radius) + trans_x, num=step)]

if __name__=='__main__':
    circle_points = circle_generation(4)
    print(circle_points)
