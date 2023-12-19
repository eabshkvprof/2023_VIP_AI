# -*- coding: utf-8 -*-
"""
Created on  Aug  28  2023
@author: evgbash

ДЛЯ ЛАБОРАТОРНОЙ 1
КЛАССИФИКАЦИЯ  ЗЕЛЕНЫЕ / СИНИИЕ

СЕТЬ ИЗ ПЯТИ НЕЙРОНОВ. 2 ВХОДНЫХ, ДВА в скрытом слое
ОДИН ВЫХОДНОЙ 
!!!!  ИНТЕРАКТИВНОСТЬ
ЗНАЧЕНИЕЯ ВЕСОВ И СМЕЩЕНИЙ ВВОДИТСЯ ИНТЕРАКТИВНО

СТРОИТСЯ НЕЯВНО ЗАДАННАЯ РАЗДЕЛЯЮЩАЯ КРИВАЯ (выход нейрона )
КРУТИМ СЛАЙДЕРЫ и СМОТРИМ на КРИВУЮ 
"""
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter as tk


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


fgColor = "#fff"
cvColor = "#aaa"
bgColor = "#444"

mainroot = tk.Tk()
mainroot.configure(background = bgColor)
mainroot.title('Interactive Plot with Tkinter')
mainroot.minsize(width = 1000 , height = 700)


# CREATE FIGURE MATPLOTLIB

# LABES FRAME ----------
def create_label_frame ():
    frameL = tk.Frame(mainroot, width=5, height=700, padx=5, pady=5, bg = bgColor)
    frameL.grid(row=0, column=1)
    
    w13_label = tk.Label(frameL, text='W13', width = 5, height = 1,
                         font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w13_label.pack(padx=5, pady=15)
    w23_label = tk.Label(frameL, text='W23', width = 5, height = 1,
                         font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w23_label.pack(padx=5, pady=15)
    b3_label = tk.Label(frameL, text='B3', width = 5, height = 1, 
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    b3_label.pack(padx=5, pady=15)
    
    w14_label = tk.Label(frameL, text='W14', width = 5, height = 1, 
                         font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w14_label.pack(padx=5, pady=15)
    w24_label = tk.Label(frameL, text='W24', width = 5, height = 1,
                         font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w24_label.pack(padx=5, pady=15)
    b4_label = tk.Label(frameL, text='B3', width = 5, height = 1, 
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    b4_label.pack(padx=5, pady=15)
    
    w35_label = tk.Label(frameL, text='W35', width = 5, height = 1,
                         font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w35_label.pack(padx=5, pady=15)
    w45_label = tk.Label(frameL, text='W45', width = 5, height = 1,
                         font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w45_label.pack(padx=5, pady=15)
    b5_label = tk.Label(frameL, text='B5', width = 5, height = 1,
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    b5_label.pack(padx=5, pady=15)

create_label_frame ()

# SLIDERS FRAME ----------
def create_slide_frame ():
        
    frameS = tk.Frame(mainroot, width=100, height=700, padx=5, pady=5, bg = bgColor)
    frameS.grid(row=0, column=2)
    
    w13_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1, orient='horizontal',
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w13_slider.pack(padx=5, pady=5)
    w13_slider.set(.6)
    w23_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1, orient='horizontal',
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w23_slider.pack(padx=5, pady=5)
    w23_slider.set(-1.)
    b3_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1, orient='horizontal',
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    b3_slider.pack(padx=5, pady=5)
    b3_slider.set(.0)
    
    w14_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1, orient='horizontal',
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w14_slider.pack(padx=5, pady=5)
    w14_slider.set(.1)
    w24_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1, orient='horizontal',
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w24_slider.pack(padx=5, pady=5)
    w24_slider.set(.5)
    b4_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1, orient='horizontal',
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    b4_slider.pack(padx=5, pady=5)
    b4_slider.set(.5)
    
    w35_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1, orient='horizontal',
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w35_slider.pack(padx=5, pady=5)
    w35_slider.set(.6)
    w45_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1, orient='horizontal',
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    w45_slider.pack(padx=5, pady=5)
    w45_slider.set(.7)
    b5_slider = tk.Scale(frameS, from_=-1, to=+1, resolution=0.1, orient='horizontal',
                        font = ('Calibri Bold', 15), fg = fgColor, bg = bgColor)
    b5_slider.pack(padx=5, pady=5)
    b5_slider.set(.0)
    return w13_slider, w23_slider, b3_slider, w14_slider, w24_slider, b4_slider, w35_slider, w45_slider, b5_slider

w13_sld, w23_sld, b3_sld, w14_sld, w24_sld, b4_sld, w35_sld, w45_sld, b5_sld = create_slide_frame ()


# FRAME FOR PLOT ---------

fig = Figure(figsize=(10, 10))
#fig.patch.set_facecolor('xkcd:gray')|
fig.patch.set_facecolor(cvColor)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=mainroot)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=3)



NX = 50
NY = 50

X = np.linspace(-10, 10, NX)
Y = np.linspace(-10, 10, NY)

# =============================================================================
# ФУНКЦИЯ ОРИСОВКИ ИНТЕРАКТИВНО
# =============================================================================
def plot(val):
    ax.cla()
      
    W13 = w13_sld.get()
    W23 = w23_sld.get()
    B3  = b3_sld.get()
    W14 = w14_sld.get()
    W24 = w24_sld.get()
    B4  = b4_sld.get()
    W35 = w35_sld.get()
    W45 = w45_sld.get()
    B5  = b5_sld.get()

    # ФУНКЦИЯ НЕЙРОНКИ
    def nn_out (x,y,func):
        A1 = x
        A2 = y 
        A3 = func(A1*W13+A2*W23+B3)
        A4 = func(A1*W14+A2*W24+B4)
        A5 = func(A3*W35+A4*W45+B5)        
        return A5
    
    Xmesh, Ymesh = np.meshgrid(X, Y)
    
    Zmesh = nn_out (Xmesh, Ymesh, activation_tanh)
    
    ax.set_facecolor('0.8')
    
    
    ax.contour(Xmesh, Ymesh, Zmesh, levels=[0], colors='r')
    ax.set_title ("Flowers Field", fontsize=16)
    ax.set_ylabel("Y", fontsize=14)
    ax.set_xlabel("X", fontsize=14)

    canvas.draw()

# Привязка события "перемещение" ползунков к функции обновления графика
w13_sld.bind("<Motion>", plot)
w23_sld.bind("<Motion>", plot)
b3_sld.bind("<Motion>", plot)
w14_sld.bind("<Motion>", plot)
w24_sld.bind("<Motion>", plot)
b4_sld.bind("<Motion>", plot)
w35_sld.bind("<Motion>", plot)
w45_sld.bind("<Motion>", plot)
b5_sld.bind("<Motion>", plot)


mainroot.mainloop()
print('NORMAL EXIT')
