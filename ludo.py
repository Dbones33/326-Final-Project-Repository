from argparse import ArgumentParser
import argparse
import json
import random
import pandas as pd 
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt

class Board:
    """Create the board for the game Ludo 
    
    Args:
        index (int): index of a cell on the board
        value (int): state of the cell on the board
        
    Attributes:
        board (list of int): a baord filled with 0's
        
    Returns:
        A board of 0's that is 4 rows and 13 columns
    """
    def __init__(self):
        """Creating the board that will have 52 0's 
        """
        self.board = [0] * 52

    def __getitem__(self, index):
        """Gives you the ability to access a certain cell on the board, subtracts 1 
        from the index
        
        Args:
            index (int): index of a cell on the board
            
        Returns: 
            the value of the cell on the board
        """
        return self.board[index - 1]

    def __setitem__(self, index, value):
        """Give you the ability to set the value of a cell when given its index
        
        Args:
            index (int): index of a cell on the board
            value (int): state of the cell on the board 
        """
        self.board[index - 1] = value
        
    def print_board(self):
        # Establishes a board with 0s for empty spaces
        
        # Side effects:
        #     evenly divide white space between board spaces
        #     print a board with all spaces set to empty spaces
        for i, cell in enumerate(self.board):
            print(f'{cell:2}', end=' ')
            if (i + 1) % 13 == 0:
                print()


class Ludo:
    # Demonstrates the board game, Ludo.
    
    #     Attributes:
    #     board(list of int): the board filled with '0' spaces
    #     players(dict of int): players 1 and 2 and four pieces assigned to each player
    #     winner(None): game's winner at the end of execution

    def __init__(self, player1_name, player2_name):
        # Initializes the players and board before playing Ludo.
        self.board = Board()
        self.players = {1: [0]*4, 2: [0]*4}
        self.winner = None
        self.player1_spaces_moved = 0
        self.player2_spaces_moved = 0
        self.player_name_dict = {1: player1_name, 2: player2_name}
        self.sent_back_count = {1: 0, 2:0}
        

    def print_board(self):
        """Prints the board within the Ludo class
        """
        self.board.print_board()

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
        return pos <= 52
    
    def restart(self, position):
        # Sends a player's piece back to start if another player lands on their space.
        
        # Args:
        #     position(int): space on the board
            
        # Side effects:
        #     A player's piece gets sent back to start if a player's piece lands on an occupied space
        player = self.board[position] 
        if player != 0:
            self.board[position] = 0
            piece = self.players[player].index(position)
            self.players[player][piece] = 0
            self.sent_back_count[player] += 1
            print(f"Player {player}'s piece got sent back to the start")
            
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
        
        #updating spaces moved attributes
        if player == 1:
            self.player1_spaces_moved += steps
        else:
            self.player2_spaces_moved += steps

        # Remove piece from the old position
        if old_pos != 0:
            self.board[old_pos] = 0

        # Place piece in the new position
        self.board[new_pos] = player
        self.players[player][piece] = new_pos

        # Check for winner
        if new_pos == 52:
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
        print(f"{self.player_name_dict[player]} rolled a {roll}.")

        valid_moves = [idx for idx, piece in enumerate(self.players[player]) 
                       if self.is_valid_move(player, idx, roll)]

        if not valid_moves:
            print("No valid moves. Skipping turn.")
            return

        while True:
            piece_choice = int(input(f"{self.player_name_dict[player]}, which piece do you want to move? {valid_moves}: "))

            if piece_choice in valid_moves:
                self.move_piece(player, piece_choice, roll)
                break
            else:
                print("Invalid choice. Try again.")
            
        save = input("Would you like to save the game? (y/n): ")
        if save == "y":
            filepath = input("Enter the name of a JSON file to save to: ")
            self.save_game(filepath)
            print("Game has been saved.")
            exit()
                
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
        
    def __repr__(self):
        print(f"{self.player_name_dict[1]} moved {self.player1_spaces_moved} spaces.")
        print(f"{self.player_name_dict[2]} moved {self.player1_spaces_moved} spaces.")
        print(f"{self.player_name_dict[1]} got sent back to start {self.sent_back_count[1]} times.")
        print(f"{self.player_name_dict[2]} got sent back to start {self.sent_back_count[2]} times.")
        
    def bar_plot(self):
        if self.winner:
            spaces_moved = OrderedDict([ ('Players', ['Player1', 'Player2']),
                            ('Spaces moved', [self.player1_spaces_moved, 
                            self.player2_spaces_moved]) ])  
            df = pd.DataFrame.from_dict(spaces_moved)
            df.plot.bar(x='Players', y='Spaces moved')
            plt.show()     
        
    def save_game(self, filepath):
        saved_game = {
           "board": self.board.board,
           "players": self.players,
           "winner": self.winner,
           "player1_spaces_moved": self.player1_spaces_moved,
           "player2_spaces_moved": self.player2_spaces_moved,
           "player_name_dict": self.player_name_dict
        }
        
        with open(filepath, "w", encoding = "utf-8") as f:
            json.dump(saved_game, f)
            
    def load_game(self, filepath):
        with open(filepath, 'r') as openfile:
            loaded_game = json.load(openfile)
         
        self.board.board = loaded_game["board"] 
        self.players = loaded_game["players"]
        self.winner = loaded_game["winner"]
        self.player1_spaces_moved = loaded_game["player1_spaces_moved"]
        self.player2_spaces_moved = loaded_game["player2_spaces_moved"]
        self.player_name_dict = loaded_game["player_name_dict"]       
        
        
def argument_parser(args):
    parser = ArgumentParser()
    parser.add_argument("--player1_name", default = "Player 1", type=str, 
                        help= "Allow player1 to change their name")
    parser.add_argument("--player2_name", default = "Player 2", type=str,
                        help= "Allow player2 to change their name")
    parser.add_argument("--load_game", type = argparse.FileType("r"),
                        help= "Load game from JSON file")
    return parser.parse_args(args)


if __name__ == "__main__":    
    args = argument_parser(sys.argv[1:])
   
    game = Ludo(args.player1_name, args.player2_name)
    
    if args.load_game:
        game.load_game(args.load_game)
        print(f"The game has been loaded from {args.load_game}")
    
    game.play()
    
    game.__repr__()
    
    game.bar_plot()
    
   
    
   
    