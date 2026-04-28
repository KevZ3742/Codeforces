# C. Grouping Increases
# https://codeforces.com/problemset/problem/1919/C
# rating: 1400

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a1 = float("inf")
    a2 = float("inf")
    toPrint = 0

    for x in a:
        if x <= a1 and x <= a2:
            if a1 == x or a2 == x:
                continue

            if a1 < a2:
                a1 = x
            else:
                a2 = x
        elif x <= a1:
            a1 = x
        elif x <= a2:
            a2 = x
        else:
            toPrint += 1

            if a1 > a2:
                a2 = x
            else:
                a1 = x

    print(toPrint)