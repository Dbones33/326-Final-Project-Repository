"""A program for playing the game, Ludo."""

class Player:
    """A player in the game, Ludo.
    
    Attributes:
        name (str): the player's name.
        other_players (set of Person): other players in the game.
    """
    
def create_board(self):
     """Creates five separate lists with string values that represents spaces
     on the board. One list for the general board, and four others for each of
     the color's separate finish lines."
            
        Side-effects:
            Will create five separate lists and modify them to have string 
            values for each space that the list should contain.      
            """
        
class Board:

    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]

    def place_piece(self, piece, x, y):
        if x < self.size and y < self.size:
            self.board[y][x] = piece
        else:
            raise ValueError("Invalid position entered.")

    def move_piece(self, piece, x, y):
        if x < self.size and y < self.size:
            piece_x, piece_y = (-1, -1)

            for i in range(self.size):
                for j in range(self.size):
                    if self.board[j][i] == piece:
                        piece_x, piece_y = (i, j)
                        break

            if piece_x != -1 and piece_y != -1:
                self.board[piece_y][piece_x] = None
                self.board[y][x] = piece
            else:
                raise ValueError("Piece not found on board.")
        else:
            raise ValueError("Invalid position entered.")

    def print_board(self):
        for row in self.board:
            print(row)


class Piece:
    def __init__(self, player_id, piece_id):
        self.player_id = player_id
        self.piece_id = piece_id

    def __repr__(self):
        return f"P{self.player_id}_{self.piece_id}"

# Example usage:
board = Board(15)
piece1 = Piece(1, 1)
piece2 = Piece(1, 2)
board.place_piece(piece1, 0, 0)
board.place_piece(piece2, 1, 1)
board.print_board()
board.move_piece(piece1, 3, 3)
board.print_board()
               
def select_piece():
    """Player selects which piece to move for their turn.
    
    Args:
        player (str): the player's name
        piece (str): the player's piece 
        
    Returns:
        The piece that the player selected to play with for their turn.
    
    """
    
def rotate():
    '''Moves player pieces around the game board.
    
    Args:
        name(str): player's name
        piece(str): player's piece
        location(int): current piece location on the board
        
    Returns:
        A player piece's location after it moves 
    '''
    # My implementation of rotate
    
# Someone take over
def restart():
    """If a player lands on a spot that contains a piece from an opposing
    player, that opposing player's piece will be returned to the start
    
    # Would write an if statement with a loop to send the piece back to the
    start position
    
    Args: 
        name(str): player's name
        piece(str): player's piece
        location(int): current piece location on the board
        start(int): the starting location where the pieces are sent back
    
    Returns:
        The players peice back to the start position
    """
