import pygame
WHITE = (255, 255, 255)
GREEN = (50,205,50)
RED = (255, 0, 0)
GOLD = (255,215,0)


class Tile(pygame.sprite.Sprite):

    tile_num = 0

    def __init__(self, interface, x, y, cell_size, row, column, board):
        super().__init__()
        self.interface = interface
        self.screen = interface.screen
        self.player = interface.player
        
        
        self.x = x
        self.y = y
        self.width = self.height = cell_size
        self.row = row
        self.column = column
        self.board = board
        

        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.set = False
        self.symbol = False
        
        Tile.tile_num += 1  
        self.draw(WHITE)

    def __str__(self) -> str:
        return f"{self.symbol}"
    
    def __repr__(self):
        return f"{self.symbol}"
        
    def __hash__(self):
        return hash(str(Tile.tile_num) + f"{' _ ' if self.symbol == None else self.symbol}")
    
    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.symbol == other.symbol
        return False
    
    def __ne__(self, other):
        if isinstance(other, Tile):
            return (self.x, self.y) != (other.x, other.y)
        return NotImplemented

    def choose(self):
        self.symbol = self.interface.player.sym
        self.board[self.row, self.column] = self
        self.draw(GOLD)

    def update(self, symbol):   

        if self.board[self.row, self.column] == None:
            self.draw(GREEN) 
            self.draw_symbol(symbol)
            return True
            
        else:
            self.draw(RED)
            return False
        
        
    def is_valid(self):
        return True if self.board[self.row, self.column] == None else False


    def draw(self, colour):
        pygame.draw.rect(self.image, colour, (0, 0, self.width, self.height))

    
    def draw_symbol(self, current_player_symbol):
        #The tile symbol must always take precendence
        
        if self.symbol:
            sym = self.get_symbol_image(self.symbol)
        else: 
            sym = self.get_symbol_image(current_player_symbol)
        
        sym = pygame.transform.scale(sym, (self.width, self.height))
        self.screen.blit(sym, (self.x, self.y))
        
    def get_symbol_image(self, symbol):
        match symbol:
            case "O":
                return pygame.image.load("images/circle.png").convert_alpha()   
            case "X":
                return pygame.image.load("images/cross.png").convert_alpha()  

   
    
    def check_if_inside(self, x, y):
        if (self.x <= x <= self.x + self.width and 
            self.y <= y <= self.y + self.height):
            return True
        return False
    
    def reset(self):
        self.draw(WHITE)