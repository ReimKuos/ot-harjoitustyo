import pygame
from startloop import StartLoop
from gameloop import GameLoop

class MainLoop:

    def __init__(self,ui,sprites):

        self.clock = pygame.time.Clock()
        self.running = True
        
        self.current_loop = StartLoop()
        self.ui = ui

    def start(self):

        self.mainloop()


    def mainloop(self):

        while self.running:

            self.clock.tick(60)
            self.current_loop.increment()
            self.draw()
        

    def draw(self):

        self.ui.render(self.current_loop.get_sprites())



if __name__ == "__main__":
    pass
