import unittest
import pygame
from entities.player import Player
from shootables.bullets import StandardBullet


class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.bullets = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((0, 0))
        self.player = Player(self.sprites, self.bullets)
        self.player_copy = Player(self.sprites, self.bullets)

    def test_player_stays_on_screen_up_and_left(self):
        # simulates key presses
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
        self.assertEqual(self.player.rect, pygame.Rect(0, 0, 32, 32))

    def test_player_stays_on_screen_down_and_right(self):
        # simulates key presses
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

    def test_player_limit_speed_speed_stays_0_if_0(self):
        self.player.limit_speed()
        self.assertEqual((self.player.x_speed, self.player.y_speed), (0, 0))

    def test_player_limit_speed_speed_drops_if_over_the_limit(self):
        self.player.x_speed = 10
        self.player.limit_speed()
        self.assertLess(self.player.x_speed, 10)

    def test_bullet_cooldown_is_not_0_after_shooting(self):
        self.player.shoot()
        self.assertGreater(self.player.bullet_cooldown,0)

    def test_bullet_cooldown_does_not_go_under_0(self):
        self.player.shoot()
        for _ in range(1000):
            self.player.tick_cooldowns()
        self.assertEqual(self.player.bullet_cooldown,0)

    def test_sprite_state_is_different(self):
        self.player.x_speed = -1
        self.player_copy.x_speed = 1
        self.assertNotEqual(self.player.image,self.player_copy.image)

