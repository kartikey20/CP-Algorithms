def solve(graph, n, k):
    res = []
    limit = 2*n//k
    visited = [False for _ in range(n)]
    count = [0]

    def dfs(node):
        visited[node] = True
        for i in graph[node]:
            if not visited[i]:
                res.append(i)
                count[0] += 1
                print(count)
                if count[0] == limit:
                    print(res)
                    exit()
                dfs(i)
    dfs(0)


n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[min(u-1, v-1)].append(max(u-1, v-1))
solve(graph, n, k)
