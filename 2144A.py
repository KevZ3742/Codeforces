# A. Cut the Array
# https://codeforces.com/problemset/problem/2144/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) % 3 == 0:
        print(1, 2)
    else:
        print(0, 0)