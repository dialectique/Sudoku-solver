import csv
import sys

from sudokupackage.util import Node, StackFrontier, QueueFrontier


class Sudoku():
    """
    A class to represent a sudoku grid and solve it
    """

    DIGITS_SET = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    def __init__(self, sudoku_grid: list = []) -> str:
        """
        convert a sudoku grid into a string
        For example:
        [[1, 2, 3],
         [3, 4, 5],   --->   "123456789"
         [6, 7, 8]]
        :param sudoku_grid: nested list of integers, size 9*9,
        0 <= integer <= 9 and 0 for empty cell.
        :type sudoku_grid: list
        :raise ValueError: if sudoku_grid is not a nested list of integers,
        size 10*10, 0 <= integer <= 9 and 0 for empty cell.
        :return: a string of integers, length = 81
        :rtype: str
        """

        # if the grid doesn't have 9 rows
        # or if each row doesn't have 9 columns
        # or it each cell is not a integer
        # or if each integer is not in range [1,9]
        # raise ValueError
        if not(len(sudoku_grid) == 9 and \
            all([len(row) == 9 for row in sudoku_grid]) and \
            all([isinstance(x, int) for x in sum(sudoku_grid, [])]) and \
            all([0 <= x <= 9 for x in sum(sudoku_grid, [])])):
            raise ValueError("sudoku grid must be a nested list, size 9*9, \
                0 <= integer <= 9 and 0 for empty cell.")

        # assign the converted grid into a string to this class attribute grid
        self.grid = "".join(list(map(str, sum(sudoku_grid, []))))


    def grid_from_string_to_list(self, grid):
        """
        convert a grid string into a nested list, size 9*9
        """
        return [[int(grid[j * 9 + i]) for i in range(9)] for j in range(9)]



    def is_solved(self, grid: str) -> bool:
        """
        check if the sudoku grid is solved:
        each column, each row, and each of the nine 3x3 subgrids
        that compose the grid must contain all of the digits from 1 to 9
        :param grid: sudoku grid converted into a string
        :type: str
        :return: True if the grid is solved, if not return False
        :rtype: bool
        """

        # list of the columns
        columns = [[grid[i+j] for i in range(0, 73, 9)] for j in range(9)]

        # list of the rows
        rows = [[grid[i+j] for i in range(9)] for j in range(0, 73, 9)]

        # list of the subgrids
        subgrids = [[grid[i+j+k] for i in range(3) for j in [0, 9, 18]]
                    for k in [0, 3, 6, 27, 30, 33, 54, 57, 60]]

        # check if each column, each row, and each subgrid contains
        # all of the digits from 1 to 9
        return all([
            all([set(col) == Sudoku.DIGITS_SET for col in columns]),
            all([set(row) == Sudoku.DIGITS_SET for row in rows]),
            all([set(sub) == Sudoku.DIGITS_SET for sub in subgrids])
        ])


    def neighbors(self, state: tuple) -> list:
        """
        compute the neigbor grids,
        ie compute the grid for each possible value at position
        :param state: grid (string) and position (int)
        :type: tuple
        :return: a list of string where each string is a neighbor
        :rtype: list
        """
        grid, position = state

        # increment position while the cell is not empty (ie != 0)
        while grid[position] != "0":
            position +=1

        # compute possible values in the row at position
        row = set(grid[(position // 9) * 9 + i] for i in range(9))
        possible_values_in_row = Sudoku.DIGITS_SET - row

        # compute possible values in the column at position
        column = set(grid[(position % 9) + i] for i in range(0, 73, 9))
        possible_values_in_column = Sudoku.DIGITS_SET - column

        # compute possible values in the subgrid at position
        subgrid = set(grid[(position // 27) * 27 + \
            ((position % 9) // 3) * 3 + i + j] \
            for i in range(3) for j in [0, 9, 18])
        possible_values_in_subgrid = Sudoku.DIGITS_SET - subgrid

        # compute possible values at position
        possible_values = possible_values_in_row & \
            possible_values_in_column & \
            possible_values_in_subgrid

        # compute the grid for each possible value
        # and return a list of the neighbors states, ie (grid, position)
        grid_list = []
        for val in possible_values:
            # when position is 80, nothing to add after the possible value
            if position == 80:
                grid_list.append((
                grid[:position] + val,
                position
                ))
            else:
                grid_list.append((
                grid[:position] + val + grid[position+1:],
                position
                ))

        return grid_list



    def solve(self):
        """
        finds a solution to the sudoku grid, if one exists,
        using deep-first search
        If several solutions exist, return the first finded
        :return: nested list of integers, size 9*9,
        1 <= integer <= 9, no 0 beacause no empty cell
        if nosolution, return an empty list []
        :rtype: list
        """

        # Keep track of number of states explored
        self.num_explored = 0

        # Initial state is the initial grid and position 0
        # position will iterates from 0 to 80 as the grid
        # have been convert into a string in __init__ method
        self.initialisation = (self.grid, 0)

        # Initialize frontier to just the starting position
        start = Node(state=self.initialisation, parent=None)
        frontier = StackFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping untill solution found
        while True:

            # If nothing left in frontier, then no solution
            if frontier.empty():
                return []

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # if node is a solved sudoku grid, then return the solution
            if self.is_solved(node.state[0]):
                return self.grid_from_string_to_list(node.state[0])

            # mark node as explored:
            self.explored.add(node.state)

            # Add neighbors to frontier
            for neighbor_state in self.neighbors(node.state):
                if not frontier.contains_state(neighbor_state) and \
                    neighbor_state not in self.explored:
                    child = Node(state=neighbor_state, parent=node)
                    frontier.add(child)


    def ping(self):
        """
        You call ping I return pong.
        """
        return "PONG"


def main():
    print("The library essai.py has been ran directly.")


if __name__ == "__main__":
    main()
