from collections import defaultdict


ans = []


def binary_search(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def solve(n):
    curr_sum = 0
    print(list(range(1, n + 1)))
    prefix = []
    for i in range(1, n + 1):
        curr_sum += i
        prefix.append(curr_sum)
    print(prefix)


t = int(input())

for _ in range(t):
    n = int(input())
    ans.append(solve(n))

for x in ans:
    print(x)


# Time Complexity: O(n^3)
# Space Complexity: O(1)
