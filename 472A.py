# A. Design Tutorial: Learn from Math
# https://codeforces.com/problemset/problem/472/A
# rating: 800

n = int(input())

if n % 2:
    print(9, n - 9)
else:
    print(4, n - 4)