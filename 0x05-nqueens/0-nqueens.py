#!/usr/bin/python3
"""The nqueen puzzle program that find the possible places
where the queen can be kept without colliding with other
queen in the chess board
"""
import sys


def nqueens(n: int):
    """Args: n type int
    """
    if not isinstance(n, int):
        print("N must be a number \n")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4 \n")
        sys.exit(1)

    def backtrack(board, row, solutions):
        """this function create another board similar to the previous board
        """
        if row == n:
            solutions.append([col[:] for col in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                backtrack(board, row + 1, solutions)
                board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    solutions = []
    backtrack(board, 0, solutions)
    return solutions


def is_valid(board, row, col):
    """
        Check this column on the current and upper rows
        Check upper left diagonal
    """
    n = len(board)

    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nqueens.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = nqueens(n)
    for solution in solutions:
        print(solution)
