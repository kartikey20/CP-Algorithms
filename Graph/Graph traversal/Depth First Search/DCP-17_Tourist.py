def solve(N, graph):
    visited = [False for _ in range(N)]
    count = 0

    def dfs(node):
        visited[node] = True
        for i in graph[node]:
            if not visited[i]:
                dfs(i)

    for i in range(N):
        if not visited[i]:
            dfs(i)
            count += 1
    return count


T = int(input())
res = []
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
    print(graph)
    res.append(solve(N, graph))

print(res)
