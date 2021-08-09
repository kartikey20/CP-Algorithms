# [
# ['.######.'],
# ['#..k...#'],
# ['#.####.#'],
# ['#.#v.#.#'],
# ['#.#.k#k#'],
# ['#k.##..#'],
# ['#.v..v.#'],
# ['.######.']
# ]

def solve(n, m, matrix):
    sheep = 0
    wolf = 0
    totalSheep = 0
    totalWolf = 0

    def dfs(i, j):

        return

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != '#':
                dfs(i, j)
                if sheep > wolf:
                    totalWolf += wolf
                else:
                    totalSheep += sheep

    return


N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(input().split()))
print(solve(N, M, matrix))
