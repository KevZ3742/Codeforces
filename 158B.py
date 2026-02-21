# B. Taxi
# https://codeforces.com/contest/158/problem/B
# rating: 1100

from collections import Counter

count = int(input())
groups = Counter(map(int, input().split()))

cars = 0

cars += groups[4]

cars += groups[3]
groups[1] = max(0, groups[1] - groups[3])

cars += groups[2] // 2
groups[2] %= 2

if groups[2] == 1:
    cars += 1
    groups[1] = max(0, groups[1] - 2)

cars += (groups[1] + 3) // 4

print(cars)