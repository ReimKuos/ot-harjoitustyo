"""
This file contains the ScoreLoop which is used to show
the user thw at most 10 highest scores made by the player
"""
import pygame
from score_fetcher import fetch_scores
from entities.sprite_text import TextSprite


class ScoreLoop:

    def __init__(self):

        self.scores = fetch_scores()
        self.sprites = pygame.sprite.Group()
        self.get_score_sprites()

        self.space_cooldown = True

    def get_score_sprites(self):

        rank = 1

        for score in self.scores:
            self.sprites.add(
                TextSprite(str(score), 256, 100+50*rank, True)
            )
            rank += 1

    def increment(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if self.space_cooldown:
                return None
            return "startloop"
        self.space_cooldown = False
        return None

    def get_sprites(self):
        """retruns sprites for the UI"""
        return self.sprites


if __name__ == "__main__":

    pass
