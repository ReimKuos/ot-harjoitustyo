import unittest
import pygame
from entities.selector import Arrow


class TestArrow(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0))
        self.arrow = Arrow(0, 0)

    def test_only_a_space_press_retruns_gameloop(self):

        keys = {
            pygame.K_UP: False,
            pygame.K_w: False,
            pygame.K_DOWN: False,
            pygame.K_s: False,
            pygame.K_SPACE: True
        }
        self.arrow.update(keys)
        self.assertEqual(self.arrow.get_event(), "gameloop")

    def test_one_down_press_retruns_scoreloop(self):
        # simulates key presses
        keys = {
            pygame.K_UP: False,
            pygame.K_w: False,
            pygame.K_DOWN: True,
            pygame.K_s: False,
            pygame.K_SPACE: True
        }
        self.arrow.update(keys)
        self.assertEqual(self.arrow.get_event(), "scoreloop")

    def test_one_up_press_retruns_scoreloop(self):
        # simulates key presses
        keys = {
            pygame.K_UP: True,
            pygame.K_w: False,
            pygame.K_DOWN: False,
            pygame.K_s: False,
            pygame.K_SPACE: True
        }
        self.arrow.update(keys)
        self.assertEqual(self.arrow.get_event(), "exit")

