import parameters as param
# Canvas
CWIDTH = 700 # CANVAS WIDTH
CHEIGHT = 700 # CANVAS LENGTH
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

NUM_OF_WHEELS = 50
NUM_OF_DRONES = 50
NUM_OF_PODS = 50

#
PIXEL_CHARGE = 20
DRONE_COST=20
WHEEL_COST=5
#
HUB = [0, 0]
