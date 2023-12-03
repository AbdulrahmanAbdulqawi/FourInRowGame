class TreeNode:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)