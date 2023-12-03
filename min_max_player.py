import random
import numpy as np
from board import FourInARowBoard
from tree_node import TreeNode


class MinimaxPlayer:
    def __init__(self, player, depth=6):
        self.player = player
        self.depth = depth

    def get_move(self, board):
        root = TreeNode(board, self.player)
        _, move = self.minimax(root, self.depth, self.player, True)
        return move

    def minimax(self, node, depth, player, maximizing_player, alpha=float('-inf'), beta=float('inf')):
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
                eval, _ = self.minimax(child_node, depth - 1, player, False, alpha, beta)
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
                eval, _ = self.minimax(child_node, depth - 1, player, True, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_move = col
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def evaluate(self, board, player):
        score = 0
        for row in range(board.rows):
            for col in range(board.cols):
                if board.board[row][col] == player:
                    score += self.score_position(board, row, col, player)
                elif board.board[row][col] == 3 - player:
                    score -= self.score_position(board, row, col, 3 - player)
        return score

    def score_position(self, board, row, col, player):
        score = 0

        # Horizontal
        for c in range(col, col + board.winning_length):
            if c >= 0 and c < board.cols:
                if board.board[row][c] == player:
                    score += 1

        # Vertical
        for r in range(row, row + board.winning_length):
            if r >= 0 and r < board.rows:
                if board.board[r][col] == player:
                    score += 1

        # Diagonal /
        for i in range(board.winning_length):
            r, c = row - i, col + i
            if r >= 0 and r < board.rows and c >= 0 and c < board.cols:
                if board.board[r][c] == player:
                    score += 1

        # Diagonal \
        for i in range(board.winning_length):
            r, c = row + i, col + i
            if r >= 0 and r < board.rows and c >= 0 and c < board.cols:
                if board.board[r][c] == player:
                    score += 1

        return score