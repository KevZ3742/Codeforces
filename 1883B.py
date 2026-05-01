# B. Chemistry
# https://codeforces.com/problemset/problem/1883/B
# rating: 900

from collections import Counter

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = Counter(input())

    numOdd = 0
    for v in a.values():
        if v % 2:
            numOdd += 1
            
    if numOdd > k + 1:
        print("NO")
    else:
        print("YES")