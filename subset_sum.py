def subset_sum(array, i, num):
    '''
    Recursively implementation
    Only outputs a boolean value
    '''
    if i == -1: return False
    if array[i] == num: return True
    if array[i] > num: return subset_sum(array, i-1, num)
    else: return subset_sum(array, i-1, num-array[i]) or subset_sum(array, i-1, num)

print(subset_sum([3,34,4,12,5,2], 5, 9))

def subset_sum_1(arr, num):
    '''
    DP implementation
    '''
    A = [[False for x in range(num+1)] for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        A[i][0] = True
    for i in range(1, len(arr)+1):
        for x in range(1, num+1):
            if arr[i-1] == x:
                A[i][x] = True
                # print(A[i])
            elif arr[i-1] < x:
                A[i][x] = A[i-1][x-arr[i-1]] or A[i-1][x]
            else:
                A[i][x] = A[i-1][x]
    for i in A:
        print(i)
    print(A[len(arr)][num])
    return A

def find_subsets(arr, num):
    '''
    Finds the number of subsets that sum to num
    '''
    A = [[0 for x in range(num+1)] for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        A[i][0] = 1
    for i in range(1, len(arr)+1):
        for x in range(1, num+1):
            if arr[i-1] > x:
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = A[i-1][x-arr[i-1]] + A[i-1][x]
    for i in A:
        print(i)

def perfect_sum(arr, num):
    '''
    Finds out all the possible subsets that sum to num
    I'm not even bothered to document this. Just know that
    the thought process is pretty much like all the other 
    find subsets function here, just with added array
    manipulation

    '''
    path = [[[] for x in range(num+1)] for i in range(len(arr)+1)] 
    for i in range(1, len(arr)+1):
        for x in range(1, num+1):
            potential_cell = []
            if path[i-1][x] != []:  # 1
                for cell in path[i-1][x]:
                    potential_cell.append(cell)
            if arr[i-1] > x:    # 2
                if path[i-1][x] != []:
                    potential_cell += path[i-1][x]
            else:
                if x-arr[i-1] == 0: # 3
                    potential_cell.append([x])
                if path[i-1][x-arr[i-1]] != []:     #4
                    for cell in path[i-1][x-arr[i-1]]:
                        print(arr[i-1])
                        new_cell = cell+[arr[i-1]]
                        potential_cell.append(new_cell)
            path[i][x] = potential_cell
        for i in path:
            print(i)
        print("new")
    print(path[len(arr)][num])

def traversal(matrix, arr, num):
    '''
    this doesn't work
    '''
    print('runs')
    print(arr[-1])
    solutions = []
    if num == 0:
        return []
    if arr[-1] > num:
        return traversal(matrix, arr[:-1], num)
    if matrix[len(arr)][num-arr[-1]] == False:
        return []
    if matrix[len(arr)][num-arr[-1]] == True:
        solution = [arr[-1]] + traversal(matrix, arr[:-1], num-arr[-1])
    if matrix[len(arr)-1][num] == True:
        return traversal(matrix, arr[:-1], num)

# class tree:
#     def __init__(self, value):
        

# matrix = subset_sum_1([3,34,4,12,5,2], 9)
# subset_sum_1([1,3,5,2,8], 9)
# traversal(matrix, [3,34,4,12,5,2], 9)
perfect_sum([1,3,2,5,4,9], 9)
# find_subsets([1,3,2,5,4,9], 9)

# 0:[True, False, False, False, False, False, False, False, False, False]
# 3:[True, False, False, True, False, False, False, False, False, False]
# 34:[True, False, False, True, False, False, False, False, False, False]
# 4:[True, False, False, True, True, False, False, True, False, False]
# 12:[True, False, False, True, True, False, False, True, False, False]
# 5:[True, False, False, True, True, True, False, True, True, True]
# 2:[True, False, True, True, True, True, True, True, True, True]
