from sudoku_bfs_solver import solve_bfs
from sudoku_dfs_solver import solve_dfs
from sudoku_astar_solver import solve_aster
from sudoku_my_solver import solve_mine

def solve_sudoku(board):
    print ("Testing on {0}x{0} board...".format(len(board)))
    print ("Problem:")
    for row in board:
        print (row)
    # solve_bfs(board)
    # solve_dfs(board)
    solve_aster(board)
    solve_mine(board)

def main():
    boards = []
    
    board_1 = [[1, 5, 0, 0, 4, 0],
             [2, 4, 0, 0, 5, 6],
             [4, 0, 0, 0, 0, 3],
             [0, 0, 0, 0, 0, 4],
             [6, 3, 0, 0, 2, 0],
             [0, 2, 0, 0, 3, 1]]
    boards.append(board_1)
    
    board_2 = [[0, 0, 0, 0, 4, 0],
             [5, 6, 0, 0, 0, 0],
             [3, 0, 2, 6, 5, 4],
             [0, 4, 0, 2, 0, 3],
             [4, 0, 0, 0, 6, 5],
             [1, 5, 6, 0, 0, 0]]
    boards.append(board_2)
    
    board_3 = [[0, 0, 9, 0, 7, 0, 0, 0, 5],
             [0, 0, 2, 1, 0, 0, 9, 0, 0],
             [1, 0, 0, 0, 2, 8, 0, 0, 0],
             [0, 7, 0, 0, 0, 5, 0, 0, 1],
             [0, 0, 8, 5, 1, 0, 0, 0, 0],
             [0, 5, 0, 0, 0, 0, 3, 0, 0],
             [0, 0, 0, 0, 0, 3, 0, 0, 6],
             [8, 0, 0, 0, 0, 0, 0, 0, 0],
             [2, 1, 0, 0, 0, 0, 0, 8, 7]]
    boards.append(board_3)
    
    board_4 = [[0, 0, 0, 8, 4, 0, 6, 5, 0], 
             [0, 8, 0, 0, 0, 0, 0, 0, 9], 
             [0, 0, 0, 0, 0, 5, 2, 0, 1], 
             [0, 3, 4, 0, 7, 0, 5, 0, 6], 
             [0, 6, 0, 2, 5, 1, 0, 3, 0], 
             [5, 0, 9, 0, 6, 0, 7, 2, 0], 
             [1, 0, 8, 5, 0, 0, 0, 0, 0], 
             [6, 0, 0, 0, 0, 0, 0, 4, 0], 
             [0, 5, 2, 0, 8, 6, 0, 0, 0]] 
    boards.append(board_4)
    
    board_5 = [[9, 7, 4, 2, 3, 6, 1, 5, 8],
             [6, 3, 8, 5, 9, 1, 7, 4, 2],
             [1, 2, 5, 4, 8, 7, 9, 3, 6],
             [3, 1, 6, 7, 5, 4, 2, 8, 9],
             [7, 4, 2, 9, 1, 8, 5, 6, 3],
             [5, 8, 9, 3, 6, 2, 4, 1, 7],
             [8, 6, 7, 1, 2, 5, 3, 9, 4],
             [2, 5, 3, 6, 4, 9, 8, 7, 1],
             [4, 9, 1, 8, 7, 3, 6, 2, 5]]
    boards.append(board_5)

    board_6 = [[3, 0, 5, 4, 2, 0, 8, 1, 0],
             [4, 8, 7, 9, 0, 1, 5, 0, 6],
             [0, 2, 9, 0, 5, 6, 3, 7, 4],
             [8, 5, 0, 7, 9, 3, 0, 4, 1],
             [6, 1, 3, 2, 0, 8, 9, 5, 7],
             [0, 7, 4, 0, 6, 5, 2, 8, 0],
             [2, 4, 1, 3, 0, 9, 0, 6, 5],
             [5, 0, 8, 6, 7, 0, 1, 9, 2],
             [0, 9, 6, 5, 1, 2, 4, 0, 8]]
    boards.append(board_6)

    board_7 = [[0, 0, 2, 0, 3, 0, 0, 0, 8],
             [0, 0, 0, 0, 0, 8, 0, 0, 0],
             [0, 3, 1, 0, 2, 0, 0, 0, 0],
             [0, 6, 0, 0, 5, 0, 2, 7, 0],
             [0, 1, 0, 0, 0, 0, 0, 5, 0],
             [2, 0, 4, 0, 6, 0, 0, 3, 1],
             [0, 0, 0, 0, 8, 0, 6, 0, 5],
             [0, 0, 0, 0, 0, 0, 0, 1, 3],
             [0, 0, 5, 3, 1, 0, 4, 0, 0]]
    boards.append(board_7)
    
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 8, 0],
        [6, 4, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 1, 8, 0, 5, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 4, 0, 2],
        [0, 0, 0, 0, 0, 9, 3, 5, 0],
        [7, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0]
        ]        

    board_ = [[0, 9, 0, 3, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 8, 0, 0, 4, 6],
             [0, 0, 0, 0, 0, 0, 8, 0, 0],
             [4, 0, 5, 0, 6, 0, 0, 3, 0],
             [0, 0, 3, 2, 7, 5, 6, 0, 0],
             [0, 6, 0, 0, 1, 0, 9, 0, 4],
             [0, 0, 1, 0, 0, 0, 0, 0, 0],
             [5, 8, 0, 0, 2, 0, 0, 0, 0],
             [2, 0, 0, 0, 0, 7, 0, 6, 0]]
    boards.append(board_)
    
    board_a = [[0, 3, 9, 0, 0, 0, 1, 2, 0],
             [0, 0, 0, 9, 0, 7, 0, 0, 0],
             [8, 0, 0, 4, 0, 1, 0, 0, 6],
             [0, 4, 2, 0, 0, 0, 7, 9, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 9, 1, 0, 0, 0, 5, 4, 0],
             [5, 0, 0, 1, 0, 9, 0, 0, 3],
             [0, 0, 0, 8, 0, 5, 0, 0, 0],
             [0, 1, 4, 0, 0, 0, 8, 7, 0]]
    boards.append(board_a)

    board_b = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 3, 0, 0],
        [0, 7, 4, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [8, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 1, 7],
        [3, 0, 6, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 4, 0]
        ]
    boards.append(board_b)

    board_c = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 3, 9, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [5, 8, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 3, 1, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 6, 0, 0, 0, 0, 5],
        [0, 0, 3, 0, 2, 0, 7, 0, 0]
        ]
    boards.append(board_c)
     
    board_d = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 9, 0],
        [0, 0, 3, 1, 0, 0, 7, 0, 0],
        [9, 2, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [0, 5, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 3, 0, 1, 0, 0, 0],
        [2, 8, 0, 0, 0, 0, 0, 5, 0]
        ]
    boards.append(board_d)

    question_index = 1
    for board in boards:
        print("Solving Question {0}...".format(question_index))
        solve_sudoku(board)
        print("")
        question_index +=1

if __name__ == "__main__":
    main()