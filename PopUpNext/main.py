""" Files """
from a_star import *
from window import *

""" Wheels varible """
wheels = Wheels("green",20)

""" The game loop """
while True:
    wheels.move()

    tk.update()
    time.sleep(0.01)

tk.mainloop()
