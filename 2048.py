"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

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
    Function that merges a single row or column in 2048.
    """
    # initialise two lists to hold the re-arranged lines
    # and the merged lines
    arranged_line = list()
    merged_line = list()
    
    # iterate through the line and get all non-zero tiles 
    # and put append them in the arrangedLine list
    for tile in line:
        if tile > 0:
            arranged_line.append(tile)
            
    #Merge paired tiles
    #Initialise the tile index
    tile_index = 0
    # loop while tile_index does not exceed the length
    # of the list
    while tile_index < len(arranged_line):
        # if the tile index is at the last element then
        # justa dd it as it is
        if tile_index == len(arranged_line) - 1:
            merged_line.append(arranged_line[tile_index])
            #increment the tile index by 1
            tile_index += 1
        # else if the adjacent tiles are pair then merge
        # and add them
        elif arranged_line[tile_index] == arranged_line[tile_index + 1]:
            merged_line.append(arranged_line[tile_index] * 2)
            #increment the tile index by 2
            tile_index += 2
        # else add the elemenet at the tile index and move on
        # to the next element
        else:
            merged_line.append(arranged_line[tile_index])
            #increment the tile index by 1
            tile_index += 1
        
    #Return the mergedList by adding empty spaces or zeroes
    # First calculate the emptyspaces by subtracting the 
    # length of mergedLine from the length of line and then
    # fill these spaces with zeroes
    empty_spaces = len(line) - len(merged_line)
    
    for empty_space in range(1,empty_spaces + 1):
        empty_space = 0
        merged_line.append(empty_space)
    
    return merged_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # Store the grid_height and grid_width
        # and call the reset function
        self._grid_height = grid_height
        self._grid_width = grid_width
        #Get the initial tile indices for each direction
        # and store them in a dictionary
        initial_indices = {}
        #Initialise 4 lists to hold the initial tile indices
        # for each direction
        direction_up = list()
        direction_down = list()
        direction_left = list()
        direction_right = list()
        # loop through each row and col to fill in the 
        # initial tile indices
        for row in range(0, grid_height):
            for col in range(0, grid_width):
                if row == 0:
                    direction_up.append((row, col))
                elif row == grid_height - 1:
                    direction_down.append((row, col))
                if col == 0:
                    direction_left.append((row, col))
                elif col == grid_width - 1:
                    direction_right.append((row, col))
        # add the tile_indices to the dictionary
        initial_indices[UP] = direction_up
        initial_indices[DOWN] = direction_down
        initial_indices[LEFT] = direction_left
        initial_indices[RIGHT] = direction_right
        # store the initial indices
        self._initial_indices = initial_indices
        TwentyFortyEight.reset(self)

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # Initialise a grid which is a list having no of elements
        # equal to grid_height and each element as a line 
        # or another list having size equal to grid_width
        grid = list()
        for row in range(0, self._grid_height):
            grid.append([])
            line = list()
            for column in range(0, self._grid_width):
                column = 0
                line.append(column)
            grid[row] = line
        #Store the grid
        self._grid = grid

        # call the new_tile method twice to add 2 random tiles
        TwentyFortyEight.new_tile(self)
        TwentyFortyEight.new_tile(self)

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # return grid object after string conversion
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # return the grid height
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # return the grid width
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # Get the initial_indices depending on the direction
        indices = self._initial_indices[direction]
        # get the tile values for either a row or a column
        # depending on the direction and send for merge
        limit = 0
        tile_value_changed = False
        if OFFSETS[direction][0] == 0:
            limit = self._grid_width
        else:
            limit = self._grid_height
            
        for index in indices:
            # get the offset value for the particular direction 
            # and get the tile values
            tile_values = list()
            row = 0
            col = 0
            for element in range(0, limit):
                if element == 0:
                    row = index[0]
                    col = index[1]
                    tile_values.append(TwentyFortyEight.get_tile(self, row, col))
                else:
                    row = row + OFFSETS[direction][0]
                    col = col + OFFSETS[direction][1]
                    tile_values.append(TwentyFortyEight.get_tile(self, row, col))
            # merge the tiles
            merged_tiles = merge(tile_values)
            row = 0
            col = 0
            
            # set the new tile values
            for element in range(0, limit):
                if element == 0:
                    row = index[0]
                    col = index[1]
                    #detect if the tile value has changed
                    if tile_values[element] != merged_tiles[element]:
                        tile_value_changed = True
                    TwentyFortyEight.set_tile(self, row, col, merged_tiles[element]) 
                else:
                    row = row + OFFSETS[direction][0]
                    col = col + OFFSETS[direction][1]
                    #detect if the tile value has changed
                    if tile_values[element] != merged_tiles[element]:
                        tile_value_changed = True
                    TwentyFortyEight.set_tile(self, row, col, merged_tiles[element])
        
        #Add a new tile if tile_value has changed
        if tile_value_changed:
            TwentyFortyEight.new_tile(self)
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # Continue selecting a random tile from the grid
        # until the tile chosen is an empty space
        tile_index = [random.randint(0, self._grid_height - 1), random.randint(0, self._grid_width - 1)]
        while self._grid[tile_index[0]][tile_index[1]] != 0:
            # choose a random row
            tile_index[0] = random.randint(0, self._grid_height - 1)
            # choose a random column
            tile_index[1] = random.randint(0, self._grid_width - 1)
        
        # choose a random value between 2 and 4 with a probability of .9 and .1 respectively
        if random.random() < 0.9:
            self._grid[tile_index[0]][tile_index[1]] = 2
        else:
            self._grid[tile_index[0]][tile_index[1]] = 4

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
