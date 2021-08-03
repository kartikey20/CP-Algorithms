# https://codeforces.com/problemset/problem/580/C
# [[], [2, 3], [4, 5], [6, 7], [], [], [], []]

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
            print(stack)
            stack.pop()

            # base case
            dp[start] += a[start]

            # update with finished children
            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True
    return dp


n, m = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
print(dfs(graph, a, n, m))
