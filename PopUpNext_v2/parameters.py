import a_star

# City Map
maze = [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0],
        [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 2, 1, 2, 0, 2, 1, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

tmaze = a_star.flip_matrix(maze) # Flipped City Map
