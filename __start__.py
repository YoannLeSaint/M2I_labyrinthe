# System import(s)
import signal

# Local import(s)
from Src.Menu.menu import Menu


def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C, Bye !')
    exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    game = Menu()
    game.launch_game()


if __name__ == "__main__":
    main()