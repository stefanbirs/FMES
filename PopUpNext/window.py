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

rd = 20 # Road width
hw = int((WIDTH-(((len(maze)/2)+0.5)*rd))/((len(maze)/2)-0.5)) # house width

# Road width
road_width= 20

# house width
house_width=int((WIDTH-(((len(maze)/2)+0.5)*road_width))/((len(maze)/2)-0.5))

""" House """
# Makes houses for every second cooroad_widthinate in the x and y axis
box_x=0
for i in range(int((len(tmaze)-1)/2)):
    box_y=0
    for i in range(int((len(tmaze[0])-1)/2)):
        canvas.create_rectangle(road_width+box_x,road_width+box_y,
        road_width+house_width+box_x,road_width+house_width+box_y)
        box_y=box_y+house_width+road_width
    box_x=box_x+house_width+road_width


"""Traffic"""
# Makes traffic for all the '1's in  tmaze
for x in range(len(tmaze)):
    for y in range(len(tmaze[0])):
        if tmaze[x][y] == 1 and not x % 2 == 0: #Makes a rectangle between buildings in the x axis
            column=((house_width+road_width)*((x/2)-0.5))+road_width
            row=(house_width+road_width)*(y/2)
            canvas.create_rectangle(column,row ,house_width+column , 20+row, fill="red")
        if tmaze[x][y] == 1 and not y % 2 == 0: #Makes a rectangle between buildings in the y axis
            row=((house_width+road_width)*((y/2)-0.5))+road_width
            column=(house_width+road_width)*(x/2)
            canvas.create_rectangle(column,row , 20+column , house_width+row, fill="red")
        if tmaze[x][y] == 1 and x % 2 == 0 and y % 2 == 0 : #Makes a squere on crossroads
            row=((house_width+road_width)*(y/2))
            column=((house_width+road_width)*(x/2))
            canvas.create_rectangle(column,row , 20+column , row+20, fill="red")



"""Goal"""
# Creates a squere at the end cooroad_widthinate
end_point_x_coord=int(end[0]*((house_width+road_width)/2))
end_y_coord=int(end[1]*((house_width+road_width)/2))
end_size_x=int(20+end[0]*((house_width+road_width)/2))
end_size_y=int(20+end[1]*((house_width+road_width)/2))
canvas.create_rectangle(end_point_x_coord, end_y_coord,end_size_x,end_size_y, fill="blue")

""" Wheels """
# Since the wheels is moving this function is called every time the canvas is updated
class Wheels:
    # Defines all the varibles we are using in the function
    def __init__(self,color, size): #(self, color of wheels, size of squere)
        # This is defining the start position of the wheels
        x_coord=int(start[0]*((house_width+road_width)/2))
        y_coord=int(start[1]*((house_width+road_width)/2))
        size_x=int(start[0]*((house_width+road_width)/2)+size)
        size_y=int(start[1]*((house_width+road_width)/2)+size)
        self.shape= canvas.create_rectangle(x_coord,y_coord,size_x,size_y, fill=color)
        # The speed of the wheels
        self.xspeed = 0
        self.yspeed = 0
        # The varibels underneath is keeping track of part of the array, path, we are looking for
        self.a=0
        self.b=1
        self.x=0
        self.y=1
        # i makes sure that we are entering the right if statement
        self.direction=0


    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)

        #saves the current position if the wheel
        current_position= canvas.coords(self.shape)

        #indentify the end coordinates
        end_point_x=int(end[0]*((house_width+road_width)/2))
        end_point_y=int(end[1]*((house_width+road_width)/2))

        if (current_position[0],current_position[1]) == (end_point_x,end_point_y) : #It only enters this statement if its at the end point
            # It stops the wheel
            self.xspeed=0
            self.yspeed=0
            # Make sure that t dosn't enter another if statement
            self.direction=4
            self.a=0
            self.b=0

        ############## Stering of the wheels direction and speed ############

        #use these values to determine direction of travel
        a_x=path[self.a][self.x]
        b_x=path[self.b][self.x]
        a_y=path[self.a][self.y]
        b_y=path[self.b][self.y]

        if a_x < b_x:
            # positive in the x direction
            self.xspeed=1
            self.yspeed=0
            self.direction=0
        elif b_x < a_x:
            # negative in the x direction
            self.xspeed=-1
            self.yspeed=0
            self.direction=1
        elif a_y < b_y:
            # positive in the y direction
            self.xspeed=0
            self.yspeed=1
            self.direction=0
        elif b_y < a_y:
            # negative in the y direction
            self.xspeed=0
            self.yspeed=-1
            self.direction=1

        ################ Checking the coordinates of the wheels ###################

        # When the wheels cooroad_widthinate has reatched a position of a new coordinate, the varibles a and b gets added by one.
        # This is done to make the if statements above to look at the next step of the path

        if current_position[0] >=((house_width+road_width)/2)*b_x and a_y == b_y and self.direction==0:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.direction=3
        # looks if the wheel has reached a new coordinate in the negative x direction
        elif current_position[0] <=((house_width+road_width)/2)*b_x and a_y == b_y and self.direction==1:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.direction=3
        # looks if the wheel has reached a new coordinate in the positive y direction
        elif current_position[1] >=((house_width+road_width)/2)*b_y and a_x == b_x and self.direction==0:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.direction=3
        # looks if the wheel has reached a new coordinate in the negative y direction
        elif current_position[1] <=((house_width+road_width)/2)*b_y and a_x == b_x and self.direction==1:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.direction=3
