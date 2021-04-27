"""this contains the bullet class used by the enemy sharp"""
import pygame


class SharpBullet(pygame.sprite.Sprite):
    """
    A bullet that kills the player if it collides with it,
    has standart speed and can move in all directions
    """

    def __init__(self, x_pos: int, y_pos: int, x_speed: int, y_speed: int):
        super().__init__()

        self.image = pygame.image.load(
            "data/sprites/Bullet_MK1.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.move_ip(x_pos - self.rect[2]//2, y_pos - self.rect[3]//2)

        self.x_speed = x_speed
        self.y_speed = y_speed

        self.points = 0
        self.lifetime = 100

    def update(self):
        """
        the update method of the class, moves the object based on it's speeds and
        decrements it's lifetime, kills the sprite when lifetime runs out
        """
        if self.y_speed < 0:
            self.kill()
        self.rect.move_ip(self.x_speed, self.y_speed)
        self.lifetime -= 1
