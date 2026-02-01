# https://codeforces.com/problemset/problem/272/A
# rating:  1000

n = int(input())
a = list(map(int, input().split()))

fingers = sum(a)
ways = 0

for i in range(1, 6):
    if (fingers + i) % (n + 1) != 1:
        ways += 1

print(ways)