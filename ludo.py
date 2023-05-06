import random

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
    
    def restart(self, position):
        player = self.board[position - 1] 
        if player != 0:
            self.board[position - 1] = 0
            piece = self.players[player].index(position)
            self.players[player][piece] = 0
            print(f"Player {player}'s piece will get sent back to start")
            
    def move_piece(self, player, piece, steps):
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

    def who_is_winning(self):
        p1_pieces_finished = 0
        for piece in self.players[1]:
            if piece == 51:
                p1_pieces_finished += 1
        p2_pieces_finished = 0
        for piece in self.players[2]:
            if piece == 51:
                p2_pieces_finished += 1
        if p1_pieces_finished != p1_pieces_finished:
            if max(p1_pieces_finished, p2_pieces_finished)==p1_pieces_finished:
                return f"Player1 is winning!"
            else:
                return f"Player2 is winning!"
        else:
            return f"The two players are tied!"

if __name__ == "__main__":
    game = Ludo()
    game.play()