# Animating More Objects
from tkinter import *
import random
import time
from .grid import Square


colors = ["red", "green", "blue", "purple", "orange", "yellow", "cyan",
          "magenta","dodgerblue", "turquoise", "grey", "gold", "pink"]
WIDTH = 500 # canvas width
HEIGHT = 400 # canvas height
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing") # Title of window
canvas.pack() # Done with the settings and show window on screen


# General rule, classes start with capital letter

# Air module (quadrotor)
class AirMod:
    # special function, executed whenever object is created
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

# Pod module (capsule for passangers)
class PodMod:

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

# Ground module (wheel frame)
class GroundMod:

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

quadrotor = AirMod()
pod = PodMod()
base = GroundMod()

while True:
    quadrotor.move()
    pod.move()
    base.move()
    tk.update()
    #time.sleep(0.01)

canvas.mainloop()
