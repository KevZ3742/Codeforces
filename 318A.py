# A. Even Odds
# https://codeforces.com/contest/318/problem/A
# rating: 900

n, k = map(int, input().split())

evenStartIndex = 0

if n % 2 == 0:
    evenStartIndex = n // 2 + 1
else:
    evenStartIndex = n // 2 + 2

if k < evenStartIndex:
    print(k * 2 - 1)
else:
    if n % 2 == 0:
        print(k * 2 - n)
    else:
        print(k * 2 - n - 1)