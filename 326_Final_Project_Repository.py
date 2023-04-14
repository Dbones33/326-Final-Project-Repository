"""A program for playing the game, Ludo."""

class Player:
    """A player in the game, Ludo.
    
    Attributes:
        name (str): the player's name.
        other_players (set of Person): other players in the game.
    """
    
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
