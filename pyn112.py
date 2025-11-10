import numpy as np
matrix = np.array([
    [5, 8, 2],
    [3, 7, 9],
    [1, 6, 4]
])
rows, cols = matrix.shape
max_value = np.max(matrix)
min_value = np.min(matrix)
print("Matrix:", matrix)
print("Number of rows:", rows)
print("Number of columns:", cols)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
