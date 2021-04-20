import pygame
from startloop import StartLoop
from gameloop import GameLoop

class MainLoop:

    def __init__(self,ui):

        self.clock = pygame.time.Clock()
        self.running = True
        
        self.current_loop = StartLoop()
        self.ui = ui

    def start(self):

        self.mainloop()

    def mainloop(self):

        while self.running:

            self.clock.tick(60)
            self.update()
            self.current_loop.increment()
            self.draw()
        

    def draw(self):

        self.ui.render(self.current_loop.get_sprites())

    def update(self):

        self.check_for_exit()

    def check_for_exit(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_q:
                    self.loop_switch("gameloop")

                if event.key == pygame.K_o:
                    print(len(self.current_loop.get_sprites().sprites()))

    def loop_switch(self, next_loop: str):

        if next_loop == "gameloop":

            self.current_loop = GameLoop()

        elif next_loop == "startloop":

            self.current_loop = StartLoop()







if __name__ == "__main__":
    pass
