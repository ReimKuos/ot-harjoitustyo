import pygame
from classes.bullets import StandardBullet

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

        self.x_speed = 0
        self.y_speed = 0

    def draw(self,window):
        
        window.blit(self.image,self.rect)


    def update(self):

        pygame.event.get()
        keys = pygame.key.get_pressed()
        
        self.input_check(keys)
        self.limit_speed()
        
        if self.x_speed < 0:
            self.image = self.images[0]
        else:
            self.image = self.images[1]

        self.rect.move_ip(self.x_speed, self.y_speed)

    def input_check(self,keys):

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y_speed -= 0.5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y_speed += 0.5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x_speed -= 0.5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x_speed += 0.5
            
        if keys[pygame.K_SPACE]:
            self.shoot()

    def limit_speed(self):

        if self.x_speed > 0:
            self.x_speed = max(0, self.x_speed - 0.3)
        else:
            self.x_speed = min(0, self.x_speed + 0.3)

        if self.y_speed > 0:
            self.y_speed = max(0, self.y_speed - 0.3)
        else:
            self.y_speed = min(0, self.y_speed + 0.3)

        self.x_speed = min(self.x_speed,4)
        self.x_speed = max(self.x_speed,-4)

        self.y_speed = min(self.y_speed,4)
        self.y_speed = max(self.y_speed,-4)


    def shoot(self):
        mep = self.groups()
        mep[0].add(StandardBullet(self.rect[0],self.rect[1],1))
            
