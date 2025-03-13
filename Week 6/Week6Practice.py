# Nama : Jackson Lawrence
# NIM : 000000
# Mata Kuliah : Numerical Analysis | IF420 - A

import numpy as np 
 
def my_ls_params(f, x, y): 
    A = np.zeros((len(x), len(f))) 
    for i, func in enumerate(f): 
        A[:, i] = func(x) 
 
    beta = np.linalg.lstsq(A, y, rcond=None)[0] 
 
    return beta 
 
def f1(x): 
    return np.ones_like(x) 
 
def f2(x): 
    return x 
 
x = np.linspace(0, 1, 101) 
y = 1 + x + x * np.random.random(len(x)) 
 
beta = my_ls_params([f1, f2], x, y) 
print(beta)