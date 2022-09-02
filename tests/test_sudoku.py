"""
test sudokui.py from sudokupackage with pytest
"""

import pytest

# from sudokupackage.sudoku import Sudoku, main
from sudokupackage.sudoku import Sudoku, main


# list of invalid sudoku grids
invalid_input = []

# empty list
invalid_input.append([])

# invalid number of rows
invalid_input.append([
    [7,0,0,  1,0,0,  0,0,6],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,8,  1,0,0],

    [0,0,8,  0,0,0,  0,0,0],
    [0,5,0,  8,0,6,  0,0,1],

    [0,0,0,  0,0,0,  0,1,0],
    [0,4,0,  5,0,0,  0,0,0],
    [0,1,5,  0,0,7,  0,0,4]
])

# invalid number of colums
invalid_input.append([
    [7,0,0,  1,0,0,  0,0,6],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,8,  1,0,0],

    [0,8,  0,0,0,  0,0,0],
    [0,5,0,  8,0,6,  0,0,1],
    [1,0,0,  0,2,0,  0,0,0],

    [0,0,0,  0,0,0,  0,1,0],
    [0,4,0,  5,0,0,  0,0,0],
    [0,1,5,  0,0,7,  0,0,4]
])

# invalid type
invalid_input.append([
    [7,0,0,  1,0,0,  0,0,6],
    [0,0,0,  "6",0,0,  0,4,0],
    [0,0,2,  0,0,8,  1,0,0],

    [0,0,8,  0,0,0,  0,0,0],
    [0,5,0,  8,0,6,  0,0,1],
    [1,0,0,  0,2,0,  0,0,0],

    [0,0,0,  0,0,0,  0,1,0],
    [0,4,0,  5,0,0,  0,0,0],
    [0,1,5,  0,0,7,  0,0,4]
])

# invalid range
invalid_input.append([
    [7,0,0,  1,0,0,  0,0,6],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,11,  1,0,0],

    [0,0,8,  0,0,0,  0,0,0],
    [0,5,0,  8,0,6,  0,0,1],
    [1,0,0,  0,2,0,  0,0,0],

    [0,0,0,  0,0,0,  0,1,0],
    [0,4,0,  -5,0,0,  0,0,0],
    [0,1,5,  0,0,7,  0,0,4]
])

# valid sudoku grid
valid_input = [
    [5,3,0,  0,7,0,  0,0,0],
    [6,0,0,  1,9,5,  0,0,0],
    [0,9,8,  0,0,0,  0,6,0],

    [8,0,0,  0,6,0,  0,0,3],
    [4,0,0,  8,0,3,  0,0,1],
    [7,0,0,  0,2,0,  0,0,6],

    [0,6,0,  0,0,0,  2,8,0],
    [0,0,0,  4,1,9,  0,0,5],
    [0,0,0,  0,8,0,  0,7,9]
]

#solved_grid
solved_grid = [
    [5,3,4,  6,7,8,  9,1,2],
    [6,7,2,  1,9,5,  3,4,8],
    [1,9,8,  3,4,2,  5,6,7],

    [8,5,9,  7,6,1,  4,2,3],
    [4,2,6,  8,5,3,  7,9,1],
    [7,1,3,  9,2,4,  8,5,6],

    [9,6,1,  5,3,7,  2,8,4],
    [2,8,7,  4,1,9,  6,3,5],
    [3,4,5,  2,8,6,  1,7,9]
]
# unsolvable_grid
valid_unsolvable_grid = [
    [0,0,0,  4,5,6,  0,0,0],
    [0,0,0,  1,2,3,  0,0,0],
    [0,0,0,  8,9,7,  0,0,0],

    [1,2,3,  0,0,0,  4,5,6],
    [4,5,6,  0,0,0,  7,8,9],
    [7,8,9,  0,0,0,  1,2,3],

    [0,0,0,  7,8,9,  0,0,0],
    [0,0,0,  2,3,1,  0,0,0],
    [0,0,0,  9,8,7,  0,0,0]
]

# valid sudoku grid 2
valid_input2 = [
    [0,0,3,  0,8,4,  0,0,0],
    [0,5,0,  2,0,0,  0,0,9],
    [4,0,0,  0,0,1,  0,6,0],

    [1,0,0,  8,0,0,  7,0,3],
    [0,0,0,  0,0,0,  0,0,0],
    [9,0,2,  0,0,6,  0,0,8],

    [0,4,0,  7,0,0,  0,0,5],
    [2,0,0,  0,0,9,  0,3,0],
    [0,0,0,  1,3,0,  6,0,0]
]

#solved_grid 2
solved_grid2 = [
    [6,2,3,  9,8,4,  5,7,1],
    [7,5,1,  2,6,3,  4,8,9],
    [4,8,9,  5,7,1,  3,6,2],

    [1,6,4,  8,9,2,  7,5,3],
    [5,3,8,  4,1,7,  2,9,6],
    [9,7,2,  3,5,6,  1,4,8],

    [3,4,6,  7,2,8,  9,1,5],
    [2,1,5,  6,4,9,  8,3,7],
    [8,9,7,  1,3,5,  6,2,4]
]



def test_list_to_string_invalid_inputs():
    for grid in invalid_input:
        with pytest.raises(ValueError):
            s = Sudoku(grid)

def test_list_to_string_valid_input():
    s = Sudoku(valid_input)
    assert s.grid == "530070000600195000098000060800060003400" \
        "803001700020006060000280000419005000080079"

def test_is_solved_with_solved_grid():
    s = Sudoku(solved_grid)
    assert s.is_solved(s.grid) == True

def test_is_solved_with_unsolved_grid():
    s = Sudoku(valid_input)
    assert s.is_solved(s.grid) == False

def test_grid_from_string_to_list():
    s = Sudoku(valid_input)
    assert s.grid_from_string_to_list(s.grid) == valid_input

def test_neighbors():
    s = Sudoku(valid_input)
    neighbor_states = s.neighbors((s.grid, 30))
    grids = [n[0] for n in neighbor_states]
    possible_values = [n[30] for n in grids]
    assert set(possible_values) == set(["5", "7", "9"])

def test_solve_solution_exists():
    s = Sudoku(valid_input)
    assert s.solve() == solved_grid

def test_solve_solution_exists2():
    s = Sudoku(valid_input2)
    assert s.solve() == solved_grid2

def test_solve_no_solution():
    s = Sudoku(valid_unsolvable_grid)
    assert s.solve() == []


def test_ping():
    s = Sudoku(valid_input)
    assert s.ping() == "PONG"

def test_main():
    assert main() == None
