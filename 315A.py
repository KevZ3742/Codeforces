# A. Sereja and Bottles
# https://codeforces.com/problemset/problem/315/A
# rating: 1400

n = int(input())

brandA = []
brandB = []
for _ in range(n):
    a, b = map(int, input().split())

    brandA.append(a)
    brandB.append(b)

toPrint = 0
for i in range(n):
    openers = brandB.count(brandA[i])

    if brandA[i] == brandB[i]:
        openers -= 1

    if openers == 0:
        toPrint += 1

print(toPrint)