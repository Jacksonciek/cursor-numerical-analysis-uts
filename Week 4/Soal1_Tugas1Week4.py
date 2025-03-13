#Nama : Jackson Lawrence
#NIM : 00000070612
#Mata Kuliah : Numerical Analysis | IF 420 - A

import numpy as np

def gaussElimination(A, B):
    n = len(A)
    for i in range(n):
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[maxRow][i]):
                maxRow = k
        A[i], A[maxRow] = A[maxRow], A[i]
        B[i], B[maxRow] = B[maxRow], B[i]
        for k in range(i+1, n):
            faktor = A[k][i] / A[i][i]
            B[k] -= faktor * B[i]
            for j in range(i, n):
                A[k][j] -= faktor * A[i][j]
    X = [0] * n
    for i in range(n-1, -1, -1):
        X[i] = B[i] / A[i][i]
        for k in range(i-1, -1, -1):
            B[k] -= A[k][i] * X[i]
    return X

A = [[3, -1, 4],
     [17, 2, 1],
     [1, 12, -7]]

X = [2, 14, 54]

solution = gaussElimination(A, X)

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

print("\nResult:")
for i, x in enumerate(solution):
    rounded_x = round(x, 3)
    print(f"x{i+1} = {rounded_x}")
