from a_star import *
from window import *

wheels = Wheels("green",20)

while True:
    wheels.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
