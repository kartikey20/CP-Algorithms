from itertools import permutations


def chunk(list, size):
    return [list[i:i + size] for i in range(0, len(list), size)]


def solve(n, prices):
    total_sum = float('inf')
    for x in permutations(prices, n):
        arr_sum = 0
        for y in chunk(x, 3):
            y = list(y)
            if len(y) == 3:
                mini = y.index(min(y))
                del y[mini]
            arr_sum += sum(y)
        total_sum = min(total_sum, arr_sum)
    return total_sum


print(solve(6, [6, 6, 7, 5, 5, 5]))
