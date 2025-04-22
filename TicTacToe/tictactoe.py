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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X 
    
    numX , numO = 0 , 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X :
                numX += 1
            elif board[i][j] == O :
                numO += 1
    
    if numX > numO :
        return O
    else :
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    moves = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY :
                moves.add((i, j))

    return moves 



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action 
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] is not EMPTY:
        raise ValueError("Invalid move: Cell is already occupied or out of bounds.")
    
    import copy 

    newBoard = copy.deepcopy(board)
    newBoard[i][j] = player(newBoard)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in board:
        if i[0] == i[1] == i[2] and i[0] is not None:
            return i[0]
        
    for j in range(len(board[0])):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None :
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    return True 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    Winner = winner(board) 
    if Winner == X :
        return 1 
    elif Winner == O :
        return -1 
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None 
    
    currentPlayer = player(board)

    if currentPlayer == X :
        best = float(-2)
        move = None

        allMoves = actions(board) 
        for action in allMoves:
            value = min_value(result(board, action))
            if value > best:
                best = value
                move = action

    if currentPlayer == O :

        best = float(2)
        move = None

        allMoves = actions(board)
        for action in allMoves:
            value = max_value(result(board, action))
            if value < best :
                best = value 
                move = action

    return move 

def min_value(board):
    if terminal(board):
        return utility(board)

    v = float(2)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v

def max_value(board):
    if terminal(board):
        return utility(board)

    v = float(-2)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v
