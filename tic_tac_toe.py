import pygame
from pygame.locals import *
from board import Board
 
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
GREEN = (79, 121, 66)

class TTT:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 600, 600
       
 
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.screen.fill(WHITE) 
        self._running = True

        self.all_sprites = pygame.sprite.Group()
        self.board = Board(self, 10)


 
    def event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for tile in self.all_sprites:
                if (tile.x <= mouse_x <= tile.x + tile.width and 
                    tile.y <= mouse_y <= tile.y + tile.height):
                        tile.draw(GREEN)
                        tile.draw_symbol()
                else: 
                    tile.draw(WHITE)

          


            
    def loop(self):
        pass


    def render(self):
        self.board.draw()
        self.all_sprites.draw(self.screen) 

    def cleanup(self):
        pygame.quit()
 
    def run(self):
        if self.init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.event(event)
            self.loop()
            self.render()
        self.cleanup()