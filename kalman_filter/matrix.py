import math
from math import sqrt
import numbers

def zeroes(height, width):
    grid = [[0.0 for _ in range(width)] for __ in range(height)]

    return Matrix(grid)

def identity(n):
    I = zeroes(n, n)

    for i in range(n):
        I.g[i][i] = 1.0
    
    return I

def dot(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Can not compute the dot product if 2 vectors have different size")
    
    return sum([x*y for x, y in zip(v1, v2)])

class Matrix(object):

    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])