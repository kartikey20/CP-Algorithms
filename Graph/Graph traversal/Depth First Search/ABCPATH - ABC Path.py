# https://www.spoj.com/problems/ABCPATH/

# [['ABE'],
# ['CFG'],
# ['BDH'],
# ['ABC']]

def solve(arr, n, m):
    def dfs(arr, i, j, visited, len):
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if ord(arr[i][j]) == ord(arr[x][y]) - 1 and visited[x][y] == False and x >= 0 and y >= 0 and x < n and y < m:
                    print(arr[x][y])
                    visited[x][y] = True
                    return dfs(arr, x, y, visited, len + 1)
        else:
            return len

    maxlen = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'A':
                visited = [[False for _ in range(m)] for _ in range(n)]
                visited[i][j] = True
                maxlen = max(maxlen, dfs(arr, i, j, visited, 0))


T = int(input())
res = []
for i in range(T):
    H, W = map(int, input().split())
    arr = []
    for _ in range(H):
        arr.append(list(input()))
    res.append(f"Case {i}: {solve(arr, H, W)}")

for x in res:
    print(x)
