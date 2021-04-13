import pygame
from random import randint

class StandardBullet(pygame.sprite.Sprite):

    def __init__(self, x_position: int, y_position: int, added_speed: int):
       
        super().__init__()

        self.image = pygame.image.load("data/sprites/Bullet_MK1.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.move_ip(x_position-1,y_position-1)

        self.lifetime = randint(30,40)
        self.velocity = added_speed + randint(3,7)


    def update(self):
        
        self.lifetime -= 1
        self.rect.move_ip(0,-self.velocity)

        if self.lifetime <= 0:
            self.kill()