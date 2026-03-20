# A. Vasya the Hipster
# https://codeforces.com/problemset/problem/581/A
# rating: 800

a, b = map(int, input().split())

print(min(a, b), (max(a, b) - min(a, b)) // 2)