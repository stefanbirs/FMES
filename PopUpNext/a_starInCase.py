import numpy

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def AllCombinations(my_list, empty_list):
    """Fills an empty list with all possible combinations from my_list"""
    count = 0
    for i in range(1, len(my_list)+1):
        #Number of combinations for given i
        count += math.factorial(len(my_list))/(math.factorial(i)*math.factorial(len(my_list)-i))
        
    for i in range(1, len(my_list)+1):
        a = itertools.combinations(my_list, i)
        for subset in a:
            empty_list.append(list(subset))

def astar(tmaze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given tmaze"""

    # Create start and end node
    start_node = Node(None, start)
    #start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    #end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):

            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node

            while current is not None:
                path.append(current.position)
                current = current.parent

            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(tmaze) - 1) or node_position[0] < 0 or node_position[1] > (len(tmaze[len(tmaze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if tmaze[node_position[0]][node_position[1]] != 0:
                continue

            if Node(current_node, node_position) in closed_list:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


tmaze=[]
rez = [[maze[j][i] for j in range(len(maze))] for i in range(len(maze[0]))]
for row in rez:
    tmaze.append(row)


start1=(0,13)
end=(6,5)


path = astar(tmaze, start1, end)


count = 0

if path == None:
    
    #Take away traffic blocks
    maze_simple = maze
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze_simple[i][j] == 1:
              maze_simple[i][j] = 0
              #print("Hi")
    
    #Find quickest path if no traffic
    
    tmaze2=[]
    rez2 = [[maze_simple[j][i] for j in range(len(maze_simple))] for i in range(len(maze_simple[0]))]
    for row in rez2:
        tmaze2.append(row)
    path_nt = astar(tmaze2, start1, end)  #path_nt is no traffic path
    
    one_count = 0  #variable indicates indice of traffic
    
    one_indices = [0] #Stores the indicies of traffic
    one_coordinates = [0] #Stores the coordinates of the traffic blocks
    j = 0;
    
    one_count_indices = 0  #used to access one_indices
    
    #Find where traffic is on this path
    
    for i in path_nt:
        if maze[i[0]][i[1]] == 1:  #check correct indexing
            one_indices[j] = one_count
            one_coordinates[j] = i
            j+=1
        one_count += 1
    count = 0
    
"""    
    
    while path_check == None and:
        #Check for rmeoving one traffic piece
        if count <= len(one_coordinates):
            if (one_coordinates[count][0] !=  one_coordinates[count+1][0]) :
                start = (one_coordinates[count][0]+1,one_coordinates[count][1])
            else:
                start = (one_coordinates[count][0],one_coordinates[count][1]+1)
            start_coord[count] = start
            #Check if path is now open
            path_check = astar(tmaze, start, end)
        else:
            
            
        
    path_arr[]
        
    #Now need to check all cooridnates
        
        
    
    while one_count < len(path_nt):
        
    
    
    
    
    
    #need to make a new path after each time you skip a piece of traffic to see if free but need to try 
    #all combinations, you will be shifting the starting point
    
    
    
              

    
    
print(path)

"""
    comb_indices = []
    AllCombinations(one_coordinates, comb_ind)
    count = 0
    test_maze = maze
    
    for i in comb_indices :
        for j in i:
            test_maze[j[0],j[1]] = 0
        
        tmaze=[]
        rez = [[test_maze[j][i] for j in range(len(test_maze))] for i in range(len(test_maze[0]))]
        for row in rez:
            tmaze.append(row)

        path = astar(tmaze, start1, end)
        
        if path != None:
            traff_ind = i
            break
        
        test_maze = maze
        count += 1
        
    sur_ind = np.zeros(len(traff_ind)) #also need to check for lists of lists of lists
    sur_count = 0
    path_count = 0
    
    #finds index of traffic in path list
    for k in traff_ind :  #need to make this work for list lists lists
        for p in path :
            if k == p:
                sur_ind[sur_count] = path_count
                sur_count += 1
            path_count += 1
        path_count = 0
        
    #Unnecessary: clean up by changing var names
    tmaze=[]
    rez = [[maze[j][i] for j in range(len(maze))] for i in range(len(maze[0]))]
    for row in rez:
        tmaze.append(row)
        
        
    path_arr = [astar(tmaze, start1, path[sur_ind[0]-1])]
    
    for i in range(0, len(sur_ind)):
        path_arr.append(astar(tmaze), path[sur_ind[i]+1], path[sur_ind[i+1]-1])
    
    path_arr.append(astar(tmaze, path[sur_ind[-1]+1], end))
        
    
        
    
print(path)
