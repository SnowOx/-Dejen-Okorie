#! python3
# mini_sudoku_creator.py

import random
import pprint

def create_grid(number_of_rows):
    grid_rows = []
    for i in range(number_of_rows):
        blank_row = ['' for j in range(number_of_rows)]
        grid_rows.append(blank_row)
    return grid_rows

number_of_rows = 5

# Todo: Create definition to define seed starting number positions




def choose_random_number(array):
    number = random.choice(array)
    return number


def get_possible_row_values(row):
    possible_row_values = [i for i in range(number_of_rows)]
    invalid_values = [value for value in possible_row_values if value in row]
    for element in invalid_values:
        possible_row_values.remove(element)
    return possible_row_values

# might be much simpler to use two lists of lists to represent the rows and columns

def insert_value_into_blank_cells(grid):
    for row in grid:
        possible_row_values = get_possible_row_values(row) # Todo: edit this to improve readability. It is difficult to read
        for cell in row:
            cell_position = row.index(cell)
            print(f'value position = {cell_position}')
            if cell is not int:
                chosen_number = get_number_that_is_not_in_the_same_column(possible_row_values, cell_position) # This is inelegant. Todo: Tidy.
                row[cell_position] = chosen_number
                possible_row_values.remove(row[cell_position])
                print (f'assigned row value = {row[cell_position]}')
                column_data['cell_position'] = chosen_number
            else:
                print('Value already inserted')


def get_number_that_is_not_in_the_same_column(possible_row_values, cell_position):
    column_elements = []
    print(cell_position)
    for k, v in column_data.items(): # Find a simpler way to do this without randomness and recursion. E.g., build temporay list?
        if k == cell_position:
            column_elements.append(v)
    possible_cell_values = set(column_elements) - set(possible_row_values)
    number = random.choice(possible_cell_values)
    return number




# Must amalagate get column and row check





# Engine

grid = create_grid(number_of_rows)
pprint.pprint(grid)
column_data = {9: 9} # column number[value]
insert_value_into_blank_cells(grid)
pprint.pprint(grid)


