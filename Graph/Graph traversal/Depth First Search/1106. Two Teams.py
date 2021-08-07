def dfs(n, graph, start=1):
    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    dp = [0] * (n + 1)
    stack = [start]

    while stack:
        start = stack[-1]

        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)

        else:
            stack.pop()
            dp[start] += 1
            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True
    return dp


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    edges = list(map(int, input().split()))
    graph[edges[0]].extend(edges[1:len(edges) - 1])

print(dfs(n, graph))
# print(graph)
