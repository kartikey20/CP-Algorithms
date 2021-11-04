from functools import reduce

n = int(input())
d, a = map(int, input().split())
adjMatrix = []
graph = [[] for _ in range(n)]
for _ in range(n):
    adjMatrix.append(list(map(int, input())))
for i in range(n):
    for j in range(n):
        if adjMatrix[i][j] == 1:
            graph[i].append(j)


def connectedComponents(n, graph):
    visited = [False] * n
    components = []

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

    return components


def prim(n, adj):
    selected = [False] * n
    min_e = [[float('inf'), -1] for _ in range(n)]
    mst_edges = []
    min_e[0][0] = 0

    for i in range(n):
        v = -1
        for j in range(n):
            if not selected[j] and (v == -1 or min_e[j][0] < min_e[v][0]):
                v = j

        if min_e[v][0] == float('inf'):
            return None, None

        selected[v] = True
        if min_e[v][1] != -1:
            mst_edges.append([v, min_e[v][1]])

        for to in range(n):
            if adj[v][to] < min_e[to][0]:
                min_e[to] = [adj[v][to], v]

    return mst_edges


connectedVertices = connectedComponents(n, graph)
mst = prim(n, adjMatrix)

# for i in range(len(connectedVertices) - 1):
#     newPrim.append([connectedVertices[i][-1], connectedVertices[i + 1][0]])


newMatrix = [[0 for _ in range(n)] for _ in range(n)]

for x in mst:
    newMatrix[x[0]][x[1]] = 1

print(newMatrix)
print(adjMatrix)
