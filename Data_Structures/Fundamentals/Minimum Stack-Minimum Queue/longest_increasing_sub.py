from bisect import bisect_left


def lengthOfLIS(self, arr: List[int]) -> int:
    print(arr)
    sub = []
    for val in arr:
        pos = bisect_left(sub, val)
        # print(pos)
        if pos == len(sub):
            sub.append(val)
        else:
            sub[pos] = val
    return len(sub)
