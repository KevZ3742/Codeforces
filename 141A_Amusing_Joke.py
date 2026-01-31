# https://codeforces.com/problemset/problem/141/A
# rating: 800

from collections import Counter

name1 = Counter(list(input()))
name2 = Counter(list(input()))
pile = Counter(list(input()))

letters = name1 + name2

if letters == pile:
    print("YES")
else:
    print("NO")