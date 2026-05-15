# A. Floor Number
# https://codeforces.com/problemset/problem/1426/A
# rating: 800

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    print(1 if n <= 2 else (n - 3) // x + 2)