def solve(n, graph, degrees):
    allEdges = []
    addedEdges = []
    eulerPath = []
    count = n
    for i in range(1, n+1):
        if degrees[i] % 2 != 0:
            count -= 1
            graph[n+1].append(i)
            graph[i].append(n+1)
            addedEdges.append([n+1, i])
            addedEdges.append([i, n+1])

    def find_euler_path(node):
        for child in graph[node]:
            graph[child].remove(node)
            graph[node].remove(child)
            find_euler_path(child)
        allEdges.append(node)

    for i in range(1, n+2):
        if len(graph[i]) > 0:
            find_euler_path(i)
            for j in range(len(allEdges)-1):
                if [allEdges[j], allEdges[j+1]] not in addedEdges:
                    eulerPath.append([allEdges[j], allEdges[j+1]])
            break
    return [count, eulerPath]


res = []
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+2)]
    degrees = [0 for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
    res.append(solve(n, graph, degrees))

for count, edges in res:
    print(count)
    for u, v in edges:
        print(u, v)
