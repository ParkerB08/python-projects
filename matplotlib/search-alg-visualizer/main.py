import matplotlib as plt
import numpy as np
import random

# recursive backtracking algorithm to randomly generate a maze 
def maze_creation(width, height):

    grid = np.array([[0 for i in range(width)] for i in range(height)]) # 2d grid of zeros

    n, s, e, w = 1, 2, 4, 8 # bit values for direction

    dx = {n: 0, s: 0, e: 1, w: -1} 
    dy = {n: -1, s: 1, e: 0, w: 0}
    d_opp = {n: s, e: w, s: n, w: e}

    def passage_creation_from(cx, cy):

        directions = [n, s, e, w] # list of bit values
        random.shuffle(directions) # randomize

        for direction in directions:

            ny, nx = cy + dy[direction], cx + dx[direction] # neighbor cells

            if (ny in range(0, len(grid))) and (nx in range(0, len(grid))) and (grid[ny][nx] == 0): # if cell is valid

                grid[cy][cx] |= direction # bitwise or to add directional values to current cell
                grid[ny][nx] |= d_opp[direction] # add opposite value to neighbor cell

                passage_creation_from(nx, ny) # recursively check and and values until maze is complete

    passage_creation_from(0, 0)

    # convert to ascii for debugging
    print(" " + "_" * (width * 2 - 1)) # north border

    for y in range(height):

        print("|", end = "") # west border
        
        for x in range(width):

            if grid[y][x] & s != 0:
                print(" ", end = "")
            else:
                print("_", end = "")

            if grid[y][x] & e != 0:
                if (grid[y][x] | grid[y][x + 1]) & s != 0:
                    print(" ", end = "")
                else:
                    print("_", end = "")
            else:
                print("|", end = "")

        print()

maze = maze_creation(10, 10)

