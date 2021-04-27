import unittest
import pygame
from entities.enemies import Sharp


class TestSharp(unittest.TestCase):
    def setUp(self):

        pygame.init()
        self.sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((0, 0))
        self.sharp = Sharp(255, 255)

    def test_sharp_has_correct_position(self):

        self.assertEqual(self.sharp.rect, pygame.Rect(239, 239, 32, 32))
