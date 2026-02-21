# A. Domino piling
# https://codeforces.com/contest/50/problem/A
# rating: 800

dimentions = list(map(int, input().split()))

dominoes = dimentions[0] * dimentions[1] // 2

print(dominoes)