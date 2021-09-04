#!/usr/bin/env python3

import heapq

def dijkstra(graph, start_node, end_node):
    best = [float('+Inf')] * len(graph)
    
    heap = []
    heapq.heappush(heap, (0, start_node, [start_node]))
    while len(heap):
        distance, node, path = heapq.heappop(heap)
        if distance >= best[node]: continue
        if node == end_node: 
            return distance, path
        best[node] = distance

        for neighbor, cost in graph[node]:
            if distance + cost >= best[neighbor]: continue
            heapq.heappush(heap, (distance+cost, neighbor, path + [neighbor]))

graph = [
    [(1, 5), (2, 15), (3, 16)],
    [(2, 13), (3, 1)],
    [(3, 1)],
    [(2, 1)],
]

print(dijkstra(graph, 0, 3))
print(dijkstra(graph, 0, 2))
print(dijkstra(graph, 0, 1))