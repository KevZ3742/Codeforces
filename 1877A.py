# A. Goals of Victory
# https://codeforces.com/problemset/problem/1877/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(-sum(a))