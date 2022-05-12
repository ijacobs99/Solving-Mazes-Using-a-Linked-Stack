from turtle import position
from linked_stack import Linked_Stack
from app import App
import numpy as np
import time
import csv


def load_maze(filename):
    """
    A function that reads a text maze from a file into a numpy array.
    :param filename: the maze file to be read
    :return: numpy array containing the maze
    """
    data = []
    for r in csv.reader(open(filename, 'r')):
        data.append(list(r[0]))
    return np.array(data)

def is_location_valid(position, rows, columns):
    """
    This function determines whether the location is valid (i.e., not a wall)
    :param columns: the number of columns in the maze
    :param rows: the number of rows in the maze
    :param position: the position being looked at, a tuple (column and row)
    :return: True, if valid; False, otherwise
    """
    ################### YOUR CODE GOES HERE ######################

    return position[0] < rows and position[1] < columns and position[0] >= 0 and position[1] >= 0 

def get_next_neighbour(current_position):
    """
    This function determines the four potential neighbours of any position in the maze (up, right, down, left).
    Neighbours are always checked in a clockwise direction starting with up. Positions that aren't valid should
    not be returned.

    :param current_position: the current position, a tuple (column and row)
    :return: the position if valid; None if not valid
    """
    ################### YOUR CODE GOES HERE ######################

    neighbour_up = (current_position[0] -1, current_position[1]) ## check the up position 
    if can_move(neighbour_up):
        return neighbour_up

    neighbour_right = (current_position[0], current_position[1] + 1) ## check the right position 
    if can_move(neighbour_right):
        return neighbour_right
    
    neighbour_down = (current_position[0] + 1, current_position[1]) ## check the down postion 
    if can_move(neighbour_down):
        return neighbour_down
   
    neighbour_left = (current_position[0], current_position[1] - 1) ## check the left position 
    if can_move(neighbour_left):
        return neighbour_left

    return None


def can_move(new_position):

    """
    This function determines if the new_position (i.e. next neighbour) is a valid move position 
    :param new_position: the position being looked at, a tuple (row and column)
    :return: True, if valid; False, otherwise
    """

    if is_location_valid(new_position, height, width):
        x = new_position[0]
        y = new_position [1]
        cell_value = my_maze[x][y] 
        return cell_value == ' ' or cell_value == "E" and cell_value != 'x'

################ ALGORITHM BEGINS HERE #####################
maze_to_run = input("Which maze would you like to run?\n")
my_maze = load_maze(maze_to_run)
height, width = my_maze.shape  # stores the number of rows (height) and columns (width) in the maze
app = App(my_maze)

############### YOUR ALGORITHM CODE GOES BELOW ###############

def get_start(my_maze, height, width):

    """
    This function determines the start ('S') position in the maze 
    :param my_maze: the maze that we are running 
    :param height: the number of rows in the maze
    :param width: the number of columns in the maze
    :return: start position 'S', a tuple (row and column)
    """

    for row in range(height):
        for col in range(width):
            if my_maze[row][col] == 'S':
                return (row, col)

# defining function positon_status to update the character code, updates positon 'E' to 'f', loop breaks when position is 'f' 
def position_status(current_position, character_code):

    """
    This function changes the position/character code in the maze 
    :param currentPosition: a tuple (row and column) of the position we are looking at 
    :param characterCode: position status (string)
    :return: updated characterCode at the currentPosition
    """

    x = current_position[0]
    y = current_position [1]

    if my_maze[x][y] == 'f':
        return

    elif my_maze[x][y] == 'E':
        my_maze[x][y] = 'f'

    else:
        my_maze[x][y] = character_code


# create a linked stack and push the start position onto the stack 
my_stack = Linked_Stack()
my_stack.push(get_start(my_maze, height, width))

# assigning varibales to count steps taken
total_steps = 0
steps_in_path = 0
reverse_steps = 0 

while not my_stack.is_empty(): 

    current_position = my_stack.peek() 

    if current_position == None: #if get next neighbour results in None 
        my_stack.pop()
        current_position = my_stack.peek()
        position_status(current_position, 'x') #change position status to "Ex path" ['x']
        my_stack.pop()
        current_position = my_stack.peek()
        reverse_steps += 1 #count the number of reverse steps (backtracks)
        total_steps -= 1 #subtrack backtrack from total number of steps 

    position_status(current_position, 'c') #change position status to "current path" ['c']
    app.on_render()

    x = current_position[0]
    y = current_position [1]
    cell_value = my_maze[x][y] 

    if cell_value == 'f': #if the character code in the cell_value of the current position is ['f'] (i.e "found"), break statement will run 
        total_steps += 1 #increment steps taken 
        steps_in_path = total_steps - reverse_steps #subtracks total_steps and reverse_steps, result is the number of steps_in_path 
        break

    if current_position != None:
        my_stack.push(get_next_neighbour(current_position)) #get next neighbour and push the position onto the stack 
        position_status(current_position, 'p') #change position status to "current position" ['p']
        total_steps += 1 #update steps in path         
        
    time.sleep(0.1)

print("Total Steps:" ,total_steps)
print("Steps In Path:" ,steps_in_path)