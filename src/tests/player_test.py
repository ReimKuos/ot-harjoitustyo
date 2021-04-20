import unittest
import pygame
from entities.player import Player
from entities.bullets import StandardBullet


class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.bullets = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((0, 0))
        self.player = Player(self.sprites, self.bullets)

    def test_player_stays_on_screen_up_and_left(self):
        #simulates key presses
        keys = {
            pygame.K_UP: True,
            pygame.K_LEFT: True,
            pygame.K_w: False,
            pygame.K_d: False,
            pygame.K_DOWN: False,
            pygame.K_RIGHT: False,
            pygame.K_s: False,
            pygame.K_a: False,
            pygame.K_SPACE: False
        }
        for _ in range(300):
            self.player.update(keys)
        self.assertEqual(self.player.rect, pygame.Rect(0,0,32,32))

    def test_player_stays_on_screen_down_and_right(self):
        #simulates key presses
        keys = {
            pygame.K_UP: False,
            pygame.K_LEFT: False,
            pygame.K_w: False,
            pygame.K_d: False,
            pygame.K_DOWN: True,
            pygame.K_RIGHT: True,
            pygame.K_s: False,
            pygame.K_a: False,
            pygame.K_SPACE: False
        }
        for _ in range(300):
            self.player.update(keys)
        self.assertEqual(self.player.rect, pygame.Rect(480, 768, 32, 32))

    def test_bullet_is_in_both_groups_aster_player_shoots(self):

        self.player.shoot()
        self.assertEqual(self.sprites.sprites(), self.bullets.sprites())
