""""this module is has the mainloop that calls all other loops in the app"""
from random import randint
import pygame
from entities.player import Player
from entities.enemies import Sharp
from entities.sprite_text import TextSprite

class GameLoop:

    """loop that is incremented if game is playing"""

    def __init__(self):

        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.info_sprites = pygame.sprite.Group()

        self.sprites = pygame.sprite.Group()

        self.player = Player(self.bullets, self.sprites)
        self.sprites.add(self.player)

        self.score = 0

    def increment(self):

        """
        updates all sprites based on their update function, also send loop killing massage
        to the mainloop if player is dead
        """
        keys = pygame.key.get_pressed()
        self.enemy_adder()
        self.player.update(keys)
        self.enemies.update()
        self.bullets.update()
        self.info_sprites.update()
        self.check_collisions()
        self.text_creator()

        if self.player.groups() == []:
            return "startloop"
        return None

    def enemy_adder(self):

        """adds enemies to the field if there are space for them"""

        if len(self.enemies.sprites()) < 5 + self.score//10000:
            enemy = Sharp(randint(30, 482), randint(30, 590))
            self.enemies.add(enemy)
            self.sprites.add(enemy)

    def check_collisions(self):

        """check all meaningful collision between sprites and acts based on them"""

        dead_enemies = pygame.sprite.groupcollide(
            self.enemies, self.bullets, dokilla=True, dokillb=True)
        for enemy in dead_enemies:
            self.score += enemy.points

        if pygame.sprite.spritecollideany(self.player, self.enemies) is not None:
            self.player.kill()
            with open("data/scores.txt", "a") as scores:
                scores.write(f"score: {self.score}\n")

    def get_sprites(self):

        """retrun the current sprites that are alive"""

        return self.sprites

    def text_creator(self):

        """
        makes sprite objects from the score and difficulty,
        so they can be used by the UI
        """

        text1 = TextSprite(f"SCORE:{str(self.score)}", 10, 10)
        text2 = TextSprite(f"DIFFICULTY:{str(self.score//10000 + 1)}", 10, 36)
        self.info_sprites.add(text1, text2)
        self.sprites.add(text1, text2)
