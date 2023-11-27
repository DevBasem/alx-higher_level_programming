#!/usr/bin/python3
"""
Solves the N-queens puzzle.

Places N non-attacking queens on an N×N chessboard.

Usage:
    nqueens N

If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1

The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
Read: Queen, Backtracking
"""

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at a given position."""
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board):
    """Print the solution in the specified format."""
    solution = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def solve_nqueens(n):
    """Solve the N-queens puzzle."""
    board = [[0] * n for _ in range(n)]
    solve_util(board, 0, n)


def solve_util(board, row, n):
    """Utility function to solve the N-queens puzzle."""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_util(board, row + 1, n)
            board[row][col] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
