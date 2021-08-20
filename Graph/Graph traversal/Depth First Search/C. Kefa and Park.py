# https://codeforces.com/problemset/problem/580/C
# [[], [2, 3], [4, 5], [6, 7], [], [], [], []]
# 0 1 0 1 1 0 0 0


def solve(graph, hasCat, m):
    n = len(graph)
    visited = [False] * (n + 1)
    countPaths = [0]

    def dfs(node, countCats):
        visited[node] = True
        if graph[node] == []:
            countPaths[0] += 1
        for child in graph[node]:
            if not visited[child]:
                if hasCat[child] == 1:
                    countCats += 1
                if hasCat[child] == 0:
                    countCats = 0
                if countCats < m:
                    dfs(child, countCats)
    dfs(1, 0)
    return countPaths[0]


n, m = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
print(solve(graph, a, m))
print(graph)
print(a)
