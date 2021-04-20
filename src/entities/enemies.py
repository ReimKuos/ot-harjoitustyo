"""module that has enemy classes"""
from random import randint
import pygame

class Enemy(pygame.sprite.Sprite):
    """a parent class for all enemies, has the basic things all enemies need"""

    def __init__(self, sprite: str, x_pos: int, y_pos: int):
        super().__init__()

        self._points = 0

        self.image = pygame.image.load(
            f"data/sprites/{sprite}").convert_alpha()
        self.rect = self.image.get_rect()

        self.width = self.rect[2]
        self.length = self.rect[3]

        self.rect.move_ip(x_pos - self.width//2, y_pos - self.length//2)

    def points(self):
        """retruns points the enemy gives, checked when enemy is killed"""
        return self._points

    def update(self):
        """base method for updatting"""
        self.rect.move_ip(0, 1)

class Sharp(Enemy):
    """basic enemy class, bounces around the screen kills the player if touched"""
    def __init__(self, x: int, y: int):
        super().__init__("ShipSpriteLeft.png", x, y)

        self.x_speed = randint(-3, 3)
        self.y_speed = randint(-3, 3)

        self.points = 200

    def update(self):
        """updates the enemies position, changes corresponding speeds direction if wall is hit"""

        self.rect.move_ip(self.x_speed, self.y_speed)

        if not 0 < self.rect[0] < 512 - self.width:
            self.x_speed *= -1

        if not 0 < self.rect[1] < 800 - self.length:
            self.y_speed *= -1


if __name__ == "__main__":
    pass
