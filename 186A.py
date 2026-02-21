# A. Comparing Strings
# https://codeforces.com/contest/186/problem/A
# rating: 1100

from collections import Counter

a = input()
b = input()

if Counter(a) != Counter(b):
    print("NO")
    exit()

difference = 0
for i in range(len(a)):
    if difference > 2:
        print("NO")
        exit()

    if a[i] != b[i]:
        difference += 1

if difference == 1:
    print("NO")
else:
    print("YES")