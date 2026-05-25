# B1. Sub-RBS (Easy Version)
# https://codeforces.com/problemset/problem/2190/B1
# rating: 1400

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    counterS = Counter(s)

    counter = 0
    for i in s:
        counter += 1
        if i == ")":
            break

    counterS[")"] -= 1
    
    for i in range(counter, n):
        if s[i] == "(" and counter + 1 <= counterS[")"]:
            counter += 1
        
    if counter == counterS[")"]:
        print(counter * 2)
    else:
        print(-1)