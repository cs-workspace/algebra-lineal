"""
Algebra Lineal - Lab 10
Entrega: 23 Nov. 2020
@steven_wilson

"""

import numpy as np

A = np.array([[4,0],
              [3,1]])
print(A)
b = np.array([[-1.41421],
              [1.41421],
              [-1.41421],
              [1.41421],
              [1.41421]])
print(b)


q, r = np.linalg.qr(A)

y = np.dot(np.transpose(q), b)

x = np.dot(np.linalg.inv(r), y)

print(x)
