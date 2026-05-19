# B. osu!mania
# https://codeforces.com/problemset/problem/2009/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    
    toPrint = []
    for i in range(n):
        row = input()

        toPrint.append(row.index("#") + 1)

    print(*toPrint[::-1])