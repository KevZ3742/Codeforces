# A. cAPS lOCK
# https://codeforces.com/problemset/problem/131/A
# rating: 1000

s = input()

if len(s) == 1 and s.islower():
    print(s.swapcase())
    exit()

if s.isupper() or s[1:].isupper():
    print(s.swapcase())
else:
    print(s)