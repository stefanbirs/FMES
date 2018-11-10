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



################################################################################
# Generates City Maps Component ################################################
################################################################################
citymap.create_houses(param.tmaze) # Generates Houses
citymap.create_traffic(param.tmaze) # Generates Traffic
citymap.create_destination(dest_list) # Generates Destination blocks



################################################################################
# Creating  Drive, Pod and Fly Modules #########################################
################################################################################
# Drive module
wheels = []
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



################################################################################
# Main Loop ####################################################################
################################################################################
while True:
    for i, wheel in enumerate(wheels):
        wheel.move(path_list[i], dest_list[i])

    for i, pod in enumerate(pods):
        pod.move(path_list[i], dest_list[i])

    for i, drone in enumerate(drones):
        drone.fly(dest_list[i])

    citymap.tk.update()
    time.sleep(0.01)



################################################################################
# END ##########################################################################
################################################################################
citymap.tk.mainloop()
