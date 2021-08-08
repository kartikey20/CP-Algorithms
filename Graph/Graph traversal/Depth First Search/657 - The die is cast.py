def solve(w, h, board):
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[0][0] = True

    def dfs(w, h, board, x, y, previousIsX, count, arr):
        if x == w and y == h:
            return count
        else:
            for i in range(x - 1, y + 2):
                for j in range(x - 1, y + 2):
                    if visited[i][j] == False and i >= 0 and j >= 0 and i < w and j < h:
                        visited[i][j] = True
                        if board[i][j] == 'X':
                            if not previousIsX:
                                count += 1
                            previousIsX = True
                        else:
                            previousIsX = False
                        dfs(w, h, board, i, j, previousIsX, count, arr)
    return dfs(w, h, board, 0, 0, False, 0, [])


width, height = map(int, input().split())
matrix = []
for _ in range(height):
    matrix.append(list(input()))
print(solve(width, height, matrix))
