import unittest
import pygame
from entities.bullets import StandardBullet


class TestBullet(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.bullets = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((0, 0))
        self.bullet = StandardBullet(10,10,0)

    def test_bullet_is_not_part_of_any_groups_after_42_frames(self):
        self.bullets.add(self.bullets)
        for _ in range(42):
            self.bullet.update()
        self.assertEqual(self.bullet.groups(),[])

    def test_bullet_travels_forvard(self):
        self.bullet.update()
        self.assertLess(self.bullet.rect[1],10)
