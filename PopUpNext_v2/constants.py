# Canvas
CWIDTH = 700 # CANVAS WIDTH
CHEIGHT = 700 # CANVAS LENGTH

#
def den_define():
    file=open("den_value.txt","r")
    data=file.readlines()
    for line in data:
        data_values=line.split(',')
        try:
            data_entry=int(data_values[0])
            if(data_entry<21):
                den_val=data_entry/50
            else:
                den_val=data_entry/50
                data_entry=0
            #print(data_entry)
        except ValueError:
            continue
    #print(DENSITY)
    file.close()
    file=open("den_value.txt","w+")
    file.write(str((data_entry)+1))
    file.close()
    return den_val
DENSITY=den_define()
def graph_check():
    if DENSITY==20/50:
        return True
    return False
GRAPH_READY=graph_check()
INFINITY=200000
import parameters as param
#

SLEEP_TIME=0.01
#

RWITDH = int ( (CWIDTH/4)  /   (len(param.tmaze)/2) + 0.5 )  # ROAD WIDTH
RLENGTH = int( (CWIDTH-(((len(param.tmaze)/2)+0.5)*RWITDH)) / ((len(param.tmaze)/2)-0.5) ) # ROAD LENGTH
SHAPE_SIZE = RWITDH

MULTIPLIER = (RLENGTH+RWITDH)/2
#
TMAZE_COLS = len(param.tmaze) # number of columns
TMAZE_ROWS = len(param.tmaze[0]) # number of rows
#

NUM_OF_WHEELS = 20
NUM_OF_DRONES = 20
NUM_OF_PODS = 20
#


PIXEL_CHARGE = 20
DRONE_COST=250
WHEEL_COST=5
#
HUB = [0, 0]
