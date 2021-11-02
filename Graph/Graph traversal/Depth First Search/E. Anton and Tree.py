# WA
import copy


def solve(n, graph, colors, color):
    count = 0
    visited = [False for _ in range(n)]

    def dfs(node):
        colors[node] = color
        visited[node] = True
        for i in graph[node]:
            if not visited[i] and colors[i] != color:
                dfs(i)

    for i in range(n):
        if not visited[i] and colors[i] != color:
            count += 1
            dfs(i)
    return count


n = int(input())
colors = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
# print(graph)
print(min(w := solve(n, graph, copy.deepcopy(colors), 0),
      b := solve(n, graph, copy.deepcopy(colors), 1)))
