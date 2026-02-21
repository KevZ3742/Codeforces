# C. Huge Pile
# https://codeforces.com/contest/2184/problem/C
# rating: 1100

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    found = False
    add = 0
    for i in range(30):
        if n == k or n + add == k:
            found = True
            print(i)
            break

        if n & 1:
            add = 1

        n = n >> 1

    if found == False:
        print(-1)