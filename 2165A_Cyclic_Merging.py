# https://codeforces.com/contest/2165/problem/A
# rating: 1300

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    maxA = max(a)
    maxIndex = a.index(maxA)
    numMax = a.count(maxA)
    a = a[maxIndex:] + a[:maxIndex] + [maxA]

    cost = 0
    stack = []
    for i in a:
        while stack and stack[-1] < i:
            stack.pop()

            if stack:
                cost += min(i, stack[-1])

        stack.append(i)
    
    if numMax > 1:
        cost += (numMax - 1) * maxA

    print(cost)