import pygame
WHITE = (255, 255, 255)
class Tile(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, width, height):
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.inside = False
        self.free = True
        self.sym = "   "

        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
  
        self.draw(WHITE)

        
    def draw(self, colour):
        pygame.draw.rect(self.image, colour, (0, 0, self.width, self.height))
        self.inside = False
    
    def draw_symbol(self, symbol=None):
        image = pygame.image.load("images/cross.png")
        image = pygame.transform.scale(image, (self.width, self.height))
        self.screen.blit(image, (self.x, self.y))
        self.inside = True