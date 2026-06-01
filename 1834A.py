# A. Unit Array
# https://codeforces.com/problemset/problem/1834/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    neg = a.count(-1)

    if neg <= n // 2:
        print(neg % 2)
    else:
        ops = neg - (n // 2)
        neg = n // 2
        if neg % 2:
            ops += 1
        print(ops)