import random
from cell import *


class Maze:

    def __init__(self, cols, rows):
        self.num_rows = rows
        self.num_cols = cols

        self.cell_rows = []
        for y in range(rows):
            cells = []
            for x in range(cols):
                cell = Cell(x, y)
                cells.append(cell)
            self.cell_rows.append(cells)

        for y in range(rows):
            for x in range(cols):
                cell = self.cell_rows[y][x]
                if x > 0:
                    cell.add_neighbour(CELL_WEST, self.cell_rows[y][x - 1])
                if x < cols - 1:
                    cell.add_neighbour(CELL_EAST, self.cell_rows[y][x + 1])
                if y > 0:
                    cell.add_neighbour(CELL_NORTH, self.cell_rows[y - 1][x])
                if y < rows - 1:
                    cell.add_neighbour(CELL_SOUTH, self.cell_rows[y + 1][x])


    def get_all_cells(self, start_from_top_row):
        if start_from_top_row:
            rows = self.cell_rows
        else:
            rows = reversed(self.cell_rows)
            
        for row in rows:
            for cell in row:
                yield cell


    def get_random_cell(self):
        x = random.randint(0, self.num_cols - 1)
        y = random.randint(0, self.num_rows - 1)
        return self.cell_rows[y][x]


    def get_number_cells(self):
        return self.num_rows * self.num_cols
