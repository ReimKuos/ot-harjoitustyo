import unittest
import pygame
from math import sqrt
from entities.sharp import Sharp
from entities.player import Player
from shootables.bullets import StandardBullet
from shootables.sharp_bullet import SharpBullet


class TestSharp(unittest.TestCase):
    def setUp(self):

        pygame.init()
        self.sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((0, 0))
        self.sharp = Sharp(200, 200, self.bullets, self.sprites)

    def test_sharp_has_correct_position(self):

        self.assertEqual(self.sharp.rect, pygame.Rect(184, 184, 32, 32))

    def test_bullet_speed_returned_is_geometricly_appriximately_3(self):
        player = Player(self.bullets, self.sprites)
        speeds = self.sharp.calculate_bullet_speed(player)
        speedsum = sqrt(speeds[0]**2 + speeds[1]**2)
        self.assertAlmostEqual(speedsum, 3)

    def test_bullet_speed_returned_is_zero_if_player_atop_enemy(self):
        self.sharp = Sharp(256, 780, self.bullets, self.sprites)
        speed = self.sharp.calculate_bullet_speed(Player(self.bullets, self.sprites))
        self.assertEqual(speed ,(0, 0))