"""files"""
from a_star import *
from tkinter import *

"""Libaries"""
import random
import time


"""___________________________________ Canvas _______________________________"""

from tkinter import *
import random
import time

WIDTH = 700
HEIGHT = 700

tk=Tk()
canvas=Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_rectangle(0,0,WIDTH,HEIGHT)

# Road width
rd= 20

# house width
hw=int((WIDTH-(((len(maze)/2)+0.5)*rd))/((len(maze)/2)-0.5))


""" House """
boxx=0
for i in range(int((len(tmaze)-1)/2)):
    boxy=0
    for i in range(int((len(tmaze[0])-1)/2)):
        canvas.create_rectangle(rd+boxx,rd+boxy,rd+hw+boxx,rd+hw+boxy)
        boxy=boxy+hw+rd
    boxx=boxx+hw+rd


"""Traffic"""
column=0
row=0
for i in range(len(tmaze)):
    for j in range(len(tmaze[0])):
        if tmaze[i][j] == 1 and not i % 2 == 0:
            column=((hw+rd)*((i/2)-0.5))+rd
            row=(hw+rd)*(j/2)
            canvas.create_rectangle(column,row ,hw+column , 20+row, fill="red")
        if tmaze[i][j] == 1 and not j % 2 == 0:
            row=((hw+rd)*((j/2)-0.5))+rd
            column=(hw+rd)*(i/2)
            canvas.create_rectangle(column,row , 20+column , hw+row, fill="red")
        if tmaze[i][j] == 1 and i % 2 == 0 and j % 2 == 0 :
            row=((hw+rd)*(j/2))
            column=((hw+rd)*(i/2))
            canvas.create_rectangle(column,row , 20+column , row+20, fill="red")



"""Goal"""
canvas.create_rectangle(int(end[0]*((hw+rd)/2)),int(end[1]*((hw+rd)/2)) ,int(20+end[0]*((hw+rd)/2)),int(20+end[1]*((hw+rd)/2)), fill="blue")

""" Wheels """
class Wheels:
    def __init__(self,color, size):
        self.shape= canvas.create_rectangle(int(start[0]*((hw+rd)/2)),int(start[1]*((hw+rd)/2)),int(start[0]*((hw+rd)/2)+size),int(start[1]*((hw+rd)/2)+size), fill=color)
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
        slutx=int(end[0]*((hw+rd)/2))
        sluty=int(end[1]*((hw+rd)/2))

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

        if pos[1] >=((hw+rd)/2)*path[self.b][self.y] and path[self.a][self.x] == path[self.b][self.x] and self.i==0:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3


        if pos[0] >=((hw+rd)/2)*path[self.b][self.x] and path[self.a][self.y] == path[self.b][self.y] and self.i==0:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3

        if pos[1] <=((hw+rd)/2)*path[self.b][self.y] and path[self.a][self.x] == path[self.b][self.x] and self.i==1:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3


        if pos[0] <=((hw+rd)/2)*path[self.b][self.x] and path[self.a][self.y] == path[self.b][self.y] and self.i==1:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3
