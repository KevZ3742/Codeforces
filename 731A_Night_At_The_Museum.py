# https://codeforces.com/contest/731/problem/A
# rating: 800

name = str(input())

curr = 'a'
turns = 0
for c in name:
    turns += min(abs(ord(curr) - ord(c)), ord(curr) + 26 - ord(c), ord(c) + 26 - ord(curr))
    curr = c

print(turns)