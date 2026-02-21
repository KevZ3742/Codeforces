# B. Shower Line
# https://codeforces.com/contest/431/problem/B
# rating: 1200

from itertools import permutations

matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))


maxHappiness = 0
for p in permutations(range(5)):
    happiness = matrix[p[0]][p[1]] + matrix[p[1]][p[0]] + 2 * matrix[p[2]][p[3]] + 2 * matrix[p[3]][p[2]] + matrix[p[1]][p[2]] + matrix[p[2]][p[1]] + 2 * matrix[p[3]][p[4]] + 2 * matrix[p[4]][p[3]]
    maxHappiness = max(maxHappiness, happiness)

print(maxHappiness)