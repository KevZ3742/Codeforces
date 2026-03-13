# A. Spell Check
# https://codeforces.com/problemset/problem/1722/A
# rating: 800

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = Counter(input())
    timur = Counter("Timur")


    if s == timur:
        print("YES")
    else:
        print("NO")

    