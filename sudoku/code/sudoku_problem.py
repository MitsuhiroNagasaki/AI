import copy
import time

class Problem(object):

    def __init__(self, initial):
        self.initial = initial
        self.type = len(initial) # Defines board type, either 6x6 or 9x9
        self.height = int(self.type/3) # Defines height of quadrant (2 for 6x6, 3 for 9x9)

    def goal_test(self, state):
        # Expected sum of each row, column or quadrant.
        total = sum(range(1, self.type+1))

        # Check rows and columns and return false if total is invalid
        for row in range(self.type):
            if (len(state[row]) != self.type) or (sum(state[row]) != total):
                return False

            column_total = 0
            for column in range(self.type):
                column_total += state[column][row]

            if (column_total != total):
                return False

        # Check quadrants and return false if total is invalid
        for column in range(0,self.type,3):
            for row in range(0,self.type,self.height):

                block_total = 0
                for block_row in range(0,self.height):
                    for block_column in range(0,3):
                        block_total += state[row + block_row][column + block_column]

                if (block_total != total):
                    return False

        return True

    # Return set of valid numbers from values that do not appear in used
    def filter_values(self, values, used):
        return [number for number in values if number not in used]

    # Return first empty spot on grid (marked with 0)
    def get_spot(self, board, state):
        for row in range(board):
            for column in range(board):
                if state[row][column] == 0:
                    return row, column
