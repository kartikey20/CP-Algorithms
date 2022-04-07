from collections import defaultdict


def solve(N, graph, strength):

    def bfs(graph, start):
        visited = defaultdict(lambda: False)
        queue = [[start, strength[start]]]
        visited[start] = True
        for city in queue:
            node, stren = city
            for child in graph[node]:
                if visited[child] == True:


T = int(input())
res = []
for _ in range(T):
    N, R, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(R):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    strength = defaultdict(int)
    for _ in range(M):
        K, S = map(int, input().split())
        strength[K] += S
    res.append(solve(N, graph, strength))
