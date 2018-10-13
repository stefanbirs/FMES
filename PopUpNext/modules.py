from tkinter import * # Imports Graphics Tools
import random # Importing random features

#########################################################
# Constants
WIDTH = 500
HEIGHT = 400
#########################################################
# Steps to create canvas (graphical window)
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("City Map") # Title of window
canvas.pack() # creates window
#########################################################
# Classes
class AirMod:
    """Air Module (quadrotor): for now it initiats as a small red circle
    with a random speed. Has a Method called move that moves around the
    graphical window.

    Methods to add:
    - Pod check: has or has not Pod
    - Pick up Pod when requested
    - Go back to charging dock when not carrying a Pod
    - Can fly over building blocks
    - Flying/battery range (Distance/charge)
    ...
    """
    def __init__(self):
        self.shape = canvas.create_oval(10, 10, 15, 15, fill="red")
        self.xspeed = random.randrange(-10,10)
        self.yspeed = random.randrange(-10,10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

class PodMod:
    """Pod Module: for now it initiats as a medium blue circle
    with a random speed. Has a Method called move that moves around the
    graphical window.

    Methods to add:
    - User check: has or has not users in pod
    - Flying check: is flying or not flying
    - Driving check: is driving or not Driving
    - Request air module or driving module or none
    - Destination check: is or is not at destination
    ...
    """

    def __init__(self):
        self.shape = canvas.create_oval(10, 10, 20, 20, fill="blue")
        self.xspeed = random.randrange(-10,10)
        self.yspeed = random.randrange(-10,10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

class GrdMod:
    """Ground module (wheel base): for now it initiats as a big black circle
    with a random speed. Has a Method called move that moves around the
    graphical window.

    Methods to add:
    - Pod check: has or has not Pod
    - Pick up Pod when requested
    - Go back to charging dock when not carrying a Pod and low in battery
    - Can only drive around building blocks
    - Battery check: is or is not low in battery
    - Driving/battery range (Distance/charge)
    ...
    """
    def __init__(self):
        self.shape = canvas.create_oval(10, 10, 25, 25, fill="black")
        self.xspeed = random.randrange(-10,10)
        self.yspeed = random.randrange(-10,10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed
