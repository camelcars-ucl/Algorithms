def solve(N, k, j):
    arr = [[0 for i in range(N)] for i in range(N)]  #displays the flow
    arr[0][0] = N
    for i in range(1, N):
        for x in range(0, i+1):
            if x == 0:
                num = (arr[i-1][x]-1)/2
                if num < 0:
                    arr[i][x] = 0
                else:
                    arr[i][x] = num
            else:
                first_num = (arr[i-1][x]-1)/2
                second_num = (arr[i-1][x-1]-1)/2
                if first_num < 0: first_num = 0
                if second_num < 0: second_num = 0
                arr[i][x] = first_num + second_num
    water_arr = [[0 for i in range(N)] for i in range(N)]  # displays water in each glass
    for i in range(0, N):
        for x in range(0, i+1):
            if arr[i][x] >= 1:
                water_arr[i][x] = 1
            else:
                water_arr[i][x] = arr[i][x]
    # for i in range(N):
    #     for x in range(i+1):
    #         print(water_arr[i][x], end=' ')
    #     print('\n')
    # for i in range(N):
    #     for x in range(i+1):
    #         print(arr[i][x], end=' ')
    #     print('\n')
    print(water_arr[k-1][j-1])

t = int(input())
for i in range(t):
    N = int(input())
    i = int(input())
    j = int(input())
    solve(N, i, j)

# solve(9, 4, 3)

