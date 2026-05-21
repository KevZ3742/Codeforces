# A. Ambitious Kid
# https://codeforces.com/problemset/problem/1866/A
# rating: 800

n = int(input())
a = list(map(abs, map(int, input().split())))

print(min(a))

