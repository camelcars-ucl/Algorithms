import math
def bellman_ford(cost_matrix, src):
    v_length = len(cost_matrix)
    distance = [math.inf for i in range(v_length)]
    distance[src] = 0
    for u in range(v_length):
        for v in range(v_length):
            if distance[v] > cost_matrix[u][v] + distance[u]:
                distance[v] = cost_matrix[u][v] + distance[u]
    return distance


def main():
    #works for this cost_matrix idk about the rest.
    cost_matrix = [[math.inf,-1,4,math.inf,math.inf],
                   [math.inf,math.inf,3,2,2],
                   [math.inf,math.inf,math.inf,math.inf,math.inf],
                   [math.inf,1,5,math.inf,math.inf],
                   [math.inf,math.inf,math.inf,-3,math.inf]]
main()