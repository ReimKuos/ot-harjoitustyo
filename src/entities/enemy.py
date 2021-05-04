from random import randint
import pygame


class Enemy(pygame.sprite.Sprite):
    """
    basic enemy class, doesn't do anything but works as a parent class for other enemies
    """

    def __init__(self, x_pos: int, y_pos: int, sprite: str):
        """
        constructor creates a new follower entity

        Args:
            x_pos: the horizontal postion of the entity
            y_pos: the vertical position of the entity
            sprite: sprite configured often by the child class
        """
        super().__init__()

        self.image = pygame.image.load(
            f"data/sprites/{sprite}.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.width = self.rect[2]
        self.length = self.rect[3]

        self.rect.move_ip(x_pos - self.width//2, y_pos - self.length//2)

        self.x_speed = randint(-3, 3)
        self.y_speed = randint(-3, 3)

        self.shoot_cooldown = randint(60, 200)
