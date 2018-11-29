# Files
import a_star # contains A* algorithm and some other functions
import citymap # contains functions that create components in citymap and canvas
from modules import DriveMod, PodMod, FlyMod



maze = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

tmaze = a_star.flip_matrix(maze) # Flipped City Map


citymap.create_houses(tmaze) # Generates Houses
citymap.create_traffic(tmaze) # Generates Traffic
citymap.create_destination([(2,10)]) # Generates Destination blocks
citymap.create_hub()


car1 = DriveMod((8,5), (2,10))
car2 = DriveMod((8,7), (2,10))
pod = PodMod((8,5),(2,10))
drone = FlyMod((7,5))

citymap.tk.mainloop()
