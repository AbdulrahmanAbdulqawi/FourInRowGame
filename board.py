import numpy as np

class FourInARowBoard:
    def __init__(self, rows=6, cols=7, winning_length=4):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.winning_length = winning_length

    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.board[0][col] == 0

    def make_move(self, col, player):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return True
        return False

    def is_full(self):
        return np.all(self.board != 0)

    def check_winner(self, player):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == player:
                    if self.check_direction(player, row, col, 1, 0) or \
                       self.check_direction(player, row, col, 0, 1) or \
                       self.check_direction(player, row, col, 1, 1) or \
                       self.check_direction(player, row, col, 1, -1):
                        return True
        return False

    def check_direction(self, player, row, col, dr, dc):
        for _ in range(self.winning_length - 1):
            row += dr
            col += dc
            if not (0 <= row < self.rows and 0 <= col < self.cols) or self.board[row][col] != player:
                return False
        return True

    def display(self):
        for row in self.board:
            print(" ".join(map(str, row)))
        print("==============")
