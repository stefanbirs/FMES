from tkinter import *
import constants as const

################################################################################
# Houses #######################################################################
################################################################################
# Makes houses for every second coordinate in the x and y axis
def create_houses(tmaze):
    box_x = 0
    for i in range(int((len(tmaze)-1)/2)):
        box_y = 0
        for i in range(int((len(tmaze[0])-1)/2)):
            canvas.create_rectangle(box_x + const.RWITDH,
                                    box_y + const.RWITDH,
                                    box_x + const.RWITDH + const.RLENGTH,
                                    box_y + const.RWITDH + const.RLENGTH )
            box_y = box_y + const.RLENGTH + const.RWITDH
        box_x = box_x + const.RLENGTH + const.RWITDH



################################################################################
# Traffic ######################################################################
################################################################################
# Makes traffic for all the '1's in  tmaze
def create_traffic(tmaze):
    for x in range(len(tmaze)):
        for y in range(len(tmaze[0])):
            if tmaze[x][y] == 1 and not x % 2 == 0: #Makes a rectangle between buildings in the x axis
                col = ((const.RLENGTH+const.RWITDH)*((x/2)-0.5))+const.RWITDH
                row = (const.RLENGTH+const.RWITDH)*(y/2)
                canvas.create_rectangle(col, row, col + const.RLENGTH, row + const.RWITDH, fill="red",tags="traffic")
            if tmaze[x][y] == 1 and not y % 2 == 0: #Makes a rectangle between buildings in the y axis
                row = ((const.RLENGTH+const.RWITDH)*((y/2)-0.5))+const.RWITDH
                col = (const.RLENGTH+const.RWITDH)*(x/2)
                canvas.create_rectangle(col, row, col + const.RWITDH, row + const.RLENGTH, fill="red",tags="traffic")
            if tmaze[x][y] == 1 and x % 2 == 0 and y % 2 == 0: #Makes a squere on crossroads
                row = ((const.RLENGTH+const.RWITDH)*(y/2))
                col = ((const.RLENGTH+const.RWITDH)*(x/2))
                canvas.create_rectangle(col, row, col + const.RWITDH ,row + const.RWITDH, fill="red",tags="traffic")



################################################################################
# Destination ##################################################################
################################################################################
# Creates a square at the destination coordinate
def create_destination(dest_list):
    for i in range (len(dest_list)):
        x1 = int( dest_list[i][0]*((const.RLENGTH+const.RWITDH)/2) )
        y1 = int( dest_list[i][1]*((const.RLENGTH+const.RWITDH)/2) )
        x2 = int( dest_list[i][0]*((const.RLENGTH+const.RWITDH)/2) + const.RWITDH )
        y2 = int( dest_list[i][1]*((const.RLENGTH+const.RWITDH)/2) + const.RWITDH )
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue",tags="dest")
def create_hub():
    x1 = int(const.HUB[0]*((const.RLENGTH+const.RWITDH)/2) )
    y1 = int(const.HUB[1]*((const.RLENGTH+const.RWITDH)/2) )
    x2 = int(const.HUB[0]*((const.RLENGTH+const.RWITDH)/2) + const.RWITDH )
    y2 = int(const.HUB[1]*((const.RLENGTH+const.RWITDH)/2) + const.RWITDH )
    canvas.create_rectangle(x1, y1, x2, y2, fill="black",tags="hub")


################################################################################
# Creating the canvas ##########################################################
################################################################################
def create_canvas():
    tk=Tk()
    canvas = Canvas(tk, width=const.CWIDTH, height=const.CHEIGHT)
    canvas.pack()
    canvas.configure(highlightthickness=0, borderwidth=0) # removes cut off on top and left edges
    return tk, canvas



################################################################################
# RUNNING CANVAS METHOD ########################################################
################################################################################

tk, canvas = create_canvas()







################################################################################
# END ##########################################################################
################################################################################
