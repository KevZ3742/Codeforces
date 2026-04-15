# B. Swap and Delete
# https://codeforces.com/problemset/problem/1913/B
# rating: 1000

from collections import Counter

t = int(input())

for _ in range(t):
    s = input()
    
    sCounter = Counter(s)

    if sCounter["0"] == sCounter["1"]:
        print(0)
        continue
    
    used = len(s)
    for i in range(len(s)):
        if s[i] == "1" and sCounter["0"]:
            sCounter["0"] -= 1
            used -= 1
        elif s[i] == "0" and sCounter["1"]:
            sCounter["1"] -= 1
            used -= 1
        else:
            break

    print(used)
