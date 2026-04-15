# B. Swap and Delete
# https://codeforces.com/problemset/problem/1913/B
# rating: 1000

from collections import Counter

t = int(input())

for _ in range(t):
    s = input()

    sCounter = Counter(s)

    for c in s:
        if c == "1" and sCounter["0"]:
            sCounter["0"] -= 1
        elif c == "0" and sCounter["1"]:
            sCounter["1"] -= 1
        else:
            break

    print(sCounter["0"] + sCounter["1"])