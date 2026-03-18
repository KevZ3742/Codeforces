# B. Minimize Equal Sum Subarrays
# https://codeforces.com/problemset/problem/1998/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    print(*([p[-1]] + p[:-1]))