# B. Polo the Penguin and Matrix
# https://codeforces.com/problemset/problem/289/B
# rating: 1400

n, m, k = map(int, input().split())

matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

