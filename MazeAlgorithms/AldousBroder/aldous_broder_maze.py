import random
from cell import Cell
from maze import Maze


class AldousBroderMaze(Maze):

    def __init__(self, cols, rows):
        super().__init__(cols, rows)


    # Aldous-Broder maze generation algorithm
    def generate_interactive(self, maze_drawer):
        maze_drawer.draw()
        cell = self.get_random_cell()
        unvisited = self.get_number_cells() - 1
        maze_drawer.draw(cell)

        while unvisited > 0:
            neighbour = cell.get_random_neighbour()
            if neighbour.get_number_links() == 0:
                cell.link(neighbour)
                unvisited -= 1

            cell = neighbour
            maze_drawer.draw(cell)


    # Aldous-Broder maze generation algorithm
    def generate(self):
        cell = self.get_random_cell()
        unvisited = self.get_number_cells() - 1

        while unvisited > 0:
            neighbour = cell.get_random_neighbour()
            if neighbour.get_number_links() == 0:
                cell.link(neighbour)
                unvisited -= 1

            cell = neighbour
