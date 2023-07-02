import pygame
from pygame.locals import *
from board import Board
from player import Player
import os


 
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
GREEN = (50,205,50)
GOLD = (255,215,0)



class TicTacToe:
    def __init__(self):
        pygame.init()
        self._running = True
        self.size = self.width, self.height = 600, 600
        
        
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.screen.fill(WHITE) 

        self.all_sprites = pygame.sprite.Group()
        
        
        self.turn = 0
        self.players = [Player("JIM", "X"), Player("JOHN", "O")]
        self.player = self.players[0]
        
        self.board_size = 3
        self.board = Board(self, self.board_size)
        self.current_tile = None

        self.clear = lambda: os.system('clear')
        
        self.finished = False
 
    def event(self, event):
        if not self.finished:
            if event.type == pygame.QUIT:
                self._running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN: #Select
                if self.current_tile.is_valid():
                    self.current_tile.choose()
                    self.get_next_player()
                    self.board.check_win()

            elif event.type == pygame.MOUSEMOTION:
                self.current_tile = self.board.get_current_tile()
                self.current_tile.update(self.player.sym)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.all_sprites = pygame.sprite.Group()
                self.board = Board(self, self.board_size)
                self.finished = False

                

            

    def loop(self):
        self.board.draw_symbols()  
        if not self.finished:
            self.current_tile = self.board.get_current_tile()
            try:
                self.current_tile.draw_symbol(self.player.sym)
            except:   
                pass
            

    def render(self):
        self.board.draw_grid()
        self.all_sprites.draw(self.screen) 

    def cleanup(self):
        pygame.quit()

    def run(self):
        while( self._running ):
            for event in pygame.event.get():
                self.event(event)
            self.loop()
            self.render()
        self.cleanup()


    def get_next_player(self):
        self.turn += 1
        self.player = self.players[self.turn % 2]