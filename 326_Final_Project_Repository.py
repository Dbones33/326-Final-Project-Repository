"""A program for playing the game, Ludo."""
import random

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

class Ludo:
    def __init__(self):
        self.board = [0]*52
        self.players = {1: [0]*4, 2: [0]*4}
        self.winner = None

    def print_board(self):
        for i, cell in enumerate(self.board):
            print(f'{cell:2}', end=' ')
            if (i + 1) % 13 == 0:
                print()

    def roll_dice(self):
        return random.randint(1, 6)

    def is_valid_move(self, player, piece, steps):
        pos = self.players[player][piece] + steps
        return pos <= 51

    def move_piece(self, player, piece, steps):
        old_pos = self.players[player][piece]
        new_pos = old_pos + steps

        # Remove piece from the old position
        if old_pos != 0:
            self.board[old_pos - 1] = 0

        # Place piece in the new position
        self.board[new_pos - 1] = player
        self.players[player][piece] = new_pos

        # Check for winner
        if new_pos == 51:
            self.winner = player

    def play_turn(self, player):
        roll = self.roll_dice()
        print(f"Player {player} rolled a {roll}.")

        valid_moves = [idx for idx, piece in enumerate(self.players[player]) if self.is_valid_move(player, idx, roll)]

        if not valid_moves:
            print("No valid moves. Skipping turn.")
            return

        while True:
            piece_choice = int(input(f"Player {player}, which piece do you want to move? {valid_moves}: ")) - 1

            if piece_choice in valid_moves:
                self.move_piece(player, piece_choice, roll)
                break
            else:
                print("Invalid choice. Try again.")

    def play(self):
        turn = 0
        while not self.winner:
            player = 1 + (turn % 2)
            self.play_turn(player)
            self.print_board()
            turn += 1

        print(f"Congratulations, player {self.winner}! You have won the game!")


if __name__ == "__main__":
    game = Ludo()
    game.play()
     
     
     
          
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
