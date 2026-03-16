# C1. Powering the Hero (easy version)
# https://codeforces.com/problemset/problem/1800/C1
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    stack = []
    power = 0

    for num in s:
        if num == 0 and stack:
            stack.sort()
            power += stack.pop()
        else:
            stack.append(num)

    print(power)