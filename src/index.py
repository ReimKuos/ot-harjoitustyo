""""the main module, constructs the game"""
import pygame
from ui.master_ui import UI
from database_init import database_init
from mainloop import MainLoop


def main():
    """
    The main function that creates and calls the mainloop
    """
    database_init()
    pygame.init()

    user_interface = UI(512, 800)
    mainloop = MainLoop(user_interface)
    mainloop.start()

    pygame.quit()


if __name__ == "__main__":
    main()
