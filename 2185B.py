# B. Prefix Max
# https://codeforces.com/contest/2185/problem/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(max(a) * n)