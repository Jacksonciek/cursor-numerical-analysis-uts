import numpy as np

from numpy.linalg import eig

a = np.array([[3,2],[5,3]])

characteristicEquation =  np.poly(a)
print("Characteristic equation : ", characteristicEquation)
print("\n")
c1 = round(characteristicEquation[0])
c2 = round(characteristicEquation[1])
c3 = round(characteristicEquation[2])
print("Coefficient of λ^2 :", c1)
print("Coefficient of λ :",  c2)
print("Constant term :", c3)
print("\nCharacteristic equation in λ : ")
print("(", c1, ")λ^2 + (", c2, ")λ + (" , c3, ")")
print("\n")

value, vector = eig(a)

print("Eigenvalue : ", value)
print("Eigenvector : ", vector)
print("\n")

print("Explanation : ")
for i in range(len(value)):
    print("When eigenvalue = ", value[i], ", the eigenvector is ", vector[:,i])

print("\n")
print("Check proving Ax = λx : ")
x = vector[:, 0]
lambdaOriginal = value[0]

Ax = np.dot(a,x)
lambdaX = lambdaOriginal * x

if np.allclose(Ax, lambdaX):
    print("Proved\nAx = λx")
    print("Ax = ", Ax)
    print("λx = ", lambdaX)
else :
    print("Ax ≠ λx")