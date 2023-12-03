class HumanPlayer:
    def __init__(self, player):
        self.player = player

    def get_move(self, board):
        while True:
            try:
                col = int(input(f"Player {self.player}, choose a column (0-{board.cols - 1}): "))
                if board.is_valid_move(col):
                    return col
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter a valid column number.")