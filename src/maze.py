##
## POEI Ausy Python
## Authors: Yoann Le Saint, Simon Tessier
## File description:
## maze class
##

from numpy import array, shape
import os

path = os.getcwd()
path_maps = "/".join(path.split("/")[:-1] + ["maps"])


class Maze(object):

    def __init__(self, maze_name):
        self._maze_path = "\\".join(path.split("\\") + ["maps"])

        maze = self._maze_path + '\\' + maze_name
        with open(maze, 'r') as f:
            mat = f.readlines()
            mat = [[lign[:-2]] for lign in mat]
        self._maze = array(mat)

        self.start = (0, 0)
        self.end   = shape(self._maze)


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


    def solve_recursive(self, state):
        x, y = state
        if state == self.end:
            return True
        elif self._maze[x, y] != " ":
            return False
        elif (x > 0 and self)

    # def solve(self):
    #     return self._solve_recursive(self.start)
    #
    # def _solve_recursive(self, current):
    #     x, y = current
    #     if current == self.end:
    #         return True
    #     if self.map_data[y][x] != " ":
    #         return False
    #     self.map_data[y] = self.map_data[y][:x] + "." + self.map_data[y][x + 1:]
    #     if (x > 0 and self._solve_recursive((x - 1, y))) \
    #             or (x < len(self.map_data[y]) - 1 and self._solve_recursive((x + 1, y))) \
    #             or (y > 0 and self._solve_recursive((x, y - 1))) \
    #             or (y < len(self.map_data) - 1 and self._solve_recursive((x, y + 1))):
    #         return True
    #     return False



    @property
    def maze(self):
        return self._maze