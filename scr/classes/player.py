import pygame
from classes.enemies import Sharp

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.images = [
            pygame.image.load("data/sprites/ShipSpriteLeft.png").convert_alpha(),
            pygame.image.load("data/sprites/ShipSpriteRight.png").convert_alpha()
            ]
        self.image = self.images[0]

        self.rect = self.image.get_rect()

        self.width = self.rect[2]
        self.length = self.rect[3]

        self.rect.move_ip(250 - self.width//2, 250 - self.length//2)

        self.speed = 3


    def draw(self,window):
        
        window.blit(self.image,self.rect)


    def update(self):

        pygame.event.get()
        keys = pygame.key.get_pressed()
        
        self.image = self.images[0]

        self.position_update(keys)
        self.rect.move_ip(0, 0)


    def position_update(self,keys):

        if keys[pygame.K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_s]:
            self.rect.move_ip(0, self.speed)
        if keys[pygame.K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_d]:
            self.rect.move_ip(self.speed, 0)
            self.image = self.images[1]
        if keys[pygame.K_c]:
            mep = self.groups()
            mep[0].add(Sharp(self.rect[0],self.rect[1]))
            
