# https://codeforces.com/problemset/problem/41/A
# rating: 800

s = str(input())
t = str(input())

s = s[::-1]

if s == t:
    print("YES")
else:
    print("NO")