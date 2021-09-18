#!/usr/bin/env python3

def floyd_warshall(graph):
    best = [[float('+Inf')] * len(graph) for _ in graph]
    for node, neighbors in enumerate(graph):
        best[node][node] = 0
        for neighbor, cost in neighbors:
            best[node][neighbor] = cost

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                best[i][j] = min(best[i][j], best[i][k] + best[k][j])
    return best


graph = [
    [(1, 5), (2, 15), (3, 16)],
    [(2, 13), (3, 1)],
    [(3, 1)],
    [(2, 1)],
]

print(floyd_warshall(graph))