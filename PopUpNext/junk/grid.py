from tkinter import *
import random
import time

WIDTH = 500
HEIGHT = 400

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing") # Title of window
canvas.pack() # Done with the settings and show window on screen

class Square:
    def __init__(self,size):
        self.shape = canvas.create_square(0, 0, 100, 100 ,fill = 'blue', outline = 'blue')

blocks = []
for i in range(10):
    blocks.append(Square)
    #time.sleep(0.01)
while True:
    tk.update()

canvas.mainloop()
