def bin_pow(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return bin_pow(a * a, b // 2)
    else:
        return a * bin_pow(a * a, b // 2)

    # Time Complexity: O(log(b))
    # Space Complexity: O(1)


print(bin_pow(2, 9))
