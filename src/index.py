""""the main module, constructs the game"""
import pygame
from ui.master_ui import UI
from mainloop import MainLoop

# IDK why pygame throws an error so a disapled no-member in pylint,
# this applies to other methods aswell
# The error is given when direct pygame functions or values are called


def main():
    """
    The main function that creates and calls the mainloop
    """

    pygame.init()

    user_interface = UI(512, 800)
    mainloop = MainLoop(user_interface)
    mainloop.start()

    pygame.quit()


if __name__ == "__main__":
    main()
