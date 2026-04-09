# A. Holiday Of Equality
# https://codeforces.com/problemset/problem/758/A
# rating: 800

n = int(input())
a = list(map(int, input().split()))

maxA = max(a)

toPrint = 0
for n in a:
    toPrint += maxA - n

print(toPrint)