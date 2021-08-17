def connectedComponents(n, graph):
    components, visited = [], [False] * n

    def dfs(start):
        component = []
        stack = [start]
        while stack:
            start = stack[-1]
            if visited[start]:
                stack.pop()
                continue
            else:
                visited[start] = True
                component.append(start)

            for i in graph[start]:
                if not visited[i]:
                    stack.append(i)

        return component

    for i in range(n):
        if not visited[i]:
            components.append(dfs(i))

    return len(components)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
print(connectedComponents(N, graph))
