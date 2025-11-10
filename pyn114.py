import numpy as np
arr = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
])
column_sum = np.sum(arr, axis=0)
print("Array:", arr)
print("Sum of each column:", column_sum)
