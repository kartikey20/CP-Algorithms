def dfs(graph, n, start=0):
    visited = [False] * n
    stack = [start]
    finished = [False] * n
    dp = [0] * n
    while stack:
        start = stack[-1]

        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)
        else:
            stack.pop()

            # base case
            dp[start] += 1

            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True
    return dp


n = int(input())
d, a = map(int, input().split())
matrix = []
graph = [[] for _ in range(n)]
for _ in range(n):
    matrix.append(list(map(int, input())))
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i].append(j)
print(graph)
print(dfs(graph, n))
