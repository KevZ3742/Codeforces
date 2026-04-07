# A. Odd Divisor
# https://codeforces.com/problemset/problem/1475/A
# rating: 900

t = int(input())

for _ in range(t):
    n = int(input())

    if n & 1:
        print("YES")
        continue

    while n % 2 == 0:
        n  //= 2

    if n == 1:
        print("NO")
    else:
        print("YES")