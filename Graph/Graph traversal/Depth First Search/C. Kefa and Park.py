# https://codeforces.com/problemset/problem/580/C
# [[], [2, 3], [4, 5], [6, 7], [], [], [], []]
# 0 1 0 1 1 0 0 0


def solve(graph, hasCat, m):
    n = len(graph)
    visited = [False] * n
    visited[1] = True
    arr = []
    count = hasCat[1]

    def dfs(node, count):
        if graph[node] == []:
            arr.append(node)
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                if hasCat[child] == 1:
                    count += 1
                else:
                    count = 0
                if count <= m:
                    dfs(child, count)
    dfs(1, count)
    return arr


n, m = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
print(solve(graph, a, m))
