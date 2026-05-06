# A. Doremy's Paint 3
# https://codeforces.com/problemset/problem/1890/A
# rating: 800

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = Counter(map(int, input().split()))

    if len(a.keys()) == 1:
        print("YES")
    elif len(a.keys()) == 2 and (n // 2) in a.values():
        print("YES")
    else:
        print("NO")

    