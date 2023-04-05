# System import(s)
import os
import random
import shutil

from numpy import array

# Local import(s)


class Recursive(object):

    # Initialization
    def __init__(self) -> None:
        if not os.listdir("./Unsolved/"):
            self._maze_name = "empty"
        else:
            self._maze_name = random.choice(os.listdir("./Unsolved/"))
        self._maze_path = "./Unsolved/" + self._maze_name
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


    def write_solution(self):
        with open(self._maze_path, 'w') as file:
            for row in self._maze:
                for c in row:
                    file.write(c)
                file.write('\n')

    def move_maze(self):
        if not os.path.exists("./Solved/" + self._maze_name):
            shutil.move(self._maze_path, "./Solved/")
        else:
            os.remove(self._maze_path)
            print("\nMaze is already solved, so I deleted it in the 'Unsoved' directory :)")


    def display_path(self):
        if (self._maze_name != "empty"):
            maze = self.get_maze()
            self._maze = maze
            self.solve_maze(maze, 0, 0)
            for row in maze:
                print(''.join(row))
            self.write_solution()
            self.move_maze()
        else:
            print("\nThere is no maze. Generate some first :)")
