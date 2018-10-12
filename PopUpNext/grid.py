from tkinter import *
import random
import time

WIDTH = 500
HEIGHT = 400

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing") # Title of window
canvas.pack() # Done with the settings and show window on screen

canvas.mainloop()
