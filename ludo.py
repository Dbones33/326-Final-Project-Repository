import random

class Ludo:
    # Demonstrates the board game, Ludo.
    
    #     Attributes:
    #     board(list of int): the board filled with '0' spaces
    #     players(dict of int): players 1 and 2 and four pieces assigned to each player
    #     winner(None): game's winner at the end of execution
    
    def __init__(self):
    # Initializes the players and board before playing Ludo.
        self.board = [0]*52
        self.players = {1: [0]*4, 2: [0]*4}
        self.winner = None

    def print_board(self):
        # Establishes a board with 0s for empty spaces
        
        # Side effects:
        #     evenly divide white space between board spaces
        #     print a board with all spaces set to empty spaces
        for i, cell in enumerate(self.board):
            print(f'{cell:2}', end=' ')
            if (i + 1) % 13 == 0:
                print()

    def roll_dice(self):
        # Rolls a die for each player's turn
        
        # Returns: 
        #     A random dice roll between 1-6
        return random.randint(1, 6)

    def is_valid_move(self, player, piece, steps):
        # Ensures that a player's piece does not go over the board's dimensions.
        
        # Args:
        #     player(int): each player in the game
        #     piece(int): board game piece from 0-3
        #     steps(int): number of spaces a piece moves after the dice roll
            
        # Returns:
        #     a space inside the board's dimensions
        pos = self.players[player][piece] + steps
        return pos <= 51
    
    def restart(self, position):
        # Sends a player's piece back to start if another player lands on their space.
        
        # Args:
        #     position(int): space on the board
            
        # Side effects:
        #     A player's piece gets sent back to start if a player's piece lands on an occupied space
        player = self.board[position - 1] 
        if player != 0:
            self.board[position - 1] = 0
            piece = self.players[player].index(position)
            self.players[player][piece] = 0
            print(f"Player {player}'s piece will get sent back to start")
            
    def move_piece(self, player, piece, steps):
        # Moves a player's piece from either start or their previous position
        # to a new space on the board.
        
        # Args:
        #     player(int): each player in the game
        #     piece(int): board game piece from 0-3
        #     steps(int): number of spaces a piece moves after the dice roll
        
        # Returns:
        #     the board with a moved piece from the last position
        old_pos = self.players[player][piece]
        new_pos = old_pos + steps
        self.restart(new_pos)

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
        # Calls the dice method and prompts the player to select a piece that they can move.
        
        # Args:
        #     player(int): each player in the game
            
        # Returns:
        #     A skipped turn
        #     A turn with a player moving one of their pieces
            
        # Side effects:
        #     A user will have to select a piece they can move if the piece they want to move
        #     cannot move from its current position.
        roll = self.roll_dice()
        print(f"Player {player} rolled a {roll}.")

        valid_moves = [idx for idx, piece in enumerate(self.players[player]) if self.is_valid_move(player, idx, roll)]

        if not valid_moves:
            print("No valid moves. Skipping turn.")
            return

        while True:
            piece_choice = int(input(f"Player {player}, which piece do you want to move? {valid_moves}: "))

            if piece_choice in valid_moves:
                self.move_piece(player, piece_choice, roll)
                break
            else:
                print("Invalid choice. Try again.")

    def play(self):
        # Starts the ludo game from turn 1
        
        # Args:
        #     player(int): specific player in the game
        #     turn(int): rotation of players rolling dice and moving pieces
            
        # Side effects:
        #     print a player winner depending on which player moves all their pieces to their goal
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