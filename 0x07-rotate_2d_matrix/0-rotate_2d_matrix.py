#!/usr/bin/python3
""" Program that solves turning the contents of a matrix on 90 degress """


def rotate_2d_matrix(matrix):
    """function that reverse 2d matrix"""
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
