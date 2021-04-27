"""contains the Arrow that can be used to visualise and choose options in the start menu"""
import pygame


class Arrow(pygame.sprite.Sprite):
    """currently has a wrong sprite, contains the methods for drawing and manuevering the start menu"""

    def __init__(self, x_position: int, y_position: int):

        super().__init__()

        self.events = {
            0: "gameloop",
            1: "scoreloop",
            2: "exit"
        }

        self.event = None

        self.pointer = 0
        self.pressed = False

        self.image = pygame.image.load(
            "data/sprites/PlanetSmol1.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.width, self.length = self.rect[2], self.rect[3]

        self.rects = [
            self.rect.move(x_position - self.width//2,
                           y_position - self.length//2),
            self.rect.move(x_position - self.width//2,
                           y_position - self.length//2 + 50),
            self.rect.move(x_position - self.width//2,
                           y_position - self.length//2 + 100)
        ]

        self.rect = self.rects[self.pointer]

    def update(self, keys):
        """updates the pointers position scrolls back to zero if postion goes over 2"""
        self.move_pointer(keys)
        self.choose_event(keys)

        self.pointer %= 3
        self.rect = self.rects[self.pointer]

    def move_pointer(self, keys):
        """gets the input for moving the pointer"""
        if keys[pygame.K_UP] or keys[pygame.K_w]:  # pylint: disable=no-member
            if not self.pressed:
                self.pointer -= 1
            self.pressed = True

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:  # pylint: disable=no-member
            if not self.pressed:
                self.pointer += 1
            self.pressed = True

        else:
            self.pressed = False

    def choose_event(self, keys):
        """checks if space is pressed if so changes event from None to the chosen one"""
        if keys[pygame.K_SPACE]:  # pylint: disable=no-member
            self.event = self.events[self.pointer]

    def get_event(self):
        """retruns the chosen event"""
        return self.event
