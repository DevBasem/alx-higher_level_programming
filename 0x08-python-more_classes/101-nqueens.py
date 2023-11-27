#!/usr/bin/python3
"""101-nqueens finds all possible solutions to the N queens puzzle.

Attempted virtual backtracking without recursion.

Attributes:
    N (int): base number of queens, and length of board side in piece positions
    candidates (list): list of all successful solutions for a given
        amount of columns checked
"""
from sys import argv

if len(argv) is not 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def init_candidate_board(board=[]):
    """Adds a column of zeroes to the right of any board about to be tested.

    Args:
        board (list): 2D list of ints, only as wide as needed to test
            the rightmost column for queen conflicts.

    Returns:
        modified 2D list
    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):
    """Sets "queen," or 1, to coordinates given in board.

    Args:
        board (list): 2D list of ints, only as wide as needed to test
            the rightmost column for queen conflicts.
        row (int): first dimension index
        col (int): second dimension index
    """
    board[row][col] = 1


def is_new_queen_safe(board, row, col):
    """Checks for conflicts in placing a new queen at given coordinates.

    Args:
        board (list): 2D list of ints, only as wide as needed to test
            the rightmost column for queen conflicts.
        row (int): first dimension index
        col (int): second dimension index

    Returns:
        True if no left side conflicts found for new queen, False otherwise.
    """
    x, y = row, col

    for i in range(1, N):
        if (y - i) >= 0:
            # check up-left diagonal
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # check left
            if board[x][y - i]:
                return False
            # check down-left diagonal
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coordinate_format(candidates):
    """Converts a board (matrix of 1 and 0) into a series of row/column
    indices of each queen/1.

    Args:
        candidates (list): list of all successful solutions for the
            amount of columns last checked

    Returns:
        holberton, the list of coordinates
    """
    holberton = []
    for x, attempt in enumerate(candidates):
        holberton.append([])
        for i, row in enumerate(attempt):
            holberton[x].append([])
            for j, col in enumerate(row):
                if col:
                    holberton[x][i].append(i)
                    holberton[x][i].append(j)
    return holberton


# init candidates list with the first column of 0s
candidates = [init_candidate_board()]

# proceed column by column, testing the rightmost
for col in range(N):
    # start a new generation of the candidate list for every round of testing
    new_candidates = []
    # test each candidate from the previous round, at the current column
    for matrix in candidates:
        # for every row in that candidate's rightmost column
        for row in range(N):
            # are there any conflicts in placing a queen at those coordinates?
            if is_new_queen_safe(matrix, row, col):
                # no? then create a "child" (copy) of that candidate
                temp = [line[:] for line in matrix]
                # place a queen in that position
                add_queen(temp, row, col)
                # and unless you're in the last round of testing,
                if col < N - 1:
                    # add a new column of 0s on the right for the next round
                    init_candidate_board(temp)
                # add that new candidate to this round's list of successes
                new_candidates.append(temp)
    # when finished with the round, discard the "parent" candidates
    candidates = new_candidates

# format results to match assignment output
for item in coordinate_format(candidates):
    print(item)
