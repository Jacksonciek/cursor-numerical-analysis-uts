#Nama : Jackson Lawrence
#NIM : 00000070612
#Mata Kuliah : Numerical Analysis | IF 420 - A

import numpy as np

def gaussJordanElimination(A, B):
    n = len(A)
    M = A
    i = 0
    for x in M:
        x.append(B[i])
        i += 1
    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass
        for j in range(k+1, n):
            q = M[j][k] / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]
    x = [0 for i in range(n)]
    x[n-1] = M[n-1][n] / M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z  + M[i][j]*x[j]
        x[i] = (M[i][n] - z) / M[i][i]
    return x

A = [[3, -1, 4],
     [17, 2, 1],
     [1, 12, -7]]

X = [2, 14, 54]

solution = gaussJordanElimination(A, X)

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
print(gaussJordanElimination(A,X),"\n")
for i, x in enumerate(solution):
    rounded_x = round(x, 3)
    print(f"x{i+1} = {rounded_x}")