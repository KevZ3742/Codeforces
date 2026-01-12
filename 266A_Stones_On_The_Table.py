# https://codeforces.com/problemset/problem/266/A
# rating: 800

n = int(input())
s = str(input())

toRemove = 0
for i in range(1, n):
    if s[i] == s[i-1]:
        toRemove += 1

print(toRemove)