class Node():
    def __init__(self):
        self.children = {}
        self.value = None

    # def find(node, key):
    #     for char in key:
    #         if char in node.children:
    #             node = node.children[char]
    #         else:
    #             return None
    #     return node.value

    def insert(root, string, value):
        node = root
        index_last_char = None
        for index_char, char in enumerate(string):
            if char in node.children:
                node = node.children[char]
            else:
                index_last_char = index_char
                break

        # append new nodes for the remaining characters, if any
        if index_last_char is not None: 
            for char in string[index_last_char:]:
                node.children[char] = Node()
                node = node.children[char]

        # store value in the terminal node
        node.value = value


def traverse(node, words):
    # stack = []
    # stack.append((None, node))
    # while stack != []:
    #     v = stack.pop()
    #     print(v[0])
    #     for key, value in v[1].children.items():
    #         stack.append((key, value))
    pass
# def reconstruct_words(node, word, all_words):
#     if node.value != None:
#         return ''
#     for char in node.children:
#         word + char + reconstruct_words(node.children[char], word)


# def main():
#     root = Node()
#     arr = ['tea', 'ted', 'ten', 'inn', 'in']
#     for value, i in enumerate(arr):
#         root.insert(i, value)
#     words = []

def solve(start_i, start_x, visited, some_word):
    if some_word in dictionary:
        if some_word not in all_words:
            all_words.append(some_word)
    if len(some_word) > parameters[some_word[0]]:
        return
    for i in range(8):
        next_x = start_x + move_x[i]
        next_i = start_i + move_y[i]
        if next_x == M or next_x < 0 or next_i == N or next_i < 0:
            continue
        if visited[next_i][next_x] == False:
            visited[next_i][next_x] = True
            solve(next_i, next_x, visited, some_word + boggle[next_i][next_x])
            visited[next_i][next_x] = False
        else:
            continue
    return


def pack(arr, step):
    '''
    divides an array into smaller chunks
    '''
    if step == 1:   # edge case
        return [[i] for i in arr]
    new_arr = []
    for i in range(1, len(arr), step):
        new_arr.append(arr[i-1:step+i-1])
    return new_arr


def set_paramaters(dictionary):
    parameters = {}  # stores character with its corresponding max length
    for word in dictionary:
        if word[0] not in parameters:
            parameters[word[0]] = len(word)
        else:
            if len(word) > parameters[word[0]]:
                parameters[word[0]] = len(word)
    return parameters


def format_output(arr):
    arr = sorted(arr)
    if arr == []:
        return -1
    result = ''
    for i in arr:
        result += i + ' '
    return result

move_x = [1, 1, 0, -1, -1, -1, 0, 1]
move_y = [0, 1, 1, 1, 0, -1, -1, -1]
t = int(input())
for i in range(t):
    all_words = []
    num = int(input())
    dictionary = input().strip().split(' ')
    dimensions = list(map(int,input().split()))
    N, M = dimensions
    boggle = pack(input().strip().split(' '), M)
    visited = [[False for x in range(M)] for i in range(N)]
    parameters = set_paramaters(dictionary)
    for i in range(N):
        for x in range(M):
            if boggle[i][x] in parameters:
                visited[i][x] = True
                solve(i, x, visited, boggle[i][x])
    print(format_output(all_words))
# dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
# N = 4
# M = 3
# boggle = [['G','I','Z'],
#           ['U','E','K'],
#           ['Q','S','E'],
#           ['H','O','K']]
# parameters = set_paramaters(dictionary)
# visited = [[False for x in range(M)] for i in range(N)]
# for i in range(N):
#     for x in range(M):
#         if boggle[i][x] in parameters:
#             visited[i][x] = True
#             solve(i, x, visited, boggle[i][x])
