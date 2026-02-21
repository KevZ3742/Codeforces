# B. Letter
# https://codeforces.com/contest/43/problem/B
# rating: 1100

from collections import Counter

s1 = Counter(input().replace(" ", ""))
s2 = Counter(input().replace(" ", ""))

for key in s2.keys():
    if s2[key] > s1[key]:
        print("NO")
        exit()

print("YES")