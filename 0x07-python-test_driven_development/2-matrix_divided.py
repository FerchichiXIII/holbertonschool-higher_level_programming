#!/usr/bin/python3
"""
Write a function
that divides all
elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix
    """
    if not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for l in matrix:
        if not isinstance(l, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for i in l:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    for l in matrix:
        if len(l) == 0:
            raise TypeError("div must be a number")
        if not isinstance(div, int) and not isinstance(int, float):
            raise TypeError("div must be a number")
        if not all(len(l)) == len(matrix[0]for l in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        return [[round(i / div, 2)for i in l]for lists in matrix]
