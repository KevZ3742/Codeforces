# B. Count the Number of Pairs
# https://codeforces.com/problemset/problem/1800/B
# rating: 1000

from collections import Counter

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = Counter(input())

    toPrint = 0

    for i in range(26):
        lower = s[chr(ord('a') + i)]
        upper = s[chr(ord('A') + i)]

        operations = min(abs(lower - upper) // 2, k)
        toPrint += min(lower, upper) + operations
        k -= operations

    print(toPrint)