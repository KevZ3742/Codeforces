# A. Wrong Subtraction
# https://codeforces.com/contest/977/problem/A
# rating: 800

n, k = map(int, input().split())

for _ in range(k):
    if n % 10 == 0:
        n = n // 10
    else:
        n -= 1

print(n)