# B. Split
# https://codeforces.com/problemset/problem/2158/B
# rating: 1200

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    counterA = Counter(a)

    toPrint = 0
    numOdds = 0
    numMod4 = 0
    for num in counterA.keys():
        if counterA[num] % 2:
            toPrint += 1
            numOdds += 1
        elif counterA[num] % 4 == 2:
            toPrint += 2
        elif counterA[num] % 4 == 0:
            numMod4 += 1
            
    if numOdds > 0:
        toPrint += numMod4 * 2
    else:
        if numMod4 % 2:
            toPrint += (numMod4 - 1) * 2
        else:
            toPrint += numMod4 * 2

    print(toPrint)