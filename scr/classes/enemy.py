import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/goodscreen.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        pass


if __name__ == "__main__":
    pass