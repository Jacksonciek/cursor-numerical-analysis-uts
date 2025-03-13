#Nama : Jackson Lawrence
#NIM : 00000070612
#Mata Kuliah : Numerical Analysis | IF 420 - A

import numpy as np

from scipy.linalg import lu

A = [[3, -1, 4],
     [17, 2, 1],
     [1, 12, -7]]

X = [2, 14, 54]

P, L, U = lu(A)

print("Equations :\n")
print("3𝑥1 − 𝑥2 + 4𝑥3 = 2")
print("17𝑥1 + 2𝑥2 +  𝑥3 = 14")
print("𝑥1 + 12𝑥2 − 7𝑥3 = 54")

print("\nEquations to Matrix\n")
print("[3\t-1\t 4]\t[x1]\t    [2]")
print("[17\t2\t 1]\t[x2]\t=   [14]")
print("[1\t12\t−7]\t[x3]\t    [54]")

print("\nAugmented Matrix : \n")
a = np.array([[3,-1,4,2],[17,2,1,14],[1,12,-7,54]])
print(a)

np.set_printoptions(precision=3)

print("\nLower Triangular Matrix:\n", L); 
print("\nUpper Triangular Matrix:\n", U); 
