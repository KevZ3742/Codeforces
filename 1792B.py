# B. Stand-up Comedian
# https://codeforces.com/problemset/problem/1792/B
# rating: 1200

t = int(input())

for _ in range(t):
    a1, a2, a3, a4 = map(int, input().split())

    toAdd = min(a2, a3)
    alice = bob = a1
    toPrint = a1 

    if a1 > 0:
        toPrint += toAdd * 2
        leftover = max(a2, a3) - min(a2, a3)
    else:
        leftover = max(a2, a3)

    if min(alice, bob) >= leftover:
        toPrint += leftover

        if a2 == max(a2, a3):
            alice += leftover
            bob -= leftover
        else:
            alice -= leftover
            bob += leftover
    else:
        toPrint += min(alice, bob)
        print(toPrint + 1)
        continue

    toPrint += min(alice, bob, a4)

    if min(alice, bob) >= a4:
        print(toPrint)
    else:
        print(toPrint + 1)
    