import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):

    def __init__(self, sprite: str, x: int, y: int):
        super().__init__()

        self.image = pygame.image.load(f"data/sprites/{sprite}").convert_alpha()
        self.rect = self.image.get_rect()

        self.width = self.rect[2]
        self.length = self.rect[3]

        self.rect.move_ip(x - self.width//2, y - self.length//2)

        self.lifetime = randint(200,1000)

    def update(self):

        self.lifetime -= 1
        
        if self.lifetime <= 0:
            self.kill()


class Sharp(Enemy):

    def __init__(self, x: int, y: int):
        super().__init__("ShipSpriteLeft.png", x, y)

        





if __name__ == "__main__":
    pass