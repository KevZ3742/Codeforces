# B. Ten Words of Wisdom
# https://codeforces.com/problemset/problem/1850/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    best_quality = -1
    winner = -1

    for i in range(1, n + 1):
        a, b = map(int, input().split())

        if a <= 10 and b > best_quality:
            best_quality = b
            winner = i

    print(winner)