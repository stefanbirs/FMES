import random
import numpy as np
from tkinter import *
import time
import numpy.matlib

WIDTH = 700
HEIGHT = 700

tk=Tk()
canvas=Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_rectangle(0,0,WIDTH,HEIGHT)

amaze = [[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

s=(2,2)
a=np.empty([2, 2])

#a=np.array([[canvas.create_rectangle(20,20 ,40 , 40, fill="blue"),canvas.create_rectangle(60,20 ,80 , 40, fill="blue")],[canvas.create_rectangle(20,60 ,40 , 80, fill="blue"),canvas.create_rectangle(60,60 ,80 , 80, fill="blue")]])

a[0][0]=canvas.create_rectangle(20,20 ,40 , 40, fill="blue")

b=a[0][0]

#b=a[0]

canvas.itemconfig(b, fill="red", outline="black")



print(a[0][0])

tk.mainloop()
