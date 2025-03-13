# Nama : Jackson Lawrence
# NIM : 000000
# Mata Kuliah : Numerical Analysis | IF420 - A

import numpy as np 
from scipy.linalg import lstsq
 
def my_ls_params(f, x, y): 
    A = np.column_stack([f_i(x) for f_i in f])
    beta,_,_,_ = lstsq(A,y)
    return beta.reshape(-1,1)

def f1(x): 
    return np.ones_like(x) 
 
def f2(x): 
    return x 
 
x = np.linspace(0, 1, 101) 
y = 1 + x + x * np.random.random(len(x)) 
 
beta = my_ls_params([f1, f2], x, y) 
print(beta)