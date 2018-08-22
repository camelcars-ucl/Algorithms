'''
Sudoku puzzle solved using backtracking
'''

def get_subgrid(matrix, i, x):
    subgrid = []
    sub_row = None
    sub_col = None
    if i in range(0, 3):
        sub_row = 1
    elif i in range(3, 6):
        sub_row = 2
    else:
        sub_row = 3
    if x in range(0, 3):
        sub_col = 1
    elif x in range(3, 6):
        sub_col = 2
    else:
        sub_col = 3
    for i in range((sub_row-1)*3,((sub_row-1)*3)+3):
        for x in range((sub_col-1)*3,((sub_col-1)*3)+3):
            subgrid.append(matrix[i][x])
    return subgrid


def is_safe(matrix, i, x, num):
    if num in matrix[i]:
        return False
    if num in get_subgrid(matrix, i, x):
        return False
    if num in [matrix[i][x] for i in range(9)]: # uses x from param
        return False
    return True


def solve(matrix):
    for row in matrix:
        if 0 in row:
            break
    else:
        return matrix
    for i in range(9):
        for x in range(9):
            if matrix[i][x] == 0:
                for num in range(1, 10):
                    if is_safe(matrix, i, x, num):
                        matrix[i][x] = num
                        if solve(matrix) == matrix:
                            return matrix
                        else:
                            matrix[i][x] = 0
                return False


def pack(arr, step):
    i = 0
    new_arr = []
    for i in range(1, len(arr), step):
        new_arr.append(arr[i-1:step+i-1])
    return new_arr


def format_output(matrix):
    output = ''
    for i in range(9):
        for x in range(9):
            output += str(matrix[i][x]) + ' '
    return output


def main():
    t = int(input())
    for i in range(t):
        nums = list(map(int,input().split()))
        ans = solve(pack(nums, 9))
        print(format_output(ans))

# example input
# 3 0 6 5 0 8 4 0 0 5 2 0 0 0 0 0 0 0 0 8 7 0 0 0 0 3 1 0 0 3 0 1 0 0 8 0 9 0 0 8 6 3 0 0 5 0 5 0 0 9 0 6 0 0 1 3 0 0 0 0 2 5 0 0 0 0 0 0 0 0 7 4 0 0 5 2 0 6 3 0 0
main()



