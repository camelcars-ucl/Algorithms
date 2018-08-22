'''
Find whether there exist aHamiltonian Path in an undirected graph
'''


def pick(matrix, visited, n):
    if False not in visited:
        return True
    for i in range(len(visited)):
        if matrix[n][i] == 1 and visited[i] == False:
            visited[i] = True
            if pick(matrix, visited, i):
                return True
            else:
                visited[i] = False
    return False


def solve(V, pairs):
    matrix = [[0 for i in range(V)] for i in range(V)]
    visited = [False for i in range(V)]
    for p in pairs:
        matrix[p[0]-1][p[1]-1] = 1
        matrix[p[1]-1][p[0]-1] = 1  # because the graph is undirected
    for i in range(V):  # Select different starting nodes
        visited[i] = True
        if pick(matrix, visited, i):
            return True
        visited[i] = False
    return False


def tuplefy(arr):
    new_arr = []
    for i in range(1, len(arr), 2):
        new_arr.append((arr[i-1], arr[i]))
    return new_arr

def main():
    t = int(input())
    for i in range(t):
        info = input().strip().split(' ')
        pairs = input().strip().split(' ')
        pairs = [int(i) for i in pairs]
        V, E = [int(i) for i in info]
        ans = solve(V, tuplefy(pairs))
        if ans:
            print(1)
        else:
            print(0)


main()