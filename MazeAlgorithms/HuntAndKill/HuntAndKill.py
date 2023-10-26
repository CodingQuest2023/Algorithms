from hunt_and_kill_maze import HuntAndKillMaze
from maze_drawer import MazeDrawer


INTERACTIVE = True
COLS = 8
ROWS = 5

maze = HuntAndKillMaze(COLS, ROWS)
maze_drawer = MazeDrawer(maze, INTERACTIVE)

if INTERACTIVE:
    maze.generate_interactive(maze_drawer)
else:
    maze.generate()

maze_drawer.draw()

