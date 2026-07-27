import matplotlib as plt
import numpy as np
import random

# recursive backtracking algorithm to randomly generate a maze 
def maze_creation(width, height):

    grid = np.array([[0 for i in range(width)] for i in range(height)])

    dx = {"e": 1, "w": -1 }
    dy = {"n": 1, "s": -1 }
    d_opp = {"n": "s", "e": "w", "s": "n", "w": "e"}

    def passage_creation_from(cx, cy, grid):
        directions = ["n", "e", "s", "w"]
        random.shuffle(directions)