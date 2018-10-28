# Libaries
from tkinter import *
import random
import numpy
import time
from pprint import pprint
##################################################################
##################################################################
##################################################################
# A* algorithm
class Node:
    """A node class for A* Pathfinding"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = self.h = self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(tmaze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given tmaze"""

    # Create start and end node
    start_node = Node(None, start)
    end_node = Node(None, end)

    #print('Printing start and end node objects:')
    #pprint(start_node.__dict__, indent=2)
    #pprint(end_node.__dict__, indent=2)

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    #print('Appending start_node to open_list')
    #print('Open list:', open_list)
    #print('Closed list:', closed_list)

    # Loop until you find the end
    while len(open_list) > 0:
        #print('########################################################')
        # Get the current node
        current_node = open_list[0]
        current_index = 0

        # Forloop that finds the node with smallest f/cost
        for index, item in enumerate(open_list):
            #print('Index:', index)
            #pprint(item.__dict__,indent=2)
            if item.f < current_node.f:
                current_node = item
                current_index = index

        #print('Current node:')
        #pprint(current_node.__dict__,indent=2)
        # Pop current off open list, add to closed list
        #print('Before:')
        #print('POP current off Open list:', open_list)
        #print('Append current to Closed list:', closed_list)
        open_list.pop(current_index) # pops off node with smallest cost
        closed_list.append(current_node) # adds poped off node to closed list
        #print('After:')
        #print('POP current off Open list:', open_list)
        #print('Append current to Closed list:', closed_list)

        #for i in closed_list:
            #print(i.position)

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
        # for loop that goes through all new positions
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares
            # Get node position
            # 1st-loop (x, y)+(0, -1) = (x, y-1)
            # 2nd-loop (x, y)+(0, 1)  = (x, y+1)
            # 3rd-loop (x, y)+(-1, 0) = (x-1, y)
            # 4th-loop (x, y)+(1, 0)  = (x+1, y)
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            #print('Node position: ', node_position)

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
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0]]

tmaze=[]
rez = [[maze[j][i] for j in range(len(maze))] for i in range(len(maze[0]))]
for row in rez:
    tmaze.append(row)

####################################################################
####################################################################
# Generates a coordinate list based on the size of the city map matrix
coord_list = [(x,y) for x in range(len(tmaze)-1) for y in range(len(tmaze[0])-1)]
# Select random numbers from 'coord_list' and places them in strt_list and dest_list
strt_list = [] # Start List
dest_list = [] # Destination List
# Selects 3 random coordinates from 'coord_list' and put them in strt_list and dest_list
for i in range(3):
    strt_list.append(random.choice(coord_list))
    dest_list.append(random.choice(coord_list))
strt_list = [(0,0), (0,0), (0,0)]
#print('coodinate list:', coord_list)
#print('start list:', strt_list)
#print('Destination list:', dest_list)
# Created a list of paths using A* algorithm
path_list = []
# Uses start and destination points from lists and iterates through them to generate 3 path
for i in range(3):
    path_list.append(astar(tmaze, strt_list[i], dest_list[i]))
#print('Path list:', path_list)
####################################################################
####################################################################

start = (3,3)
end = (1,5)

path1 = astar(tmaze, start, end)

print('path1', path1)


##################################################################
##################################################################
##################################################################
"Canvas and blocks"

# Constants
WIDTH = 700
HEIGHT = 700

# Canvas
tk=Tk()
canvas=Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("City Map") # Title of window
canvas.pack() # create window
canvas.create_rectangle(0, 0, WIDTH, HEIGHT) # defining edges
#########################################################################

RWITDH = 20 # Road witdh
RLENGHT = 93 # Road lenght
RW_RL = RWITDH + RLENGHT # Sum of road witdh and lenght

# Building Blocks
boxx = 0
for i in range(len(tmaze)-1):
    boxy = 0
    for i in range(len(tmaze[0])-1):
        canvas.create_rectangle(RWITDH + boxx, RWITDH + boxy, RW_RL + boxx, RW_RL + boxy)
        boxy = boxy + RW_RL
    boxx = boxx + RW_RL

# Traffic jams
row = col = 0 # row and column
for i in range(len(tmaze)+1):
    for j in range(len(tmaze[0])+1):
        if tmaze[i-1][j-1] == 1:
            row = (RW_RL)*(i-1)
            col = (RW_RL)*(j-1)
            canvas.create_rectangle(row, col, RWITDH + row, RWITDH + col, fill="red")

# Destination
for i in range (3):
    canvas.create_rectangle(dest_list[i][0]*(RW_RL), dest_list[i][1]*(RW_RL),
                        RWITDH+dest_list[i][0]*(RW_RL), RWITDH+dest_list[i][1]*(RW_RL), fill="purple")

    canvas.create_rectangle(end[0]*(RW_RL), end[1]*(RW_RL),
                        RWITDH+end[0]*(RW_RL), RWITDH+end[1]*(RW_RL), fill="blue")

#############################################################################
# classes
""" Wheels """
class Wheels:
    def __init__(self, size):
        self.shape = canvas.create_rectangle(0, 0, size, size, fill ="green")
        self.xspeed = 0
        self.yspeed = 0
        self.a = 0
        self.b = 1
        self.x = 0
        self.y = 1
        self.i = 0

    def move(self, path, end):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)

        if (pos[0],pos[1]) == (end[0]*(RW_RL), end[1]*(RW_RL)):
            self.xspeed = 0
            self.yspeed = 0
            self.i = 4
            self.a = 0
            self.b = 0

        if path[self.a][self.x] < path[self.b][self.x]:
            self.xspeed = 1
            self.yspeed = 0
            self.i = 0

        if path[self.b][self.x] < path[self.a][self.x]:
            self.xspeed = -1
            self.yspeed = 0
            self.i = 1

        if path[self.a][self.y] < path[self.b][self.y]:
            self.xspeed = 0
            self.yspeed = 1
            self.i = 0

        if path[self.b][self.y] < path[self.a][self.y]:
            self.xspeed = 0
            self.yspeed = -1
            self.i = 1

        if pos[1]>=(RW_RL)*path[self.b][self.y] and path[self.a][self.x] == path[self.b][self.x] and self.i==0:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3

        if pos[0]>=(RW_RL)*path[self.b][self.x] and path[self.a][self.y] == path[self.b][self.y] and self.i==0:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3

        if pos[1]<=(RW_RL)*path[self.b][self.y] and path[self.a][self.x] == path[self.b][self.x] and self.i==1:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3

        if pos[0]<=(RW_RL)*path[self.b][self.x] and path[self.a][self.y] == path[self.b][self.y] and self.i==1:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3
################################################################################
################################################################################
################################################################################

# "Main"
wheels = Wheels(RWITDH)
#wheels1 = Wheels(RWITDH)
#wheels2 = Wheels(RWITDH)
#wheels3 = Wheels(RWITDH)

while True:
    wheels.move(path1, end)
    #wheels1.move(path_list[0], dest_list[0])
    #wheels2.move(path_list[1], dest_list[1])
    #wheels3.move(path_list[2], dest_list[2])
    tk.update()
    time.sleep(0.01)

tk.mainloop()
