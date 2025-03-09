from itertools import permutations

V = 4

def travel_salesman(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = []
    next_permutation = permutations(vertex)
    
    for i in next_permutation:
        current_path_weight = 0
        k = s
        for j in i:
            current_path_weight += graph[k][j]
            k = j
        current_path_weight += graph[k][s]
        min_path.append(current_path_weight)
        x = sorted(min_path)

    return x[0]

graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]

s = 0
print(travel_salesman(graph, s))
