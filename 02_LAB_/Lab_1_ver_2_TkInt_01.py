# -*- coding: utf-8 -*-
"""
Created on  Aug  28  2023
@author: evgbash

ДЛЯ ЛАБОРАТОРНОЙ 1
КЛАССИФИКАЦИЯ  ЗЕЛЕНЫЕ / СИНИИЕ

СЕТЬ ИЗ ПЯТИ НЕЙРОНОВ. 2 ВХОДНЫХ, ДВА в скрытом слое
ОДИН ВЫХОДНОЙ 
!!!!  ИНТЕРАКТИВНОСТИ НЕТ. ПРОСТО ЗАДАЕМ ЗНАЧЕНИЯ КОЭФФИЦИЕНТОВ

СТРОИТСЯ НЕЯВНО ЗАДАННАЯ РАЗДЕЛЯЮЩАЯ КРИВАЯ (выход последнего нейрона )

В ЦВЕТЕ ПРОСТО ОТОБРАЖАЕЮТЯ ЦВЕТОЧКИ НАД и ПОД РАЗДЕЛЯЮЩЕЙ КРИВОЙ

"""
import numpy as np
import matplotlib.pyplot as plt


# ФУНКЦИИ АКТИВАЦИИ
# функция активации - линейная
def activation_linear (x):
    return (x)
# функция активации - сигмоида
def activation_sigmoid (x):
    return 1/(1+np.exp(-x))
# функция активации - гипертангент
def activation_tanh (x):
    return np.tanh(x)
# функция активации - signum
def activation_signum (x):
    return np.sign(x)


# ФУНКЦИЯ НЕЙРОНКИ
def nn_out (x,y,func):
    A1 = x
    A2 = y 
    A3 = func(A1*W13+A2*W23+B3)
    A4 = func(A1*W14+A2*W24+B4)
    A5 = func(A3*W35+A4*W45+B5)        
    return A5


# ВЕСА и СМЕЩЕНИЯ НЕЙРОНОВ
# ВЕСА и СМЕЩЕНИЕ НЕЙРОНА 3
W13 = 0.1
W23 = -0.2
B3  = -0.9
# ВЕСА и СМЕЩЕНИЕ НЕЙРОНА 4
W14 = 0.5
W24 = 0.9
B4  = 1.
# ВЕСА и СМЕЩЕНИЕ НЕЙРОНА 5
W35 = 0.1
W45 = 0.6
B5 = -0.5


x_test = 0
y_test = 0
test_out = nn_out (x_test, y_test, activation_tanh) 
print ('X = ', x_test, 'Y = ', y_test, 'X = ', test_out)


NX = 50
NY = 50

X = np.linspace(-10, 10, NX)
Y = np.linspace(-10, 10, NY)

GF = list()
GF.append(list())
GF.append(list())

BF = list()
BF.append(list())
BF.append(list())

print('ЗЕЛЕНЫЕ', GF, 'СИНИЕ', BF)

for i in range(len(X)):
    for j in range(len(Y)):
        
        if nn_out (X[i], Y[j], activation_tanh) > 0.0 :
            GF[0].append(X[i])
            GF[1].append(Y[j])
        else :
            BF[0].append(X[i])
            BF[1].append(Y[j])
       
        
fig = plt.figure(figsize=(8, 6))
ax1 = fig.subplots()
plt.scatter(GF[0],GF[1], c='g')
plt.scatter(BF[0],BF[1], c='b')
# plt.show()


#---------------------

fig2 = plt.figure (figsize=(8, 6))
ax2 = fig2.subplots()

# x_val = np.linspace(-10, 10, NX)
# y_val = np.linspace(-10, 10, NY)
Xmesh, Ymesh = np.meshgrid(X, Y)
Zmesh = nn_out (Xmesh, Ymesh, activation_tanh)
   
ax2.set_facecolor('0.8')
ax2.contour(Xmesh, Ymesh, Zmesh, levels=[0], colors='r')
ax2.set_title ("Flowers Field", fontsize=16)
ax2.set_ylabel("Y", fontsize=14)
ax2.set_xlabel("X", fontsize=14)
plt.show()
    


