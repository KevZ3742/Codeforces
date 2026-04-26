# F. Gravity Falls
# https://codeforces.com/contest/2148/problem/F
# rating: 1800

t = int(input())

for _ in range(t):
    n = int(input())

    stacks = []
    size = []
    for i in range(n):
        a = list(map(int, input().split()))
        size.append(a[0])
        stacks.append(a[1:])

    size = max(size)

    toPrint = []
    while len(toPrint) < size:
        stacks.sort()
        toPrint += stacks[0]

        for i in range(len(stacks)):
            stacks[i] = stacks[i][len(toPrint):]

        stacks = list(filter(None, stacks))

    print(*toPrint)

# wip
