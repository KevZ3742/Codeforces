# D. Binary String Battle
# https://codeforces.com/problemset/problem/2123/D
# rating: 1200

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    if s.count("1") <= k:
        print("Alice")
    elif k > n // 2:
        print("Alice")
    else:
        print("Bob")