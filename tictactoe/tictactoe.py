"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    print("initial_state")
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    print("player")
    # count the number of X's and O's on the board
    num_X = 0
    num_O = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num_X += 1
            elif board[i][j] == O:
                num_O += 1

    # if there are more X's than O's, then it is O's turn
    if num_X > num_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    print("actions")
    # find all the empty cells on the board, these are the available actions
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_cells.append((i, j))
    return empty_cells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print("result")
    # mark the action on the board
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # print("winner")
    return end_game(board)[1]



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # print("terminal")
    # check if there are any three consecutive X's or O's in a row
    return end_game(board)[0]

def end_game(board):
    """
    Returns True if game is over and also returns the winner, False and Empty otherwise.
    """
    # print("end_game")
    # check if there are any three consecutive X's or O's in a row
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return True, board[i][0]

    # check if there are any three consecutive X's or O's in diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return True, board[0][0]

    # check if there are any three consecutive X's or O's in other diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return True, board[0][2]

    return False, EMPTY

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    print("utility")
    # if X has won, return 1, else if O has won, return -1, else return 0
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    print("minimax")
    best_action = None
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            board[action[0]][action[1]] = X
            max_v = utility(board)
            board[action[0]][action[1]] = EMPTY
            if max_v > v:
                v = max_v
                best_action = action
    else:
        v = math.inf
        for action in actions(board):
            board[action[0]][action[1]] = O
            min_v = utility(board)
            board[action[0]][action[1]] = EMPTY
            if min_v < v:
                v = min_v
                best_action = action
    return best_action
