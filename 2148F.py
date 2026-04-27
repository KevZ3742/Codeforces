# F. Gravity Falls
# https://codeforces.com/contest/2148/problem/F
# rating: 1800

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())

    stacks = []
    for i in range(n):
        a = list(map(int, input().split()))
        stacks.append(deque(a[1:]))

    stacks.sort(key=lambda x: -len(x))

    toPrint = []
    while stacks:
        toAppend = min(stacks)
        toPrint += toAppend

        while stacks and len(stacks[-1]) <= len(toAppend):
            stacks.pop()

        for i in range(len(stacks)):
            for j in range(len(toAppend)):
                stacks[i].popleft()

    print(*toPrint)