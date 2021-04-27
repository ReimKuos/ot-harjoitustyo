"""containt the sprite for StaticSprite used for backgrounds and logos etc."""
import pygame


class SatticSprite(pygame.sprite.Sprite):
    """has position and sprite which can be drawn when needed"""

    def __init__(self, x_position: int, y_position: int, sprite):
        super().__init__()

        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()

        width, length = self.rect[2], self.rect[3]

        self.rect.move_ip(x_position - width//2, y_position - length//2)

    def get_rect(self):
        return self.rect
