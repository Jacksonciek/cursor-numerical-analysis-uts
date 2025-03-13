import numpy as np

A = [[3, -1, 4],
     [17, 2, 1],
     [1, 12, -7]]

X = [2, 14, 54]

result = np.linalg.solve(A,X)

np.set_printoptions(precision=3)

print(result)