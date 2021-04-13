import pygame
from entities.player import Player

class GameLoop:

    def __init__(self):

        self.sprites = pygame.sprite.Group()

        self.sprites.add(Player())

        
    def increment(self):

        self.sprites.update()

    def get_sprites(self):

        return self.sprites