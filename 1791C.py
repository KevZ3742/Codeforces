# C. Prepend and Append
# https://codeforces.com/problemset/problem/1791/C
# rating: 900

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    s = deque(input())

    while s and ((s[0] == "0" and s[-1] == "1") or (s[0] == "1" and s[-1] == "0")):
        s.popleft()
        s.pop()

    print(len(s))
    