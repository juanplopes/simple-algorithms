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

while True:
    C, P = map(int, input().split())
    if C == 0 and P == 0: break
    graph = [[] for _ in range(2*P)]

    for i in range(C):
        y1, y2, n1, n2 = map(int, input().split())
        if y1 == 0: y1 = y2
        if y2 == 0: y2 = y1
        if n1 == 0: n1 = n2
        if n2 == 0: n2 = n1
        if y1 != 0:
            graph[y1 + P - 1].append(y2 - 1) # not y1 -> y2
            graph[y2 + P - 1].append(y1 - 1) # not y2 -> y1
        if n1 != 0:
            graph[n1 - 1].append(n2 + P - 1) # n1 -> not n2
            graph[n2 - 1].append(n1 + P -1) # n1 -> not n2
    sets = (set(c) for c in kosaraju(graph))

    print ('no' if any(node + P in component or node - P in component 
               for component in sets
               for node in component)
            else 'yes')