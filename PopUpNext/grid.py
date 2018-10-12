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
