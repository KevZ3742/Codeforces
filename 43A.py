# A. Football
# https://codeforces.com/problemset/problem/43/A
# rating: 1000

from collections import defaultdict

n = int(input())

teams = defaultdict(int)
for _ in range(n):
    team = input()
    teams[team] += 1

print(max(teams, key=teams.get))