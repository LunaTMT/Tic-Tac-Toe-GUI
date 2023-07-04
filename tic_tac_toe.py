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
    def __init__(self, board_size):

        self._running = True
        self.size = self.width, self.height = 600, 600 
        self.board_size = board_size
        self.turn = 0
        self.current_tile = None
        self.finished = False

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.screen.fill(WHITE) 
        self.all_sprites = pygame.sprite.Group()
        self._running = True

        self.players = [Player("JIM", "X"), Player("JOHN", "O")]
        self.current_player = self.players[0]

        self.board = Board(self, self.board_size)
 
    def event(self, event):
        if not self.finished:
            if event.type == pygame.QUIT:
                self._running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                """
                Whenever we select a tile by clicking it, we will do the following:
                - Check to see if it a valid tile (I.e. has this already been chosen?)
                - Change the next turn to the next player
                - Check to see if there is a winner """
                if not self.current_tile.set:
                    self.current_tile.choose()
                    self.get_next_player()
                    self.board.check_win()

            elif event.type == pygame.MOUSEMOTION:
                """For any mouse motion we want to update the previous and new tile"""
                self.board.update_current()
                self.current_tile.update()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                "Once the game is over, a form of reinitialisation is performed"
                self.all_sprites = pygame.sprite.Group()
                self.board = Board(self, self.board_size)
                self.finished = False
                self.current_player = self.players[0]
                self.turn = 0

    def loop(self):
        self.board.draw_symbols()  
        
    def render(self):
        self.board.draw_grid()
        self.all_sprites.draw(self.screen) 

    def cleanup(self):
        pygame.quit()

    def run(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.event(event)
            self.loop()
            self.render()
        self.cleanup()


    def get_next_player(self):
        """
        to modulus any number by 2 will always produce 0 or 1, 
        this can be used in conjunction with the parity of numbers (even, odd, even, odd, even, odd -->)
        to constatly produce an iterator switching between 0 and 1
        This is used to switch between the players in the 2 length player list"""
        self.turn += 1
        self.current_player = self.players[self.turn % 2]
        