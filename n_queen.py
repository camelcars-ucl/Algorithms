def print_board(board):
    for i in board:
        print(i)


def check_diagonal(row, col, N, board):
    '''
    Helper function to is_safe
    '''
    row_2 = row
    col_2 = col
    while row != 0 and col != 0:
        row -= 1
        col -= 1 
        if board[row][col] == 1:
            return False
    while col_2 != 0 and row_2 != N-1:
        row_2 += 1
        col_2 -= 1
        if board[row_2][col_2] == 1:
            return False
    return True


def is_safe(row, col, N, board):
    '''
    checks that the queen is in a valid position
    '''
    for i in range(col):
        if board[row][i] == 1:
            return False
    if check_diagonal(row, col, N, board) == False:
        return False
    return True


def place(col, N, board):
    '''
    Finds 1 solution to the n-queen problem
    '''
    if col == N:
        return board
    for i in range(N):
        if is_safe(i, col, N, board):
            board[i][col] = 1
            if place(col + 1, N, board) == board:
                return board
            else:
                board[i][col] = 0
    return False


def place_2(col, N, board, solutions):
    '''
    Find all solutions to the problem
    '''
    if col == N:
        board = [[i for i in row] for row in board]     # A copy of the board is required
        solutions.append(board)
        return solutions
    for i in range(N):
        if is_safe(i, col, N, board):
            board[i][col] = 1
            solutions+place_2(col + 1, N, board, solutions)     # where the magic happens
            board[i][col] = 0
    return solutions


def solve(N):
    board = [[0 for i in range(N)] for i in range(N)]
    solutions = []
    return place_2(0, N, board, solutions)

def get_pos(array):
    '''
    Helper func to format_func
    '''
    result = []
    N = len(array)
    for i in range(N):
        for x in range(N):
            if array[x][i] == 1:
                result.append(x+1)
    return result


def format_func(solutions, N):
    '''
    formatting it in the way geeksforgeeks wanted it
    '''
    final_positions = []
    for sol in solutions:   
        final_positions.append(get_pos(sol))
    result = ''
    for sol in final_positions:
        result += '['
        for num in sol:
            result += str(num) + ' '
        result += '] '
    return result

t = int(input())

for i in range(t):
    N = int(input())
    ans = solve(N)
    if ans == []:
        print('-1')
    else:
        print(format_func(ans, N))
