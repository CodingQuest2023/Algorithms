import pygame
from maze import Maze
from cell import *


WINDOW_WIDTH    = 1920
WINDOW_HEIGHT   = 1080
CELLSIZE        = 96       # cell width/height in pixels in tilesheet
SCALE_FACTOR    = 2
CELLSIZE_SCALED = CELLSIZE * SCALE_FACTOR


class MazeDrawer:

    def __init__(self, maze, interactive):
        self.maze = maze
        pygame.init()
        # open window
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # load tile sheet, and extract the cell images
        self.tilesheet = pygame.image.load("../../Assets/SpriteSheets/MazeTileSet/MazeTileset.png").convert_alpha()
        self.cell_images = []
        for y in range(4):
            for x in range(4):
                rect = (128 * x, 128 * y, CELLSIZE, CELLSIZE)
                image = self.tilesheet.subsurface(rect)
                image = pygame.transform.scale_by(image, (SCALE_FACTOR, SCALE_FACTOR))
                self.cell_images.append(image)
        image = self.tilesheet.subsurface((512, 128, 16, 16))
        self.wizard_image = pygame.transform.scale_by(image, (SCALE_FACTOR, SCALE_FACTOR))
        # draw the outside walls around the maze
        self.draw_background()
        # center the maze
        self.maze_offset_x = (WINDOW_WIDTH - self.maze.num_cols * CELLSIZE_SCALED) // 2
        self.maze_offset_y = (WINDOW_HEIGHT - self.maze.num_rows * CELLSIZE_SCALED) // 2

        self.visited_cells = []
        self.highlight_surface = pygame.Surface((CELLSIZE_SCALED, CELLSIZE_SCALED))
        self.highlight_surface.set_alpha(50)
        self.highlight_surface.fill("yellow")
        self.darken_surface = pygame.Surface((CELLSIZE_SCALED, CELLSIZE_SCALED))
        self.darken_surface.set_alpha(100)
        self.darken_surface.fill("black")
        self.interactive = interactive


    def draw(self, select_cell = None, visit = True):
        self.draw_cells(select_cell, visit)
        pygame.display.flip()
        self.wait_key()
        

    def wait_key(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                break


    def draw_cells(self, select_cell = None, visit = True):
        for cell in self.maze.get_all_cells(False):
            # Check which cell walls need to be drawn
            hasWallNorth = False
            hasWallSouth = False
            hasWallWest  = False
            hasWallEast  = False

            if CELL_WEST not in cell.neighbours:
                hasWallWest = True
            elif cell.neighbours[CELL_WEST] not in cell.links:
                hasWallWest = True

            if CELL_NORTH not in cell.neighbours:
                hasWallNorth = True
            elif cell.neighbours[CELL_NORTH] not in cell.links:
                hasWallNorth = True

            if CELL_EAST not in cell.neighbours:
                hasWallEast = True
            elif cell.neighbours[CELL_EAST] not in cell.links:
                hasWallEast = True

            if CELL_SOUTH not in cell.neighbours:
                hasWallSouth = True
            elif cell.neighbours[CELL_SOUTH] not in cell.links:
                hasWallSouth = True

            # x,y coords of the cell in pixels
            x = cell.x * CELLSIZE_SCALED
            y = cell.y * CELLSIZE_SCALED

            # find the correct image for the cell
            index = 0
            if hasWallEast:  index += 1
            if hasWallWest:  index += 2
            if hasWallSouth: index += 4
            if hasWallNorth: index += 8
            self.display_surface.blit(self.cell_images[index], (x + self.maze_offset_x, y + self.maze_offset_y))

            # highlight the selected cell, and draw wizard in this cell
            if cell == select_cell:
                if visit:
                    self.visited_cells.append(cell)
                self.display_surface.blit(self.highlight_surface, (x + self.maze_offset_x, y + self.maze_offset_y))
                self.display_surface.blit(self.wizard_image, (x + self.maze_offset_x + CELLSIZE_SCALED // 2, y + self.maze_offset_y  + CELLSIZE_SCALED // 2))

            # make unvisited cells darker
            if cell not in self.visited_cells and self.interactive:
                self.display_surface.blit(self.darken_surface, (x + self.maze_offset_x, y + self.maze_offset_y))


    def draw_background(self):
        image = self.tilesheet.subsurface((512, 0, CELLSIZE, CELLSIZE))
        image = pygame.transform.scale_by(image, (SCALE_FACTOR, SCALE_FACTOR))
        for y in range(WINDOW_HEIGHT // CELLSIZE_SCALED + 1):
            for x in range(WINDOW_WIDTH // CELLSIZE_SCALED + 1):
                self.display_surface.blit(image, (x * CELLSIZE_SCALED, y * CELLSIZE_SCALED))
