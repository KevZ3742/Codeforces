# https://codeforces.com/contest/734/problem/A
# rating: 800

from collections import Counter

n = int(input())
games = Counter(input())

if games["A"] > games["D"]:
    print("Anton")
elif games["A"] < games["D"]:
    print("Danik")
else:
    print("Friendship")