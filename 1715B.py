# B. Beautiful Array
# https://codeforces.com/problemset/problem/1715/B
# rating: 1000

t = int(input())

for _ in range(t):
    n, k, b, s = map(int, input().split())

    toAppend = min(b * k + k - 1, s)

    if toAppend == s:
        if s // k != b:
            print(-1)
            continue

    toPrint = [toAppend]
    s -= toAppend
    for i in range(1, n):
        toAppend = min(k - 1, s)
        toPrint.append(toAppend)
        s -= toAppend

    if s > 0:
        print(-1)
    else:
        print(*toPrint)