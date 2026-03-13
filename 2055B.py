# B. Crafting
# https://codeforces.com/problemset/problem/2055/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    aLess = 0
    diff = []
    operations = float('inf')
    for i in range(n):
        diff.append(b[i] - a[i])

        if a[i] < b[i]:
            aLess += 1
        else:
            operations = min(operations, a[i] - b[i])

    operateOn = max(diff)

    if aLess > 1:
        print("NO")
    elif aLess == 0:
        print("YES")
    else:
        if operateOn <= operations:
            print("YES")
        else:
            print("NO")