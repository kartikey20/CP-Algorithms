from collections import defaultdict
from operator import sub
from functools import reduce
from typing import List


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
