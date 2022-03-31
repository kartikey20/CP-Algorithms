# def FN(ins):
#     a = False
#     n = 2
#     while not a:
#         um = set([])
#         for i, item in enumerate(ins):
#             ni = item/n
#             if ni in um:
#                 a = True
#                 break
#             else:
#                 um.add(ni)
#             n = n+1
#     return n


from turtle import position


def FN(ins):
    possible = [i for i in range(2, 8+1)]
    for i in range(2, 8+1):
        set_nums = set()
        for item in ins:
            mod = item % i
            if mod in set_nums:
                possible.remove(i)
                break
            set_nums.add(mod)
    return possible


print(FN([1000, 5000, 8000, 6000, 2100]))
