##
## POEI Ausy Python
## Authors: Yoann Le Saint, Simon Tessier
## File description:
## maze class
##

from numpy import array
import os

path = os.getcwd()
path_maps = "/".join(path.split("/")[:-1] + ["maps"])

# print(path)
# print(path.split("/"))
# print(path.split("/")[:-1] + ["maps"])
# print("/".join(path.split("/")[:-1] + ["maps"]))
# print(path_maps)


class Maze(object):

    def __init__(self, maze_name):
        self._maze_path = "/".join(path.split("/")[:-1] + ["maps"])
        self._maze = self.load_maze(self._maze_path, maze_name)


    def print_maze(self):
        print(self._maze)


    def load_maze(self, maze_name):
        maze = self._maze_path + '/' + maze_name
        with open(maze, 'r') as f:
            mat = f.readlines()
            mat = [[lign[:-2]] for lign in mat]
        self._maze = array(mat)

    def len(self):
        return len(self._maze), len(self._maze[0])


    def right(self):
        lenght = self.len()
        start = [0,1]
        # 4 -> impossible                #
        # 3 -> demi-tour               # o #
        # 2 -> donne la direction        #
        # 1 -> tourner a droite
        self.next_step(x, y)

    def next_step(self, x, y, prev_x, prev_y):
        new_x, new_y = x, y
        # look neighbors
        neighbors = self._maze[x, y-1]=='#' + self._maze[x-1, y]=='#' + \
                    self._maze[x+1, y]=='#' + self._maze[x, y+1]=='#'
        match neighbors:
            case 1:
                # turn right
                pass
            case 2:
                # follow the direction
                if self._maze[]
                pass
            case 3:
                # u-turn
                # if   self._maze[x, y-1] != '#':
                #     new_x, new_y = x, y-1
                # elif self._maze[x, y+1] != '#':
                #     new_x, new_y = x, y+1
                # elif self._maze[x+1, y] != '#':
                #     new_x, new_y = x+1, y
                # elif self._maze[x-1, y] != '#':
                #     new_x, new_y = x-1, y
                new_x, new_y   = prev_x, prev_y
                prev_x, prev_y = x, y
            case _:
                raise(ValueError)
        return new_x, new_y, prev_x, prev_y