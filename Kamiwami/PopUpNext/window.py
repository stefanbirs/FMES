# Libaries
from tkinter import *
import random
import numpy
import time
from pprint import pprint
################################################################################
################################################################################
################################################################################
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

maze = [[0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0]]

tmaze=[]
rez = [[maze[j][i] for j in range(len(maze))] for i in range(len(maze[0]))]
for row in rez:
    tmaze.append(row)

################################################################################
################################################################################
################################################################################
NUM_OF_WHEELS = 10 # The number of wheels in the city map
# Generates a coordinate list based on the size of the city map matrix
coord_list = [] # coordinate List
strt_list = [] # Start List
dest_list = [] # Destination List
path_list = [] # Path List
for x in range(len(tmaze)-1): # iterates through number of columns
    for y in range(len(tmaze[0])-1): # iterates through number of rows
        if tmaze[x][y] == 0: # if There is no traffic in this coordinate "0" then append coordinate
            coord_list.append((x,y)) # Coordinate list that does not have traffic
        elif tmaze[x][y] == 1: # else if there is traffic in this coordinate "1" do nothing
            continue
# Select random numbers from 'coord_list' and places them in strt_list and dest_list
for i in range(NUM_OF_WHEELS):
    strt_list.append(random.choice(coord_list))
    dest_list.append(random.choice(coord_list))
print('start list:', strt_list)
print('destination list:', dest_list)
# Created a list of paths using A* algorithm
for i in range(NUM_OF_WHEELS):
    path_list.append(astar(tmaze, strt_list[i], dest_list[i]))
print('Path list:', path_list)
################################################################################
################################################################################
################################################################################
# Generates Canvas
WIDTH = 700 # Width of canvas
HEIGHT = 700 # Height of canvas
# Canvas
tk=Tk()
canvas=Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("City Map") # Title of window
canvas.pack() # Creates window
canvas.configure(highlightthickness=0, borderwidth=0) # removes cut off on top and left edges
#canvas.create_rectangle(0, 0, WIDTH, HEIGHT) # Defining edges
################################################################################
################################################################################
################################################################################
# Generates Building Blocks, Traffic Jams and Destination Blocks
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

# Create a single Docking station for drone (bottom left corner)
bot_rightx = (len(tmaze)-1)*(RW_RL) # row length of city map
bot_righty = (len(tmaze[0])-1)*(RW_RL) # column length of city map
dock = canvas.create_rectangle(bot_rightx, bot_righty, bot_rightx + RWITDH, bot_righty + RWITDH)
dock_pos = canvas.coords(dock) # Dock position

print("bot_rightx", bot_rightx)
print("bot_righty", bot_righty)

# Traffic Jams
row = col = 0 # row and column
for i in range(len(tmaze)+1):
    for j in range(len(tmaze[0])+1):
        if tmaze[i-1][j-1] == 1:
            row = (RW_RL)*(i-1)
            col = (RW_RL)*(j-1)
            canvas.create_rectangle(row, col, RWITDH + row, RWITDH + col, fill="red")

# Destination Blocks
for i in range (NUM_OF_WHEELS):
    canvas.create_rectangle(dest_list[i][0]*(RW_RL), dest_list[i][1]*(RW_RL),
                        RWITDH+dest_list[i][0]*(RW_RL), RWITDH+dest_list[i][1]*(RW_RL), fill="blue")

################################################################################
################################################################################
################################################################################
# The Wheels Class
class Wheels:
    def __init__(self, size, path):
        self.shape = canvas.create_rectangle(path[0][0]*(RW_RL), path[0][1]*(RW_RL),
                                            size+path[0][0]*(RW_RL), size+path[0][1]*(RW_RL), fill ="green")
        self.xspeed = 0
        self.yspeed = 0
        self.a = 0
        self.b = 1
        self.x = 0
        self.y = 1
        self.i = 0

    def move(self, path, end):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape) # returns -> (x1,y1,x2,y2)


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

# The Pod Class
class Pod:
    def __init__(self, size, path):
        self.shape = canvas.create_oval(path[0][0]*(RW_RL), path[0][1]*(RW_RL),
                                            size+path[0][0]*(RW_RL), size+path[0][1]*(RW_RL), fill ="grey")
        self.xspeed = 0
        self.yspeed = 0
        self.a = 0
        self.b = 1
        self.x = 0
        self.y = 1
        self.i = 0

    def move(self, path, end):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape) # returns -> (x1,y1,x2,y2)

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

# The Drone Class
print("dock position", dock_pos)
class Drone:
    def __init__(self, size, dock_pos):
        # cross shape
        self.shape = canvas.create_line(dock_pos[0], dock_pos[1], dock_pos[2], dock_pos[3],
                                        dock_pos[0], dock_pos[3], dock_pos[2], dock_pos[1])
        self.xspeed = 0
        self.yspeed = 0

    def move(self):
        pass






################################################################################
################################################################################
################################################################################
# "Main"
wheels = []
for i in range(NUM_OF_WHEELS):
    wheels.append(Wheels(RWITDH, path_list[i]))

pod = Pod(RWITDH, path_list[0])

drone = Drone(RWITDH, dock_pos)

while True:

    for i, wheel in enumerate(wheels):
        wheel.move(path_list[i], dest_list[i])

    pod.move(path_list[0], dest_list[0])
    drone.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
