import pygame

class TextSprite(pygame.sprite.Sprite):

    def __init__(self,x_position: int, y_position: int, sprite):

        super().__init__()

        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()

        width,length = self.rect[2],self.rect[3]

        self.rect.move_ip(x_position - width//2, y_position - length//2)

        print(self.rect)


        