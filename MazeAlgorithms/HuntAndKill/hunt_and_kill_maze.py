import random
from cell import Cell
from maze import Maze


class HuntAndKillMaze(Maze):

    def __init__(self, cols, rows):
        super().__init__(cols, rows)


    # Hunt and kill maze generation algorithm
    def generate_interactive(self, maze_drawer):
        maze_drawer.draw()
        current_cell = self.get_random_cell()

        while current_cell != None:
            maze_drawer.draw(current_cell)
            
            neighbours = current_cell.get_all_neighbours()
            unvisited_neighbours = []
            for neighbour in neighbours:
                if neighbour.get_number_links() == 0:
                    unvisited_neighbours.append(neighbour)
                    
            if len(unvisited_neighbours) > 0:
                neighbour = random.choice(unvisited_neighbours)
                current_cell.link(neighbour)
                current_cell = neighbour
            else:
                current_cell = None
                for cell in self.get_all_cells(start_from_top_row = True):
                    maze_drawer.draw(cell, visit=False)
                    if cell.get_number_links() == 0:
                        neighbours = cell.get_all_neighbours()
                        visited_neighbours = []
                        for neighbour in neighbours:
                            if neighbour.get_number_links() != 0:
                                visited_neighbours.append(neighbour)
                    
                        if len(visited_neighbours) > 0:
                            current_cell = cell
                            neighbour = random.choice(visited_neighbours)
                            current_cell.link(neighbour)
                            break


    # Hunt and kill generation algorithm
    def generate(self):
        current_cell = self.get_random_cell()

        while current_cell != None:
            neighbours = current_cell.get_all_neighbours()
            unvisited_neighbours = []
            for neighbour in neighbours:
                if neighbour.get_number_links() == 0:
                    unvisited_neighbours.append(neighbour)
                    
            if len(unvisited_neighbours) > 0:
                neighbour = random.choice(unvisited_neighbours)
                current_cell.link(neighbour)
                current_cell = neighbour
            else:
                current_cell = None
                for cell in self.get_all_cells(start_from_top_row = True):
                    if cell.get_number_links() == 0:
                        neighbours = cell.get_all_neighbours()
                        visited_neighbours = []
                        for neighbour in neighbours:
                            if neighbour.get_number_links() != 0:
                                visited_neighbours.append(neighbour)
                    
                        if len(visited_neighbours) > 0:
                            current_cell = cell
                            neighbour = random.choice(visited_neighbours)
                            current_cell.link(neighbour)
                            break
