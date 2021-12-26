from collections import defaultdict

arr = [1, 2, 3, 4, 5, 65, 6, 7, 7, 1, 2, 3]

k = 9

prefix_sum = defaultdict(list)
sums = 0
res = []
prefix_sum[0] = [-1]
for i in range(len(arr)):
    sums += arr[i]
    start_list = prefix_sum[sums-k]
    for x in start_list:
        res.append([x+1, i])
    start_list2 = prefix_sum[sums]
    start_list2.append(i)
    prefix_sum[sums] = start_list2


for x in res:
    print(x)
