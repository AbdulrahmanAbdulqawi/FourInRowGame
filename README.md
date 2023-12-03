
Task 1 report
Four in Row Game Implementation and Performance Analysis Report

Introduction
Four in Row game is a classic two-player board game in which the objective is to be the first to form a line of four of one's own discs, either horizontally, vertically, or diagonally. In this report, we discuss the implementation of the Four in Row game in Python and analyze the performance of two AI players using the Minimax algorithm with and without alpha-beta pruning.
Game Implementation
Components
The game implementation consists of the following components:
•	FourInARowBoard: Represents the game board, checks for valid moves, records player moves, and determines the winner.
•	HumanPlayer: Represents a human player.
•	MinMinimaxPlayer: Represents an AI player using the Minimax algorithm without alpha-beta pruning.
•	MinMaxAlphaBetaPlayer: Represents an AI player using the Minimax algorithm with alpha-beta pruning.
•	Main: Manages the game flow and player interactions.
Performance Analysis
Comparison of Minimax Players
To evaluate the performance of the Minimax algorithm with and without alpha-beta pruning, we set up a game between two AI players: one using Minimax (MinMinimaxPlayer) and the other using Minimax with alpha-beta pruning (MinMaxAlphaBetaPlayer). We measured the runtime of each game to assess which player was faster in terms of decision-making.
Results
•	Minimax Player (without Alpha-Beta Pruning): The game between two Minimax players without alpha-beta pruning took a certain amount of time to complete.
•	Minimax Alpha-Beta Player: The game between two Minimax players with alpha-beta pruning took significantly less time to complete.
Conclusion
The performance analysis demonstrates that the Minimax algorithm with alpha-beta pruning is faster and more efficient compared to the Minimax algorithm without alpha-beta pruning. This result can be attributed to the following reasons:
1.	Alpha-Beta Pruning: Alpha-beta pruning is an optimization technique that allows the algorithm to prune branches of the game tree that are guaranteed not to affect the final decision. It reduces the number of nodes explored, resulting in a shallower search and faster decision-making.
2.	Time Complexity: The Minimax algorithm without alpha-beta pruning has an exponential time complexity in the depth of the game tree. In games with a large branching factor like Four in Row, this can lead to a slow decision-making process. Alpha-beta pruning significantly reduces the effective branching factor, leading to shorter search times.
3.	Search Space Reduction: Alpha-beta pruning efficiently identifies promising and unpromising moves early in the search, reducing the search space. This reduction in the number of evaluated positions results in faster decisions.
In conclusion, the implementation and analysis of the Four in Row game reveal that the Minimax algorithm with alpha-beta pruning outperforms the Minimax algorithm without alpha-beta pruning in terms of runtime. This is due to the effective pruning of branches in the game tree, reducing the search space and allowing for quicker decision-making. Alpha-beta pruning is a crucial optimization that enhances the efficiency of the Minimax algorithm in game-playing scenarios.

