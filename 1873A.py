# A. Short Sort
# https://codeforces.com/problemset/problem/1873/A
# rating: 

t = int(input())

for _ in range(t):
    s = input()

    diffCount = 0

    if s[0] != "a":
        diffCount += 1

    if s[1] != "b":
        diffCount += 1

    if s[2] != "c":
        diffCount += 1

    if diffCount > 2:
        print("NO")
    else:
        print("YES")