# A. Lucky?
# https://codeforces.com/problemset/problem/1676/A
# rating: 800

t = int(input())

for _ in range(t):
    s = input()

    if int(s[0]) + int(s[1]) + int(s[2]) == int(s[-1]) + int(s[-2]) + int(s[-3]):
        print("YES")
    else:
        print("NO")