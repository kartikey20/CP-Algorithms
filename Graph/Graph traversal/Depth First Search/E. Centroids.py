def solve(graph, n):
    visited = [False for _ in range(n+1)]
    count = [0 for _ in range(n+1)]
    maxSubTree = [0 for _ in range(n+1)]
    centroid = [-1]
    childrenOfCentroid = [[set(), -1, 0], [set(), -1, 0]]
    res = [0 for _ in range(n+1)]

    def findCentroid(node, visited):
        visited[node] = True
        count[node] = 1
        maxSubTree[node] = 0
        for child in graph[node]:
            if not visited[child]:
                findCentroid(child, visited)
                count[node] += count[child]
                maxSubTree[node] = max(maxSubTree[node], count[child])
        if max(maxSubTree[node], n - count[node]) <= n//2:
            centroid[0] = node

    def recalulateNodes(node, visited):
        visited[node] = True
        count[node] = 1
        for child in graph[node]:
            if not visited[child]:
                recalulateNodes(child, visited)
                count[node] += count[child]

    def findCentroidChildren(node, visited):
        visited[node] = True
        for child in graph[node]:
            if not visited[child]:
                if childrenOfCentroid[0][2] < count[child]:
                    childrenOfCentroid[0] = childrenOfCentroid[1]
                    childrenOfCentroid[0][2] = count[child]
                    childrenOfCentroid[0][1] = child
                elif childrenOfCentroid[1][2] < count[child]:
                    childrenOfCentroid[1][2] = count[child]
                    childrenOfCentroid[1][1] = child

    def findSubset(node, visited):
        visited[node] = True
        childrenOfCentroid[0][0].add(node)
        for child in graph[node]:
            if not visited[child]:
                findSubset(child, visited)

    def dfs(node, visited):
        visited[node] = True
        if node == centroid[0]:
            res[node] = 1
        else:
            if node in childrenOfCentroid[0][0]:
                if n - count[node] - childrenOfCentroid[1][2] <= n//2:
                    res[node] = 1
                elif n - childrenOfCentroid[0][2] <= n//2:
                    res[node] = 1
            elif n - count[node] - childrenOfCentroid[0][2] <= n//2:
                res[node] = 1
        for child in graph[node]:
            if not visited[child]:
                dfs(child, visited)

    findCentroid(1, visited[:])
    recalulateNodes(centroid[0], visited[:])
    findCentroidChildren(centroid[0], visited[:])
    if centroid[0] != -1:
        findSubset(childrenOfCentroid[0][1], visited[:])
        dfs(centroid[0], visited[:])
    return " ".join(str(x) for x in res)


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(solve(graph, n))
