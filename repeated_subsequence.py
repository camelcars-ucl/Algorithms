def longest_repeated_subsequence(stringA):
    '''
    returns length of the sequence
    '''
    table = len(stringA)+1
    L = [[0 for i in range(table)] for x in range(table)]
    for x in range(1, table):
        for i in range(1, table):
            if stringA[i-1] == stringA[x-1] and i != x:
                L[x][i] = 1 + max(L[x-1][i], L[x][i-1])
            else:
                L[x][i] = max(L[x-1][i], L[x][i-1])
    print(L[table-1][table-1])
    return L[table-1][table-1]


def longest_repeated_subsequence_2(stringA):
    '''
    returns length of the sequence
    '''
    table = len(stringA)+1
    L = [["" for i in range(table)] for x in range(table)]
    for x in range(1, table):
        for i in range(1, table):
            if stringA[i-1] == stringA[x-1] and i != x:
                if len(L[x-1][i]) > len(L[x][i-1]):
                    L[x][i] = L[x-1][i] + stringA[i-1] 
                else:
                    L[x][i] = L[x][i-1] + stringA[i-1] 
            elif len(L[x-1][i]) > len(L[x][i-1]):
                L[x][i] = L[x-1][i]
            else:
                L[x][i] = L[x][i-1]
    print(L[table-1][table-1])
    return L[table-1][table-1]
def test_func():
    longest_repeated_subsequence("AABEBCDD")
    longest_repeated_subsequence("AABB")
    longest_repeated_subsequence("AAB")
    longest_repeated_subsequence_2("AABEBCDD")
    longest_repeated_subsequence_2("AABB")
    longest_repeated_subsequence_2("AAB")

test_func()