"""contains a sprite that is used to get text on the screen"""
import pygame


class TextSprite(pygame.sprite.Sprite):
    """a child class of a pygame Sprite, makes sprite object from a string"""
    def __init__(self, text: str, x_pos: int, y_pos: int):
        super().__init__()
        color = (120, 120, 255)
        font = pygame.font.SysFont("courier", 32, bold=True, italic=False)
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect()

        self.rect.move_ip(x_pos, y_pos)
        self.lifetime = 1

    def update(self):
        """kills the sprite when called, quick fix to piling up of text sprites"""
        self.kill()
