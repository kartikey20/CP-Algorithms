from collections import defaultdict

arr = [1, 2, 3, 4, 5, 5, 6, 7, 3, 3, 2]

prefix_sum = defaultdict(list)
sums = 0
prefix_sum[0] = [-1]
k = 10
count = 0
for i in range(len(arr)):
    sums += arr[i]
    indices = prefix_sum[sums - k]
    for x in indices:
        print(x+1, i)
    indices = prefix_sum[sums]
    indices.append(i)
    prefix_sum[sums] = indices
