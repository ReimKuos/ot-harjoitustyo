"""cointains the player class that is used in the gameloop to play"""
import pygame
from entities.bullets import StandardBullet



class Player(pygame.sprite.Sprite):
    """the player class that holds the postion, takes input, handles update, and holds sprites"""

    def __init__(self, bullets, sprites):

        super().__init__()

        self.bullets = bullets
        self.sprites = sprites 

        self.images = [
            pygame.image.load(
                "data/sprites/ShipSpriteLeft.png").convert_alpha(),
            pygame.image.load(
                "data/sprites/ShipSpriteRight.png").convert_alpha()
        ]

        self.image = self.images[0]

        self.rect = self.image.get_rect()

        self.width = self.rect[2]
        self.length = self.rect[3]

        self.rect.move_ip(256 - self.width//2, 780 - self.length//2)

        self.x_speed = 0
        self.y_speed = 0

        self.bullet_cooldown = 0

    def update(self, keys):
        """calculates the next postion of the player based on key presses and increments cooldowns"""

        self.input_check(keys)
        self.limit_speed()
        self.update_sprite_state()
        self.update_position()
        self.tick_cooldowns()

    def tick_cooldowns(self):
        """lowers all cooldowns if they are not 0"""

        if self.bullet_cooldown > 0:
            self.bullet_cooldown -= 1

    def update_sprite_state(self):
        """decides which player sprite needs to be drawn based on players speed"""

        if self.x_speed < 0:
            self.image = self.images[0]
        else:
            self.image = self.images[1]

    def update_position(self):
        """makes sure that player postion remains on the screen"""

        self.rect.move_ip(self.x_speed, self.y_speed)

        x_pos = self.rect[0]
        y_pos = self.rect[1]

        y_pos = min(y_pos, 800 - self.length)
        y_pos = max(y_pos, 0)

        x_pos = min(x_pos, 512 - self.width)
        x_pos = max(x_pos, 0)

        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.length)

    def input_check(self, keys):
        """takes input and makes movement based on that"""

        if keys[pygame.K_UP] or keys[pygame.K_w]: # pylint: disable=no-member
            self.y_speed -= 0.5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: # pylint: disable=no-member
            self.y_speed += 0.5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: # pylint: disable=no-member
            self.x_speed -= 0.5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # pylint: disable=no-member
            self.x_speed += 0.5

        if keys[pygame.K_SPACE]: # pylint: disable=no-member
            self.shoot()

    def limit_speed(self):
        """forces the speed to remain in certein bounds"""

        if self.x_speed > 0:
            self.x_speed = max(0, self.x_speed - 0.3)
        else:
            self.x_speed = min(0, self.x_speed + 0.3)

        if self.y_speed > 0:
            self.y_speed = max(0, self.y_speed - 0.3)
        else:
            self.y_speed = min(0, self.y_speed + 0.3)

        self.x_speed = min(self.x_speed, 4)
        self.x_speed = max(self.x_speed, -4)

        self.y_speed = min(self.y_speed, 4)
        self.y_speed = max(self.y_speed, -4)

    def shoot(self):
        """creates a bullet"""

        if self.bullet_cooldown == 0:
            bullet = StandardBullet(self.rect[0], self.rect[1], self.y_speed)
            self.bullets.add(bullet)
            self.sprites.add(bullet)
            self.bullet_cooldown = 10
