# https://codeforces.com/contest/677/problem/A
# rating: 800

n, h = map(int, input().split())
a = list(map(int, input().split()))

w = 0
for i in a:
    if i > h:
        w += 2
    else:
        w += 1

print(w)