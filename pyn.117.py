import numpy as np
arr = np.array(['Hello', 'Python', 'WORLD', 'NumPy'])
lengths = np.char.str_len(arr)
swapped = np.char.swapcase(arr)
print("Original Array:", arr)
print("Length of each string:", lengths)
print("Swapped Case Array:", swapped)
