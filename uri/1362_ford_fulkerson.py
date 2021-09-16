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
               for neighbors in graph]
    total = 0
    while True:
        sent = dfs(network, source, sink, float('+Inf'), set())
        if sent == 0: break
        total += sent
    return total

tests = int(input())
tshirts = ['XXL', 'XL', 'L', 'M', 'S', 'XS']

for test in range(tests):
    N, M = map(int, input().split())
    graph = [[] for i in range(1 + 6 + M + 1)]
    for i in range(6):
        graph[0].append((i + 1, N//6))

    for i in range(M):
        T1, T2 = map(tshirts.index, input().split())
        graph[T1 + 1].append((7 + i, 1))
        graph[T2 + 1].append((7 + i, 1))
        graph[7 + i].append((7 + M, 1))

    flow = ford_fulkerson(graph, 0, 7+M)
    print('YES' if flow == M else 'NO')