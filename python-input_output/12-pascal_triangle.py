#!/usr/bin/python3
"""
Module that returns Pascal’s triangle (n rows) as a list of integer lists..
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list of lists of int: A list where each element is a list
        representing a row of Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
