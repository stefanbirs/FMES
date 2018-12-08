import numpy as np
import random as rand

def generate_city(size, traffic_desity):
    '''Generates matrix with 0's(free road), 1's(traffic) and 2's(buildings)'''
    # generates matrix with 0's and 1's with given size and traffic desity
    matrix = np.random.choice([0, 1], size=size, p=[ (1 - traffic_desity) , traffic_desity] )

    # places 2's in matrix
    for row in range(size[0]): # rows
        for col in range(size[1]): # columns
            if(matrix[row][col]==1):
                matrix[row][col]=np.random.choice([1,2,3], size=1, p=[1/3, 1/3, 1/3])
            if row != 0 and row != size[0]-1 and col != 0 and col != size[1]-1 : # ignores borders
<<<<<<< HEAD
                if row %2 != 0 and col %2 != 0: # if true then and 4 to odd numbered indexes
                    matrix[row][col] = 4
                elif row%2==0 and col%2==0:
                    matrix[row][col] = 0
    #print(matrix)
=======
                if row %2 != 0 and col %2 != 0: # if true then and 2 to odd numbered indexes
                    matrix[row][col] = 2
>>>>>>> parent of cfd744e... rise and fall implemented
    return matrix
