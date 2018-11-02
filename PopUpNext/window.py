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
tk=Tk()

# Defining the size of the canvas
WIDTH = 700
HEIGHT = 700

# Creating the canvas
canvas=Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
# removes cut off on top and left edges
canvas.configure(highlightthickness=0, borderwidth=0) # removes cut off on top and left edges

# Road width
rd= 20

# house width
hw=int((WIDTH-(((len(maze)/2)+0.5)*rd))/((len(maze)/2)-0.5))


""" House """
# Makes houses for every second coordinate in the x and y axis
boxx=0
for i in range(int((len(tmaze)-1)/2)):
    boxy=0
    for i in range(int((len(tmaze[0])-1)/2)):
        canvas.create_rectangle(rd+boxx,rd+boxy,rd+hw+boxx,rd+hw+boxy)
        boxy=boxy+hw+rd
    boxx=boxx+hw+rd


"""Traffic"""
# Makes traffic for all the 1 in the maze
for x in range(len(tmaze)):
    for y in range(len(tmaze[0])):
        if tmaze[x][y] == 1 and not x % 2 == 0: #Makes a rectangle between buildings in the x axis
            column=((hw+rd)*((x/2)-0.5))+rd
            row=(hw+rd)*(y/2)
            canvas.create_rectangle(column,row ,hw+column , 20+row, fill="red")
        if tmaze[x][y] == 1 and not y % 2 == 0: #Makes a rectangle between buildings in the y axis
            row=((hw+rd)*((y/2)-0.5))+rd
            column=(hw+rd)*(x/2)
            canvas.create_rectangle(column,row , 20+column , hw+row, fill="red")
        if tmaze[x][y] == 1 and x % 2 == 0 and y % 2 == 0 : #Makes a squere on crossroads
            row=((hw+rd)*(y/2))
            column=((hw+rd)*(x/2))
            canvas.create_rectangle(column,row , 20+column , row+20, fill="red")



"""Goal"""
# Creates a squere at the end coordinate
canvas.create_rectangle(int(end[0]*((hw+rd)/2)),int(end[1]*((hw+rd)/2)) ,int(20+end[0]*((hw+rd)/2)),int(20+end[1]*((hw+rd)/2)), fill="blue")

""" Wheels """
# Since the wheels is moving this function is called every time the canvas is updated
class Wheels:
    # Defines all the varibles we are using in the function
    def __init__(self,color, size): #(self, color of wheels, size of squere)
        # This is defining the start position of the wheels
        self.shape= canvas.create_rectangle(int(start[0]*((hw+rd)/2)),int(start[1]*((hw+rd)/2)),int(start[0]*((hw+rd)/2)+size),int(start[1]*((hw+rd)/2)+size), fill=color)
        # The speed of the wheels
        self.xspeed = 0
        self.yspeed = 0
        # The varibels underneath is keeping track of part of the array, path, we are looking for
        self.a=0
        self.b=1
        self.x=0
        self.y=1
        # i makes sure that we are entering the right if statement
        self.i=0


    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)

        #saves the current position if the wheel
        pos= canvas.coords(self.shape)

        #indentify the end coordinates
        slutx=int(end[0]*((hw+rd)/2))
        sluty=int(end[1]*((hw+rd)/2))

        if (pos[0],pos[1]) == (slutx,sluty) : #It only enters this statement if its at the end point
            # It stops the wheel
            self.xspeed=0
            self.yspeed=0
            # Make sure that t dosn't enter another if statement
            self.i=4
            self.a=0
            self.b=0


        ############## Stering of the wheels direction and speed ############

        # Sees if the x coordinate in the array, path, is bigger that the previous one
        if path[self.a][self.x] < path[self.b][self.x]:
            # If it is make the wheel go positive in the x direction
            self.xspeed=1
            self.yspeed=0
            # Indicate that the wheel is moving in a possitive direction
            self.i=0

        # Sees if the x coordinate in the array, path, is smaller that the previous one
        if path[self.b][self.x] < path[self.a][self.x]:
            # If it is make the wheel go negative in the x direction
            self.xspeed=-1
            self.yspeed=0
            # Indicate that the wheel is moving in a negative direction
            self.i=1

        # Sees if the y coordinate in the array, path, is bigger that the previous one
        if path[self.a][self.y] < path[self.b][self.y]:
            # If it is make the wheel go positive in the y direction
            self.xspeed=0
            self.yspeed=1
            # Indicate that the wheel is moving in a possitive direction
            self.i=0

        # Sees if the y coordinate in the array, path, is smaller that the previous one
        if path[self.b][self.y] < path[self.a][self.y]:
            # If it is make the wheel go negative in the y direction
            self.xspeed=0
            self.yspeed=-1
            # Indicate that the wheel is moving in a negative direction
            self.i=1


        ################ Checking the coordinates of the wheels ###################

        # When the wheels coordinate has reatched a possition of a new coordinate, the varibles a and b gets added by one.
        # This is done to make the if statements above to look at the next step of the path

        # looks if the wheel has reached a new coordinate in the positive x direction
        if pos[0] >=((hw+rd)/2)*path[self.b][self.x] and path[self.a][self.y] == path[self.b][self.y] and self.i==0:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3
        # looks if the wheel has reached a new coordinate in the negative x direction
        if pos[0] <=((hw+rd)/2)*path[self.b][self.x] and path[self.a][self.y] == path[self.b][self.y] and self.i==1:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3
        # looks if the wheel has reached a new coordinate in the positive y direction
        if pos[1] >=((hw+rd)/2)*path[self.b][self.y] and path[self.a][self.x] == path[self.b][self.x] and self.i==0:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3
        # looks if the wheel has reached a new coordinate in the negative y direction
        if pos[1] <=((hw+rd)/2)*path[self.b][self.y] and path[self.a][self.x] == path[self.b][self.x] and self.i==1:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i=3
