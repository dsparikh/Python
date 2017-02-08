""" 
By: Dhrumilkumar Parikh
Logic for 2048 game
"""

import poc_2048_gui
import random
import math

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result = fix(line)
    for index in range(len(result)):
        if index < len(result)-1:
            if result[index] == result[index+1]:
                result[index]=2*result[index]
                result[index+1]=0
    fixed_result = fix(result)
    return fixed_result

def fix(lis):
    """
    fix the list
    """
    add_zeros = 0
    result = []
    for index in range(len(lis)):
        if lis[index]!=0:
            result.append(lis[index])
        else:
            add_zeros+=1
    for index in range(add_zeros):
        result.append(0)
        index = index
    return result

#######################################################################################

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self.reset()
        
        upp = [(0, col) for col in range(self._width)]
        down = [(self._height-1, col) for col in range(self._width)]
        left = [(row, 0) for row in range(self._height)]
        right = [(row, self._width-1) for row in range(self._height)]
        
        self._move_dictionary = {UP:upp, DOWN:down, LEFT:left, RIGHT:right}
        
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = [[(col+row) - (col+row) for col in range(self._width)] for row in range(self._height)]     
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str([val for val in self._board]).replace("],", "]\n")  

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        moved = False
        
        for val in self._move_dictionary[direction]:
            temp_list = []
            row = val[0]
            col = val[1]
            
            if direction == UP or direction == DOWN:
                counter = self._height
            else:
                counter = self._width
            
            for num in range(counter):
                temp_list.append(self._board[row][col])
                row += OFFSETS[direction][0]
                col += OFFSETS[direction][1]
                num = num
            
            temp_list = merge(temp_list)
            
            row = val[0]
            col = val[1]
            ind = 0
            
            for num in range(counter):
                if self._board[row][col] != temp_list[ind]:
                    moved = True
                    
                self._board[row][col] = temp_list[ind]
                row += OFFSETS[direction][0]
                col += OFFSETS[direction][1]
                ind += 1
            
        if moved:
            self.new_tile()
        
        
        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        random_row = random.randint(0, self._height - 1)
        random_col = random.randint(0,self._width-1)
        random_tile = random.choice([2,2,2,2,2,2,2,2,2,4])
        
        while self.get_tile(random_row, random_col) != 0:
            random_row = random.randint(0, self._height - 1)
            random_col = random.randint(0,self._width-1)
        
        self.set_tile(random_row,random_col,random_tile)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value 

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]

#gui module for 2048 
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
