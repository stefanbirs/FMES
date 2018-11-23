
import numpy

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(tmaze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given tmaze"""

    # Create start and end node
    start_node = Node(None, start)
    #start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    #end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):

            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node

            while current is not None:
                path.append(current.position)
                current = current.parent

            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(tmaze) - 1) or node_position[0] < 0 or node_position[1] > (len(tmaze[len(tmaze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if tmaze[node_position[0]][node_position[1]] != 0:
                continue

            if Node(current_node, node_position) in closed_list:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)



maze = [[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
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

tmaze=[]
rez = [[maze[j][i] for j in range(len(maze))] for i in range(len(maze[0]))]
for row in rez:
    tmaze.append(row)


start=(0,0)
end=(6,5)

path = astar(tmaze, start, end)
print(path)



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


class Car:
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


åben=[]

for i in range(len(tmaze)):
    for j in range(len(tmaze[0])):

        if tmaze[i][j] == 1:
            åben.append((i,j))


a = [None]*len(åben)

for i in range(len(a)):
    for j in range(len(a)):
        if i==j:
            continue
        if åben[i][0]==åben[j][0]+1 and åben[i][1]==åben[j][1] or åben[i][0]==åben[j][0]-1 and åben[i][1]==åben[j][1] or åben[i][1]==åben[j][1]+1 and åben[i][0]==åben[j][0] or åben[i][1]==åben[j][1]-1 and åben[i][0]==åben[j][0]:
            if a[i]== None:
                a[i]=j
            else:
                a[i]=a[i],j




# lal=[]
#
# for i in range(len(a)):
#     for j in range(len(a)):
#         print("i",i)
#         print("j",j)
#         if i in a[j]:
#             lal.append(j)


# print(lal)

car=Car("green",20)

while True:
    car.move()
    tk.update()
    time.sleep(0.01)

print("pik")

tk.mainloop()
