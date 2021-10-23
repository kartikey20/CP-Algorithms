# TLE
def solve(graph, n, k):
    res = []
    stop = (2*n+k-1)//k
    visited = [False for _ in range(n+1)]

    def dfs(node):
        visited[node] = True
        res.append(node)
        for i in graph[node]:
            if not visited[i]:
                dfs(i)
                res.append(node)
    dfs(1)
    ans = []
    count = 0
    for i in range(k):
        beg = i * stop
        ends = min((i+1) * stop, len(res))
        if ends <= beg:
            print("1 1\n")
            continue
        ans.append([ends-beg])
        for j in range(beg, ends):
            ans[count].append(res[j])
        count += 1
    for x in ans:
        print(' '.join(map(str, x)))


n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
solve(graph, n, k)
