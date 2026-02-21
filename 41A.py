# A. Translation
# https://codeforces.com/contest/41/problem/A
# rating: 800

s = str(input())
t = str(input())

s = s[::-1]

if s == t:
    print("YES")
else:
    print("NO")