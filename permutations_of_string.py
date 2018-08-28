def solve(string, picked, sub_string, permutations):
    if len(sub_string) == len(string):
        permutations.append(sub_string)
        return 
    for i in range(len(string)):
        if picked[i] == False:
            picked[i] = True
            solve(string, picked, sub_string+string[i], permutations)
            picked[i] = False
    return 


def main():
    string = str(input())
    picked = [False for i in range(len(string))]
    permutations = []
    for i in range(len(string)):
        picked[i] = True
        solve(string, picked, string[i], permutations)
        picked[i] = False
    print(permutations)

main()
