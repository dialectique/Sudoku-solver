"""
test project-sudoku api deployed on Heroku
"""
import json
import requests


sudoku_grid = [
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

solved_grid = [
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

URL = "https://sudokuapi9999.herokuapp.com/"

def test_get_on_heroku():
    response = requests.get(URL)
    assert response.status_code == 200

def test_solve_sudoku_on_heroku():
    params = {"sudoku_grid": json.dumps(sudoku_grid)}
    url = URL + "solve_sudoku"
    response = requests.get(url, params=params)
    assert response.json().get('solution') == solved_grid
