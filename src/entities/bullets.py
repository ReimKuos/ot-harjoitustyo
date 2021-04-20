""""has the class bullet that works whit the player"""
import pygame

class StandardBullet(pygame.sprite.Sprite):
    """A standart bullet that works whit the player, travels forward and destroys enemies"""

    def __init__(self, x_position: int, y_position: int, added_speed: int):

        super().__init__()

        self.image = pygame.image.load(
            "data/sprites/Bullet_MK1.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.move_ip(x_position-1, y_position-1)

        self.lifetime = 40
        self.velocity = 20 - added_speed

    def update(self):
        """
        updates the bullets position using it's speed and decrements it's lifetime
        if life time is 0 it kills the bullet
        """

        self.lifetime -= 1
        self.rect.move_ip(0, -self.velocity)

        if self.lifetime <= 0:
            self.kill()
