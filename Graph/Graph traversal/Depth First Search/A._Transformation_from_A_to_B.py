a, b = map(int, input().split())

flag = [False]
temp = [a]
res = []


def dfs(x, temp):
    if flag[0] == True:
        return
    if x == b:
        flag[0] = True
        res.extend(temp)
        return
    if x > b:
        return
    temp.append(2 * x)
    dfs(2 * x, temp)
    temp.pop()
    n = str(x)
    n = list(str(x)) + ['1']
    n = ''.join(n)
    n = int(n)
    temp.append(n)
    dfs(n, temp)
    temp.pop()


dfs(a, temp)
if flag[0] == False:
    print('NO')
else:
    print("YES")
    print(len(res))
    print(*res)
