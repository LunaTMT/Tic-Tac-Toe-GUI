from tile import Tile
import pygame

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

class Board(pygame.sprite.Sprite):
    
    def __init__(self, interface, k):
        super().__init__()
        self.width  = interface.width
        self.height = interface.height
        self.screen = interface.screen

        self.grid_size = k
        self.cell_size = self.width // self.grid_size

        # Calculate the width and height of the grid
        self.grid_width = self.grid_size * self.cell_size
        self.grid_height = self.grid_size * self.cell_size

        # Calculate the starting position of the grid to center it on the screen
        self.start_x = (self.width - self.grid_width) // 2
        self.start_y = (self.height - self.grid_height) // 2

        interface.all_sprites.add(self.generate_tiles())


    def draw(self):
        """This function """
        for x in range(1, self.grid_size):
            pygame.draw.line(self.screen, BLACK, (x * self.cell_size, 0), (x * self.cell_size, self.height), 2) #vertical
            pygame.draw.line(self.screen, BLACK, (0, x * self.cell_size), (self.width, x * self.cell_size), 2) #horizontal
        pygame.display.flip()


    def generate_tiles(self):
        tiles = []
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x = self.start_x + col * self.cell_size
                y = self.start_y + row * self.cell_size
                tiles.append(Tile(self.screen, x, y, self.cell_size, self.cell_size))
        return tiles




  