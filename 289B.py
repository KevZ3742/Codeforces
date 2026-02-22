# B. Polo the Penguin and Matrix
# https://codeforces.com/problemset/problem/289/B
# rating: 1400

n, m, d = map(int, input().split())

matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix += row

remainder = matrix[0] % d

matrix.sort()
median = matrix[len(matrix) // 2]

moves = 0
for i in matrix:
    if i % d != remainder:
        print(-1)
        exit()
    
    moves += abs(median - i) // d

print(moves)