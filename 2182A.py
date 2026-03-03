# A. New Year String
# https://codeforces.com/problemset/problem/2182/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if "2026" in s:
        print(0)
        continue

    if "2025" not in s:
        print(0)
    else:
        print(1)
