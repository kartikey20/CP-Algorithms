import sys


def solve(maze, start, end):
    visited = [[False for _ in range(30)] for _ in range(30)]

    def valid(row, col):
        return row >= 0 and row < 30 and col >= 0 and col < 30

    def floodfill(row, col):
        visited[row][col] = True
        if valid(row + 1, col) and (maze[row+1][col] == '.' or maze[row + 1][col] == 'G') and not visited[row+1][col]:
            floodfill(row+1, col)
        if valid(row - 1, col) and (maze[row-1][col] == '.' or maze[row - 1][col] == 'G') and not visited[row-1][col]:
            floodfill(row-1, col)
        if valid(row, col + 1) and (maze[row][col+1] == '.' or maze[row][col + 1] == 'G') and not visited[row][col+1]:
            floodfill(row, col+1)
        if valid(row, col - 1) and (maze[row][col-1] == '.' or maze[row][col - 1] == 'G') and not visited[row][col-1]:
            floodfill(row, col-1)
    floodfill(start[0]-1, start[1])
    if visited[end[0]-1][end[1]]:
        return 'Possible'
    else:
        return 'Impossible'


count = 1
maze = []
res = []
for line in sys.stdin:
    maze.append(temp := list(input()))
    if 'P' in temp:
        start = (count, temp.index('P'))
    if 'G' in temp:
        goal = (count, temp.index('G'))
    count += 1
    if count % 30 == 0:
        res.append(solve(maze, start, goal))
        maze = []

print(count % 30)
