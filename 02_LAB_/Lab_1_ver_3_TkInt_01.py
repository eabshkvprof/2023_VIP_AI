# -*- coding: utf-8 -*-
"""
Created on  Aug  29  2023
@author: evgbash


ИЛЛЮСТРАЦИЯ ДЛЯ ЛАБОРАТОРНОЙ 1
КЛАССИФИКАЦИЯ  ЗЕЛЕНЫЕ / СИНИИЕ
СЕТЬ ИЗ СЕМИ НЕЙРОНОВ.
ДВА входных ТРИ в скрытом слое  ДВА выходных

Выходы OUT (А5, А6) нейронов сравниваются и,
в зависимсооти какой больше (перевешивает), поле раскрашивается цветочками

ИСПОЛЬЗУЕТСЯ ИНТЕРАКТИВНОСТЬ:
ЗНАЧЕНИЕЯ ВЕСОВ И СМЕЩЕНИЙ ВВОДИТСЯ ИНТЕРАКТИВНО
КРУТИМ СЛАЙДЕРЫ и ПОДБИРАЕМ РАССАДКУ

ВЕРСИЯ 1.
"""
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# %% DIFFERENT FUNCTIONS
# =============================================================================
# ФУНКЦИИ РАЗДЕЛЕНИЯ ЦВЕТОЧКОВ
# =============================================================================
# Синусоидальная функция разделения цветочков


def separate_sin(x, ks, As):
    '''
    x - аргумент
    k - коэффициент наклона
    s - Амплитуда синусоиды
    '''
    return As * np.sin(1.5 * x) + ks * x


Asin = 1
Ksin = 0.5

# Гипертангенс функция разделения цветочков


def separate_th(x, As, Bs):
    '''
    x - аргумент
    k - коэффициент наклона
    s - Амплитуда синусоиды
    '''
    return As * np.tanh(x-Bs)


Aht = 5
Bht = 3

# =============================================================================
# ФУНКЦИИ АКТИВАЦИИ
# =============================================================================

# функция активации - линейная


def activation_linear(x):
    return (x)

# функция активации - сигмоида


def activation_sigmoid(x):
    return 1/(1+np.exp(-x))

# функция активации - гипертангент


def activation_tanh(x):
    return np.tanh(x)

# функция активации - signum


def activation_signum(x):
    return np.sign(x)

# =============================================================================
# CREATE TINTER MAIN ROOT FRAME
# =============================================================================


fgColor = "#fff"
cvColor = "#aaa"
bgColor = "#444"

mainroot = tk.Tk()
mainroot.configure(background=bgColor)
mainroot.title('Interactive Plot with Tkinter')
mainroot.minsize(width=1000, height=700)


# %% Label Frame1
# =============================================================================
# LABES FRAME --- ПОЛЕ МЕТОК -------
# =============================================================================

frameL = tk.Frame(mainroot, width=5, height=700, padx=5, pady=5, bg=bgColor)
frameL.grid(row=0, column=2)

# Нейрон 4
w13_label = tk.Label(frameL, text='W13', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w13_label.pack(padx=5, pady=15)
w23_label = tk.Label(frameL, text='W23', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w23_label.pack(padx=5, pady=15)
b3_label = tk.Label(frameL, text='B3', width=5, height=1,
                    font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
b3_label.pack(padx=5, pady=15)

# Нейрон 4
w14_label = tk.Label(frameL, text='W14', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w14_label.pack(padx=5, pady=15)
w24_label = tk.Label(frameL, text='W24', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w24_label.pack(padx=5, pady=15)
b4_label = tk.Label(frameL, text='B4', width=5, height=1,
                    font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
b4_label.pack(padx=5, pady=15)

# Нейрон 5
w15_label = tk.Label(frameL, text='W15', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w15_label.pack(padx=5, pady=15)
w25_label = tk.Label(frameL, text='W25', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w25_label.pack(padx=5, pady=15)
b5_label = tk.Label(frameL, text='B5', width=5, height=1,
                    font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
b5_label.pack(padx=5, pady=15)


# %% Siders  Frame1
# =============================================================================
# SLIDERS FRAME -----ПОЛЕ СЛАЙДЕРОВ -----
# =============================================================================

frameS = tk.Frame(mainroot, width=100, height=700, padx=5, pady=5, bg=bgColor)
frameS.grid(row=0, column=3)

# Нейрон 3
w13_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal', font=('Calibri Bold', 15),
                      fg=fgColor, bg=bgColor)
w13_slider.pack(padx=5, pady=5)
w13_slider.set(.2)
w23_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal', font=('Calibri Bold', 15),
                      fg=fgColor, bg=bgColor)
w23_slider.pack(padx=5, pady=5)
w23_slider.set(.2)
b3_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1,
                     orient='horizontal', font=('Calibri Bold', 15),
                     fg=fgColor, bg=bgColor)
b3_slider.pack(padx=5, pady=5)
b3_slider.set(-.1)

# Нейрон 4
w14_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal', font=('Calibri Bold', 15),
                      fg=fgColor, bg=bgColor)
w14_slider.pack(padx=5, pady=5)
w14_slider.set(-.1)
w24_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal', font=('Calibri Bold', 15),
                      fg=fgColor, bg=bgColor)
w24_slider.pack(padx=5, pady=5)
w24_slider.set(-.4)
b4_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1,
                     orient='horizontal', font=('Calibri Bold', 15),
                     fg=fgColor, bg=bgColor)
b4_slider.pack(padx=5, pady=5)
b4_slider.set(.1)

# Нейрон 5
w15_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal', font=('Calibri Bold', 15),
                      fg=fgColor, bg=bgColor)
w15_slider.pack(padx=5, pady=5)
w15_slider.set(-.8)
w25_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal', font=('Calibri Bold', 15),
                      fg=fgColor, bg=bgColor)
w25_slider.pack(padx=5, pady=5)
w25_slider.set(.6)
b5_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1,
                     orient='horizontal', font=('Calibri Bold', 15),
                     fg=fgColor, bg=bgColor)
b5_slider.pack(padx=5, pady=5)
b5_slider.set(-.2)


# %% Label Frame2
# =============================================================================
# LABES FRAME --- ПОЛЕ МЕТОК -------
# =============================================================================

frameL2 = tk.Frame(mainroot, width=5, height=700, padx=5, pady=5, bg=bgColor)
frameL2.grid(row=0, column=4)

# Нейрон 6
w36_label = tk.Label(frameL2, text='W36', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w36_label.pack(padx=5, pady=15)
w46_label = tk.Label(frameL2, text='W46', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w46_label.pack(padx=5, pady=15)
w56_label = tk.Label(frameL2, text='W56', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w56_label.pack(padx=5, pady=15)
b6_label = tk.Label(frameL2, text='B6', width=5, height=1,
                    font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
b6_label.pack(padx=5, pady=15)

# Нейрон 7
w37_label = tk.Label(frameL2, text='W37', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w37_label.pack(padx=5, pady=15)
w47_label = tk.Label(frameL2, text='W47', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w47_label.pack(padx=5, pady=15)
w57_label = tk.Label(frameL2, text='W57', width=5, height=1,
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w57_label.pack(padx=5, pady=15)
b7_label = tk.Label(frameL2, text='B7', width=5, height=1,
                    font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
b7_label.pack(padx=5, pady=15)


# %% Siders  Frame2
# =============================================================================
# SLIDERS FRAME -----ПОЛЕ СЛАЙДЕРОВ -----
# =============================================================================

frameS2 = tk.Frame(mainroot, width=100, height=700, padx=5, pady=5, bg=bgColor)
frameS2.grid(row=0, column=5)

# Нейрон 6  3 входа + смещение
w36_slider = tk.Scale(frameS2, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal', font=('Calibri Bold', 15),
                      fg=fgColor, bg=bgColor)
w36_slider.pack(padx=5, pady=5)
w36_slider.set(-.2)
w46_slider = tk.Scale(frameS2, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal',
                      font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w46_slider.pack(padx=5, pady=5)
w46_slider.set(.1)

w56_slider = tk.Scale(frameS2, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal',
                      font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w56_slider.pack(padx=5, pady=5)
w56_slider.set(.1)

b6_slider = tk.Scale(frameS2, from_=-1, to=+1, resolution=0.05,
                     orient='horizontal',
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
b6_slider.pack(padx=5, pady=5)
b6_slider.set(.0)

# Нейрон 7: 3 входа + смещение
w37_slider = tk.Scale(frameS2, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal',
                      font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w37_slider.pack(padx=5, pady=5)
w37_slider.set(-.3)
w47_slider = tk.Scale(frameS2, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal',
                      font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
w47_slider.pack(padx=5, pady=5)
w47_slider.set(.4)

w57_slider = tk.Scale(frameS2, from_=-1, to=+1, resolution=0.1,
                      orient='horizontal', font=('Calibri Bold', 15),
                      fg=fgColor, bg=bgColor)
w57_slider.pack(padx=5, pady=5)
w57_slider.set(-.1)

b7_slider = tk.Scale(frameS2, from_=-1, to=+1, resolution=0.05,
                     orient='horizontal',
                     font=('Calibri Bold', 15), fg=fgColor, bg=bgColor)
b7_slider.pack(padx=5, pady=5)
b7_slider.set(.1)


# %% PLOT Frame
# =============================================================================
# FRAME FOR PLOT --- ПОЛЕ ДЛЯ ГРАФИКА
# =============================================================================

fig = Figure(figsize=(10, 10))
# fig.patch.set_facecolor('xkcd:gray')|
fig.patch.set_facecolor(cvColor)
ax = fig.add_subplot(111)

canvas1 = FigureCanvasTkAgg(fig, master=mainroot)  # A tk.DrawingArea.
canvas1.draw()
canvas1.get_tk_widget().grid(row=0, column=6)

# ЭТО ДЛЯ РИСУНКА СЕТИ

riss1 = tk.PhotoImage(file='./Lab_1_Ris_2.png')

frameimage = tk.Frame(mainroot, width=300, height=700,
                      padx=5, pady=5, bg=bgColor)
frameimage.grid(row=0, column=1)
image_label = tk.Label(frameimage, image=riss1)
image_label.pack(padx=5, pady=15)

# Размер грядки по X, по Y
NX = 50
NY = 50

X = np.linspace(-10, 10, NX)
Y = np.linspace(-10, 10, NY)

print('Грядка ', X, 'на', Y, 'всего', X*Y)

FG = list()
FG.append(list())
FG.append(list())

FB = list()
FB.append(list())
FB.append(list())

print('ПРОВЕРКА: ЗЕЛЕНЫЕ', FG, 'СИНИЕ', FB, 'ПУСТО')

# %% DROWING


def plot(val):
    '''
    ===========================================================================
    ФУНКЦИЯ ОРИСОВКИ ИНТЕРАКТИВНО
    ===========================================================================
    '''
    def nn_out(x, y, func):
        A1 = x
        A2 = y
        A3 = func(A1*W13+A2*W23+B3)
        A4 = func(A1*W14+A2*W24+B4)
        A5 = func(A1*W15+A2*W25+B5)
        A6 = func(A3*W36+A4*W46+A5*W56+B6)
        A7 = func(A3*W37+A4*W47+A5*W57+B7)
        return A6, A7

    FG = list()
    FG.append(list())
    FG.append(list())

    FB = list()
    FB.append(list())
    FB.append(list())

    W13 = w13_slider.get()
    W23 = w23_slider.get()
    B3 = b3_slider.get()
    W14 = w14_slider.get()
    W24 = w24_slider.get()
    B4 = b4_slider.get()
    W15 = w15_slider.get()
    W25 = w25_slider.get()
    B5 = b5_slider.get()
    W36 = w36_slider.get()
    W46 = w46_slider.get()
    W56 = w56_slider.get()
    B6 = b6_slider.get()
    W37 = w37_slider.get()
    W47 = w47_slider.get()
    W57 = w57_slider.get()
    B7 = b7_slider.get()

    for x in X:
        for y in Y:
            R1, R2 = nn_out(x, y, activation_sigmoid)
            # R1, R2 = nn_out(x, y, activation_linear)
            if R1 >= (R2 + .005):
                FG[0].append(x)
                FG[1].append(y)
            elif R1 <= (R2 - .005):
                FB[0].append(x)
                FB[1].append(y)

    ax.cla()
    ax.set_facecolor('0.8')

    ax.scatter(FG[0], FG[1], c='g')
    ax.scatter(FB[0], FB[1], c='b')

    ax.set_title("Flowers Field", fontsize=16)
    ax.set_ylabel("Y", fontsize=14)
    ax.set_xlabel("X", fontsize=14)

    canvas1.draw()


# %% SLIDERS BINDING
# Привязка события "перемещение" ползунков к функции обновления графика
w13_slider.bind("<Motion>", plot)
w23_slider.bind("<Motion>", plot)
b3_slider.bind("<Motion>", plot)

w14_slider.bind("<Motion>", plot)
w24_slider.bind("<Motion>", plot)
b4_slider.bind("<Motion>", plot)

w15_slider.bind("<Motion>", plot)
w25_slider.bind("<Motion>", plot)
b5_slider.bind("<Motion>", plot)

w36_slider.bind("<Motion>", plot)
w46_slider.bind("<Motion>", plot)
w56_slider.bind("<Motion>", plot)
b6_slider.bind("<Motion>", plot)

w37_slider.bind("<Motion>", plot)
w47_slider.bind("<Motion>", plot)
w57_slider.bind("<Motion>", plot)
b7_slider.bind("<Motion>", plot)


# %% MAIN LOOP
mainroot.mainloop()
print('NORMAL EXIT')
