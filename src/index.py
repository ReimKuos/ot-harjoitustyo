import pygame
from random import randint
from classes.player import Player
from classes.enemies import Sharp
from ui.master_ui import UI
from mainloop import MainLoop

def main():

    pygame.init()

    ui = UI(500,500)
    mainloop = MainLoop(ui)
    mainloop.start()

    pygame.quit()

if __name__ == "__main__":
    main()
