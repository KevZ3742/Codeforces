# A. Bachgold Problem
# https://codeforces.com/problemset/problem/749/A
# rating: 800

n = int(input())

print(n // 2)

if n % 2:
    print("2 " * (n // 2 - 1) + "3")
else:
    print("2 " * (n // 2))