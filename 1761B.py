# B. Elimination of a Ring
# https://codeforces.com/problemset/problem/1761/B
# rating: 1000

from collections import Counter

t = int(input())

for i in range(t):
    n = int(input())
    a = Counter(map(int, input().split()))

    if len(a.keys()) == 2:
        print(n // 2 + 1)
    else:
        print(n)