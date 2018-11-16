import constants as const
import parameters as param
import citymap


################################################################################
# Ground Module ################################################################
################################################################################
class DriveMod:
    # Initializes varibles when object is created
    id = 0
    def __init__(self, start):
        # This is defining the start position of the DriveMod
        self.id = DriveMod.id
        DriveMod.id += 1
        x1 = int( start[0]*((const.RLENGTH+const.RWITDH)/2) )
        y1 = int( start[1]*((const.RLENGTH+const.RWITDH)/2) )
        x2 = int( start[0]*((const.RLENGTH+const.RWITDH)/2) + const.SHAPE_SIZE )
        y2 = int( start[1]*((const.RLENGTH+const.RWITDH)/2) + const.SHAPE_SIZE )
        self.shape = citymap.canvas.create_rectangle(x1, y1, x2, y2, fill="green", tags="drive%d"%self.id)
        # The speed of the DriveMod
        self.xspeed = self.yspeed = 0
        # The varibels underneath is keeping track of part of the array, path, we are looking for
        self.a = self.x = 0
        self.b = self.y = 1
        # i makes sure that we are entering the right if statement
        self.i = 0 # control variable
    def has_pod(self):
        tags = citymap.canvas.gettags(self.shape)
        for tag in tags:
            if "pair" in tag:
                return True
        return False
    def pairing_tag(self):
        tags = citymap.canvas.gettags(self.shape)
        for tag in tags:
            if "pair" in tag:
                return tag
        return ""                                # WHY THIS?
    def move(self, path, end, tag="none"):
        if(self.has_pod() == True):
            ids_to_move = citymap.canvas.find_withtag(self.pairing_tag())
            for num_elements in range(0,len(ids_to_move)):
                citymap.canvas.move(ids_to_move[num_elements], self.xspeed, self.yspeed)
        else:
            citymap.canvas.move(self.shape, self.xspeed, self.yspeed)
        # saves the current position if the ground mod
        pos = citymap.canvas.coords(self.shape) # Current position of ground module
        cur_pos = [pos[0], pos[1]]
        # indentify the end coordinates
        dest_x = int( end[0]*((const.RLENGTH+const.RWITDH)/2) )
        dest_y = int( end[1]*((const.RLENGTH+const.RWITDH)/2) )
        dest = [dest_x, dest_y]

        # if ground module has reached its destination
        if cur_pos == dest:
            # It stops the ground mod
            self.xspeed = self.yspeed = 0
            self.a = self.b = 0
            self.i = 4 # Make sure that it doesn't enter another if statement

        # Steering of the DriveMod i and speed ###########################
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

        # Checking the coordinates of the DriveMod
        # When the DriveMod coordinate has reached a position of a new
        # coordinate, the varibles a and b gets added by one.
        # This is done to make the if statements above to look at the next step of the path
        if cur_pos[0] >= ((const.RLENGTH+const.RWITDH)/2)*b_x and a_y == b_y and self.i == 0:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3 # control variable
        # if the ground mod has reached a new coordinate in the negative x direction
        if cur_pos[0] <= ((const.RLENGTH+const.RWITDH)/2)*b_x and a_y == b_y and self.i == 1:
            self.xspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3 # control variable
        # if the ground mod has reached a new coordinate in the positive y direction
        if cur_pos[1] >= ((const.RLENGTH+const.RWITDH)/2)*b_y and a_x == b_x and self.i == 0:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3 # control variable
        # if the ground mod has reached a new coordinate in the negative y direction
        if cur_pos[1] <= ((const.RLENGTH+const.RWITDH)/2)*b_y and a_x == b_x and self.i == 1:
            self.yspeed = 0
            self.a = self.a + 1
            self.b = self.b + 1
            self.i = 3 # control variable





################################################################################
# Fly Module ###################################################################
################################################################################
class FlyMod:
    # Initializes varibles when object is created
    id = 0
    def __init__(self, start):
        self.id = FlyMod.id
        FlyMod.id += 1
        self.charge = 100*const.PIXEL_CHARGE
        self.threshold = 40*const.PIXEL_CHARGE
        self.speed = 2
        x1 = int( start[0]*((const.RLENGTH+const.RWITDH)/2) )
        y1 = int( start[1]*((const.RLENGTH+const.RWITDH)/2) )
        x2 = int( start[0]*((const.RLENGTH+const.RWITDH)/2) + const.SHAPE_SIZE )
        y2 = int( start[1]*((const.RLENGTH+const.RWITDH)/2) + const.SHAPE_SIZE )

        #print("%d,%d,%d,%d" %(x1,x2,y1,y2))
        self.shape = [citymap.canvas.create_line(x1, y1, x2, y2, fill="black",width=3,tags=("fly%d"%self.id)),
        citymap.canvas.create_line(x1, y2, x2, y1, fill="black",width=3,tags=("fly%d"%self.id))]
        #print("This the shape %d %d" %(self.shape[0],self.shape[1]))
        self.xspeed = self.yspeed = 0
    #Methods
    #fly to wheels with pods
    #pick up pod
    #drop off pod
    #check if has pod
    def has_pod(self):
        tags=citymap.canvas.gettags(self.shape[0])
        for tag in tags:
            if "pair" in tag:
                return True
        return False
    def charge(self):
        if(self.charge > threshold):
            return False
        return True
    def pairing_tag(self):
        tags=citymap.canvas.gettags(self.shape[0])
        for tag in tags:
            if "pair" in tag:
                return tag
        return ""
    def charge_for_dest(self,end):
        pos = citymap.canvas.coords(self.shape[0])
        dist_travel=[pos[0]-end[0],pos[1]-end[1]]
        tot_dist=abs(dist_travel[0])+abs(dist_travel[1])
        if (self.charge-tot_dist)>self.threshold:
            return True
        return False
    #fly directly to Destination
    def fly(self, end):
        if self.charge_for_dest(end)==True or end==const.HUB:
            pos = citymap.canvas.coords(self.shape[0])
            cur_pos = [pos[0], pos[1]]
            self.xspeed = 0.0
            self.yspeed = 0.0

            dest_x = round(end[0]*((const.RLENGTH+const.RWITDH)/2) )
            dest_y = round(end[1]*((const.RLENGTH+const.RWITDH)/2) )
            dest = [dest_x,dest_y]
            #print("End Point: %d,%d" %(dest_x,dest_y))
            #print("Current Position: %d,%d" %(cur_pos[0],cur_pos[1]))
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
                if(self.has_pod() == True):
                    ids_to_move = citymap.canvas.find_withtag(self.pairing_tag())
                    for num_elements in range(0,len(ids_to_move)):
                        citymap.canvas.move(ids_to_move[num_elements], self.xspeed, self.yspeed)
                else:
                    for num_elements in range(0,len(self.shape)):
                        citymap.canvas.move(self.shape[num_elements], self.xspeed, self.yspeed)
                #self.charge-=(self.xspeed+self.yspeed)
                return False



''' The default of the tkinter toolkit draws new items on top of existing ones.
 If we want drones to pick up pods they have to be declared sequentially'''
################################################################################
# Pod Module ###################################################################
################################################################################
class PodMod:
    # Initializes varibles when object is created
    id = 0
    def __init__(self, start):
        # This is defining the start position of the DriveMod
        self.id = PodMod.id
        PodMod.id += 1
        x1 = int( start[0]*((const.RLENGTH+const.RWITDH)/2) )
        y1 = int( start[1]*((const.RLENGTH+const.RWITDH)/2) )
        x2 = int( start[0]*((const.RLENGTH+const.RWITDH)/2) + const.SHAPE_SIZE )
        y2 = int( start[1]*((const.RLENGTH+const.RWITDH)/2) + const.SHAPE_SIZE )
        self.shape = citymap.canvas.create_oval(x1, y1, x2, y2, fill="grey",tags="pod%d"%self.id)
        # The speed of the DriveMod
        self.xspeed = self.yspeed = 0
        # The varibels underneath is keeping track of part of the array, path, we are looking for
        self.a = self.x = 0
        self.b = self.y = 1
        # i makes sure that we are entering the right if statement
        self.i = 0 # control variable

    # 1) follow airmod/DriveMod
    # 2) check if it's not on airmod/DriveMod
    # 3) check if has reached final destination
    # 4) check if has passengers


class CommonFunctions:
    def add_tags(curr_tags, pairing_tag):
        for curr_tag in curr_tags:
            citymap.canvas.addtag_withtag(pairing_tag, curr_tag)
        #print("Pairing: %s"%pairing_tags)
        #print(canvas.find_withtag(pairing_tags))
    def remove_tags(curr_tags, pairing_tag):
        for curr_tag in curr_tags:
            citymap.canvas.dtag((citymap.canvas.find_withtag(curr_tag), pairing_tag))
        #print("Pairing: %s"%pairing_tag)
        #print(canvas.find_withtag(pairing_tag))


################################################################################
# END ##########################################################################
################################################################################
