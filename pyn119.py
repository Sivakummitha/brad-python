import numpy as np
arr = np.array([10, 20, 10, 30, 20, 10, 40])
unique, counts = np.unique(arr, return_counts=True)
reversed_arr = arr[::-1]
print("Original Array:", arr)
print("Unique Values:", unique)
print("Frequency of Each Value:", counts)
print("Reversed Array:", reversed_arr)
