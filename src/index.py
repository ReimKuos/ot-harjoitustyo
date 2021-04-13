import pygame
from random import randint
from entities.bullets import StandardBullet
from entities.player import Player
from entities.enemies import Sharp
from ui.master_ui import UI
from ui.text_sprite import TextSprite
from mainloop import MainLoop
from gameloop import GameLoop
from startloop import StartLoop

def main():

    pygame.init()

    ui = UI(500,500)
    mainloop = MainLoop(ui)
    mainloop.start()

    pygame.quit()

if __name__ == "__main__":
    main()
