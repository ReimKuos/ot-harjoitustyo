"""contain the MainLoop class"""
import pygame
from startloop import StartLoop
from gameloop import GameLoop
from scoreloop import ScoreLoop


class MainLoop:
    """the mainloop that limits frames and handles 'subloops'"""

    def __init__(self, user_inteface):

        self.clock = pygame.time.Clock()
        self.running = True

        self.current_loop = StartLoop()
        self.user_inteface = user_inteface

    def start(self):
        """method that can be called to satrt the mainloop"""

        self.mainloop()

    def mainloop(self):
        """the mainloop of the mainloop, calls all nesessary methods 60 a second"""

        while self.running:

            self.clock.tick(60)
            self.update()
            event = self.current_loop.increment()
            if event is not None:
                self.loop_switch(event)
            self.draw()

    def draw(self):
        """gives sprites to the user interface and calls the to be drawn"""

        self.user_inteface.render(self.current_loop.get_sprites())

    def update(self):
        """calls all methods that pertain to the funcytionality of the loop"""

        self.check_for_exit()

    def check_for_exit(self):
        """checks if any exit conditions have happened"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # pylint: disable=no-member
                self.running = False

            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member

                if event.key == pygame.K_ESCAPE:  # pylint: disable=no-member
                    self.running = False

    def loop_switch(self, next_loop: str):
        """this function chooses the next current_loop based on itäs input"""

        if next_loop == "gameloop":

            self.current_loop = GameLoop()

        elif next_loop == "startloop":

            self.current_loop = StartLoop()

        elif next_loop == "scoreloop":

            self.current_loop = ScoreLoop()

        elif next_loop == "exit":

            self.running = False


if __name__ == "__main__":
    pass
