from collections import defaultdict

arr = [1, 2, 2, 4, 4]
# arr.sort()
prod = 1
prefix_prod = defaultdict(list)
prefix_prod[0] = [1]
target = 4
res = []
for i in range(len(arr)):
    prod *= arr[i]
    indices = prefix_prod[prod//target]
    for x in indices:
        res.append((x+1, i))
    indices = prefix_prod[prod]
    indices.append(i)
    prefix_prod[prod] = indices
print(res)
