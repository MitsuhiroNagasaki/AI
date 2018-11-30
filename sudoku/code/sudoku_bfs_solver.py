import time
import copy
from sudoku_problem import Problem
from queue import Queue


class BFSProblem(Problem):
    def actions(self, state):
        # Defines set of valid numbers that can be placed on board
        number_set = range(1, self.type + 1)
        used_in_column = []  # List of valid values in spot's column
        used_in_block = []  # List of valid values in spot's quadrant

        # Get first empty spot on board
        row, column = self.get_spot(self.type, state)

        # Filter valid values based on row
        used_in_row = [number for number in state[row] if (number != 0)]
        options = self.filter_values(number_set, used_in_row)

        # Filter valid values based on column
        for column_index in range(self.type):
            if state[column_index][column] != 0:
                used_in_column.append(state[column_index][column])
        options = self.filter_values(options, used_in_column)

        # Filter with valid values based on quadrant
        row_start = int(row / self.height) * self.height
        column_start = int(column / 3) * 3

        for block_row in range(0, self.height):
            for block_column in range(0, 3):
                used_in_block.append(
                    state[row_start + block_row][column_start + block_column])
        options = self.filter_values(options, used_in_block)

        for number in options:
            yield number, row, column

    # Returns updated board after adding new valid value
    def result(self, state, action):

        play = action[0]
        row = action[1]
        column = action[2]

        # Add new valid value to board
        new_state = copy.deepcopy(state)
        new_state[row][column] = play

        return new_state


class Node:
    def __init__(self, state, action=None):
        self.state = state
        self.action = action

    # Use each action to create a new board state
    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    # Return node with new board state
    def child_node(self, problem, action):
        next = problem.result(self.state, action)
        return Node(next, action)


def BFS(problem):
    # Create initial node of problem tree holding original board
    node = Node(problem.initial)
    # Check if original board is correct and immediately return if valid
    if problem.goal_test(node.state):
        return node

    frontier = Queue()
    frontier.put(node)

    visited_node_num = 0
    while (frontier.qsize() != 0):
        node = frontier.get()
        for child in node.expand(problem):
            visited_node_num += 1
            if problem.goal_test(child.state):
                print ("Found solution")
                print("The number of visited nodes : " + str(visited_node_num))

                return child
            frontier.put(child)
    return None


def solve_bfs(board):
    print ("\nSolving with BFS...")
    start_time = time.time()

    problem = BFSProblem(board)
    solution = BFS(problem)
    elapsed_time = time.time() - start_time

    if solution:
        for row in solution.state:
            print (row)
    else:
        print ("No possible solutions")

    print ("Elapsed time: " + str(elapsed_time))
