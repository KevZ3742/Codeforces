# A. Pangram
# https://codeforces.com/contest/520/problem/A
# rating: 800

n = int(input())
s = set(input().lower())

if len(s) != 26:
    print("NO")
else:
    print("YES")