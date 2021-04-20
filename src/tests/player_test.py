import unittest
import pygame
from entities.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.bullets = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((0, 0))
        self.player = Player(self.sprites, self.bullets)

    def test_created_player_exists(self):
        self.assertNotEqual(self.player, None)
