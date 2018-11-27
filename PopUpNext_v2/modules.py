import constants as const
import parameters as param
import a_star
import citymap
import time
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

pod_data = [[] for i in range(const.NUM_OF_PODS)]
################################################################################
# Ground Module ################################################################
################################################################################
class DriveMod:
    # Initializes varibles when object is created
    id = 0

    def __init__(self, start, end):
        # This is defining the start position of the DriveMod
        self.id = DriveMod.id
        DriveMod.id += 1
        self.tag = "drive%d"%self.id
        x1 = int( start[0] * const.MULTIPLIER )
        y1 = int( start[1] * const.MULTIPLIER )
        x2 = int( start[0] * const.MULTIPLIER + const.SHAPE_SIZE )
        y2 = int( start[1] * const.MULTIPLIER + const.SHAPE_SIZE )
        self.shape = citymap.canvas.create_rectangle(x1, y1, x2, y2, fill="green", tags=self.tag)
        # The speed of the DriveMod
        self.xspeed = self.yspeed = 0
        # The varibels underneath is keeping track of part of the array, path, we are looking for
        self.a = self.x = 0
        self.b = self.y = 1
        # i makes sure that we are entering the right if statement
        self.i = 0 # control variable

        self.start = start
        self.end = end

        self.path = a_star.astar(param.tmaze, start, end) # Generates initial path


################################################################################
    def has_pod(self):
        tags = citymap.canvas.gettags(self.shape)
        for tag in tags:
            if "pair" in tag:
                return True
        return False


################################################################################
    def pairing_tag(self):
        tags = citymap.canvas.gettags(self.shape)
        for tag in tags:
            if "pair" in tag:
                #print("Drive %s"%tag)
                return tag
        return ""

################################################################################
    def drive(self, tag="none"):
        if(self.has_pod() == True):
            ids_to_move = citymap.canvas.find_withtag(self.pairing_tag())
            for num_elements in range(0, len(ids_to_move)):
                citymap.canvas.move(ids_to_move[num_elements], self.xspeed, self.yspeed)
            CommonFunctions.add_cost(self.pairing_tag(),const.WHEEL_COST,"wheel")
        else:
            citymap.canvas.move(self.shape, self.xspeed, self.yspeed)

        # saves the current position if the ground mod
        pos = citymap.canvas.coords(self.shape) # Current position of ground module
        cur_pos = [pos[0], pos[1]]

        # indentify the end coordinates
        dest_x = int( self.end[0]*const.MULTIPLIER )
        dest_y = int( self.end[1]*const.MULTIPLIER )
        dest = [dest_x, dest_y]

        # If no path, dont move(so far) ########################################
        if self.path == None:
            self.xspeed = self.yspeed = 0
            self.a = self.b = 0
            self.i = 4 # Make sure that it doesn't enter another if statement

        # If path, move to destination #########################################
        else:
            # if reached its destination, STOP!
            if cur_pos == dest:
                # It stops the ground mod
                self.xspeed = self.yspeed = 0
                self.a = self.b = 0
                self.i = 4 # Make sure that it doesn't enter another if statement

            # else if not reached destination, CONTINUE!
            elif cur_pos != dest:

                # Determines car direction #####################################
                a_x = self.path[self.a][self.x]
                b_x = self.path[self.b][self.x]
                a_y = self.path[self.a][self.y]
                b_y = self.path[self.b][self.y]

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

                def calc_new_path():
                    self.path.pop(0) # removes first entery of the path
                    self.path = a_star.astar(param.tmaze, self.path[0], self.path[-1])
                    #print("path", self.path)

                # Checking the coordinates of the DriveMod
                # When the DriveMod coordinate has reached a position of a new
                # coordinate, the varibles a and b gets added by one.
                # This is done to make the if statements above to look at the next step of the path


                # if the ground mod has reached a new coordinate in the negative x direction
                if cur_pos[0] >= const.MULTIPLIER * b_x and a_y == b_y and self.i == 0:
                    self.i = 3 # control variable
                    self.xspeed = 0
                    calc_new_path()

                # if the ground mod has reached a new coordinate in the negative x direction
                if cur_pos[0] <= const.MULTIPLIER * b_x and a_y == b_y and self.i == 1:
                    self.i = 3 # control variable
                    self.xspeed = 0
                    calc_new_path()

                # if the ground mod has reached a new coordinate in the positive y direction
                if cur_pos[1] >= const.MULTIPLIER * b_y and a_x == b_x and self.i == 0:
                    self.i = 3 # control variable
                    self.yspeed = 0
                    calc_new_path()

                # if the ground mod has reached a new coordinate in the negative y direction
                if cur_pos[1] <= const.MULTIPLIER * b_y and a_x == b_x and self.i == 1:
                    self.i = 3 # control variable
                    self.yspeed = 0
                    calc_new_path()



################################################################################
# Fly Module ###################################################################
################################################################################
class FlyMod:
    # Initializes varibles when object is created
    id = 0
    def __init__(self, start):
        self.id = FlyMod.id
        FlyMod.id += 1
        self.charge = 100 * const.PIXEL_CHARGE
        self.threshold = 40 * const.PIXEL_CHARGE
        self.speed = 3
        x1 = int( start[0] * const.MULTIPLIER )
        y1 = int( start[1] * const.MULTIPLIER )
        x2 = int( start[0] * const.MULTIPLIER + const.SHAPE_SIZE )
        y2 = int( start[1] * const.MULTIPLIER + const.SHAPE_SIZE )

        #print("%d,%d,%d,%d" %(x1,x2,y1,y2))
        self.tag=("fly%d"%self.id)
        self.shape = [citymap.canvas.create_line(x1, y1, x2, y2, fill="black",width=2,tags=self.tag),
        citymap.canvas.create_line(x1, y2, x2, y1, fill="black",width=2,tags=self.tag)]
        #print("This the shape %d %d" %(self.shape[0],self.shape[1]))
        self.xspeed = self.yspeed = 0
    #Methods
    #fly to wheels with pods
    #pick up pod
    def pick_up_pod(self,pod):
        pod_tag=pod.tag
        pos = citymap.canvas.coords(self.shape[0])
        cur_pos = [pos[0], pos[1]]
        pod_pos = citymap.canvas.coords(pod.shape[0])
        pod_cur_pos = [pod_pos[0], pod_pos[1]]
        #print("Current Pos: %d,%d"%(cur_pos[0],cur_pos[1]))
        #print("Pod Pos: %d, %d"%(pod_cur_pos[0],pod_cur_pos[1]))
        at_dest=False
        if (self.has_pod()==False):
            at_dest=self.fly(pod_cur_pos)
            #print(at_dest)
            if at_dest==True:
                CommonFunctions.remove_tags([self.tag,pod_tag])
                CommonFunctions.add_tags("pair10%d"%self.id,[self.tag, pod_tag])
        elif self.has_pod()==True:
            self.fly(pod.dest)
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
        #print(tot_dist)
        if (self.charge-tot_dist)>self.threshold:
            return True
        return False
    #fly directly to Destination
    def fly(self, end):
        #currently doesnt account for astar positions, but shouldnt need to
        dest_x = (end[0])
        dest_y = (end[1])
        dest = [dest_x,dest_y]
        result=self.charge_for_dest(dest)
        if result==True:
            pos = citymap.canvas.coords(self.shape[0])
            cur_pos = [pos[0], pos[1]]
            self.xspeed = 0.0
            self.yspeed = 0.0
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
                    CommonFunctions.add_cost(self.pairing_tag(),const.DRONE_COST,"drone")
                else:
                    for num_elements in range(0,len(self.shape)):
                        citymap.canvas.move(self.shape[num_elements], self.xspeed, self.yspeed)

                return False




################################################################################
# Pod Module ###################################################################
################################################################################
class PodMod:
    # Initializes varibles when object is created
    id = 0
    def __init__(self, start,end):
        # This is defining the start position of the DriveMod
        self.id = PodMod.id
        PodMod.id += 1
        dest_x = int(end[0]* const.MULTIPLIER )
        dest_y = int(end[1]* const.MULTIPLIER )
        self.dest = [dest_x, dest_y]
        self.tag="pod%d"%self.id
        x1 = int( start[0] * const.MULTIPLIER )
        y1 = int( start[1] * const.MULTIPLIER )
        x2 = int( start[0] * const.MULTIPLIER + const.SHAPE_SIZE )
        y2 = int( start[1] * const.MULTIPLIER + const.SHAPE_SIZE )
        self.shape=[citymap.canvas.create_oval(x1, y1, x2, y2, fill="grey",tags=[self.tag,"d_cost=0","w_cost=0"]),
        citymap.canvas.create_text( x2, y2,text=self.id,tags=self.tag,anchor="nw")]
        citymap.canvas.create_text(end[0]* const.MULTIPLIER + const.SHAPE_SIZE,
        end[1]*const.MULTIPLIER + const.SHAPE_SIZE,text=self.id,anchor="nw")
        #print(citymap.canvas.gettags(self.shape[0]))
        self.d_cost=0
        self.w_cost=0

    # 1) follow airmod/DriveMod
    # 2) check if it's not on airmod/DriveMod
    # 3) check if has reached final destination
    # 4) check if has passengers
    def at_dest(self):
        pos = citymap.canvas.coords(self.shape[0])
        cur_pos = [pos[0], pos[1]]
        self.xspeed = 0.0
        self.yspeed = 0.0
        if cur_pos == self.dest:
            return True
        return False

class CommonFunctions:

    def add_tags(pairing_tag, curr_tags):
        for curr_tag in curr_tags:
            citymap.canvas.addtag_withtag(pairing_tag, curr_tag)
    def remove_tags(curr_tags):
        for curr_tag in curr_tags:
            items=citymap.canvas.find_withtag(curr_tag)
            for item in items:
                all_tags=citymap.canvas.gettags(item)
                #print(all_tags)
                for tag in all_tags:
                    if not ("pod" in tag or "drive" in tag or "fly" in tag or "cost" in tag):
                        citymap.canvas.dtag(item, tag)
    def add_cost_to_tag(tag,value):
        split_tag=tag.split('=')
        number=int(split_tag[1])
        number+=value
        return_tag=split_tag[0]+'='+str(number)
        #print(return_tag)
        return return_tag

    def add_cost(pairing_tag,value,sender):
        items=citymap.canvas.find_withtag(pairing_tag)
        for item in items:
            all_tags=citymap.canvas.gettags(item)
            for tag in all_tags:
                #print(tag)
                if "pod" in tag:
                    split_tag=tag.replace("pod","")
                    id=int(split_tag)
                    new_cost=pod_data[id][len(pod_data[id])-1]+value
                    #print(new_cost)
                    pod_data[id].append(new_cost)
                if ("d_cost" in tag and sender=="drone") or ("w_cost" in tag and sender=="wheel"):
                    #print(tag)
                    new_cost=CommonFunctions.add_cost_to_tag(tag,value)
                    citymap.canvas.addtag_withtag(new_cost,item)
                    citymap.canvas.dtag(item, tag)
                    #print(citymap.canvas.gettags(item))
                    break


class GenerateResults:
    def export_txt(pods):
        file=open("PopUpResultsGeneral.txt","w+")
        for i in range(0,len(pods)):
            pod_id=citymap.canvas.find_withtag(pods[i].tag)
            #print(pod_id[1])
            all_tags=citymap.canvas.gettags(pod_id[0])
            file.write("\r\n")
            for tag in all_tags:
                #print(tag)
                file.write(tag)
                file.write("\r\n")

        file.close()
        for i in range(0,const.NUM_OF_PODS):
            file=open("PopUpResults%d.txt"%pods[i].id,"w+")
            for count in range(0,len(pod_data[i])):
                file.write(str(pod_data[i][count]))
                file.write("\r\n")
            file.close()
    def generate_graphs():
        for i in range(0,const.NUM_OF_PODS):
            x_data=[]
            for count in range(0,len(pod_data[i])):
                x_data.append(count*const.SLEEP_TIME)
            y_data = pod_data[i]

            trace = go.Scatter(
                x = x_data,
                y = y_data
            )
            data = [trace]
            py.iplot(data, filename='Pod%d'%i)
    def init_pod_data():
        for i in range(0,const.NUM_OF_PODS):
            pod_data[i].append(0)

################################################################################
# END ##########################################################################
################################################################################
