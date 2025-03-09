"""
Tic Tac Toe Player
"""
import copy
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
    # print("player")
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
    # print("actions")
    # find all the empty cells on the board, these are the available actions
    empty_cells = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_cells.add((i, j))
    return empty_cells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # print("result")
    # check for a negative out-of-bounds move, and if so, then throw an exception
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("Invalid move - out of bounds")

    # check if the cell is already filled, and if so, then throw an exception
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move - cell already filled")

    # mark the action on the board
    board[action[0]][action[1]] = player(board)
    return board

def revert_action(board, action):
    """
    Returns the board that results from reverting the move (i, j) on the board.
    """
    # print("revert_action")
    # un-mark the action on the board
    board[action[0]][action[1]] = EMPTY
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

    # check if there are any three consecutive X's or O's in a column
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return True, board[0][i]

    # check if there are any three consecutive X's or O's in diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return True, board[0][0]

    # check if there are any three consecutive X's or O's in other diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return True, board[0][2]

    # check if all the cells are filled
    if all(all(cell is not EMPTY for cell in row) for row in board):
        return True, None

    return False, EMPTY

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # print("utility")
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
    #return the best action for the current player using minimax algorithm

    if not terminal(board):
        if player(board) == X:
            v = -math.inf
            for action in actions(board):
                # create new board with the action
                new_board = copy.deepcopy(result(board, action))
                revert_action(board, action)

                # check if utility is 1, then return the action
                if utility(new_board) == 1:
                    return action

                max_val = min_value(new_board)
                if max_val > v:
                    v = max_val
                    best_action = action
        else:
            v = math.inf
            for action in actions(board):
                #create new board with the action
                new_board = copy.deepcopy(result(board, action))
                revert_action(board, action)

                # check if utility is -1, then return the action
                if utility(new_board) == -1:
                    return action

                min_val = max_value(new_board)
                if min_val < v:
                    v = min_val
                    best_action = action

    return best_action

def max_value(board):
    """
    Returns the max value of the board.
    """
    # print("max_value")
    #return the max value of the board
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        new_board = copy.deepcopy(result(board, action))
        revert_action(board, action)

        # check if utility is 1, then return the action
        if utility(new_board) == 1:
            return utility(new_board)
        else:
            max_val = utility(new_board) + min_value(new_board)
            if max_val > v:
                v = max_val

    return v

def min_value(board):
    """
    Returns the min value of the board.
    """
    # print("min_value")
    #return the min value of the board
    if terminal(board):
        return utility(board)

    v = math.inf
    best_action = None
    for action in actions(board):
        new_board = copy.deepcopy(result(board, action))
        revert_action(board, action)

        # check if utility is -1, then return the action
        if utility(new_board) == -1:
            return utility(new_board)
        else:
            min_val = utility(new_board) + max_value(new_board)
            if min_val < v:
                v = min_val
                best_action = action

    return v
