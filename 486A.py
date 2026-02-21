# A. Calculating Function
# https://codeforces.com/contest/486/problem/A
# rating: 800

n = int(input())

if n % 2 == 0:
    print(n // 2)
else:
    print(-(n + 1) // 2)