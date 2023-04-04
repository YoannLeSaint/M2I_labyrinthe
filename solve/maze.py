##
## POEI Ausy Python
## Authors: Yoann Le Saint, Simon Tessier
## File description:
## maze class
##

from numpy import chararray, array
import os

path = os.getcwd()
path_maps = "/".join(path.split("/")[:-1] + ["maps"])

print(path)
print(path.split("/"))
print(path.split("/")[:-1] + ["maps"])
print("/".join(path.split("/")[:-1] + ["maps"]))
print(path_maps)


class Maze(object):

    def __init__(self, path_maps, maze_name):
        self._maze = self.load_maze(path_maps, maze_name)


    def print_maze(self):
        print("print")
        print(self._maze)


    def load_maze(self, path_maps, name, display=True):
        if display:
            print("maze load ...")
        maze = path_maps+'/'+name
        with open(maze, 'r') as f:
            mat = f.readlines()
            mat = [[lign[:-2]] for lign in mat]
        self._maze = array(mat)


# test
# print(path)
# print("yes {}", path_maps)
# m = Maze(path_maps, 'maze_1.txt')
# m.print_maze()
