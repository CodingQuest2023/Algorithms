import random
from cell import *
from maze import Maze


class BinaryTreeMaze(Maze):

    def __init__(self, cols, rows):
        super().__init__(cols, rows)


    # Binary tree maze generation algorithm
    def generate_interactive(self, maze_drawer):

        maze_drawer.draw()

        for cell in self.get_all_cells(start_from_top_row = False):
            neighbours = []
 
            maze_drawer.draw(cell)

            neighbour = cell.get_neighbour(CELL_NORTH)
            if neighbour:
                neighbours.append(neighbour)

            neighbour = cell.get_neighbour(CELL_EAST)
            if neighbour:
                neighbours.append(neighbour)

            if len(neighbours) > 0:
                neighbour = random.choice(neighbours)
                cell.link(neighbour)


    # Binary tree maze generation algorithm
    def generate(self):
        for cell in self.get_all_cells(start_from_top_row = False):
            neighbours = []

            neighbour = cell.get_neighbour(CELL_NORTH)
            if neighbour:
                neighbours.append(neighbour)

            neighbour = cell.get_neighbour(CELL_EAST)
            if neighbour:
                neighbours.append(neighbour)

            if len(neighbours) > 0:
                neighbour = random.choice(neighbours)
                cell.link(neighbour)
