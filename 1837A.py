# A. Grasshopper on a Line
# https://codeforces.com/problemset/problem/1837/A
# rating: 800

t = int(input())

for _ in range(t):
    x, k = map(int, input().split())

    toPrint = []
    toSubtract = x
    while x > 0:
        if toSubtract % k == 0:
            toSubtract -= 1
        else:
            toPrint.append(toSubtract)
            x -= toSubtract
            toSubtract = x

    print(len(toPrint))
    print(*toPrint)
