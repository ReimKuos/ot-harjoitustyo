"""contains the StartLoop class"""
import pygame
from entities.static_sprite import SatticSprite
from entities.selector import Arrow
from entities.sprite_text import TextSprite


class StartLoop:
    """loopclass used in the startmenu, called by the Mainloop"""

    def __init__(self):

        self.sprites = pygame.sprite.Group()

        self.keysup = True

        self.pointer = Arrow(150, 500)

        self.sprites.add(SatticSprite(256, 200, "data/sprites/SpriteLogo.png"),
                         SatticSprite(
                             256, 500, "data/sprites/SpriteStart.png"),
                         SatticSprite(
                             256, 500, "data/sprites/SpriteStart.png"),
                         SatticSprite(
                             256, 550, "data/sprites/SpriteScore.png"),
                         SatticSprite(256, 600, "data/sprites/SpriteExit.png"),
                         self.pointer,
                         )

    def increment(self):
        """increments the loop, which moves the pointer and chooses the next loop"""

        keys = pygame.key.get_pressed()

        # A non-permanent fix
        if self.keysup and keys[pygame.K_SPACE]:
            return None
        self.keysup = False

        self.sprites.update(keys)

        return self.pointer.get_event()

    def get_sprites(self):
        """retrun drawable sprites"""
        return self.sprites


if __name__ == "__main__":
    pass
