# A. Presents
# https://codeforces.com/contest/136/problem/A
# rating: 800

n = int(input())
p = list(map(int, input().split()))

toPrint = [0] * n

for i in range(n):
    toPrint[p[i] - 1] = i + 1

print(*toPrint)