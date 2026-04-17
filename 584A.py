# A. Olesya and Rodion
# https://codeforces.com/problemset/problem/584/A
# rating: 1000

n, t = map(int, input().split())

for i in range(10 ** (n - 1), 10 ** n):
    if i % t == 0:
        print(i)
        break
else:
    print(-1)