# -*- coding: utf-8 -*-
"""
КЛАССИФИКАЦИЯ
КРАСНЫЕ СИНИИЕ
ЛИНЕЙНО РАЗДЕЛЕННОЕ ПРОСТРАНСТВА

НЕЙРОНКА  из ПРИМЕРА

"""
import numpy as np
import matplotlib.pyplot as plt


W1 = 0.6
W2 = 0.1

W3 = 0.5
W4 = 0.5

W5 = 0.1
W6 = 0.6

W7 = 0.1
W8 = 0.1
W9 = 0.1

W10 = 0.5
W11 = 0.5
W12 = 0.5

B1 = 0.2
B2 = 0.1
B3 = 0.2
B4 = 0.6
B5 = 0.0


# def func(X):
#     X=1/(1+(math.e**(-X))
#     return X

def func(X):
    '''
    Tis is function
    '''
    return X


NX = 100
NY = 100

X = np.arange(-NX, NX, 1)
x = np.arange(-1.0, 1.001, 1/NX)
Y = np.arange(-NY, NY, 1)
y = np.arange(-1.0, 1.001, 1/NY)

FR = list()
FR.append(list())
FR.append(list())

FB = list()
FB.append(list())
FB.append(list())

print('КРАСНЫЕ', FR, 'СИНИЕ', FB)

FL = list()
FL.append(list())
FL.append(list())


for i in range(len(X)):
    for j in range(len(Y)):
        A1 = func(X[i]*W1+Y[j]*W2+B1)
        A2 = func(X[i]*W3+Y[j]*W4+B2)
        A3 = func(X[i]*W5+Y[j]*W6+B3)
        R1 = func(A1*W7+A2*W8+A3*W9+B4)
        R2 = func(A1*W10+A2*W11+A3*W12+B5)
        if R1 >= (R2 + 2):
            FR[0].append(X[i])
            FR[1].append(Y[j])
        elif R1 <= (R2 - 2):
            FB[0].append(X[i])
            FB[1].append(Y[j])

# for i in range(len(X)):
#     for j in range(len(Y)):
#         A1=func(x[i]*W1+y[j]*W2+B1)
#         A2=func(x[i]*W3+y[j]*W4+B2)
#         A3=func(x[i]*W5+y[j]*W6+B3)
#         R1=func(A1*W7+A2*W8+A3*W9+B4)
#         R2=func(A1*W10+A2*W11+A3*W12+B5)
#         if R1 >= (R2 + 0.005):
#             FR[0].append(X[i])
#             FR[1].append(Y[j])
#         elif R1 <= (R2 - 0.005):
#             FB[0].append(X[i])
#             FB[1].append(Y[j])

fig = plt.figure(figsize=(8, 6))
ax1 = fig.subplots()
plt.scatter(FR[0], FR[1], c='r')
plt.scatter(FB[0], FB[1], c='b')
plt.show()


for i in range(len(X)):
    for j in range(len(Y)):
        A1 = func(X[i]*W1+Y[j]*W2+B1)
        A2 = func(X[i]*W3+Y[j]*W4+B2)
        A3 = func(X[i]*W5+Y[j]*W6+B3)
        R1 = func(A1*W7+A2*W8+A3*W9+B4)
        R2 = func(A1*W10+A2*W11+A3*W12+B5)
        if np.abs(R1-R2) < 0.5:
            FL[0].append(X[i])
            FL[1].append(Y[j])

fig = plt.figure(figsize=(8, 6))
ax1 = fig.subplots()
plt.scatter(FL[0], FL[1], c='g')
plt.show()
