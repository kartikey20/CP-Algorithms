from heapq import heappop, heappush
from tkinter import N


def dijkstra(graph, start):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = 10
    dist = [float('int')] * N
    parents = [0] * N
    queue = [(start, 0)]
    dist[start] = 0
    while queue:

        node, cost = heappop(queue)
        if cost == dist[node]:
            for child, child_cost in graph[node]:
                if cost + child_cost < dist[child]:
                    dist[child] = cost + child_cost
                    parents[child] = node
                    heappush(queue, (child + cost + child_cost))
    return dist
