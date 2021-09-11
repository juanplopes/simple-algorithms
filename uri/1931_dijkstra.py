import heapq

def dijkstra(graph, start_node, end_node):
    best = [float('+Inf')] * len(graph)
    
    heap = []
    heapq.heappush(heap, (0, start_node))
    while len(heap):
        distance, node = heapq.heappop(heap)
        if distance >= best[node]: continue
        if node == end_node: 
            return distance
        best[node] = distance

        for neighbor, cost in graph[node]:
            if distance + cost >= best[neighbor]: continue
            heapq.heappush(heap, (distance+cost, neighbor))
    return -1

while True:
    try:
        C, V = map(int, input().split(' '))
        graph = [[] for _ in range(C)]
        for i in range(V):
            A, B, cost = map(int, input().split(' '))
            graph[A - 1].append((B - 1, cost))
            graph[B - 1].append((A - 1, cost))
            
        graph2 = [[] for _ in range(C)]
        for node, neighbors in enumerate(graph):
            for neighbor, cost in neighbors:
                for neighbor2, cost2 in graph[neighbor]:
                    graph2[node].append((neighbor2, cost + cost2))

        print(dijkstra(graph2, 0, C-1))
    except EOFError:
        break