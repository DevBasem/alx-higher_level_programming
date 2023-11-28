#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): The matrix to be divided, each element
        should be int or float.
        div (int or float): The dividing number.

    Raises:
        TypeError: If matrix is not a list of lists of int or float,
                   or each row of matrix is not of the same size,
                   or div is neither an int nor float.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with elements rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0 or not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
