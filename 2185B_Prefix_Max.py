# https://codeforces.com/contest/2185/problem/B
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(max(a) * n)