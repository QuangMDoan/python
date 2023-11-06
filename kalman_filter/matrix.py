import math
from math import sqrt
import numbers

def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    grid = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(grid)

def identity(n):
    """
    Creates a n x n identity matrix.
    """    
    I = zeroes(n, n)

    for i in range(n):
        I.g[i][i] = 1.0
    
    return I

def dot(v1, v2):
    """
    Compute the dot product of the two vectors 
    """
    if len(v1) != len(v2):
        raise ValueError("Can not compute the dot product if 2 vectors have different size")
    
    return sum([x*y for x, y in zip(v1, v2)])

class Matrix(object):

    def __init__(self, grid):
        """
        Construct a matrix given a list of list of values
        """
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

   # Primary matrix math methods 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise ValueError("Cannot calculate determinant of a non square matrix")
        if self.h > 2:
            raise NotImplementedError("Calculating determinant not implemented for nmatrices larger than 2x2")
        
        if self.h == 1:
            return self.g[0][0]
        
        return self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries)
        """
        if not self.is_square():
            raise ValueError("Cannot calculate the trace of a non-square matrix")
        
        return sum(self.g[i][i] for i in range(self.h))

    def inverse(self):
        """
        Calulates the inverse of a 1x1 or 2x2 matrix
        """
        if not self.is_square():
            raise ValueError("Non-square Matrix does not have an inverse")
        if self.h > 2:
            raise NotImplementedError("inversion not implemented for matrices larger than 2x2")
        
        M = None
        if self.h == 1:
            if self.g[0][0] == 0:
                raise ValueError("Matrix does not have an inverse")
            x = 1.0/self.g[0][0]
            M = Matrix([[x]])
        else:
            det = self.determinant()
            if det == 0:
                raise ValueError("Matrix does not have an inverse")
            mult = 1.0/det
            B = self.trace()*identity
            C = B - self
            M = mult * C
        
        return M
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        B = []
        for j in range(self.w):
            column = [self.g[i][j] for i in range(self.h)]
            B.append(column)
        
        return Matrix(B)
    
    def is_square(self):
        return self.h == self.w
    
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.
        """
        return self.g[idx]
    
    def __repr__(self):
        s = ""
        for row in self.g:
            s+= " ". join([f"{v:6.2f}" for v in row]) +"\n"
        return s
    
    def __add__(self, other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise ValueError("Matrices can only be added if the dimensions are the same")
        
        grid = [
            [self.g[i][j] + other.g[i][j] for j in range(self.w)] for i in range(self.h)
        ]

        return Matrix(grid)
    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)
        """
        return Matrix([[-n for x in row] for row in self.g])

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        return self + -other
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """

        if self.w != other.h:
            raise ValueError("Matrices can only be multiplied if the dimensions are matched")
        
        A = self.g
        B = other.T().g

        grid = [[dot(a, b) for b in B] for a in A]
        return Matrix(grid)

    def __rmul__(self,other):
        """
        Called when the thing on the left of the * is not a matrix.
        """
        if not  isinstance(other, numbers.Number):
            raise ValueError("Argument must be a scalar")
        
        grid = [[other*x for x in row] for row in self.g]
        return Matrix(grid)

