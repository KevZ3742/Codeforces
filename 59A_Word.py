# https://codeforces.com/problemset/problem/59/A
# rating: 800

s = str(input())

upper = lower = 0

for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

if lower >= upper:
    print(s.lower())
else: 
    print(s.upper())