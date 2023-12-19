# -*- coding: utf-8 -*-
"""
КЛАССИФИКАЦИЯ
КРАСНОЕ СИНИИЕ
ЦВЕТОЧКИ РАСПРЕДЕЛЕНЫ __НОРМАЛЬНО__ возле центра

"""
import numpy as np
import matplotlib.pyplot as plt
import math

np.random.seed(100)
 
# ПОЛЕ
X_min = -2
X_max =  2
Y_min =  0
Y_max =  1


N = 100

# НОРМАЛЬНОЕ РАСПРЕДЕЛЕНИЕ ЦВЕТОЧКОВ 

# Gx = -0.5 + 0.5 * np.random.randn(N)
# Gy =        0.5 * np.random.randn(N)
# G = np.column_stack((Gx,Gy))
# Bx =  0.5 + 0.5 * np.random.randn(N)
# By =        0.5 * np.random.randn(N)
# B = np.column_stack((Bx,By))
# print ('КРАСНЫЕ \n', G)
# print ('СИНИЕ \n', B)

# РАВНОМЕРНОЕ РАСПРЕДЕЛЕНИЕ ЦВЕТОЧКОВ 
Gx = np.random.uniform(-2,0,N)
Gy = np.random.uniform(0,1,N)

for i in range(N):
    Gy[i] = Gy[i] * 0.5*np.abs(Gx[i])

G  = np.column_stack((Gx,Gy))

Bx = np.random.uniform(-1.8, 2,N)
By = np.random.uniform(0,1,N)
for i in range(N):
    if Bx[i] < 0 : 
        By[i] = 1.0 - By[i]*np.abs(1.8+Bx[i])*0.5

B = np.column_stack((Bx,By))
print ('ЗЕЛЕНЫЕ \n', Gx,Gy)
print ('СИНИЕ \n', B)

#Разделительная кривая 
def class_line (x):
    return -0.5*x + .1

x = np.arange(X_min, X_max, 0.1)


fig = plt.figure(figsize=(8, 6))
ax1 = fig.subplots()
ax1.set(xlim=(X_min, X_max), ylim=(Y_min, Y_max))
plt.scatter(G[:,0],G[:,1], c='g')
plt.scatter(B[:,0],B[:,1], c='b')
plt.plot(x,class_line(x), c = 'r')
plt.show()

