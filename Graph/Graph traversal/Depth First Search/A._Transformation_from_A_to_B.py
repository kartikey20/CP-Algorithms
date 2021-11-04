a, b = map(int, input().split())


def solve(a, b):
    def dfs(x):
        dfs(2*x)
        dfs()
    dfs(a)
