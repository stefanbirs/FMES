# Animating More Objects
from tkinter import *
import random
import time

WIDTH = 500
HEIGHT = 400
colors = ["red", "green", "blue", "purple", "orange", "yellow", "cyan",
          "magenta","dodgerblue", "turquoise", "grey", "gold", "pink"]

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing") # Title of window
canvas.pack() # Done with the settings and show window on screen

class Ball: # General rule, classes start with capital letter
    # special function, executed whenever object is created
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill=color)
        self.xspeed = random.randrange(-10,10)
        self.yspeed = random.randrange(-10,10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

# property of objects in python: objects can be treated like any other variable
balls = []
for i in range(200):
    # adding new balls to end of list
    balls.append(Ball(random.choice(colors), random.randrange(10, 30)))
while True:
    for ball in balls:
        ball.move()
    tk.update()
    #time.sleep(0.01)

canvas.mainloop()
