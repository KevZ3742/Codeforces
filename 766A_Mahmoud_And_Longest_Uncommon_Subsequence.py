# https://codeforces.com/contest/766/problem/A
# rating: 1000

a = str(input())
b = str(input())

if a == b:
    print(-1)
else:
    print(max(len(a), len(b)))