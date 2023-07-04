import pygame
import colours

class Tile(pygame.sprite.Sprite):

    tile_num = 0

    def __init__(self, interface, x, y, cell_size, row, column, board) -> None:
        super().__init__()
        self.interface = interface
        self.screen = interface.screen
        self.player = interface.current_player
        
        #Rect image 
        self.width = self.height = cell_size
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

        self.rect.x = self.x = x
        self.rect.y = self.y = y
        
        self.row = row
        self.column = column
        self.board = board
        
        self.cross = pygame.image.load("images/cross.png").convert_alpha()  
        self.circle = pygame.image.load("images/circle.png").convert_alpha()  
        
        self.set = False
        self.symbol = None
        self.colour = colours.WHITE
        
        #For every instantiation of a tile object the ID is incremented and used within the HASH dunder for unique identification
        Tile.tile_num += 1  

    def __str__(self) -> str:
        return f"{self.symbol}"
    
    def __hash__(self) -> hash:
        """ This dunder method is used so that the object can be utilised in a numpy array"""
        return hash(str(Tile.tile_num))
    
    def __eq__(self, other) -> bool:
        """This dunder is just used for comparison between two tile objects to see if their symbols match"""
        if isinstance(other, Tile):
            return self.symbol == other.symbol
        return False


    def choose(self) -> None:
        """
        This function is used when a tile is selected
        The symbol of the tile is set and the tile is essentially frozen to change (I.e. set = True)
        """
        self.symbol = self.interface.current_player.symbol
        self.set = True
        self.colour = colours.GOLD
        self.board.total += 1


    def update(self) -> None:
        """
        If the tile object is available we can change its colour to green to denote accessibility
        Along with setting the symbol to the current player

        If the tile has already been set then we cannot allow the symbol to change
        We indicate its inaccessibility by change its colour to RED
        """   
        if not self.set:
            self.symbol = self.interface.current_player.symbol
            self.colour = colours.GREEN
        else:
            self.colour = colours.RED

        
    
    def draw(self) -> None:
        """
        This function draws the tile rectangle and blits upon it the current symbol attribute for that given object"""
        pygame.draw.rect(self.image, self.colour, (0, 0, self.width, self.height))

        def get_symbol_image(symbol) -> pygame.image:
            """Loads the image asset to its equivalent symbol"""
            match symbol:
                case "O":
                    return self.circle
                case "X":
                    return self.cross
                case "_":
                    return None

        if self.symbol:
            sym = get_symbol_image(self.symbol)
            sym = pygame.transform.scale(sym, (self.width, self.height))
            self.screen.blit(sym, (self.x, self.y))
    
  
    def check_if_inside(self, x, y) -> bool:
        """ Checks to see if the given coordinates are within the current tile object"""
        if (self.x <= x <= self.x + self.width and 
            self.y <= y <= self.y + self.height):
            return True
        return False
    


    def reset(self) -> None:
        """Resets a tile
        
        The discrepency between this and self.default() is as follows:
        
        When the user highlights over a new tile, we want to reset the previous one to its original state.
        If the tile has been set then we must keep its current symbol shown otherwise no choice would ever be logged"""
        self.colour = colours.WHITE
        if not self.set:
            self.symbol = None