from collections import defaultdict
from operator import sub
from functools import reduce
from typing import List


def minSubArrayLen(k: int, nums: List[int]) -> int:
    # nums.sort()
    prefix_sum = defaultdict(set)
    sums = 0
    prefix_sum[0].add(-1)
    res = []
    n = len(nums)
    for i in range(n):
        sums += nums[i]
        for _, v in enumerate([0] + nums):
            indices = prefix_sum[sums - k]
            for x in indices:
                # print(sums)
                res.append([x+1, i])
            indices = prefix_sum[sums]
            indices.add(i)
            prefix_sum[sums] = indices
    
    
    min_len = float('inf')
    print(prefix_sum)
    # print("ddfdsfsdfds")
    print(res)
    for l, r in res:
        min_len = min(min_len, r - l + 1)
    return min_len if min_len != float('inf') else 0


print(minSubArrayLen(20,
                     [2, 16, 14, 15]))
