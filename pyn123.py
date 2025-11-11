import numpy as np
from scipy import linalg
A=np.array([[1,2],[2,3]])
B=np.array([[1,3],[2,4]])
print("matrix of A:\n",A)
print("matrix of B:\n",B)
det_A=linalg.det(A)
det_B=linalg.det(B)
inv_A=linalg.inv(A)
inv_B=linalg.inv(B)
matrix_mul=A@B
inverse_A=A@inv_A
inverse_B=B@inv_B
print("det_A:\n",det_A)
print("det_B:\n",det_B)
print("inv_A:\n",inv_A)
print("inv_B:\n",inv_B)
print("matrix multiplication:\n",matrix_mul)
print("inverse of a:\n",inv_A)
print("inverse of b:\n",inv_B)