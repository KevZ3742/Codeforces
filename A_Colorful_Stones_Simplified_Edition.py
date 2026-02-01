# https://codeforces.com/contest/265/problem/A
# rating: 800

s = str(input())
t = str(input())

pos = 0
for n in t:
    if n == s[pos]:
        pos += 1

print(pos + 1)