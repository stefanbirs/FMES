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

rd= 20

# house width
hw=int((WIDTH-(((len(amaze)/2)+0.5)*rd))/((len(amaze)/2)-0.5))

s = (len(amaze),len(amaze[0]))
Trafmaze=np.zeros(s)
NoTrafmaze=np.zeros(s)

for i in range(len(Trafmaze)):
    for j in range(len(Trafmaze)):
        if amaze[i][j]==1:
            Trafmaze[i][j]=random.randrange(1,2000)
        if Trafmaze[i][j]>0:
            Trafmaze[i][j]=Trafmaze[i][j]-1
        if Trafmaze[i][j]==1:
            amaze[i][j]=0

for i in range(len(NoTrafmaze)):
    for j in range(len(NoTrafmaze)):
        if amaze[i][j]==0:
            NoTrafmaze[i][j]=random.randrange(1,2000)
        if NoTrafmaze[i][j]>1:
            NoTrafmaze[i][j]=NoTrafmaze[i][j]-1
        if NoTrafmaze[i][j]==1:
            amaze[i][j]=1

class Dotclass:

    def upright(self):
        self.column=50
        self.row=50
        self.shape = canvas.create_rectangle(self.column,self.row ,50+self.column , 50+self.row, fill="red")
pik=Dotclass()

i=0
bob=[]
lal=pik.upright()

# bob.append(lal)
# print(pik.upright())

while True:



    #
    # if i>200:
    #     canvas.delete(bob[0])
    #
    # i=i+1

    tk.after(10, pik.upright())

tk.mainloop()
