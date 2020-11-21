"""
Created By: Damian Young
Project: Sudoku Solver
Description: Simple backtracking algorithm implementation
             to solve any Sudoku puzzle that has a solution
"""
def solve(board):
    """
    Solves a sudoku board using backtracking
    :param board: 2d list of ints
    :return: completed sudoku solution
    """
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def find_empty(board):
    """
    Finds an empty space in the board
    :param board: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None