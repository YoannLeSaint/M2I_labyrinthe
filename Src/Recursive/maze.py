##
## POEI Ausy Python
## Authors: Yoann Le Saint, Simon Tessier
## File description:
## maze class
##

from numpy import array, shape
import os
import shutil

path = os.getcwd()
path_maps = "/".join(path.split("/")[:-1] + ["maps"])


class Maze(object):

    def __init__(self, maze_name):
        self._maze_folder = "\\".join(path.split("\\") + ["maps"])
        self._maze_path = self._maze_folder + '\\' + maze_name

        with open(self._maze_path, 'r') as f:
            mat = f.readlines()
            mat = [[lign[:-2]] for lign in mat]
        self._maze = array(mat)

        self.start = (0, 0)
        self.end = shape(self._maze)


    def print_maze(self):
        print('print : ')
        print(self._maze)

    """
    def find_in_and_out(self):
        # find where is the start and the stop
        start, end = 0, 0
        for y, row in enumerate(self._maze):
            if row[0] == " ":
                start = (0, y)
            elif row[-1] == " ":
                end = (len(row) - 1, y)
        return start, end
    """

    def len(self):
        return len(self._maze), len(self._maze[0])

    def solve(self):
        return self.solve_recursive(self.start)

    def solve_recursive(self, state):
        x, y = state
        if state == self.end:
            return True
        if self._maze[x, y] != " ":
            return False
        self._maze[y] = self._maze[:x, y] + 'X' + self._maze[x+1:, y]
        if (x > 0 and self.solve_recursive((x - 1, y))) \
            or (x < len(self._maze[y]) - 1 and self.solve_recursive((x + 1, y))) \
            or (y > 0 and self.solve_recursive((x, y - 1))) \
            or (y < len(self._maze) - 1 and self.solve_recursive((x, y + 1))):
            return True
        return False


    def move(self, new_path):
        # ajout commande SQL
        shutil.move(self._maze_path, new_path)