# https://codeforces.com/contest/268/problem/A
# rating: 800

from collections import Counter

n = int(input())
home = []
away = []


for _ in range(n):
    h, a = map(int, input().split())
    home.append(h)
    away.append(a)

homeCounts = Counter(home)
awayCounts = Counter(away)

counter = 0
for color in homeCounts:
    if color in awayCounts:
        counter += homeCounts[color] * awayCounts[color]

print(counter)