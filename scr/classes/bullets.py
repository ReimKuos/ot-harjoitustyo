import pygame

class StandardBullet(pygame.sprite.Sprite):

    def __init__(self, x_position: int, y_position: int, added_speed: int):
       
        super().__init__()

        self.lifetime = 70
        self.velocity = 5 + added_speed
        self.x_pos = x_position
        self.y_pos = y_position


    def update(self):
        
        self.lifetime -= 1
        self.y_pos += self.velocity