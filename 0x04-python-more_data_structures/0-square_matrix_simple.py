#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    squared_matrix = [[0 for _ in range(len(matrix[0]))]
                      for _ in range(len(matrix))]

    # Iterate through each element in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Square the element and store it in the new matrix
            squared_matrix[i][j] = matrix[i][j] ** 2

    return squared_matrix
