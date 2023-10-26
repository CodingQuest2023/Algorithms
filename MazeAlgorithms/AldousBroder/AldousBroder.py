from aldous_broder_maze import AldousBroderMaze
from maze_drawer import MazeDrawer


INTERACTIVE = True
COLS = 8
ROWS = 5

maze = AldousBroderMaze(COLS, ROWS)
maze_drawer = MazeDrawer(maze, INTERACTIVE)

if INTERACTIVE:
    maze.generate_interactive(maze_drawer)
else:
    maze.generate()

maze_drawer.draw()
