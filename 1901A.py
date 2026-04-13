# A. Line Trip
# https://codeforces.com/problemset/problem/1901/A
# rating: 800

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    fuel = [a[0]]
    prev = a[0]
    for i in range(1, n):
        fuel.append(a[i] - prev)
        prev = a[i]

    fuel.append((x - a[-1]) * 2)

    print(max(fuel))