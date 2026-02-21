# A. Rank List
# https://codeforces.com/contest/166/problem/A
# rating: 1100

n, k = map(int, input().split())

teams = []
for _ in range(n):
    p, t = map(int, input().split())
    teams.append((-p, t))

teams.sort()

print(teams.count(teams[k - 1]))