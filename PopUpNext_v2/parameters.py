import a_star
import generate_citymap
import constants as const
# City Map
maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0],
        [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]]
tmaze = a_star.flip_matrix(maze) # Flipped City Map

eq_len = 25
len_x = eq_len # maze length x
len_y = eq_len # maze length y
size = (len_x, len_y)

tmaze = generate_citymap.generate_city(size, (const.DENSITY))
