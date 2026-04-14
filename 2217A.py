# A. The Equalizer
# https://codeforces.com/contest/2217/problem/A
# rating: ?

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if sum(a) % 2 or (k * n) % 2 == 0:
        print("YES")
    else:
        print("NO")