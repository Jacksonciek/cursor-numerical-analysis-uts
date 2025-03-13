# Nama : Jackson Lawrence
# NIM : 000000
# Mata Kuliah : Numerical Analysis | IF420 - A

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

x = np.linspace(0,1,101)
y = 1+x+x*np.random.random(len(x))

A = np.vstack([x,np.ones(len(x))]).T
y = y[:, np.newaxis]

alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
print(alpha)

plt.figure(figsize=(10,8))
plt.plot(x,y,'b.')
plt.plot(x,alpha[0]*x+alpha[1],'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()