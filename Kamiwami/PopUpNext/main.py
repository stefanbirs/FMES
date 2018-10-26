from a_star import *
from window import *


wheels1 = Wheels("green",20)
wheels2 = Wheels("green",20)
wheels3 = Wheels("green",20)

while True:
    wheels1.move()
    wheels2.move()
    wheels3.move()

    tk.update()
    time.sleep(0.01)

tk.mainloop()
