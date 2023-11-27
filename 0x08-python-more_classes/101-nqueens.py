#!/usr/bin/python3
"""
N-Queens problem
"""

import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col) on the board."""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col):
    """Recursive function to solve the N-Queens problem."""
    n = len(board)
    if col == n:
        print([[i, j] for i, row in enumerate(board) for j, val in enumerate(row) if val == 1])
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1)
            board[i][col] = 0

def nqueens(n):
    """Main function to solve the N-Queens problem."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)
