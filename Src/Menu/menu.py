from sys import exit

# from Generation.generator import Generator
# from Recursive.maze import Maze
# from Save.save import Backup

class Menu(object):

    def __init__(self) -> None:
        self._option = 0
        self._lenght_generation = 0
        self._width_generation = 0

    def __str__(self) -> str:
        return f'The option is {self._option}'

    def __repr__(self) -> str:
        return f'Menu(\'{self._option})'

    def display_menu(self) -> None:
         print("\nMENU :\n"
               "---------------------------\n"
               "1 : Diplay all solved mazes\n"
               "2 : Load random maze\n"
               "3 : Generate new maze\n"
               "4 : Exit\n"
               "---------------------------\n"
               "Your Choice : ", end = '')

    def launch_game(self):
        self.display_menu()
        while (True):
            self._option = input()
            match self._option:
                case '1':
                    # Backup.display_data()
                    self.launch_game()
                case '2':
                    # Maze.solve_recursive()
                    self.launch_game()
                case '3':
                    # Generator.generate_maze()
                    self.launch_game()
                case '4':
                    print("Bye !")
                    exit(0)
                case _:
                    print("Please choose a valid option :)")
                    self.display_menu()

