from tile import Tile

import pygame
import numpy as np
import os
import colours

class Board(pygame.sprite.Sprite):
    
    def __init__(self, interface, k) -> None:
        super().__init__()
        self.interface      = interface
        self.all_sprites    = interface.all_sprites
        self.width          = interface.width
        self.height         = interface.height
        self.screen         = interface.screen

        self.grid_size = k #For example: (3X3) (KXK)
        self.cell_size = self.width // self.grid_size

        # Calculate the width and height of the grid
        self.grid_width = self.grid_size * self.cell_size
        self.grid_height = self.grid_size * self.cell_size
        
        #Empty numpy array with object datatype and generate all the tiles
        self.board = self.generate_tiles()
        self.slices = self.get_slices()

        self.current_tile  = None
        self.total = 0

        self.clear = lambda: os.system('clear')

        
    def __getitem__(self, index):
        """
        This dunder method is used simple to make access to the numpy attribute (self.board) cleaner
        """
        return self.board[index]

        
    def display(self) -> None:
        """
        This function displays the board values on the console
        """
        self.clear()
        for r in self.board:
            for tile in r:
                print(tile, end=' ')
            print("\n")

    def draw_grid(self) -> None:
        """
        This function draws both horizontal and vertical grid lines for a board of size k
        """
        for x in range(1, self.grid_size):
            pygame.draw.line(self.screen, colours.BLACK, (x * self.cell_size, 0), (x * self.cell_size, self.height), 2) #vertical
            pygame.draw.line(self.screen, colours.BLACK, (0, x * self.cell_size), (self.width, x * self.cell_size), 2)  #horizontal
        pygame.display.flip()
    
    def draw_symbols(self) -> None:
        """
        This function draws all the symbols that are on our board (np.arrary)
        """
        for row in self.board:
            for tile in row:
                tile.draw()

    def draw_all(self, colour) -> None:
        """
        This function changes the colour of every tile object to the argument passed in
        """
        for row in self.board:
                for tile in row:
                    tile.colour = colour
                    

    def generate_tiles(self) -> np.ndarray:
        """
        This function initialises the board with all the tile objects in their respective location
        """ 
         
        board = np.empty((self.grid_size, self.grid_size), dtype=Tile)
        
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                x =  c * self.cell_size
                y =  r * self.cell_size
                tile = Tile(self.interface, x, y, self.cell_size, r, c, self)      
                self.interface.all_sprites.add(tile)   
                board[r][c] = tile 
        return board

    
    def update_current(self) -> None:
        """
        This function checks to see if the current x,y position is a new tile or if we're on the same 'current tile'
        if the new position is a new tile then we update the current tile in our interface class
        """
        x, y = pygame.mouse.get_pos()
        for tile in self.all_sprites:
            if tile.check_if_inside(x, y) and self.is_new_tile(tile):
                self.interface.current_tile = tile
                return

    
    def is_new_tile(self, new_tile) -> bool:
        """
        If the new tile differs from the currently stored one then we update this current value to the new argument passed in
        In addition the previous tile (i.e - current_tile) is reset.
        """

        if new_tile is not self.current_tile:
            #Only if there has beeen a previous can we reset it, otherwise there is no object to call on
            if self.current_tile != None: 
                self.current_tile.reset()
            self.current_tile = new_tile
            return True
        return False

    def check_win(self) -> None:
        """
        This fuction simple checks if there has been an end game state, i.e. - a winner or a draw
        The row(s) that win are highlighted GOLD
        If it is a draw all tiles are changed to red to indicate no winner.
        """

        self.clear()
        for slice_ in self.slices:
            tiles = set((tile.symbol for tile in slice_))
            
            if tiles == {"X"} or tiles == {"O"}:
                for tile in slice_:
                    tile.colour = colours.GOLD
                    self.interface.finished = True
                return
                
        if self.total == self.grid_size ** 2:
            self.draw_all(colours.RED)
            self.interface.finished = True

    def get_slices(self) -> list:   
        """
        This function returns a list of lists.
        The lists contained within are the diagnoals and all rows and columns of the board
        """

        diagnoal_1 = np.diagonal(self.board)
        diagnoal_2 = np.diagonal(np.fliplr(self.board))

        slices = [diagnoal_1, diagnoal_2]

        for i in range(self.grid_size):
            slices.append(self[:, i])
            slices.append(self[i, :])
        return slices
    


