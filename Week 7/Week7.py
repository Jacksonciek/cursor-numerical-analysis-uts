# Nama : Jackson Lawrence
# NIM : 00000070612
# Mata Kuliah : Numerical Analysis | IF420 - A

def my_lin_interp(a, b, C):
    hasil = []
    i = 0
    
    while i < len(C):
        if C[i] <= a[0]:  
            temp = (b[1] - b[0]) * (C[i] - a[0]) / (a[1] - a[0])
            hasil.append(b[0] + temp)
        elif C[i] >= a[-1]: 
            temp = (b[-1] - b[-2]) * (C[i] - a[-1]) / (a[-1] - a[-2])
            hasil.append(b[-1] + temp)
        else: 
            j = 0
            while a[j+1] < C[i]:
                j += 1
            temp = (b[j+1] - b[j]) * (C[i] - a[j]) / (a[j+1] - a[j])
            hasil.append(b[j] + temp)
        i = i + 1
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

