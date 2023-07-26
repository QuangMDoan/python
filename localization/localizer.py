# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    beliefs = [ [1./area for _ in range(width)] for _ in range(height)]    
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    hits = [[(color == x) for x in row] for row in grid]
    multipliers = [[hit*p_hit + (1-hit)*p_miss for hit in row] for row in hits]

    new_beliefs = [ [multiplier * beliefs[i][j] for j, multiplier in enumerate(row)] for i, row in enumerate(multipliers)]

    total = sum([sum(row) for row in new_beliefs])
    new_beliefs = [[x/total for x in row] for row in new_beliefs]
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for y, row in enumerate(beliefs):
        for x, cell in enumerate(row):
            new_i = (y + dy ) % width
            new_j = (x + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
