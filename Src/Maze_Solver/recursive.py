# System import(s)
import os, random

from numpy import array


class Recursive(object):

    # Initialization
    def __init__(self) -> None:
        self._maze_name = random.choice(os.listdir('./Unsolved/'))
        self._maze_path = './Unsolved/' + self._maze_name
        self._maze = []
        self._rows = 0
        self._columns = 0


    def __str__(self) -> str:
        return f'Maze name : {self._maze_name}, \
                Maze path : {self._maze_path}, \
                Maze : {self._maze}, \
                Rows : {self._rows}, \
                Columns : {self._columns}'


    def __repr__(self) -> str:
        return f'Recursive(\'{self._maze_name}\', \
                        {self._maze_path}\', \
                        {self._maze}\', \
                        {self._rows}\', \
                        {self._columns})'


    # Methods
    def get_maze(self):
        with open(self._maze_path, 'r') as f:
            mat = f.readlines()
            line = [element.split('\n')[0] for element in mat]
        maze = array(line)
        maze = [list(row) for row in maze]
        return maze


    def solve_maze(self, maze, row, col):
        if row == len(maze)-1 and col == len(maze[0])-1:
            maze[row][col] = 'o'
            return True
        if maze[row][col] == '#' or maze[row][col] == 'o':
            return False
        maze[row][col] = 'o'
        if col < len(maze[0])-1 and self.solve_maze(maze, row, col+1):
            return True
        if row < len(maze)-1 and self.solve_maze(maze, row+1, col):
            return True
        if col > 0 and self.solve_maze(maze, row, col-1):
            return True
        if row > 0 and self.solve_maze(maze, row-1, col):
            return True
        maze[row][col] = ' '
        return False


    def display_path(self):
        maze = self.get_maze()
        self.solve_maze(maze, 0, 0)
        for row in maze:
            print(''.join(row))