"""A program for playing the game, Ludo."""

class Player:
    """A player in the game, Ludo.
    
    Attributes:
        name (str): the player's name.
        other_players (set of Person): other players in the game.
    """
    
class LudoBoard:
    
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
               
     def roll_dice(self):
            return random.randint(1, 6)

        def move_piece(self, player, piece):
            roll = self.roll_dice()
            new_position = self.players[player][piece] + roll

            if new_position <= 57:
                self.players[player][piece] = new_position

                if new_position == 57:
                    self.finished_pieces[player] += 1
                    if self.finished_pieces[player] == 4:
                        self.winner = player

        def play_game(self):
            while not self.winner:
                self.play_round()
             print(f"The winner is {self.winner}, congratulations!")


class Piece:
    def __init__(self, player_id, piece_id, position_id):
        self.player_id = player_id
        self.piece_id = piece_id
        self.position_id = position_id

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
    
class Select_Piece(Piece):
    def __init__(self, player, piece):
        self.player = player
        self.piece = piece 
        
    def selection(self):
        self.player = input("Which player are you?: ")
        self.piece = input("Which piece would you like to move? [1, 2, 3, 4]: ")    
        
    def __repr__(self):
        return f"{self.player} has selected {self.piece}"
        
        
      
    
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
