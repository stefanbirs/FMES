import parameters as param
# Canvas
CWIDTH = 700 # CANVAS WIDTH
CHEIGHT = 700 # CANVAS LENGTH
#
RWITDH = 20 # ROAD WIDTH
RLENGTH = int( (CWIDTH-(((len(param.maze)/2)+0.5)*RWITDH)) / ((len(param.maze)/2)-0.5) ) # ROAD LENGTH
SHAPE_SIZE = RWITDH
#
TMAZE_COLS = len(param.tmaze) # number of columns
TMAZE_ROWS = len(param.tmaze[0]) # number of rows
#

NUM_OF_WHEELS = 100
NUM_OF_DRONES = 0
NUM_OF_PODS = 0

#
PIXEL_CHARGE = 20
#
HUB = [0, 0]
