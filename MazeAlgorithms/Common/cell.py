import random


CELL_NORTH = 1
CELL_EAST  = 2
CELL_SOUTH = 3
CELL_WEST  = 4


class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.links = []
        self.neighbours = dict()


    def add_neighbour(self, direction, cell):
        self.neighbours[direction] = cell


    def get_neighbour(self, direction):
        if direction in self.neighbours:
            return self.neighbours[direction]
        else:
            return None


    def get_random_neighbour(self):
        cell_list = list(self.neighbours.values())
        return random.choice(cell_list)


    def get_all_neighbours(self):
        return list(self.neighbours.values())


    def link(self, cell):
        self.links.append(cell)
        cell.links.append(self)


    def get_number_links(self):
        return len(self.links)
