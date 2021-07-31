# https: // www.spoj.com/problems/EAGLE1/

# [[], [2, 3], [3, 4], [4, 5], []]
from itertools import accumulate


def solve(graph, dist, n):
    # dfs using stack
    def dfs(graph, dist, n, start=1):
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
                dp[start] += dist[start]

                # update with finished children
                for child in graph[start]:
                    if finished[child]:
                        dp[start] += dp[child]
                finished[start] = True
        return dp
    down = dfs(graph, dist, n)[1:]
    return ' '.join(map(str, accumulate(down, lambda self,
                                        x: down[0] - x if down[0] - x > x else x)))


T = int(input())
res = []
for i in range(T):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    dist = [0] * (n + 1)
    for i in range(1, n):
        u, v, d = map(int, input().split())
        graph[min(u, v)].append(max(u, v))
        dist[i] = d
    res.append(solve(graph, dist, n))

for x in res:
    print(x)
