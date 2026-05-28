# A. Problem Generator
# https://codeforces.com/problemset/problem/1980/A
# rating: 800

from collections import Counter

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = Counter(input())

    ans = 0

    for ch in "ABCDEFG":
        if a[ch] < m:
            ans += m - a[ch]

    print(ans)