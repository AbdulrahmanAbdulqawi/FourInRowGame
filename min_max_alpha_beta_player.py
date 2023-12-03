import random
import numpy as np
from board import FourInARowBoard
from min_max_player import MinimaxPlayer
from tree_node import TreeNode


class MinimaxAlphaBetaPlayer(MinimaxPlayer):
    def __init__(self, player, depth=5):
        super().__init__(player, depth)

    def get_move(self, board):
        root = TreeNode(board, self.player)
        _, move = self.minimax_alpha_beta(root, self.depth, self.player, float('-inf'), float('inf'), True)
        return move

    def minimax_alpha_beta(self, node, depth, player, alpha, beta, maximizing_player):
        if depth == 0 or node.board.is_full() or node.board.check_winner(3 - player):
            return self.evaluate(node.board, player), None

        valid_moves = [col for col in range(node.board.cols) if node.board.is_valid_move(col)]
        random.shuffle(valid_moves)

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for col in valid_moves:
                board_copy = FourInARowBoard()
                board_copy.board = np.copy(node.board.board)
                board_copy.make_move(col, player)
                child_node = TreeNode(board_copy, player)
                node.add_child(child_node)
                eval, _ = self.minimax_alpha_beta(child_node, depth - 1, player, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = col
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for col in valid_moves:
                board_copy = FourInARowBoard()
                board_copy.board = np.copy(node.board.board)
                board_copy.make_move(col, 3 - player)
                child_node = TreeNode(board_copy, 3 - player)
                node.add_child(child_node)
                eval, _ = self.minimax_alpha_beta(child_node, depth - 1, player, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = col
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move