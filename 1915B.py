# B. Not Quite Latin Square
# https://codeforces.com/problemset/problem/1915/B
# rating: 800

t = int(input())

for _ in range(t):
    grid = [input().strip() for _ in range(3)]

    for row in grid:
        if '?' in row:
            for ch in "ABC":
                if ch not in row:
                    print(ch)
                    break