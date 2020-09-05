"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    nr_X = 0
    nr_O = 0

    for row in board:
        for col in row:
            if col == X:
                nr_X += 1
            elif col == O:
                nr_O += 1

    if nr_X > nr_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avail_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                avail_actions.add((i, j))

    if len(avail_actions) == 0:
        return None
    else:
        return avail_actions


def make_move(board, action):
    if action in actions(board):
        this_player = player(board)
        board[action[0]][action[1]] = this_player
        return board
    else:
        return False


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        new_board = copy.deepcopy(board)
        return make_move(board, action)
    except ResultError:
        print('Invalid action')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check horizontally
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]

    # check vertically
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            return board[0][j]

    # check diagonally
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or \
            (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
                return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if actions(board) is None or winner(board) in [X, O]:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    this_winner = winner(board)

    if this_winner == X:
        return 1
    elif this_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        return None


def max_value(board):
    v = -math.inf

    # Base case
    if terminal(board):
        return utility(board)

    # Recursive case
    avail_actions = actions(board)
    for action in avail_actions:
        v = max(v, min_value(result(board, action)))
        return v


def min_value(board):
    v = math.inf

    # Base case
    if terminal(board):
        return utility(board)

    # Recursive case
    avail_actions = actions(board)
    for action in avail_actions:
        v = min(v, max_value(result(board, action)))
        return v


class Error(Exception):
    pass


class ResultError(Error):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
