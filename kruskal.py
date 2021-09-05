#!/usr/bin/env python3

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, index):
        if self.parent[index] == index: return index
        self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
        a, b = self.find(index1), self.find(index2)
        if a < b: a, b = b, a
        self.parent[b] = a

def kruskal(graph):
    edges = sorted((cost, node, neighbor)
        for node, neighbors in enumerate(graph) 
        for neighbor, cost in neighbors)

    sets = UnionFind(len(graph))
    tree = []
    
    for cost, node1, node2 in edges:
        set1, set2 = sets.find(node1), sets.find(node2)
        if set1 == set2: continue
        sets.union(set1, set2)
        tree.append(((node1, node2), cost))
    return tree

graph = [
    [(1, 5), (2, 15), (3, 16)],
    [(2, 13), (3, 1)],
    [(3, 1)],
    []
]

print(kruskal(graph))