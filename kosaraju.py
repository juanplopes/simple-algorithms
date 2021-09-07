#!/usr/bin/env python3

def dfs(graph, node, visited, exit_order):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, exit_order)
    exit_order.append(node)

def topological_sort(graph):
    visited = set()
    order = []
    for node in range(len(graph)):
        if node in visited: continue
        dfs(graph, node, visited, order)
    return order[::-1]    

def kosaraju(graph):
    transposed = [[] for _ in graph]
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            transposed[neighbor].append(node)

    visited = set()
    components = []
    for node in topological_sort(graph):
        if node in visited: continue
        components.append([])
        dfs(transposed, node, visited, components[-1])
    return components

graph = [
    [1, 2, 3],
    [2, 3],
    [3, 1],
    []
]

print(kosaraju(graph))