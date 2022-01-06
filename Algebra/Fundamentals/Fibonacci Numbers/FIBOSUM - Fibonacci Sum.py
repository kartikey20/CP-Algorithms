def fib_generator(n):
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])
    print(arr)


print(fib_generator(67))
