import numpy as np
import random as rand

eq_len = 31
len_x = eq_len # maze length x
len_y = eq_len # maze length y
size = (len_x, len_y)

def generate_city(size, traffic_desity):
    '''Generates matrix with 0's(free road), 1's(traffic) and 2's(buildings)'''
    # generates matrix with 0's and 1's with given size and traffic desity
    matrix = np.random.choice([0, 1], size=size, p=[ (1 - traffic_desity) , traffic_desity] )

    # places 2's in matrix
    for row in range(size[0]): # rows
        for col in range(size[1]): # columns
            if row != 0 and row != size[0]-1 and col != 0 and col != size[1]-1 : # ignores borders
                if row %2 != 0 and col %2 != 0: # if true then and 2 to odd numbered indexes
                    matrix[row][col] = 2
    return matrix
