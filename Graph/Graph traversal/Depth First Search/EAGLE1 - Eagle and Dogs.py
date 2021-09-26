# TODO: logic working but NZEC error in spoj
def maxCost(n, graph, start):
    visited = [False for _ in range(n)]
    count = [0]

    def dfs(node, cost):
        visited[node] = True
        for i in graph[node]:
            if not visited[i[0]]:
                cost.append(i[1])
                dfs(i[0], cost[:])
                cost.pop()
        count[0] = max(count[0], sum(cost))
    dfs(start, [])
    return count[0]


def solve(n, graph):
    res = []
    for i in range(n):
        res.append(maxCost(n, graph, i))
    return res


res = []
T = int(input())
for _ in range(T):
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, d = map(int, input().split())
        graph[u - 1].append([v - 1, d])
        graph[v - 1].append([u - 1, d])
    res.append(" ".join(map(str, solve(n, graph))))

for i in res:
    print(i)
