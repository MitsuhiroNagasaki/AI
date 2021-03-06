import time
import copy
from sudoku_problem import Problem

class DFSProblem(Problem):
    # Get the values we can use for tthe row.
    def filter_row(self, state, row):
    	nums = range(1, self.type + 1)
    	used_in_row = [number for number in state[row] if number!=0]
    	return self.filter_values(nums, used_in_row)

    # Get the values we can use for the column.
    def filter_column(self, options, state, column):
    	used_in_column = []
    	for row in range(self.type):
    		if state[row][column] != 0:
    			used_in_column.append(state[row][column])
    	return self.filter_values(options, used_in_column)

    # Filter valid values based on quadrant
    def filter_quad(self, options, state, row, column):
        used_in_block = []
        row_start = int(row/self.height)*self.height
        column_start = int(column/3)*3

        for block_row in range(0, self.height):
            for block_column in range(0,3):
                used_in_block.append(state[row_start + block_row][column_start + block_column])

        return self.filter_values(options, used_in_block)


    def actions(self, state):
        row,column = self.get_spot(self.type, state) # Get first empty spot on board

        # Remove spot's invalid options
        options = self.filter_row(state, row)
        options = self.filter_column(options, state, column)
        options = self.filter_quad(options, state, row, column)

        # Yield a state for each valid option
        for number in options:
            new_state = copy.deepcopy(state)
            new_state[row][column] = number
            yield new_state

class Node:
	def __init__(self, state):
		self.state = state

	def expand(self, problem):
		# Get the valid states after one action.
		return [Node(state) for state in problem.actions(self.state)]


def DFS(problem):
	initial_node = Node(problem.initial)
	if problem.goal_test(initial_node.state):
		return initial_node.state

	stack = []
	stack.append(initial_node)

	visited_node_num = 0
	while stack:
		node = stack.pop()
		visited_node_num+=1
		if problem.goal_test(node.state):
			print ("Found solution")
			print("The number of visited nodes : " + str(visited_node_num))
			return node.state
		stack.extend(node.expand(problem))

	return None

def solve_dfs(board):
    print ("\nSolving with DFS...")
    start_time = time.time()
    problem = DFSProblem(board)
    solution = DFS(problem)
    elapsed_time = time.time() - start_time

    if solution:
        for row in solution:
            print (row)
    else:
        print ("No possible solutions")
