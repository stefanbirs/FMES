import random
import numpy as np
import math
import itertools
import sys


class block():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None,weight=0):
        self.parent = parent
        self.position = position
        self.weight=weight
        self.g = 0
        self.h = 0
        self.f = 0

    def set_parent(self, block):
        self.parent=block
    def get_parent():
        return self.parent

def generate_city(size, traffic_desity):
    '''Generates matrix with 0's(free road), 1's-3's(traffic) and 4's(buildings)'''
    # generates matrix with 0's and 1's with given size and traffic desity
    matrix = np.random.choice([0,1], size=size, p=[ (1 - traffic_desity) , traffic_desity] )
    # places 2's in matrix
    for row in range(size[0]): # rows
        for col in range(size[1]): # columns
            if(matrix[row][col]==1):
                matrix[row][col]=np.random.choice([1,2,3], size=1, p=[1/3, 1/3, 1/3])
            if row != 0 and row != size[0]-1 and col != 0 and col != size[1]-1 : # ignores borders
                if row %2 != 0 and col %2 != 0: # if true then and 4 to odd numbered indexes
                    matrix[row][col] = 4
                elif row%2==0 and col%2==0:
                    matrix[row][col] = 0
    print(matrix)
    return matrix
def weighted_sum(maze,sum,block,end):
    if block.position==end.position:
        return sum
    else:
        next_step=[]
        x=block.position[0]
        y=block.position[1]
        if (y+1)<=len(maze[0][:])-1:
            #print(maze[x][y+1].weight)
            if maze[x][y+1].weight!=4:
                #maze[x][y+1].parent=block
                next_step.append(maze[x][y+1])
        if (y-1)>=0:
            if maze[x][y-1].weight!=4:
                #maze[x][y-1].parent=block
                next_step.append(maze[x][y-1])
        if (x+1)<=len(maze[:][0])-1:
            if maze[x+1][y].weight!=4:
                #maze[x+1][y].parent=block
                next_step.append(maze[x+1][y])
        if (x-1)>=0:
            if maze[x-1][y].weight!=4:
                #maze[x-1][y].parent=block
                next_step.append(maze[x-1][y])
        sum=[]
        for i in range(0,len(next_step)):
            sum.append(weighted_sum(maze,sum+next_step[i].weight,next_step[i],end))
        return min(sum)
def network_weights(maze, start, end):
    start_block = block(None, start)
    end_block = block(None, end)
    block_maze = [[0 for x in range(0,len(maze[0][:]))] for y in range(0,len(maze[:][0]))]
    for row in range(0,len(maze[0][:])):
        for col in range(0,len(maze[:][0])):
            block_maze[row][col]=block(None,[row,col],maze[row][col])
    for row in range(0,len(maze[0][:])):
        for col in range(0,len(maze[:][0])):
            print(block_maze[row][col].position)
            print(block_maze[row][col].weight)
            print(block_maze[row][col].parent)
    sum=weighted_sum(block_maze,0,start_block,end_block)
    print(sum)

network_weights(generate_city([10,10], 0.3),[5,5],[0,0])
