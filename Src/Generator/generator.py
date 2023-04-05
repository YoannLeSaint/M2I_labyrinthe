# System import(s)
import random
import shutil

# Local import(s)


class Generator(object):

    # Initialization
    def __init__(self) -> None:
        self._txt_name = ""
        self._maze = ""


    def __str__(self) -> str:
        return f'Maze name : {self._txt_name}, \
                Maze : {self._maze}'


    def __repr__(self) -> str:
        return f'Generator(\'{self._txt_name}\', \
                        {self._maze})'


    # Methods
    def generate_maze(self):
        width = random.randint(3, 100)
        height = random.randint(2, 100)
        maze = [['#']*width for _ in range(height)]
        start = (1, 1)
        end = (height-2, width-2)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = [start]

        while stack:
            current = stack[-1]
            maze[current[0]][current[1]] = ' '
            neighbors = []
            for d in directions:
                neighbor = (current[0] + d[0]*2, current[1] + d[1]*2)
                if 0 < neighbor[0] < height-1 and 0 < neighbor[1] < width-1 \
                    and maze[neighbor[0]][neighbor[1]] == '#':
                    neighbors.append(neighbor)
            if neighbors:
                neighbor = random.choice(neighbors)
                maze[current[0] + (neighbor[0]-current[0])//2][current[1] + \
                    (neighbor[1]-current[1])//2] = ' '
                stack.append(neighbor)
            else:
                stack.pop()

        maze[start[0]][start[1]] = ' '
        maze[end[0]][end[1]] = ' '
        maze[0][0] = ' '
        maze[0][1] = ' '
        maze[1][0] = ' '
        maze[1][1] = ' '
        maze[-2][-2] = ' '
        maze[-1][-2] = ' '
        maze[-2][-1] = ' '
        maze[-1][-1] = ' '
        maze_str = '\n'.join([''.join(row) for row in maze])
        self._maze = maze_str


    def create_maze_txt(self, id_txt):
        self._txt_name = "maze_" + str(id_txt) + ".txt"
        print("\n{} created !".format(self._txt_name))


    def generator(self, id_txt):
        self.generate_maze()
        self.create_maze_txt(id_txt)
        with open(self._txt_name, 'w') as file:
            file.write(self._maze)
        shutil.move(("./" + self._txt_name), './Unsolved/')

