##
## POEI Ausy Python
## Authors: Yoann Le Saint, Simon Tessier
## File description:
## maze class
##
import numpy as np
from numpy import array, shape
import os
import shutil

# path = os.getcwd()
# path_maps = "/".join(path.split("/")[:-1] + ["maps"])


# class Maze(object):
#
#     def __init__(self, _maze_folder, maze_name):
#         self._maze_folder = _maze_folder
#         self._maze_path = self._maze_folder + '\\' + maze_name+'.txt'
#
#         with open(self._maze_path, 'r') as f:
#             mat = f.readlines()
#             mat = [[lign[:-2]] for lign in mat]
#         self._maze = array(mat)
#
#         self._start = (0, 0)
#         self._end = shape(self._maze)
#
#
#     def print_maze(self):
#         print('print : ')
#         print(self._maze)
#
#     """
#     def find_in_and_out(self):
#         # find where is the start and the stop
#         start, end = 0, 0
#         for y, row in enumerate(self._maze):
#             if row[0] == " ":
#                 start = (0, y)
#             elif row[-1] == " ":
#                 end = (len(row) - 1, y)
#         return start, end
#     """
#
#     def len(self):
#         return len(self._maze), len(self._maze[0])
#
#     def solve(self):
#         return self.solve_recursive(self._start)
#
#     def solve_recursive(self, state):
#         print("test")
#         x, y = state
#         if state == self._end:
#             return True
#         if self._maze[x, y] != " ":
#             return False
#         self._maze[x] = self._maze[:x, y] + 'X' + self._maze[x+1:, y]
#         if (x > 0 and self.solve_recursive((x - 1, y))) \
#           or (x < len(self._maze[y]) - 1 and self.solve_recursive((x + 1, y))) \
#           or (y > 0 and self.solve_recursive((x, y - 1))) \
#           or (y < len(self._maze) - 1 and self.solve_recursive((x, y + 1))):
#             return True
#         return False
#
#
#     def move(self, new_path):
#         # ajout commande SQL
#         shutil.move(self._maze_path, new_path)



class Maze:
    def __init__(self, _maze_folder, maze_name):
        self._maze_folder = _maze_folder
        self._maze_path = self._maze_folder + '\\' + maze_name + '.txt'

        with open(self._maze_path, 'r') as f:
            mat = f.readlines()
            mat = [ [element.split('\n')[0] for element in mat] ]
        self._maze = array(mat)

        self._start = (0, 0)
        self._end = (shape(self._maze)[0]-1, shape(self._maze)[1]-1)
        print(shape(self._maze))
        self.visited = np.zeros(shape(self._maze)).astype(bool)
        self.path = []

    def get_neighbors(self, x, y):
        neighbors = []
        if x > 0 and not self.visited[x-1, y] and self._maze[x-1, y] != "#":
            neighbors.append((x-1, y))
        if x < self._maze.shape[0]-1 and not self.visited[x+1, y] and self._maze[x+1, y] != "#":
            neighbors.append((x+1, y))
        if y > 0 and not self.visited[x, y-1] and self._maze[x, y-1] != "#":
            neighbors.append((x, y-1))
        if y < self._maze.shape[1]-1 and not self.visited[x, y+1] and self._maze[x, y+1] != "#":
            neighbors.append((x, y+1))
        return neighbors

    def solve_maze(self): #start_x, start_y, end_x, end_y
        start_x, start_y = self._start
        end_x, end_y = self._end
        print(self._start, self._end)
        print(start_x, start_y, end_x, end_y )
        stack = [(start_x, start_y)]
        while stack:
            x, y = stack.pop()
            self.visited[x, y] = True
            if x == end_x and y == end_y:
                self.path.append((x, y))
                return True
            neighbors = self.get_neighbors(x, y)
            for neighbor_x, neighbor_y in neighbors:
                stack.append((neighbor_x, neighbor_y))
                self.path.append((neighbor_x, neighbor_y))
        return False

    def __str__(self):
        output = ""
        for y in range(self._maze.shape[0]):
            for x in range(self._maze.shape[1]):
                if (x, y) == self.path[0]:
                    output += "S"
                elif (x, y) == self.path[-1]:
                    output += "E"
                elif self._maze[x][y] == "#":
                    output += "#"
                elif (x, y) in self.path:
                    output += "."
                else:
                    output += " "
            output += "\n"
        return output

    def move(self, new_path):
        # ajout commande SQL
        shutil.move(self._maze_path, new_path)

    def print_maze(self):
        print('print : ')
        print(self._maze)