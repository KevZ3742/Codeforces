# A. Extremely Round
# https://codeforces.com/problemset/problem/1766/A
# rating: 800

t = int(input())

for _ in range(t):
    n = input().strip()
    print(9 * (len(n) - 1) + int(n[0]))