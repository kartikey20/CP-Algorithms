def solve(cols, rows, board, count):
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True

    def dfs(x, y, previousIsX, count):
        if x == cols and y == rows:
            return count
        else:
            if visited[x][y] == False and x >= 0 and y >= 0 and x < rows and y < cols:
                visited[x][y] = True
                if board[x][y] == 'X':
                    if not previousIsX:
                        count += 1
                    previousIsX = True
                else:
                    previousIsX = False
            dfs(x + 1, y, previousIsX, count)
            dfs(x - 1, y, previousIsX, count)
            dfs(x, y + 1, previousIsX, count)
            dfs(x, y - 1, previousIsX, count)
    return dfs(0, 0, False)


cols, rows = map(int, input().split())
matrix = []
for i in range(rows):
    matrix.append(list(input()))
_ = map(int, input().split())
print(solve(cols, rows, matrix))
