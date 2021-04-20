import pygame
from random import randint


class UI:

    def __init__(self, width: int, height: int):

        self.display = pygame.display.set_mode((width, height))
        self.stars = [(randint(0, width), randint(0, height), 2, 2)
                      for _ in range(400)]

    def render(self, sprites: pygame.sprite.Group):

        self.display.fill((0, 0, 0))
        for star in self.stars:
            pygame.draw.rect(self.display, (200, 200, 200), star)
        sprites.draw(self.display)
        pygame.display.update()
