"""
test sudoku.py from sudokupackage
"""

from sudokupackage.sudoku import Sudoku, main

s = Sudoku()

def test_ping():
    assert s.ping() == "PONG"

def test_main():
    assert main() == None
