import pygame

class UI:

    def __init__(self, width: int, height: int):

        self.display = pygame.display.set_mode((width,height))
    
    def render(self, sprites: pygame.sprite.Group):
        
        self.display.fill((40,40,40))
        pygame.draw.rect(self.display,(0,0,0),(5,5,610,800))

        sprites.draw(self.display)

        pygame.display.update()

    

    


