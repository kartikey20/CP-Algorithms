def solve(n, arr, d):
    min_arr = []
    for i in range(n-d+1):
        min_arr.append(max(arr[i:i+d]))
    return min(min_arr)


n, q = map(int, input().split())
arr = list(map(int, input().split()))
res = []
for _ in range(q):
    d = int(input())
    res.append(solve(n, arr, d))

for x in res:
    print(x)
