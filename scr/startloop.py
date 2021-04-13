import pygame
from classes.text_sprite import TextSprite

class StartLoop:

    def __init__(self):

        self.sprites = pygame.sprite.Group()

        self.sprites.add(TextSprite(250,200,"data/sprites/Start_sprite_placeholder.png"),
                         TextSprite(250,250,"data/sprites/Score_sprite_placeholder.png"),
                         TextSprite(250,300,"data/sprites/Exit_sprite_placeholder.png"))

    def increment(self):

        pass

    def get_events(self):

        pass

    def get_sprites(self):
        
        return self.sprites


if __name__ == "__main__":

    pygame.init()

    screen = pygame.display.set_mode((300,300))
    screen.fill((10,10,10))

    mep = StartLoop()
    mep.get_sprites()

    pygame.quit()