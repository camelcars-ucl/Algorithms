import math
def bellman_ford(cost_matrix, src):
    v_length = len(cost_matrix)
    distance = [math.inf for i in range(v_length)]
    distance[src] = 0
    for u in range(v_length):
        for v in range(v_length):
            if distance[v] > cost_matrix[u][v] + distance[u]:
                distance[v] = cost_matrix[u][v] + distance[u]
    return distance


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
    LMIS([5,2,8,7,3,1,6,5,4])
    a = [5,2,8,7,3,1,6,5,4]
    print(recurse_LMIS(a, len(a)-1, len(a)-2))
main()