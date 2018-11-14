################################################################################
# IMPORTING FILES AND LIBRARIES ################################################
################################################################################
# Files
import a_star # contains A* algorithm and some other functions
import citymap # contains functions that create components in citymap and canvas
import constants as const # paramaters that don't change often
import parameters as param # paramaters that might change often
import modules as mod # contains the Drive, Fly and Pod modules
# Libraries
import numpy
from tkinter import *
import random
import time
from pprint import pprint


################################################################################
# START ########################################################################
################################################################################
# generates multiple random start and end positions
strt_list, dest_list = a_star.random_start_dest(param.tmaze, const.NUM_OF_WHEELS)
# generates multiple paths for the given start and end positions
path_list = a_star.multiple_astar_paths(param.tmaze, const.NUM_OF_WHEELS, strt_list, dest_list)

<<<<<<< HEAD
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
    def __init__(self, size, start,id):
        self.pod_status = False
        self.charge = 100
        self.speed = 5
        x1 = round(start[0]*((RLENGTH+RWITDH)/2) )
        y1 = round(start[1]*((RLENGTH+RWITDH)/2) )
        x2 = round(start[0]*((RLENGTH+RWITDH)/2) + size )
        y2 = round(start[1]*((RLENGTH+RWITDH)/2) + size )

        #print("%d,%d,%d,%d" %(x1,x2,y1,y2))
        self.shape = [canvas.create_line(x1, y1, x2, y2, fill="black",width=3, tags=("quadcopter%d"%id)),
        canvas.create_line(x1, y2, x2, y1, fill="black",width=3, tags=("quadcopter%d"%id))]
        print(canvas.gettags(self.shape[0]))

        self.xspeed = self.yspeed = 0
    #Methods
    def addtags(self,tags):
        for num_elements in range(len(self.shape)):
            canvas.itemconfig(self.shape[num_elements],tags=tags)
        pprint(canvas.gettags(self.shape[0]))
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
    def fly(self,end,tag):
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
            ids_to_move=canvas.find_withtag(tag)
            print(ids_to_move)
            for num_elements in range(0,len(ids_to_move)):
                canvas.move(ids_to_move[num_elements], self.xspeed, self.yspeed)
            return False

# Pod Module ###################################################################
class PodMod:
    # Initializes varibles when object is created
    def __init__(self, size, start, i):
        self.id = 'P' + str(i) #Gi ground module number i
        # This is defining the start position of the GrdMod
        x1 = round(start[0]*((RLENGTH+RWITDH)/2) )
        y1 = round(start[1]*((RLENGTH+RWITDH)/2) )
        x2 = round(start[0]*((RLENGTH+RWITDH)/2) + size )
        y2 = round(start[1]*((RLENGTH+RWITDH)/2) + size )
        self.shape = canvas.create_oval(x1, y1, x2, y2, fill="grey",tags=("pod%d"%i))
        #print(canvas.gettags(self.shape))
        # The speed of the GrdMod
        self.xspeed = self.yspeed = 0
        # The varibles underneath is keeping track of part of the array, path, we are looking for
        self.a = self.x = 0
        self.b = self.y = 1
        # i makes sure that we are entering the right if statement
        self.i = 0 # control variable

    # 1) follow airmod/grdmod
    def move(self, path, end):
        GrdMod.move(self, path, end)
=======


################################################################################
# Generates City Maps Component ################################################
################################################################################
citymap.create_houses(param.tmaze) # Generates Houses
citymap.create_traffic(param.tmaze) # Generates Traffic
citymap.create_destination(dest_list) # Generates Destination blocks
>>>>>>> kamybranch





def addtags(curr_tags, pairing_tag):
    for curr_tag in curr_tags:
        canvas.addtag_withtag(pairing_tag, curr_tag)
    #print("Pairing: %s"%pairing_tags)
    #print(canvas.find_withtag(pairing_tags))
def removetags(curr_tags, pairing_tag):
    for curr_tag in curr_tags:
        canvas.dtag((canvas.find_withtag(curr_tag), pairing_tag))
    #print("Pairing: %s"%pairing_tag)
    #print(canvas.find_withtag(pairing_tag))

################################################################################
# Creating  Drive, Pod and Fly Modules #########################################
################################################################################
# Drive module
wheels = []
<<<<<<< HEAD
pods = []
for i in range(NUM_OF_WHEELS):
    wheels.append(GrdMod(RWITDH, strt_list[i], i))

# Pod module
# pod = PodMod(RWITDH, strt_list[0], 0) # creating pod at first wheel position
for i in range(NUM_OF_WHEELS):
    pods.append(PodMod(RWITDH, strt_list[i], i))

# fly module
drones = []
done_check = []

check_at_dest = 0
for i in range(NUM_OF_WHEELS):
    pairing=[]
    drones.append(FlyMod(RWITDH, strt_list[i],i))
    addtags(["pod%d"%i,"quadcopter%d"%i],"p%d"%i)
    done_check.append(False)
print("Ground Mod:")
pprint(vars(wheels[0]))
=======
for i in range(const.NUM_OF_WHEELS):
    wheels.append(mod.DriveMod(strt_list[i]))

# Pod module
pods = []
for i in range(const.NUM_OF_WHEELS):
    pods.append(mod.PodMod(strt_list[i]))

# Fly module
drones = []
for i in range(const.NUM_OF_WHEELS):
    drones.append(mod.FlyMod(strt_list[i]))

print("Drive Mod:")
pprint(vars(wheels[0]))
print("Pod Mod:")
pprint(vars(pods[0]))
print("Fly Mod:")
pprint(vars(drones[0]))


>>>>>>> kamybranch

################################################################################
# Main Loop ####################################################################
################################################################################
while True:
    for i, wheel in enumerate(wheels):
        wheel.move(path_list[i], dest_list[i])

<<<<<<< HEAD
        #pods[i].move(path_list[i], dest_list[i])

    for i, drone in enumerate(drones):
        if done_check[i] == False:
            check_at_dest = 0
            done_check[i] = drone.fly(dest_list[i],"p%d"%i)
        else:
            check_at_dest += 1
            #if check_at_dest == len(wheels):
                #time.sleep(0.5)
                #quit()
    tk.update()
=======
    for i, pod in enumerate(pods):
        pod.move(path_list[i], dest_list[i])

    for i, drone in enumerate(drones):
        drone.fly(dest_list[i])

    citymap.tk.update()
>>>>>>> kamybranch
    time.sleep(0.01)



################################################################################
# END ##########################################################################
################################################################################
citymap.tk.mainloop()
