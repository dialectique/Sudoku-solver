"""
sudoku solver api with fastAPI and Uvicorn
"""
import json
import ast
from fastapi import FastAPI

from sudokupackage.sudoku import Sudoku


app = FastAPI()

#define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}


# define a "/solve" endpoint
@app.get("/solve_sudoku")
def solve_sudoku(sudoku_grid):
    """
    finds a solution to the sudoku grid, if one exists
    """
    # convert string represention of a list to a list
    grid_list_format = ast.literal_eval(sudoku_grid)

    # instantiate sudoku class
    s = Sudoku(grid_list_format)

    # compute and return the solution of sudoku_grid
    solution = s.solve()
    return {"solution": solution}
