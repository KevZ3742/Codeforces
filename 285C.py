# C. Building Permutation
# https://codeforces.com/problemset/problem/285/C
# rating: 1200

n = int(input())
a = list(map(int, input().split()))

a.sort()

toPrint = 0
for p in range(n):
    toPrint += abs(p + 1 - a[p])

print(toPrint)