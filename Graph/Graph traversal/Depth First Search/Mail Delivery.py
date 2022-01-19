def solve(n, graph, degrees):
    for i in range(1, n+1):
        if degrees[i] % 2 != 0:
            print("IMPOSSIBLE")
            return
    allEdges = []

    def findEulerPath(node):
        for child in graph[node]:
            graph[node].remove(child)
            graph[child].remove(node)
            findEulerPath(child)
        allEdges.append(node)

    for i in range(1, n+1):
        if degrees[i] > 0:
            findEulerPath(i)
            break
    print(*allEdges)


n, m = map(int, input().split())
graph = [set() for _ in range(n+1)]
degrees = [0 for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
    degrees[u] += 1
    degrees[v] += 1
for i in range(len(graph)):
    graph[i] = list(graph[i])
solve(n, graph, degrees)
