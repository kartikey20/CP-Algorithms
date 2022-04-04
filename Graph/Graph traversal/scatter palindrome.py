def numHyperdomes(s):
    dp = {0: 1}
    bs = 0
    ret = 0
    for ch in s:
        bi = ord(ch) - 97
        bs ^= (1 << bi)

        ret += dp.get(bs, 0)
        oneActive = 1 << 25
        while oneActive:
            ret += dp.get(bs ^ oneActive, 0)
            oneActive >>= 1

        dp[bs] = dp.get(bs, 0) + 1

    return ret


bitset

print(numHyperdomes("abc"))
