# A. The number of positions
# https://codeforces.com/contest/124/problem/A
# rating: 1000

n, a, b = map(int, input().split())

init = max(1 + a, n - b)
positions = n - init + 1

print(positions)