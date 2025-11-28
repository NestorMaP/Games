import copy
import random

from PlayerEnum import Player
from Node import Node



EMPTY = '_'

def is_full_board(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

# Generate all boards, each one in a different state and the whole set of states
def create_boards(board, turn, level) -> Node:
    # Create the node to add it to the tree
    node = Node(board[:], turn)

    if (not is_full_board(board) and level >= 0):
        for i in range(len(board)):
            for j in range(len(board[i])):
                # Place X or O if it's available
                if(board[i][j] == EMPTY):
                    copy_of_board = copy.deepcopy(board)
                    copy_of_board[i][j] = turn
                    # Call recursion with new board
                    next_turn = Player.Player1 if turn == Player.Player2 else Player.Player2
                    children = create_boards(copy_of_board, next_turn, level-1)
                    if(children != None):
                        node.childrens.append(children)
        return node
    else:
        return None

init_player = random.choice(list(Player))

board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

# Empty boartd, first player and deep level
tree = create_boards(board, init_player, 4)