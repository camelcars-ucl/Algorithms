def knapsack(profit, weight, index, size):
    '''
    Recursive implementation of the 0-1 knapsack problemu
    To understand why this works, you've saved the link to
    a really good visualization in your bookmarks
    Can be solved using DP
    '''
    if index == -1:
        return 0
    if weight[index] > size:
        return knapsack(profit, weight, index-1, size)
    else:
        return max(profit[index] + knapsack(profit, weight, index-1, size-weight[index]),
                                    knapsack(profit, weight, index-1, size))


def test_knapsack():
    profit = [7,3,8,6,5]
    weight = [10,15,2,4,5]
    print(knapsack(profit, weight, len(weight)-1, 20))


test_knapsack()