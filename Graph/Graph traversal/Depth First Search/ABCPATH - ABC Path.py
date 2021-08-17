# https://www.spoj.com/problems/ABCPATH/
# TODO: EOF error
# [['ABE'],
# ['CFG'],
# ['BDH'],
# ['ABC']]

def solve(arr, n, m):
    def dfs(arr, i, j, visited, len):
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if ord(arr[i][j]) == ord(arr[x][y]) - 1 and visited[x][y] == False and x >= 0 and y >= 0 and x < n and y < m:
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
                maxlen = max(maxlen, dfs(arr, i, j, visited, 1))
    return maxlen


res = []
H, W = map(int, input().split())
while H != 0 and W != 0:
    arr = []
    for _ in range(H):
        arr.append(input())
    res.append(solve(arr, H, W))
    H, W = map(int, input().split())


for i in range(len(res)):
    print(f"Case {i + 1}: {res[i]}")
