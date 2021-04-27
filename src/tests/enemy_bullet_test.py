import unittest
import pygame
from shootables.sharp_bullet import SharpBullet


class TestEnemyBullet(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.bullets = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((0, 0))
        self.bullet = SharpBullet(0, 0, -1, -2)

    def test_enemy_bullet_is_not_part_of_any_groups_after_101_frames(self):
        self.bullets.add(self.bullet)
        for _ in range(1000):
            self.bullet.update()
        self.assertEqual(self.bullet.groups(), [])

    def test_enemy_bullet_travels_forvard(self):
        self.bullet.update()
        self.assertLess(self.bullet.rect[1], 10)