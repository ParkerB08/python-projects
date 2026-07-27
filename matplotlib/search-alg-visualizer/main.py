import matplotlib as plt
import numpy as np
import random

# recursive backtracking algorithm to randomly generate a maze 
def maze_creation(width, height):

    grid = np.array([[0 for i in range(width)] for i in range(height)])

    n, s, e, w = 1, 2, 4, 8 

    dx = {n: 0, s: 0, e: 1, w: -1}
    dy = {n: 1, s: -1, e: 0, w: 0}
    d_opp = {n: s, e: w, s: n, w: e}

    def passage_creation_from(cx, cy, grid):

        directions = [n, s, e, w]   
        random.shuffle(directions)

        for direction in directions:

            ny, nx = cy + dy[direction], cx + dx[direction]

            if (ny in range(0, len(grid) - 1)) and (nx in range(0, len(grid) - 1)) and (grid[ny][nx] == 0):

                grid[cy][cx] |= direction
                grid[ny][nx] |= d_opp[direction]

                passage_creation_from(cy, cx, grid)

    passage_creation_from(0, 0, grid)


maze = maze_creation(100, 100)

