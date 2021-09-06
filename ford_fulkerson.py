#!/usr/bin/env python3

import collections

def dfs(network, source, sink, flow, visited):
    visited.add(source)
    if source == sink: return flow

    for neighbor, capacity in network[source].items():
        if capacity <= 0 or neighbor in visited: continue
        sent = dfs(network, neighbor, sink, min(flow, capacity), visited)
        if not sent: continue
        network[source][neighbor] -= sent
        network[neighbor][source] += sent
        return sent
    return 0

def ford_fulkerson(graph, source, sink):
    #initialize residual network with default capacity 0 for undefined nodes
    network = [collections.defaultdict(lambda: 0, neighbors)
               for node, neighbors in enumerate(graph)]
    total = 0
    while True:
        sent = dfs(network, source, sink, float('+Inf'), set())
        if sent == 0: break
        total += sent
    return total

graph = [
    [(1, 5), (2, 15), (3, 16)],
    [(2, 13), (3, 1)],
    [(3, 1)],
    [(2, 1)],
]

print(ford_fulkerson(graph, 0, 3))