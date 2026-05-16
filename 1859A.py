# A. United We Stand
# https://codeforces.com/problemset/problem/1859/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    if a[-1] == a[0]:
        print(-1)
    else:
        it = 0
        while a[it] == a[0]:
            it += 1

        print(it, n - it)

        for j in range(it):
            print(a[j], end=" ")

        for j in range(it, n):
            print(a[j], end=" ")

        print()