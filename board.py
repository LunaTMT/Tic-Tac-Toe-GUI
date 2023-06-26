from tile import Tile
import pygame
import numpy as np
import os

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

class Board(pygame.sprite.Sprite):
    
    def __init__(self, interface, k):
        super().__init__()
        self.interface      = interface
        self.all_sprites    = interface.all_sprites
        self.width          = interface.width
        self.height         = interface.height
        self.screen         = interface.screen

        self.grid_size = 3 #(3X3) (KXK)
        self.cell_size = self.width // self.grid_size

        # Calculate the width and height of the grid
        self.grid_width = self.grid_size * self.cell_size
        self.grid_height = self.grid_size * self.cell_size
        
        self.board = np.empty((self.grid_size, self.grid_size), dtype=object)

        self.generate_tiles()

        #self.default_tile  = self.interface.all_sprites.sprites()[0]
        self.current_tile  = None

        self.clear = lambda: os.system('clear')


        self.total = 0
        self.slices = self.get_slices()

    def __setitem__(self, index, item):
        row, col = index
        self.board[row, col] = item
        self.total += 1
        
        self.clear()
        self.display()

    def __getitem__(self, index):
        row, col = index
        return self.board[row, col]

        
    def display(self):
       # print(self.board)
        for r in self.board:
            for tile in r:
                print(tile, end=' ')
            print("\n")

    def draw_grid(self):
        """This function """
        for x in range(1, self.grid_size):
            pygame.draw.line(self.screen, BLACK, (x * self.cell_size, 0), (x * self.cell_size, self.height), 2) #vertical
            pygame.draw.line(self.screen, BLACK, (0, x * self.cell_size), (self.width, x * self.cell_size), 2)  #horizontal
        pygame.display.flip()
    def draw_symbols(self):
        for row in self.board:
            for tile in row:
                if isinstance(tile, Tile) and tile.symbol != "":
                    tile.draw_symbol(tile.symbol)
                    

    def generate_tiles(self):  
        for r in range(self.grid_size):
            row = []
            for c in range(self.grid_size):
                x =  c * self.cell_size
                y =  r * self.cell_size
                tile = Tile(self.interface, x, y, self.cell_size, r, c, self)       
                self.interface.all_sprites.add(tile)   
  
    def get_tile(self):
        x, y = pygame.mouse.get_pos()
        if (x,y) == (0, 0):
            return None  
        else:
            for tile in self.all_sprites:
                if tile.check_if_inside(x, y): 
                    self.check_if_new_tile(tile)
                    return tile
        
        
    
    def check_if_new_tile(self, new_tile):       
        if new_tile != self.current_tile:
            try:
                self.current_tile.reset()
            except:
                pass
            
            self.current_tile = new_tile
            return True
        return False
    
    def check_win(self):

        
        winner = True
        for slice_ in self.slices:
            print(slice_)
            if all(isinstance(tile, Tile) for tile in slice_) and len(set(slice_)) == 1:
                print("winner")
                print(slice_)
                print(set(slice_))
                
   
        if self.total == 9:
            print("DRAW")

    def get_slices(self) -> list:
        """This function returns a list of lists
        The lists contained within are the diagnoals and all rows and columns
        """

        diagnoal_1 = np.diagonal(self.board)
        diagnoal_2 = np.diagonal(np.fliplr(self.board))

        slices = [diagnoal_1, diagnoal_2]

        for i in range(self.grid_size):
            slices.append(self[:, i])
            slices.append(self[i, :])

        return slices