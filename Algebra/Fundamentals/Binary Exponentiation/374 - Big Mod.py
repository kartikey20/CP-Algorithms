while True:
    try:
        a = int(input())
        b = int(input())
        m = int(input())
        print(pow(a, b, m))
        input()
    except EOFError:
        break
