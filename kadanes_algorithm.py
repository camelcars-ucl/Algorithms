def solve(arr):
    val = arr[0]
    max_so_far = arr[0]
    start = 0
    end = 0
    for i in range(1,len(arr)):
        if arr[i] > val + arr[i]:
            val = arr[i]
            start = i
        else:
            val = val + arr[i]
        if val > max_so_far:
            end = i
            max_so_far = val
    print(max_so_far)


def main():
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr)


main()
