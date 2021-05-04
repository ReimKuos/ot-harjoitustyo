""""this module is has the mainloop that calls all other loops in the app"""
from random import randint
import pygame
from entities.follower import Follower
from entities.player import Player
from entities.sharp import Sharp
from entities.sprite_text import TextSprite
from score_adder import add_score


class GameLoop:

    """loop that is incremented if game is being played"""

    def __init__(self):
        
        """
        constructor of the gameloop, sets up all
        the necessary entities for the gameloop to run
        """

        self.enemies = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.info_sprites = pygame.sprite.Group()

        self.sprites = pygame.sprite.Group()

        self.player = Player(self.bullets, self.sprites)
        self.sprites.add(self.player)

        self.game_over = False
        self.score = 0

    def increment(self):
        """
        updates all sprites based on their update function, also send loop killing massage
        to the mainloop if player is dead
        """
        keys = pygame.key.get_pressed()
        if self.game_over:
            if keys[pygame.K_r]:
                return "gameloop"
            if keys[pygame.K_t]:
                return "startloop"
            return None
        self.enemy_adder()
        self.player.update(keys)
        self.enemies.update(self.player)
        self.enemy_bullets.update()
        self.bullets.update()
        self.info_sprites.update()
        self.check_collisions()
        self.text_creator()

        if self.player.groups() == []:
            self.sprites.empty()
            self.end_game()
            self.game_over = True
        return None

    def enemy_adder(self):
        """
        adds enemies to the field if there are space for them
        """

        if len(self.enemies.sprites()) < 5 + self.score//10000:
            if randint(0, 1) == 1:
                enemy = Sharp(randint(30, 482), randint(30, 590),
                              self.enemy_bullets, self.sprites)
            else:
                enemy = Follower(randint(30, 482), randint(30, 590))

            self.enemies.add(enemy)
            self.sprites.add(enemy)

    def check_collisions(self):
        """check all meaningful collision between sprites and acts based on them"""

        dead_enemies = pygame.sprite.groupcollide(
            self.enemies, self.bullets, dokilla=True, dokillb=True)
        for enemy in dead_enemies:
            self.score += enemy.points()

        if pygame.sprite.spritecollideany(self.player, self.enemies) is not None:
            self.player.kill()

        if pygame.sprite.spritecollideany(self.player, self.enemy_bullets) is not None:
            self.player.kill()

    def get_sprites(self):
        """
        retrun the current sprites that are alive

        Returns:
            returns the sprite group containing all
            the sprites that need to be drawn
        """

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

    def end_game(self):
        """adds the score to the database and kills the current gameloop"""

        add_score(self.score)
        self.sprites.add(
            TextSprite("GAME OVER", 256, 250, True),
            TextSprite(f"SCORE: {self.score}", 256, 300, True),
            TextSprite("press 't' to end game", 256, 400, True),
            TextSprite("press 'r' to restart", 256, 440, True)
        )
