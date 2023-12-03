import time
from board import FourInARowBoard
from min_max_alpha_beta_player import MinimaxAlphaBetaPlayer
from min_max_player import MinimaxPlayer


PLAYER_1 = 0
PLAYER_2 = 1


def is_game_over(board, total_runtimes, player_names):
    for player in [PLAYER_1, PLAYER_2]:
        if board.check_winner(player + 1):
            board.display()
            print(f"Player {player + 1} wins!")
            print(f"Total runtime for {player_names[PLAYER_1]}: {total_runtimes[PLAYER_1]:.4f} seconds.")
            print(f"Total runtime for {player_names[PLAYER_2]}: {total_runtimes[PLAYER_2]:.4f} seconds.")
            faster_player = player_names[PLAYER_1] if total_runtimes[PLAYER_1] < total_runtimes[PLAYER_2] else player_names[PLAYER_2]
            print(f"{faster_player} is faster.")
            return True
    if board.is_full():
        board.display()
        print("It's a draw!")
        print(f"Total runtime for {player_names[PLAYER_1]}: {total_runtimes[PLAYER_1]:.4f} seconds.")
        print(f"Total runtime for {player_names[PLAYER_2]}: {total_runtimes[PLAYER_2]:.4f} seconds.")
        if total_runtimes[PLAYER_1] < total_runtimes[PLAYER_2]:
            print(f"{player_names[PLAYER_1]} is faster.")
        elif total_runtimes[PLAYER_1] > total_runtimes[PLAYER_2]:
            print(f"{player_names[PLAYER_2]} is faster.")
        else:
            print("Both players have the same runtime.")
        return True
    return False

if __name__ == "__main__":
    board = FourInARowBoard(rows=6, cols=7, winning_length=4)
    players = [MinimaxPlayer(1), MinimaxAlphaBetaPlayer(2)]
    player_names = ["Minimax", "Minimax with Alpha-Beta"]
    total_runtimes = [0, 0]

    for player, player_name in zip(players, player_names):
        print(f"Player {player_name}: {player.player}")

    while True:
        for player in players:
            board.display()

            start_time = time.time()
            col = player.get_move(board)
            end_time = time.time()

            player_index = player.player - 1
            total_runtimes[player_index] += end_time - start_time

            print(f"Player {player.player} took {end_time - start_time:.4f} seconds to make a move.")

            board.make_move(col, player.player)

            if is_game_over(board, total_runtimes, player_names):
                exit(0)
