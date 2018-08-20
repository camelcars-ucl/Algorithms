move_x = [2, 1, -1, -2, -2, -1,  1,  2]
move_y = [1, 2,  2,  1, -1, -2, -2, -1]

def print_board(board):
    for i in board:
        print(i)

def move(start_x, start_y, board):
    if check_status(board) == False:
        pass
    else:
        return True
    for i in range(8):
        new_x = start_x + move_x[i]
        new_y = start_y + move_y[i]
        if new_x < 0 or new_x > 7 or new_y < 0 or new_y > 7:    # out of bounds
            continue
        if new_x == 0 and new_y == 0:   # edge case
            continue
        if board[new_y][new_x] == -1:    # not visited
            board[new_y][new_x] = board[start_y][start_x] + 1
            if move(new_x, new_y, board) == True:
                print_board(board)
                return True
            else:
                board[new_y][new_x] = -1
    else:
        return False

def check_status(board):
    for i in range(8):
        if -1 in board[i]:
            return False
    return True

def is_valid(matrix):
    '''
    check if my solution is valid
    '''
    cell = {}
    move_x_y = []
    for i in range(8):
        move_x_y.append([move_x[i], move_y[i]])
    for i in range(8):
        for x in range(8):
            cell[matrix[i][x]] = (i, x)
    for i in range(1, 64):
        move = [cell[i][0] - cell[i-1][0], cell[i][1] - cell[i-1][1]]
        if move in move_x_y:
            pass
        else:
            return False
    return True

def solve():
    '''
    solution to the knight's tour problem using backtracking
    '''
    board = [[-1 for i in range(8)] for i in range(8)]
    board[0][0] = 0     # starting cell
    ans = move(0, 0, board)
    if ans == False:
        print('solution does not exist')
    else:
        print('solution found')

solve()


# ans = [[0, 37, 58, 35, 42, 47, 56, 51],
#         [59, 34, 1, 48, 57, 50, 43, 46],
#         [38, 31, 36, 41, 2, 45, 52, 55],
#         [33, 60, 39, 26, 49, 54, 3, 44],
#         [30, 9, 32, 61, 40, 25, 22, 53],
#         [17, 62, 27, 10, 23, 20, 13, 4],
#         [8, 29, 18, 15, 6, 11, 24, 21],
#         [63, 16, 7, 28, 19, 14, 5, 12]]


