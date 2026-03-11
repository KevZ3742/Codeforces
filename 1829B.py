# B. Blank Space
# https://codeforces.com/problemset/problem/1829/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    toPrint = 0
    cur = 0
    for i in a:
        if i == 0:
            cur += 1
            toPrint = max(toPrint, cur)
        else:
            cur = 0

    print(toPrint)