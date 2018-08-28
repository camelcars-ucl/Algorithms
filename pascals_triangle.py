def solve(N):
    arr = [[0 for i in range(N)] for i in range(N)]
    arr[0][0] = 1
    for i in range(1,N):
        for x in range(0, i+1):
            if x == 0:
                arr[i][x] = arr[i-1][x]
            else:
                arr[i][x] = arr[i-1][x] + arr[i-1][x-1]
    for i in range(N):
        for x in range(i+1):
            print(arr[i][x], end=' ')
        print('\n')


solve(5)