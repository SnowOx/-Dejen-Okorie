#! python3
# mini_sudoku_creator.py

import random
import pprint
import logging
logging.basicConfig(level=logging.DEBUG)

GRID_SIDE_LENGTH = 3

def create_grid():
    grid_rows = []
    for i in range(GRID_SIDE_LENGTH):
        blank_row = ['x' for j in range(GRID_SIDE_LENGTH)]
        grid_rows.append(blank_row)
    return grid_rows


def get_cell_value_that_fits(row_values, column_values):
    for row, column in zip(row_values, column_values):
        logging.info(f'row = {row} column = {column}')
        possible_cell_values = get_possible_cells()
        if row in possible_cell_values:
            possible_cell_values.remove(row)
        if column in possible_cell_values:
            possible_cell_values.remove(column)
        value = choose_random_number(possible_cell_values)
        #print(f'randomly chosen number = {value}')
        return value


def get_possible_cells():
    cells = [i for i in range(GRID_SIDE_LENGTH)]
    logging.info(f'possible_cells = {cells}')
    return cells


def choose_random_number(array):
    number = random.choice(array)
    return number


def get_row_values(grid):
    rows = []
    for row in grid:
        #print(f'row = {row}')
        row_values = []
        for cell in row:
            row_values.append(cell)
    return rows


def get_column_values(grid):
    columns = []
    for i in range(len(grid)):
        column_values = []
        for j in range(len(grid)):
            cell = grid[j][i]
            print(f'59 cell = {cell}')
            column_values.append(cell)
        columns.append(column_values)
    #print(f'columns = {columns}')
    return columns


def insert_numbers_into_grid(grid):
    for row in grid:
        print(f'67 row = {row}')
        for cell in row:
            print(f'69 cell = {cell}')
            row_values = get_row_values(grid)
            logging.info(f'row values = {row_values}')
            column_values = get_column_values(grid)
            logging.info(f'column_values = {column_values}')
            cell_value = get_cell_value_that_fits(row_values, column_values)
            logging.info(f'cell_value = {cell_value}')
            cell_position = row.index(cell)
            row[cell_position] = cell_value


def engine():
    grid = create_grid()
    logging.info(f' grid = {grid}')
    insert_numbers_into_grid(grid)
    print(f' end grid = {grid}')


engine()
