from random import randint
from entities.enemy import Enemy
import pygame


class Follower(Enemy):
    """
    basic enemy class, bounces around the screen and tries to touch the player,
    kills the player if touched
    """

    def __init__(self, x_pos: int, y_pos: int):
        """
        constructor creates a new follower entity

        Args:
            x_pos: the horizontal postion of the entity
            y_pos: the vertical position of the entity
        """
        super().__init__(x_pos, y_pos, "FollowerSprite")

    def update(self, player):
        """
        updates the enemies position and speed, and makes it impossible
        for the entity to float out of sthe users view

        Args:
            player: The player the user controls, it is used to find the
                    possible speed modifications needed.
        """

        if player.rect[0] < self.rect[0]:
            self.x_speed -= 0.05
        elif player.rect[0] < self.rect[0]:
            self.x_speed += 0.05

        if player.rect[1] < self.rect[1]:
            self.y_speed -= 0.05
        elif player.rect[1] > self.rect[1]:
            self.y_speed += 0.05

        self.x_speed = max(-3, min(self.x_speed, 3))
        self.y_speed = max(-3, min(self.y_speed, 3))

        if self.rect[0] < 0:
            self.x_speed = abs(self.x_speed)
        elif self.rect[0] > 512 - self.width:
            self.x_speed = -abs(self.x_speed)

        if self.rect[1] < 0:
            self.y_speed = abs(self.y_speed)
        elif self.rect[1] > 800 - self.length:
            self.y_speed = -abs(self.y_speed)

        self.rect.move_ip(self.x_speed, self.y_speed)

    def points(self):
        """
        method for getting the points the follower gives when destroyd

        returns:
            points the entity gives
        """
        return 300
