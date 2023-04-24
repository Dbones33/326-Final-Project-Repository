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
    board = []
    i = 1
    while i <= 52:
        board.append(f"space{i}")
        i += 1

    yellow_finish_line = []
    count = 1
    while count <= 6:
        yellow_finish_line.append(f"space{i}")
        count += 1
    blue_finish_line = []
    count = 1
    while count <= 6:
        blue_finish_line.append(f"space{i}")
        count += 1
    orange_finish_line = []
    count = 1
    while count <= 6:
        orange_finish_line.append(f"space{i}")
        count += 1
    green_finish_line = []
    count = 1
    while count <= 6:
        green_finish_line.append(f"space{i}")
        count += 1   
               
def select_piece():
    """Player selects which piece to move for their turn.
    
    Args:
        player (str): the player's name
        piece (str): the player's piece 
        
    Returns:
        The piece that the player selected to play with for thier turn.
    
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
