# A. Lawn Mower
# https://codeforces.com/contest/2194/problem/A
# rating: ?

t = int(input())

for _ in range(t):
    n, w = map(int, input().split())

    if w == 1:
        print(0)
        continue

    if n < w:
        print(n)
        continue
    
    groups = n // w
    boards = n - groups

    print(boards)