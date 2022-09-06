# sudoku solver app

- Solve sudoku puzzles, using deep first search algorithm.
https://en.wikipedia.org/wiki/Sudoku
https://en.wikipedia.org/wiki/Depth-first_search

- This app is an API built with fastAPI

- This app is deployed with Docker on Heroku

- API URL : https://sudokuapi9999.herokuapp.com/

## usage :
- sudoku_grid must be a nested list (9 * 9)
- the api returns the solved grid as nested list (9 * 9)
- see example below
```
import json
import requests
url = "https://sudokuapi9999.herokuapp.com/solve_sudoku"
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
params = {"sudoku_grid": json.dumps(sudoku_grid)}
response = requests.get(url, params=params)
solved_grid = response.json().get('solution')
```
- value of the solved_grid variable:
```
[
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
```

## Install package
```
pip install -e sudokuapp
```

## tests
- tests are done on localhost and on the Heroku deployed app

- first, run the server on localhost:
```
make run_api
```

- then run the tests with:
```
make tests
```

## Check out Makefile for other usefull command lines
