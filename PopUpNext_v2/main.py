import numpy
from tkinter import *
import random
import time
from pprint import pprint
import math
import itertools
################################################################################
# A* ###########################################################################
################################################################################
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
    
    
def AllCombinations(my_list, empty_list):
    """Fills an empty list with all possible combinations from my_list"""
    count = 0
    for i in range(1, len(my_list)+1):
        #Number of combinations for given i
        count += math.factorial(len(my_list))/(math.factorial(i)*math.factorial(len(my_list)-i))
        
    for i in range(1, len(my_list)+1):
        a = itertools.combinations(my_list, i)
        for subset in a:
            empty_list.append(list(subset))
            
def trafficBlock(maze, start1, end, empty_fly_arr):
    """Returns an array that requires flying
    path_arr = [[start,critical_traffic_1),(critcial_traffic_1, critical_traffic_2),...,(critical_traffic_N,end]]
    adds start and end coordinates to empty_fly_arr
    """
    #Remove traffic
    maze_simple = np.copy(maze)
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze_simple[j][i] == 1:
              maze_simple[j][i] = 0
              

    
    #Find quickest path if no traffic    
    tmaze3=[]
    rez3 = [[maze_simple[j][i] for j in range(len(maze_simple))] for i in range(len(maze_simple[0]))]
    for row in rez3:
        tmaze3.append(row)
    path_nt = astar(tmaze3, start1, end)  #path_nt is no traffic path
    
    one_count = 0  #variable indicates indice of traffic
    
    one_indices = [] #Stores the indicies of traffic
    one_coordinates = [] #Stores the coordinates of the traffic blocks
    j = 0;

    
    #Find where traffic is on this path    
    for i in path_nt:
        if maze[i[1]][i[0]] == 1:  
            one_indices.append(one_count)
            one_coordinates.append(i)
            j+=1
        one_count += 1
    count = 0
    

    comb_indices = []
    AllCombinations(one_coordinates, comb_indices) #all possible combinaions of traffic indices
    count = 0
    test_maze = np.copy(maze)
    
    #i is a combination of different traffic indices
    #j is the traffic indices constituting the combination
    #This loop iterates through all combinations, removing traffic at tests indices and seeing 
    #if a path is possible
    for i in comb_indices :
        for j in i:
            test_maze[j[1]][j[0]] = 0
        
        tmaze2=[]
        rez2 = [[test_maze[j][i] for j in range(len(test_maze))] for i in range(len(test_maze[0]))]
        for row in rez2:
            tmaze2.append(row)

        path = astar(tmaze2, start1, end)
        
        if path != None:
            traff_ind = i
            break
        
        test_maze = np.copy(maze)
        count += 1
        
    sur_ind = np.zeros(len(traff_ind)) #stores indice of removed traffic
    sur_count = 0
    path_count = 0
    
    #finds index of traffic in path list
    for k in traff_ind :  
        for p in path :
            if k == p:
                sur_ind[sur_count] = path_count
                sur_count += 1
            path_count += 1
        path_count = 0
        
     
    #Fill path_arr with different components of rravel
    
    path_arr = [astar(tmaze, start1, path[int(sur_ind[0]-1)][::-1])]
    
    if sur_ind.size > 2:
    
        for i in range(1, len(sur_ind)):
            path_arr.append(astar(tmaze), path[sur_ind[i-1]+1][::-1], path[sur_ind[i]-1][::-1])
        
    path_arr.append(astar(tmaze, path[int(sur_ind[-1]+1)][::-1], end))
    
    start_coor = path_arr[0][-1]
    
    count = 0
    
    for i in path_arr:
        if count > 0:
            end_coor = i[0]
            empty_fly_arr.append([start_coor,end_coor])
            start_coor = i[-1]
        else:
            count += 1
            
        
        
    
    print(path_arr)

def astar(tmaze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given tmaze"""
    #Enables intuitive accessung of maze
    start = (start[1],start[0])
    end = (end[1], end[0])
    
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


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

# Flips the matrix in the crossaxis to get the visuals the match x and y
tmaze=[]
rez = [[maze[j][i] for j in range(len(maze))] for i in range(len(maze[0]))]
for row in rez:
    tmaze.append(row)

#start=(0,0)
#end=(6,5)
#path = astar(tmaze, start, end)
#if path == None:
#    trafficBlock(maze, start1, end)

#else:
#    print(path)

# multiple paths ###############################################################
NUM_OF_WHEELS = 10
def multiple_astar_paths(tmaze, NUM_OF_WHEELS, astar):
    # Generates a coordinate list based on the size of the city map matrix
    coord_list = [] # coordinate List
    for x in range(len(tmaze)-1): # iterates through number of columns
        for y in range(len(tmaze[0])-1): # iterates through number of rows
            if tmaze[x][y] == 0: # if There is no traffic in this coordinate "0" then append coordinate
                coord_list.append((x,y)) # Coordinate list that does not have traffic
            elif tmaze[x][y] == 1: # else if there is traffic in this coordinate "1" do nothing
                continue
            elif tmaze[x][y] == 2: # else if there is traffic in this coordinate "1" do nothing
                continue
    # Select random numbers from 'coord_list' and places them in strt_list and dest_list
    strt_list = [] # Start List
    dest_list = [] # Destination List
    for i in range(NUM_OF_WHEELS):
        strt_list.append(random.choice(coord_list))
        dest_list.append(random.choice(coord_list))
    print('start list:', strt_list)
    print('destination list:', dest_list)
    # Created a list of paths using A* algorithm
    path_list = [] # Path List
    for i in range(NUM_OF_WHEELS):
        path_list.append(astar(tmaze, strt_list[i], dest_list[i]))
    print('Path list:', path_list)
    return strt_list, dest_list, path_list

strt_list, dest_list, path_list = multiple_astar_paths(tmaze, NUM_OF_WHEELS, astar)
################################################################################
# WINDOW #######################################################################
################################################################################

tk=Tk()

# Defining the size of the canvas
CWIDTH = 700 # CANVAS WIDTH
CHEIGHT = 700 # CANVAS LENGTH
RWITDH = 20 # ROAD WIDTH
RLENGTH = int( (CWIDTH-(((len(maze)/2)+0.5)*RWITDH)) / ((len(maze)/2)-0.5) ) # ROAD LENGTH

# Creating the canvas
canvas = Canvas(tk, width=CWIDTH, height=CHEIGHT)
canvas.pack()
canvas.configure(highlightthickness=0, borderwidth=0) # removes cut off on top and left edges

# Houses #######################################################################
# Makes houses for every second coordinate in the x and y axis
box_x = 0
for i in range(int((len(tmaze)-1)/2)):
    box_y = 0
    for i in range(int((len(tmaze[0])-1)/2)):
        canvas.create_rectangle(box_x + RWITDH,
                                box_y + RWITDH,
                                box_x + RWITDH + RLENGTH,
                                box_y + RWITDH + RLENGTH )
        box_y = box_y + RLENGTH + RWITDH
    box_x = box_x + RLENGTH + RWITDH

# Traffic ######################################################################
# Makes traffic for all the '1's in  tmaze
for x in range(len(tmaze)):
    for y in range(len(tmaze[0])):
        if tmaze[x][y] == 1 and not x % 2 == 0: #Makes a rectangle between buildings in the x axis
            col = ((RLENGTH+RWITDH)*((x/2)-0.5))+RWITDH
            row = (RLENGTH+RWITDH)*(y/2)
            canvas.create_rectangle(col, row, col + RLENGTH, row + RWITDH, fill="red")
        if tmaze[x][y] == 1 and not y % 2 == 0: #Makes a rectangle between buildings in the y axis
            row = ((RLENGTH+RWITDH)*((y/2)-0.5))+RWITDH
            col = (RLENGTH+RWITDH)*(x/2)
            canvas.create_rectangle(col, row, col + RWITDH, row + RLENGTH, fill="red")
        if tmaze[x][y] == 1 and x % 2 == 0 and y % 2 == 0: #Makes a squere on crossroads
            row = ((RLENGTH+RWITDH)*(y/2))
            col = ((RLENGTH+RWITDH)*(x/2))
            canvas.create_rectangle(col, row, col + RWITDH ,row + RWITDH, fill="red")

# Destination ##################################################################
# Creates a square at the destination coordinate
def create_destination(RWITDH, RLENGTH, NUM_OF_WHEELS, dest_list):
    for i in range (NUM_OF_WHEELS):
        x1 = int( dest_list[i][0]*((RLENGTH+RWITDH)/2) )
        y1 = int( dest_list[i][1]*((RLENGTH+RWITDH)/2) )
        x2 = int( dest_list[i][0]*((RLENGTH+RWITDH)/2) + RWITDH )
        y2 = int( dest_list[i][1]*((RLENGTH+RWITDH)/2) + RWITDH )
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

create_destination(RWITDH, RLENGTH, NUM_OF_WHEELS, dest_list)

# Ground Module ################################################################
class GrdMod:
    # Initializes varibles when object is created
    def __init__(self, size, start, i):
        # This is defining the start position of the GrdMod
        self.id = 'G' + str(i) #Gi ground module number i
        x1 = int( start[0]*((RLENGTH+RWITDH)/2) )
        y1 = int( start[1]*((RLENGTH+RWITDH)/2) )
        x2 = int( start[0]*((RLENGTH+RWITDH)/2) + size )
        y2 = int( start[1]*((RLENGTH+RWITDH)/2) + size )
        self.shape = canvas.create_rectangle(x1, y1, x2, y2, fill="green")
        print(self.shape)
        # The speed of the GrdMod
        self.xspeed = self.yspeed = 0
        # The varibels underneath is keeping track of part of the array, path, we are looking for
        self.a = self.x = 0
        self.b = self.y = 1
        # i makes sure that we are entering the right if statement
        self.i = 0 # control variable

    def move(self, path, end):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        # saves the current position if the ground mod
        pos = canvas.coords(self.shape) # Current position of ground module
        cur_pos = [pos[0], pos[1]]
        # indentify the end coordinates
        dest_x = int( end[0]*((RLENGTH+RWITDH)/2) )
        dest_y = int( end[1]*((RLENGTH+RWITDH)/2) )
        dest = [dest_x, dest_y]

        # if ground module has reached its destination
        if cur_pos == dest:
            # It stops the ground mod
            self.xspeed = self.yspeed = 0
            self.a = self.b = 0
            self.i = 4 # Make sure that it doesn't enter another if statement

        # Steering of the GrdMod i and speed ###########################
        #use these values to determine i of travel
        a_x = path[self.a][self.x]
        b_x = path[self.b][self.x]
        a_y = path[self.a][self.y]
        b_y = path[self.b][self.y]

        if a_x < b_x:
            # positive in the x i
            self.xspeed = 1
            self.yspeed = 0
            self.i = 0 # control variable
        if b_x < a_x:
            # negative in the x i
            self.xspeed = -1
            self.yspeed = 0
            self.i = 1 # control variable
        if a_y < b_y:
            # positive in the y i
            self.xspeed = 0
            self.yspeed = 1
            self.i = 0 # control variable
        if b_y < a_y:
            # negative in the y i
            self.xspeed = 0
            self.yspeed = -1
            self.i = 1 # control variable

        # Checking the coordinates of the GrdMod
        # When the GrdMod coordinate has reached a position of a new
        # coordinate, the varibles a and b gets added by one.
        # This is done to make the if statements above to look at the next step of the path
        if cur_pos[0] >= ((RLENGTH+RWITDH)/2)*b_x and a_y == b_y and self.i == 0:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3 # control variable
        # if the ground mod has reached a new coordinate in the negative x direction
        if cur_pos[0] <= ((RLENGTH+RWITDH)/2)*b_x and a_y == b_y and self.i == 1:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3 # control variable
        # if the ground mod has reached a new coordinate in the positive y direction
        if cur_pos[1] >= ((RLENGTH+RWITDH)/2)*b_y and a_x == b_x and self.i == 0:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3 # control variable
        # if the ground mod has reached a new coordinate in the negative y direction
        if cur_pos[1] <= ((RLENGTH+RWITDH)/2)*b_y and a_x == b_x and self.i == 1:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3 # control variable

        return cur_pos, dest, id

class FlyMod:
    # Initializes varibles when object is created
    def __init__(self, size, start):
        self.pod_status = False
        self.charge = 100
        self.speed = 2
        x1 = int( start[0]*((RLENGTH+RWITDH)/2) )
        y1 = int( start[1]*((RLENGTH+RWITDH)/2) )
        x2 = int( start[0]*((RLENGTH+RWITDH)/2) + size )
        y2 = int( start[1]*((RLENGTH+RWITDH)/2) + size )

        #print("%d,%d,%d,%d" %(x1,x2,y1,y2))
        self.shape = [canvas.create_line(x1, y1, x2, y2, fill="black",width=3),
        canvas.create_line(x1, y2, x2, y1, fill="black",width=3)]
        #print("This the shape %d %d" %(self.shape[0],self.shape[1]))
        self.xspeed = self.yspeed = 0
    #Methods
    #fly to wheels with pods
    #pick up pod
    #drop off pod
    #check if has pod
    def has_pod(self):
        return self.pod_status
    def charge(self):
        threshold = 20
        if(self.charge>threshold):
            return False
        return True
    #fly directly to Destination
    def fly(self,end):
        pos=canvas.coords(self.shape[0])
        cur_pos=[pos[0], pos[1]]
        self.xspeed=0.0
        self.yspeed=0.0

        dest_x = round(end[0]*((RLENGTH+RWITDH)/2) )
        dest_y = round(end[1]*((RLENGTH+RWITDH)/2) )
        dest = [dest_x,dest_y]
        #print("End Point: %d,%d" %(dest_x,dest_y))
        #print("Current Position: %d,%d" %(cur_pos[0],cur_pos[1]))
        print()
        if cur_pos == dest:
            self.xspeed = self.yspeed = 0.0
            return True
        else:
            rise = (dest_y-cur_pos[1])
            run = (dest_x-cur_pos[0])
            if(run != 0):
                if(rise != 0):
                    slope = abs(rise/run)
                    self.xspeed = (run/abs(run))*self.speed/(slope+1)
                    self.yspeed = (rise/abs(rise))*slope*abs(self.xspeed)
                else:
                    self.yspeed = 0.0
                    self.xspeed = (run/abs(run))*self.speed
            else:
                self.xspeed = 0.0
                self.yspeed = (rise/abs(rise))*self.speed
            if(abs(self.yspeed) > abs(rise)):
                self.yspeed = rise
            if(abs(self.xspeed) > abs(run)):
                self.xspeed = run
            for num_elements in range(0,len(self.shape)):
                canvas.move(self.shape[num_elements], self.xspeed, self.yspeed)
            return False

# Pod Module ###################################################################
class PodMod:
    # Initializes varibles when object is created
    def __init__(self, size, start, i):
        self.id = 'P' + str(i) #Gi ground module number i
        # This is defining the start position of the GrdMod
        x1 = int( start[0]*((RLENGTH+RWITDH)/2) )
        y1 = int( start[1]*((RLENGTH+RWITDH)/2) )
        x2 = int( start[0]*((RLENGTH+RWITDH)/2) + size )
        y2 = int( start[1]*((RLENGTH+RWITDH)/2) + size )
        self.shape = canvas.create_oval(x1, y1, x2, y2, fill="grey")
        # The speed of the GrdMod
        self.xspeed = self.yspeed = 0
        # The varibels underneath is keeping track of part of the array, path, we are looking for
        self.a = self.x = 0
        self.b = self.y = 1
        # i makes sure that we are entering the right if statement
        self.i = 0 # control variable

    # 1) follow airmod/grdmod
    def move(self, path, end):
        GrdMod.move(self, path, end)

    # 2) check if it's not on airmod/grdmod

    # 3) check if has reached final destination
    # 4) check if has passengers

################################################################################
# MAIN #########################################################################
################################################################################

# Ground module
wheels = []
for i in range(NUM_OF_WHEELS):
    wheels.append(GrdMod(RWITDH, strt_list[i], i))

# Pod module
pod = PodMod(RWITDH, strt_list[0], 0) # creating pod at first wheel position



# fly module
drones = []
done_check=[]
check_at_dest=0
for i in range(NUM_OF_WHEELS):
    drones.append(FlyMod(RWITDH, strt_list[i]))
    done_check.append(False)

print("Ground Mod:")
pprint(vars(wheels[0]))
print("Pod Mod:")
pprint(vars(pod))

while True:
    for i, wheel in enumerate(wheels):
        wheel.move(path_list[i], dest_list[i])

    pod.move(path_list[0], dest_list[0])

    for i, drone in enumerate(drones):
        if done_check[i] == False:
            check_at_dest = 0
            done_check[i] = drone.fly(dest_list[i])
        else:
            check_at_dest += 1
            #if check_at_dest == len(wheels):
                #time.sleep(0.5)
                #quit()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
