import math
def bellman_ford(cost_matrix, src):
    v_length = len(cost_matrix)
    distance = [math.inf for i in range(v_length)]
    distance[src] = 0
    for u in range(v_length):
        for v in range(v_length):
            if distance[v] > cost_matrix[u][v] + distance[u]:
                distance[v] = cost_matrix[u][v] + distance[u]
    print(distance)

def LCS(arr_1,arr_2):
    '''
    This works but feels very hacky, notice how i initialized
    arrays in each cells. You can't easily do this in other
    languages
    '''
    A = [[[] for i in range(len(arr_2)+1)] for x in range(len(arr_1)+1)]
    for i in range(1, len(arr_1)+1):
        for x in range(1, len(arr_2)+1):
            if arr_1[i-1] == arr_2[x-1]:
                A[i][x] = [arr_1[i-1]] + A[i-1][x-1]
            elif len(A[i-1][x]) > len(A[i][x-1]):
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = A[i][x-1]
    print(A[len(arr_1)][len(arr_2)])


def LCS_2(arr_1,arr_2):
    '''
    The while loop basically traverses the 2-D array
    backwards. It is basically following what we did
    in reverse
    '''
    A = [[0 for i in range(len(arr_2)+1)] for x in range(len(arr_1)+1)]
    for i in range(1, len(arr_1)+1):
        for x in range(1, len(arr_2)+1):
            if arr_1[i-1] == arr_2[x-1]:
                A[i][x] = 1 + A[i-1][x-1]
            else:
                A[i][x] = max(A[i-1][x], A[i][x-1])
    subsequence = []
    i = len(arr_1)
    x = len(arr_2)
    while A[i][x] != 0:
        if arr_1[i-1] == arr_2[x-1]:
            subsequence.append(arr_1[i-1])
            i -= 1
            x -= 1
        elif A[i-1][x] > A[i][x-1]:
            i -= 1
        else:
            x -= 1 
    print(subsequence)


def LMIS(array):
    '''
    longest_monotonically_increasing_subsequence
    '''
    L = [[0 for x in range(len(array)+1)] for i in range(len(array)+1)]
    for i in range(1, len(array)+1):
        for n in range(1, len(array)+1):
            if array[i-1] > array[n-1]:
                L[i][n] = 1 + L[i][n-1]
            else:
                L[i][n] = L[i-1][n-1]
    for i in L:
        print(i)
    print(L[len(array)][len(array)-1])


def recurse_LMIS(array, i, n):
    if n < 0:
        return 0
    elif array[i] > array[n]:
        return 1 + recurse_LMIS(array, i, n-1)
    else:
        return recurse_LMIS(array, i-1, n-1)


def main():
    #works for this cost_matrix idk about the rest.
    cost_matrix = [[math.inf,-1,4,math.inf,math.inf],
                   [math.inf,math.inf,3,2,2],
                   [math.inf,math.inf,math.inf,math.inf,math.inf],
                   [math.inf,1,5,math.inf,math.inf],
                   [math.inf,math.inf,math.inf,-3,math.inf]]
    LCS([5,2,8,7,3,1,6,5], [5,1,7,2,3,1,8,4])
    LCS_2([5,2,8,7,3,1,6,5], [5,1,7,2,3,1,8,4])
    LMIS([5,2,8,7,3,1,6,5,4])
    a = [5,2,8,7,3,1,6,5,4]
    print(recurse_LMIS(a, len(a)-1, len(a)-2))
main()