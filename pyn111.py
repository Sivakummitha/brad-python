import numpy as np
arr = np.array([1, 2, 3, 1, 2, 3, 4, 1, 2, 3])
sequence = np.array([1, 2, 3])
count = 0
for i in range(len(arr) - len(sequence) + 1):
    if np.array_equal(arr[i:i+len(sequence)], sequence):
        count += 1
print("Array:", arr)
print("Sequence:", sequence)
print("Number of occurrences:", count)
