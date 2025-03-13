# Nama : Jackson Lawrence
# NIM : 00000070612
# Mata Kuliah : Numerical Analysis | IF420 - A

def my_lin_interp(a, b, C):
    hasil = []
    for x in C:
        i = 0
        while i < len(a)-1 and x > a[i+1]:
            i = i + 1
        if i < len(a) - 1:
            temp = (b[i+1] - b[i]) * (x - a[i]) / (a[i+1] - a[i])
            hasil.append(b[i] + temp)
        else:
            hasil.append(b[-1])
    return hasil

x = [0, 1, 2]
y = [1, 3, 2]
X = [0.0, 0.5, 1.0, 1.5, 2.0]

Y = my_lin_interp(x, y, X)
print(Y)

print("\n")

x2 = [-2, 0, 2, 3, 6]
y2 = [2, 0, 2, 1, 2]
X2 = [-1, -0.5, 0.5, 1, 2.5, 4, 5]

Y2 = my_lin_interp(x2, y2, X2)
print(Y2)

