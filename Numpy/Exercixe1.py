import numpy as np
from numpy import random
from numpy.random import rand

# 1.Create a matrix from a list which has 4 rows and 3 columns

a = ([[1, 2, 3],[4, 5, 8], [1, 2, 4], [5, 3, 32]])
a_array = np.array(a)

print(a_array)

# 2. Create the following matrix

b = ([[2, 7, 12, 0],[4, 9, 3, 4], [4, 0, 1,3]])
b_array = np.array(b)

print(b_array)

# 3.Create a 2D matrix with size of 10

matrix2d = np.random.randint(10, size=10).reshape(2,5)
print(matrix2d)


print("==========")

# 4.Create a 3D matrix of ones which has 2 rows, 3 columns, and 3 depth
matrix3d = np.ones((2,3,3))
print(matrix3d)
