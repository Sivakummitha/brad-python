from scipy import io
import numpy as np
arr = np.array([[1, 2], [3, 4]])
io.savemat("example.mat", {"array": arr})
data = io.loadmat("example.mat")
print(data["array"])
