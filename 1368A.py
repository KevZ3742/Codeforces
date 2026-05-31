# A. C+=
# https://codeforces.com/problemset/problem/1368/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())

    counter = 0
    while b <= n:
        a, b = max(a,b), a + b
        counter += 1

    print(counter)