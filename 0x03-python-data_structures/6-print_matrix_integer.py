#!/usr/bin/python3
def print_matrix_integer(matrix=None):
    if matrix is None:
        print()
    else:
        for row in matrix:
            for item in row:
                if row.index(item) != len(row) - 1:
                    endspace = " "
                else:
                    endspace = ""
                print("{:d}".format(item), end=endspace)
            print()
