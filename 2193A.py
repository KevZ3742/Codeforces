# A. DBMB and the Array
# https://codeforces.com/contest/2193/problem/A
# rating: 800

t = int(input())

for _ in range(t):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))

    remainder = s - sum(a)

    if remainder < 0:
        print("NO")
        continue

    if remainder % x == 0:
        print("YES")
    else:
        print("NO")