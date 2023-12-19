# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:32:44 2020
@author: Dartmoor
"""
import numpy as np
import matplotlib.pyplot as plt
import math
W1=0.6
W2=0.1

W3=0.5
W4=0.5

W5=0.1
W6=0.6

W7=0.1
W8=0.1
W9=0.1

W10=0.5
W11=0.5
W12=0.5

B1=0.2
B2=0.1
B3=0.2
B4=0.6
B5=0.0

def func(X):
    X=1/(1+(math.e**(-X))) 
    return X

X = np.arange(-100, 100, 1)
x = np.arange(-1.0, 1.001, 0.01)
Y = np.arange(-100, 100, 1)
y = np.arange(-1.0, 1.001, 0.01)

RX=list()
RX.append(list())
RX.append(list())

RY=list()
RY.append(list())
RY.append(list())

# for i in range(len(X)):
#     for j in range(len(Y)):
#         A1=func(X[i]*W1+Y[j]*W2+B1)
#         A2=func(X[i]*W3+Y[j]*W4+B2)
#         A3=func(X[i]*W5+Y[j]*W6+B3)
#         R1=func(A1*W7+A2*W8+A3*W9+B4)
#         R2=func(A1*W10+A2*W11+A3*W12+B5)
#         if R1>=R2:
#             RX[0].append(X[i])
#             RX[1].append(Y[j])
#         else:
#             RY[0].append(X[i])
#             RY[1].append(Y[j])

for i in range(len(X)):
    for j in range(len(Y)):
        A1=func(x[i]*W1+y[j]*W2+B1)
        A2=func(x[i]*W3+y[j]*W4+B2)
        A3=func(x[i]*W5+y[j]*W6+B3)
        R1=func(A1*W7+A2*W8+A3*W9+B4)
        R2=func(A1*W10+A2*W11+A3*W12+B5)
        if R1>=R2:
            RX[0].append(X[i])
            RX[1].append(Y[j])
        else:
            RY[0].append(X[i])
            RY[1].append(Y[j])

        
        
fig = plt.figure(figsize=(6, 4))
ax1 = fig.subplots()
plt.scatter(RX[0],RX[1], c='r')
plt.scatter(RY[0],RY[1], c='b')
plt.show()
