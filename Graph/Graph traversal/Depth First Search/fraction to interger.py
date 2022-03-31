from math import remainder


def fraction_to_decimal(num, denom):
    res = ''
    remainder_set = {}
    rem = num % denom
    while rem != 0 and rem not in remainder_set:
        remainder_set[rem] = len(res)
        rem = rem * 10
        quotient = rem // denom
        res += str(quotient)
        rem = rem % denom