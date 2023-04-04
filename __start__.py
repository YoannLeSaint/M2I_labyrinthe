import signal

from Src.Menu.menu import Menu
# from Src.Recursive.maze import Maze
# import os
# path = os.getcwd()
# path_maze =  "\\".join(path.split("\\") + ["Unsolved"])
# print(path_maze)

def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C, Bye !')
    exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    game = Menu()
    game.launch_game()
    # m1 = Maze(path_maze, 'maze_1.txt')
    # m1.print_maze()
    # m1.solve_maze()
    # print(m1)




if __name__ == "__main__":
    main()