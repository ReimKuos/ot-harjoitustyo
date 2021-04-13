import pygame
from random import randint
from classes.player import Player
from classes.enemies import Sharp
from ui.master_ui import UI
from mainloop import MainLoop

def main():

    pygame.init()

    sprites = pygame.sprite.Group()

    ui = UI(960,810)

    player = Player()
    enemy = Sharp(100,100)
    sprites.add([player,enemy])

    mainloop = MainLoop(ui,sprites)

    mainloop.start()

    pygame.quit()

if __name__ == "__main__":
    main()
