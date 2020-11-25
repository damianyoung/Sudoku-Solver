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

    for i in range(1, 10):
        if is_valid(board, (row, col), i):
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


def is_valid(bo, pos, num):
    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """

    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    """
    prints the board
    :param bo: 2d List of ints
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")


# create the board
BOARD = [
        [0, 0, 0, 7, 9, 0, 0, 3, 4],
        [5, 0, 9, 2, 0, 0, 0, 1, 8],
        [0, 3, 0, 6, 0, 0, 0, 0, 0],
        [2, 4, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 4, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 4, 7],
        [0, 0, 0, 0, 0, 8, 0, 2, 0],
        [1, 8, 0, 0, 0, 2, 4, 0, 3],
        [4, 7, 0, 0, 1, 3, 0, 0, 0]
]

solve(BOARD)
print_board(BOARD)
