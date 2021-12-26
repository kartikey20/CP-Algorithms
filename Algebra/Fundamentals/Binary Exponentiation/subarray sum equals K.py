from typing import List
from collections import defaultdict


def subarraySum(self, nums: List[int], k: int) -> int:
    sums = 0
    count = 0
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    for i in range(len(nums)):
        sums += nums[i]
        if prefix_sum[sums - ]
        prefix_sum[sums] += 1
    return count
