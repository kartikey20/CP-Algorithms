arr = ['1', '0', '0', '1', '0', '0', '1', '1', '1', '0']
count = 0


def exists_1(arr):
    res = [False] * len(arr)
    for i in range(len(arr)):
        if arr[i] == '0':
            res[i] = True
    if all(res):
        return False
    return True


while exists_1(arr):
    if arr[-1] == '1' and arr[-2] == '0':
        arr[len(arr)-1] = '0'

    for i in range(len(arr)-1):
        if arr[i] == '1' and arr[i+1] == '0':
            arr[i] = '0'
        elif arr[i] == '1' and arr[i+1] == '1':
            arr[i+1] = '0'
    count += 1
