import pygame

class StartLoop:

    def __init__(self):

        self.sprites = pygame.sprite.Group()

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