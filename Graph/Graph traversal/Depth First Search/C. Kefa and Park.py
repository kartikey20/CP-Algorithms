# https://codeforces.com/problemset/problem/580/C

def solve(graph, n, m):
    def dfs(graph, start=1):
        stack = [start]
        dp = [0] * (n + 1)
        visited, finished = [False] * (n + 1), [False] * (n + 1)
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
                dp[start] =

    return


n, m = map(int, input().split())
a = list(map(int, input().split()))
res = []
graph = [[] for i in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    res.append(solve(graph, n, m))

for i in res:
    print(i)
