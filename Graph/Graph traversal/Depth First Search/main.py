def solve(S, K):
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return days[(days.index(S) + K) % 7]


print(solve('Sat', 3))
