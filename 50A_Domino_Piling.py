# https://codeforces.com/problemset/problem/50/A
# rating: 800

dimentions = list(map(int, input().split()))

dominoes = dimentions[0] * dimentions[1] // 2

print(dominoes)