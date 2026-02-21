# A. Stones on the Table
# https://codeforces.com/contest/266/problem/A
# rating: 800

n = int(input())
s = str(input())

toRemove = 0
for i in range(1, n):
    if s[i] == s[i-1]:
        toRemove += 1

print(toRemove)