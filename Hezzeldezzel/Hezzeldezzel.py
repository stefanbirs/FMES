
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



maze = [[0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0]]

tmaze=[]
rez = [[maze[j][i] for j in range(len(maze))] for i in range(len(maze[0]))]
for row in rez:
    tmaze.append(row)


start=(0,0)
end=(5,1)

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



""" Huse """
boxx=0
for i in range(len(tmaze)-1):
    canvas.create_rectangle(20+boxx,20,20+93+boxx,20+93)
    boxy=0
    for i in range(len(tmaze[0])-1):
        canvas.create_rectangle(20+boxx,20+boxy,20+93+boxx,20+93+boxy)
        boxy=boxy+93+20
    boxx=boxx+93+20


"""Trafik"""

række=0
kollone=0
for i in range(len(tmaze)+1):
    række=(93+20)*(i-1)
    for j in range(len(tmaze[0])+1):
        if tmaze[i-1][j-1] == 1:
            kollone=(93+20)*(j-1)
            canvas.create_rectangle(række,kollone ,20+række,20+kollone, fill="red")

"""Mål"""
canvas.create_rectangle(end[0]*(93+20),end[1]*(93+20) ,20+end[0]*(93+20),20+end[1]*(93+20), fill="blue")


class Car:
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


åben=[]

for i in range(len(tmaze)):
    for j in range(len(tmaze[0])):

        if tmaze[i][j] == 1:
            åben.append((i,j))

print(åben)

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




lal=[]

for i in range(len(a)):
    for j in range(len(a)):
        print("i",i)
        print("j",j)
        if i in a[j]:
            lal.append(j)


print(åben)
print(a,"pik")
print(lal)

car=Car("green",20)

while True:
    car.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
