# https://codeforces.com/problemset/problem/580/C

def solve(graph, a, n, m):
    def dfs(graph, a, n, m, start=1):
        stack = [start]
        dp = [0] * (n + 1)
        visited, finished = [False] * (n + 1), [False] * (n + 1)

        while stack:
            start = stack[-1]

            # push unvisited children into stack
            if not visited[start]:
                visited[start] = True
                for child in graph[start]:
                    if not visited[child]:
                        stack.append(child)
            else:
                stack.pop()

                # base case
                if a[start] == 0 and m > 0:
                    dp[start] += 1
                    m -= 1

                # update with finished children
                for child in graph[start]:
                    if finished[child]:
                        dp[start] += dp[child]

                finished[start] = True
        return dp

    print(dfs(graph, a, n, m))


n, m = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
graph = [[] for i in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
solve(graph, a, n, m)
