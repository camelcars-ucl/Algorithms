def longest_subsequence(stringA, stringB):
    L = [[0 for x in range(len(stringA)+1)] for i in range(len(stringB)+1)]
    for i in range(1, len(stringB)+1):
        for x in range(1, len(stringA)+1):
            if stringB[i-1] == stringA[x-1]:
                L[i][x] = 1 + L[i-1][x-1]
            else:
                L[i][x] = max(L[i-1][x], L[i][x-1])
    return L[len(stringB)][len(stringA)]


def test_longest_sequence():
    assert longest_subsequence("ABCDGH", "AEDFHR") == 3
    assert longest_subsequence("AGGTAB", "GXTXAYB") == 4

test_longest_sequence()
