from binary_tree_maze import BinaryTreeMaze
from maze_drawer import MazeDrawer


INTERACTIVE = True
COLS = 8
ROWS = 5

maze = BinaryTreeMaze(COLS, ROWS)
maze_drawer = MazeDrawer(maze, INTERACTIVE)

if INTERACTIVE:
    maze.generate_interactive(maze_drawer)
else:
    maze.generate()

maze_drawer.draw()
