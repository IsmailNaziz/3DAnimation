import math
import numpy as np


def translate(axis, distance):
    return


def rotate(point, axis, angle):
    cos = math.cos(angle)
    sin = math.sin(angle)
    rotation_matrixs = \
        {'x': np.array([[1, 0, 0], [0, cos, -1 * sin], [0, sin, cos]]),
         'y': np.array([[cos, 0, sin], [0, 1, 0], [-1 * sin, 0, cos]]),
         'z': np.array([[cos, -1 * sin, 0], [sin, cos, 0], [0, 0, 1]])}
    if axis not in rotation_matrixs.keys():
        raise ValueError('Provide a correct axis')
    else:
        rotation_matrix = rotation_matrixs[axis]
        return np.dot(rotation_matrix, point)


def change_basis(point, matrix):
    return


def matrix_shift(direction, num=1):
    '''
    (1,2,9) must be shifted to (9,1,2) for a shift to right and num=1
    :param num: how many shift
    :param direction: shift to left or right
    :return:
    '''
    return
