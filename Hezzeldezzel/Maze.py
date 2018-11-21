import random
import numpy as np
from tkinter import *
import time

WIDTH = 700
HEIGHT = 700

tk=Tk()
canvas=Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_rectangle(0,0,WIDTH,HEIGHT)

amaze = [[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

rd= 20

# house width
hw=int((WIDTH-(((len(amaze)/2)+0.5)*rd))/((len(amaze)/2)-0.5))

s = (len(amaze),len(amaze[0]))
Trafmaze=np.zeros(s)
NoTrafmaze=np.zeros(s)

a=[]
b=[]

for i in range(len(amaze)):
    for j in range(len(amaze[0])):
        if amaze[i][j] != 2 and not i % 2 == 0:
            column=((hw+rd)*((i/2)-0.5))+rd
            row=(hw+rd)*(j/2)
            a.append(canvas.create_rectangle(column,row ,hw+column , 20+row, fill=""))
        if amaze[i][j] != 2 and not j % 2 == 0:
            row=((hw+rd)*((j/2)-0.5))+rd
            column=(hw+rd)*(i/2)
            a.append(canvas.create_rectangle(column,row , 20+column , hw+row, fill=""))
        if amaze[i][j] != 2 and i % 2 == 0 and j % 2 == 0 :
            row=((hw+rd)*(j/2))
            column=((hw+rd)*(i/2))
            a.append(canvas.create_rectangle(column,row , 20+column , row+20, fill=""))
        if amaze[i][j]==2:
            a.append(0)

while True :



    for i in range(len(Trafmaze)):
        for j in range(len(Trafmaze)):
            trafchance=random.randrange(1,1000)
            if amaze[i][j]==1 and Trafmaze[i][j]==0:
                Trafmaze[i][j]=200
            if Trafmaze[i][j]>0:
                Trafmaze[i][j]=Trafmaze[i][j]-1
            if Trafmaze[i][j]==0:
                amaze[i][j]=0

            if amaze[i][j]==0 and trafchance==1:
                amaze[i][j]=1


    for i in range(len(amaze)):
        for j in range(len(amaze[0])):
            if amaze[i][j] == 1 and not i % 2 == 0:
                column=((hw+rd)*((i/2)-0.5))+rd
                row=(hw+rd)*(j/2)
                canvas.itemconfig(a[i+(j*13)], fill="red", outline="black")
            if amaze[i][j] == 1 and not j % 2 == 0:
                row=((hw+rd)*((j/2)-0.5))+rd
                column=(hw+rd)*(i/2)
                canvas.itemconfig(a[i+(j*13)], fill="red", outline="black")
            if amaze[i][j] == 1 and i % 2 == 0 and j % 2 == 0 :
                row=((hw+rd)*(j/2))
                column=((hw+rd)*(i/2))
                canvas.itemconfig(a[i+(j*13)], fill="red", outline="black")
            if amaze[i][j] == 0 and not i % 2 == 0:
                column=((hw+rd)*((i/2)-0.5))+rd
                row=(hw+rd)*(j/2)
                canvas.itemconfig(a[i+(j*13)], fill="", outline="")
            if amaze[i][j] == 0 and not j % 2 == 0:
                row=((hw+rd)*((j/2)-0.5))+rd
                column=(hw+rd)*(i/2)
                canvas.itemconfig(a[i+(j*13)], fill="", outline="")
            if amaze[i][j] == 0 and i % 2 == 0 and j % 2 == 0 :
                row=((hw+rd)*(j/2))
                column=((hw+rd)*(i/2))
                canvas.itemconfig(a[i+(j*13)], fill="", outline="")

    tk.update()

tk.mainloop()
