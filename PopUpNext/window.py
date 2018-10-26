from a_star import *
from tkinter import *
import random
import time

WIDTH = 700
HEIGHT = 700

tk=Tk()
canvas=Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.create_rectangle(0,0,WIDTH,HEIGHT)

""" House """
boxx=0
for i in range(len(tmaze)-1):
    canvas.create_rectangle(20+boxx,20,20+93+boxx,20+93)
    boxy=0
    for i in range(len(tmaze[0])-1):
        canvas.create_rectangle(20+boxx,20+boxy,20+93+boxx,20+93+boxy)
        boxy=boxy+93+20
    boxx=boxx+93+20

"""Trafic"""
række=0
kollone=0
for i in range(len(tmaze)+1):
    række=(93+20)*(i-1)
    for j in range(len(tmaze[0])+1):
        if tmaze[i-1][j-1] == 1:
            kollone=(93+20)*(j-1)
            canvas.create_rectangle(række,kollone ,20+række,20+kollone, fill="red")

"""Goal"""
canvas.create_rectangle(end[0]*(93+20),end[1]*(93+20) ,20+end[0]*(93+20),20+end[1]*(93+20), fill="blue")

class Wheels:
    def __init__(self,color, size):
        self.shape= canvas.create_rectangle(0,0,size,size, fill=color)
        self.xspeed = 0
        self.yspeed = 0
        self.a=0
        self.b=1
        self.x=0
        self.y=1
        self.i=0

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos= canvas.coords(self.shape)
        slutx=end[0]*(93+20)
        sluty=end[1]*(93+20)

        if (pos[0],pos[1]) == (slutx,sluty) :
            self.xspeed=0
            self.yspeed=0
            self.i=4
            self.a=0
            self.b=0

        if path[self.a][self.x] < path[self.b][self.x]:
            self.xspeed=1
            self.yspeed=0
            self.i=0

        if path[self.b][self.x] < path[self.a][self.x]:
            self.xspeed=-1
            self.yspeed=0
            self.i=1

        if path[self.a][self.y] < path[self.b][self.y]:
            self.xspeed=0
            self.yspeed=1
            self.i=0

        if path[self.b][self.y] < path[self.a][self.y]:
            self.xspeed=0
            self.yspeed=-1
            self.i=1
            #print("-y")

        if pos[1] >=(93+20)*path[self.b][self.y] and path[self.a][self.x] == path[self.b][self.x] and self.i==0:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3

        if pos[0] >=(93+20)*path[self.b][self.x] and path[self.a][self.y] == path[self.b][self.y] and self.i==0:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3

        if pos[1] <=(93+20)*path[self.b][self.y] and path[self.a][self.x] == path[self.b][self.x] and self.i==1:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3

        if pos[0] <=(93+20)*path[self.b][self.x] and path[self.a][self.y] == path[self.b][self.y] and self.i==1:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3

wheels=Wheels("green",20)

while True:
    wheels.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
