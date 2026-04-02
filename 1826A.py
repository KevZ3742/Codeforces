# A. Trust Nobody
# https://codeforces.com/problemset/problem/1826/A
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    for liarCount in range(n + 1):
        liars = 0
        for i in l:
            if not (liarCount >= i):
                liars += 1

        if liars == liarCount:
            print(liarCount)
            break
    else:
        print(-1)