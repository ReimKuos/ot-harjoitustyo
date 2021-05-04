"""module that has enemy classes"""
from random import randint
from math import sqrt
from entities.enemy import Enemy
from shootables.sharp_bullet import SharpBullet


class Sharp(Enemy):
    """
    basic enemy class, bounces around the screen kills the player if touched,
    also shoot dangerous projectiles
    """

    def __init__(self, x_pos: int, y_pos: int, bullet_list, sprite_group):
        """
        constructor for the enemy class

        Args:
            x_pos: horizontal postion of enemy
            y_pos: vertical postion of enemy
            sprite_group: a sprite group where enemy resides
            bullet_list: a sprite group where bullets are stored
        """

        super().__init__(x_pos, y_pos, "Sharp")

        self.shoot_cooldown = randint(60, 200)

        self.sprite_group = sprite_group
        self.enemy_bullets = bullet_list

    def update(self, player):
        """
        updates the enemies position, changes corresponding
        speeds direction if wall is hit, also makes enemy shoot
        the player if possible

        Args:
            player: 
        """

        self.rect.move_ip(self.x_speed, self.y_speed)
        self.shoot(player)

        if not 0 < self.rect[0] < 512 - self.width:
            self.x_speed *= -1

        if not 0 < self.rect[1] < 800 - self.length:
            self.y_speed *= -1

    def points(self):
        """retruns points the enemy gives, checked when enemy is killed"""
        return 200

    def shoot(self, player):
        """
        The shooting mwthod of the class if cooldown is on, it decrements it
        otherwise it calculates the speed of the bullet and creates a bullet
        instance that is added into all of the sharps groups

        Args:
            player: the user entity
        """

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        else:
            bullet_speed = self.calculate_bullet_speed(player)
            bullet = SharpBullet(
                self.rect[0] + self.rect[2]//2,
                self.rect[1] + self.rect[3]//2,
                bullet_speed[0],
                bullet_speed[1]
            )
            self.enemy_bullets.add(bullet)
            self.sprite_group.add(bullet)
            self.shoot_cooldown = randint(30, 200)

    def calculate_bullet_speed(self, player):
        """
        calculates the speed vector for a shot bullet that
        has the lenght of 3

        Args:
            player: the user entity
        """

        if player.rect == self.rect:
            return (0, 0)

        player_pos = player.get_position()
        own_pos = (self.rect[0] + self.rect[2]//2,
                   self.rect[1] + self.rect[3]//2)

        horizontal_diff = player_pos[0] - own_pos[0]
        diagonal_diff = player_pos[1] - own_pos[1]

        normalizer = 1/sqrt(horizontal_diff**2 + diagonal_diff**2)

        x_speed = 3 * normalizer * horizontal_diff
        y_speed = 3 * normalizer * diagonal_diff

        return (x_speed, y_speed)
