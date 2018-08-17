def LCS(stringA, stringB):
    '''
    Longest common subsequence e.g.
    LCS for input Sequences “AGGTAB” and “GXTXAYB” 
    is “GTAB” of length 4.
    This function returns the length of the LCS

    '''
    L = [[0 for x in range(len(stringA)+1)] for i in range(len(stringB)+1)]
    for i in range(1, len(stringB)+1):
        for x in range(1, len(stringA)+1):
            if stringB[i-1] == stringA[x-1]:
                L[i][x] = 1 + L[i-1][x-1]
            else:
                L[i][x] = max(L[i-1][x], L[i][x-1])
    return L[len(stringB)][len(stringA)]

def lcs_recurse(stringA, stringB, a, b):
    if a < 0: return 0
    if b < 0: return 0
    if stringA[a] == stringB[b]:
        return 1 + lcs_recurse(stringA, stringB, a-1, b-1)
    else:
        return max(lcs_recurse(stringA, stringB, a-1, b), lcs_recurse(stringA, stringB, a, b-1))

def LCS_1(arr_1,arr_2):
    '''
    This function returns the actual contents of the LCS
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
    return A[len(arr_1)][len(arr_2)]

def LCS_2(arr_1,arr_2):
    '''
    This is an improved version of lcs_1
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
    return subsequence

def test_longest_sequence():
    print(lcs_recurse("ABCDGH", "AEDFHR", 5, 5))
    assert LCS("ABCDGH", "AEDFHR") == 3
    assert LCS("AGGTAB", "GXTXAYB") == 4
    assert LCS_1([5,2,8,7,3,1,6,5], [5,1,7,2,3,1,8,4]) == [1, 3, 7, 5]
    assert LCS_2([5,2,8,7,3,1,6,5], [5,1,7,2,3,1,8,4]) == [1, 3, 7, 5]

test_longest_sequence()
