from argparse import ArgumentParser
import json
import random
import pandas as pd 
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt

class Board:
    def __init__(self):
        self.board = [0] * 52

    def __getitem__(self, index):
        return self.board[index]

    def __setitem__(self, index, value):
        self.board[index] = value


class Ludo:
    def __init__(self):
        self.board = Board()
        self.players = {1: [0]*4, 2: [0]*4}
        self.winner = None
        self.player1_spaces_moved = 0
        self.player2_spaces_moved = 0

    def print_board(self):
        for i, cell in enumerate(self.board):
            print(f'{cell:2}', end=' ')
            if (i + 1) % 13 == 0:
                print()

    def roll_dice(self):
        return random.randint(1, 6)

    def is_valid_move(self, player, piece, steps):
        pos = self.players[player][piece] + steps
        return pos <= 52
    
    def restart(self, position):
        player = self.board[position - 1] 
        if player != 0:
            self.board[position - 1] = 0
            piece = self.players[player].index(position)
            self.players[player][piece] = 0
            print(f"Player {player}'s piece got sent back to the start")
            
    def move_piece(self, player, piece, steps):
        old_pos = self.players[player][piece]
        new_pos = old_pos + steps
        self.restart(new_pos)
        
        #updating spaces moved attributes
        if self.players[player] == self.players[1]:
            self.player1_spaces_moved += steps
        else:
            self.player2_spaces_moved += steps

        # Remove piece from the old position
        if old_pos != 0:
            self.board[old_pos - 1] = 0

        # Place piece in the new position
        self.board[new_pos - 1] = player
        self.players[player][piece] = new_pos

        # Check for winner
        if new_pos == 52:
            self.winner = player

    def play_turn(self, player):
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
        turn = 0
        while not self.winner:
            player = 1 + (turn % 2)
            self.play_turn(player)
            self.print_board()
            turn += 1

        print(f"Congratulations, player {self.winner}! You have won the game!")
        
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
           "board": self.board,
           "players": self.players,
           "winner": self.winner,
           "player1_spaces_moved": self.player1_spaces_moved,
           "player2_spaces_moved": self.player2_spaces_moved 
        }
        
        with open(filepath, "w", encoding = "utf-8") as f:
            json.dump(saved_game, f)
            
    def load_game(self, filepath):
        with open(filepath, 'r') as openfile:
            loaded_game = json.load(openfile)
                  
        print(loaded_game)
        print(type(loaded_game))
        
def argument_parser(args):
    parser = ArgumentParser()
    parser.add_argument("--player1_name", type=str, help= "Allow player1 to change their name")
    parser.add_argument("--player2_name", type=str, help= "Allow player2 to change their name")
    parser.add_argument("--save_game", type=str, help= "Save game to JSON file")
    parser.add_argument("--load_game", type=str, help= "Load game from JSON file")
    return parser.parse_args(args)


if __name__ == "__main__":    
    args = argument_parser(sys.argv[1:])
   
    game = Ludo()
    
    if args.player1_name:
        game.players[1] = args.player1_name
        print(f"Player 1's name is {args.player1_name}")
    if args.player2_name:
        game.players[2] = args.player2_name
        print(f"Player 2's name is {args.playe21_name}")
    if args.load_game:
        game.load_game(args.load_game)
        print(f"The game has been loaded from {args.load_game}")
    
    game.play()
    
    if args.save_game:
        game.save_game(args.save_game)
        print(f"The game has been saved to {args.save_game}")
    
    game.bar_plot()
    
   
    
   
    