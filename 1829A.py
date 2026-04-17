# A. Love Story
# https://codeforces.com/problemset/problem/1829/A
# rating: 800

t = int(input())

for _ in range(t):
    s = input()

    target = "codeforces"

    toPrint = 0
    for i in range(10):
        if target[i] != s[i]:
            toPrint += 1

    print(toPrint)