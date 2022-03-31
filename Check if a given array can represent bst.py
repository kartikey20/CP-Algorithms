pre = [1, 2, 4]


def canRepresentBST(pre):
    stack = []
    root = float('-inf')

    for val in pre:
        if val < root:
            return False
        while len(stack) > 0 and stack[-1] < val:
            root = stack.pop()
        stack.append(val)
    return True


def test():
    test_cases = [([2, 4, 3], True), ([2, 4, 1], False),
                  ([40, 30, 35, 80, 100], True), ([40, 30, 35, 20,  80, 100], False)]
    for i in range(len(test_cases)):
        print(f'Test Case {i+1}: {test_cases[i][0]}', 'Passed'
              if canRepresentBST(test_cases[i][0]) == test_cases[i][1] else 'Failed')


test()
