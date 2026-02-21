# A. Amusing Joke
# https://codeforces.com/contest/141/problem/A
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