import random

def generate_maze(width, height):
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
            if 0 < neighbor[0] < height-1 and 0 < neighbor[1] < width-1 and maze[neighbor[0]][neighbor[1]] == '#':
                neighbors.append(neighbor)
        if neighbors:
            neighbor = random.choice(neighbors)
            maze[current[0] + (neighbor[0]-current[0])//2][current[1] + (neighbor[1]-current[1])//2] = ' '
            stack.append(neighbor)
        else:
            stack.pop()

    maze[start[0]][start[1]] = ' '
    maze[end[0]][end[1]] = ' '

    maze_str = '\n'.join([''.join(row) for row in maze])
    return maze_str


maze = generate_maze(23, 11)
print(maze)